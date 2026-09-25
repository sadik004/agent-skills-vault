#!/usr/bin/env python3
"""
Agent Skills Vault Sync Utility.
Synchronizes skills between agent-skills-vault and local workspace or global configs.

Usage:
  python scripts/sync_skills.py --to-workspace E:/Bug/.agents/skills
  python scripts/sync_skills.py --from-workspace E:/Bug/.agents/skills
  python scripts/sync_skills.py --to-global
"""

import os
import sys
import shutil
import argparse
from pathlib import Path

VAULT_ROOT = Path(__file__).resolve().parent.parent
VAULT_SKILLS = VAULT_ROOT / "skills"
GLOBAL_SKILLS = Path.home() / ".gemini" / "config" / "skills"

def sync_dir(src: Path, dst: Path, direction_name: str):
    if not src.exists():
        print(f"Source directory {src} does not exist!")
        return
    dst.mkdir(parents=True, exist_ok=True)
    for item in src.iterdir():
        if item.is_dir():
            target_sub = dst / item.name
            shutil.copytree(item, target_sub, dirs_exist_ok=True)
            print(f"Synced [{direction_name}] skill: {item.name}")

def main():
    parser = argparse.ArgumentParser(description="Sync agent skills vault")
    parser.add_argument("--to-workspace", type=str, help="Target workspace .agents/skills path")
    parser.add_argument("--from-workspace", type=str, help="Source workspace .agents/skills path to import")
    parser.add_argument("--to-global", action="store_true", help="Sync vault to ~/.gemini/config/skills/")
    parser.add_argument("--from-global", action="store_true", help="Sync ~/.gemini/config/skills/ into vault")

    args = parser.parse_args()

    if args.to_workspace:
        sync_dir(VAULT_SKILLS, Path(args.to_workspace), "Vault -> Workspace")
    elif args.from_workspace:
        sync_dir(Path(args.from_workspace), VAULT_SKILLS, "Workspace -> Vault")
    elif args.to_global:
        sync_dir(VAULT_SKILLS, GLOBAL_SKILLS, "Vault -> Global")
    elif args.from_global:
        sync_dir(GLOBAL_SKILLS, VAULT_SKILLS, "Global -> Vault")
    else:
        parser.print_help()

if __name__ == "__main__":
    main()
