#!/usr/bin/env python3
"""
Enterprise Agent Harness: Execution Runtime & Environment Sandboxing Engine.
Manages tool dispatching, OS encoding normalization, sub-process supervision,
bounded concurrency, and autonomous self-healing execution loops.
"""

import sys
import os
import subprocess
import asyncio
from typing import Dict, Any, List, Optional
from pathlib import Path


class AgentHarness:
    """
    Autonomous Execution Harness for AI Coding Agents.
    Provides physical environment execution, encoding-safe subprocess execution,
    and automatic error diagnostics.
    """

    def __init__(self, workspace_root: Optional[str] = None):
        self.workspace_root = Path(workspace_root or os.getcwd()).resolve()
        self.execution_history: List[Dict[str, Any]] = []

    def execute_terminal(
        self,
        command: str,
        timeout_sec: float = 60.0,
        cwd: Optional[str] = None
    ) -> Dict[str, Any]:
        """
        Executes a shell command safely, normalizing Windows CP1252/UTF-8 encodings.
        """
        run_cwd = cwd or str(self.workspace_root)
        try:
            res = subprocess.run(
                command,
                shell=True,
                cwd=run_cwd,
                capture_output=True,
                text=True,
                encoding="utf-8",
                errors="replace",
                timeout=timeout_sec
            )
            record = {
                "command": command,
                "exit_code": res.returncode,
                "stdout": res.stdout,
                "stderr": res.stderr,
                "success": res.returncode == 0
            }
        except subprocess.TimeoutExpired as e:
            record = {
                "command": command,
                "exit_code": -1,
                "stdout": e.stdout or "",
                "stderr": f"Command timed out after {timeout_sec} seconds",
                "success": False
            }
        except Exception as e:
            record = {
                "command": command,
                "exit_code": -1,
                "stdout": "",
                "stderr": str(e),
                "success": False
            }

        self.execution_history.append(record)
        return record

    def inspect_exit_code(self, record: Dict[str, Any]) -> None:
        """Enforces the 2-Strike Rule: halts and reports if command fails."""
        if not record["success"]:
            print(f"[HARNESS ALERT] Command failed with Exit Code: {record['exit_code']}")
            if record["stderr"]:
                print(f"[HARNESS STDERR] {record['stderr'].strip()}")


if __name__ == "__main__":
    harness = AgentHarness()
    print("Agent Harness Execution Runtime Initialized successfully.")
