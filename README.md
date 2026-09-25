# Agent Skills Vault 🧠

The Complete Enterprise Knowledge Repository, Skill Codex (1,430+ Skills), and Master Agent Harness Runtime for Autonomous AI Coding Agents.

---

## 📌 Repository Purpose & Architecture
This vault acts as the permanent, immutable **Working Memory on Disk** and execution harness for autonomous AI coding agents collaborating across enterprise projects:
- **[sadik004/behavioral-playwright](https://github.com/sadik004/behavioral-playwright)**: Stealth behavioral browser automation, anti-bot evasion, and closed-loop process control.
- **[sadik004/fastapi-clean-architecture](https://github.com/sadik004/fastapi-clean-architecture)**: 3-tier clean architecture, DSA optimization, and financial precision.

---

## 📂 Vault Hierarchy

```
agent-skills-vault/
├── harness/
│   ├── README.md               # Master Agent Harness Architecture & Scaffolding
│   ├── HARNESS_ARCHITECTURE.md # Execution runtime, tool dispatching & sandboxing
│   └── runtime_bridge.py       # Safe subprocess execution & encoding normalization
├── skills/                     # 1,430+ Production Skills
│   ├── scraping-production/    # 50 Master Guardrails, Kinematics, Swarms, Project 13
│   ├── browser-automation/     # Lifecycle pooling, Route abortion, CDP isolation
│   ├── fastapi-production/     # 3-Tier Architecture, Strict Financial Math (Decimal), Zero Raw SQL
│   ├── agent-harness/          # Agent Harness execution rules & scaffolding
│   ├── biomechanics/           # Plamondon Log-Normal Kinematics & Tremor models
│   ├── keystrokes/             # Polyphonic rollover & continuous Shift dynamics
│   └── ... (1,430+ domain-specific engineering & scientific skills)
├── scripts/
│   └── sync_skills.py          # Two-way sync engine between projects and global agent configs
└── README.md
```

---

## 🛡️ Core Operational Invariants
1. **Radical Anti-Sycophancy ("জিরো তেলবাজি" পলিসি)**: Deliver objective, mathematically grounded engineering facts. Flattery, emotional theatrics, or agreeing with flawed premises is strictly prohibited.
2. **2-Strike Rule**: If a selector, test, or terminal command fails twice, immediately halt, perform Root Cause Analysis (RCA), document it, and re-plan.
3. **Zero Hand-Waving & No Stubs**: Strictly no `# TODO: implement rest` or `pass` in production code.
4. **Mandatory Terminal Verification**: Never declare work complete without automated test suite execution and confirming exit code 0.
5. **Financial Precision**: Strictly `Decimal(18, 4)` for currency/pricing; binary floating-point `float` is strictly banned.

---

## 🚀 Two-Way Synchronization

Sync skills to a project workspace:
```bash
python scripts/sync_skills.py --to-workspace /path/to/repo/.agents/skills
```

Sync newly hardened skills from a workspace into this vault:
```bash
python scripts/sync_skills.py --from-workspace /path/to/repo/.agents/skills
```

Sync directly to global agent config:
```bash
python scripts/sync_skills.py --to-global
```
