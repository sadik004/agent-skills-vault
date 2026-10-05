---
name: zero-fraud-engineering
description: Enterprise zero-fraud engineering codex, mathematical rigor, anti-sycophancy governance, adversarial mutation gates, and reality verification for mission-critical software.
---

# Zero-Fraud Engineering & Mathematical Rigor Codex ("জিরো ফ্রড ইঞ্জিনিয়ারিং")

> **Core Philosophy:** "জিরো ফ্রড ইঞ্জিনিয়ারিং" (Zero-Fraud Engineering) & "জিরো তেলবাজি" (Radical Anti-Sycophancy).  
> **Primary Law:** Working code executes without error; honest code refuses to declare success without live, observable, cryptographically verified state changes.

---

## 1. Radical Anti-Sycophancy ("জিরো তেলবাজি" পলিসি)
1. **Objective Truth Over Flattery**: Agreeing with flawed premises, masking broken behavior, or artificially passing tests to please users, mentors, or reviewers is classified as engineering malpractice.
2. **The Test Illusion Trap**: A test suite with 100% green checkmarks can conceal complete architectural failure if assertions rely on tautologies (`assert True`), mocks, or unverified return codes.
3. **No Metric Impersonation**: Brier score is not ECE; static string generation is not runtime DOM evasion; synthetic packets are not physical PCIe DMA events. Every metric must be computed strictly via its mathematical formula.

---

## 2. The Verification-First Architecture
Under no circumstances may an untrusted layer establish trusted execution:

```text
Proposal (Agent / LLM / Deterministic Planner)
       <
Execution (WorkflowExecutor via PageSession)
       <
Observation (Live DOM Snapshot, Attributes, Elements)
       <
Verification (Independent WorkflowVerifier)
       <
Cryptographic Audit (WorkflowProvenanceChain HMAC-SHA256)
```

### Trust Boundary Rules:
- **The Planner Has Zero Verification Authority**: An AI agent or deterministic planner proposing a step sequence can never mark a step as `COMPLETED` or `VERIFIED`. Its proposal remains in `StepStatus.PENDING`.
- **The Executor Cannot Verify Itself**: Execution captures live runtime evidence (`dom_hash`, `url`, `element_count`, `inner_text`). Only the independent `WorkflowVerifier` evaluates whether the evidence satisfies postconditions.
- **Cryptographic Provenance Binding**: Observation bundles must be sealed at capture time with HMAC-SHA256 signatures binding execution IDs, session IDs, PIDs, and artifact hashes. `verify_chain_integrity()` strictly verifies that `rec.workflow_id == self.workflow_id`, eliminating cross-workflow injection.

---

## 3. Strict Rules of Reality Verification

### A. Physical OS Process Verification
- Claims of live browser automation must be backed by live OS process verification (`OpenProcess` on Windows or `os.kill(pid, 0)` on POSIX) in the OS process table.
- Mocks, simulators, and dry-runs must NEVER return `status: "success"` or register as `REAL_SUCCESS`.

### B. Live Artifact Hashing
- Artifacts (screenshots, recordings, HTML dumps, network logs) must be re-read directly from disk and their SHA-256 byte digests calculated live.
- Zero empty or placeholder files allowed.

### C. Live DOM Authority & Financial Precision
- **Missing vs. Empty Distinction**: Missing DOM element must return `None`. Present DOM element with empty text must return `""`. Conflating `None` and `""` causes false-positive extraction.
- **Financial Precision**: Binary floating-point `float` is strictly prohibited for monetary values. All currency math must use `Decimal(18, 4)`.
- **Precedence Order**:
  $$\text{Live DOM} > \text{JSON-LD} > \text{OpenGraph} > \text{Hydration State}$$

---

## 4. The 26 Invariant Laws of System Integrity

1. **Zero Monolithic Code Slop**: No monolithic multi-thousand-line files with untyped dict returns escaping the API boundary.
2. **Untrusted Existing Test Assumption**: Existing tests are evidence only. Passing existing tests does NOT grant a release pass.
3. **Falsification Over Confirmation**: Every claim must have an adversarial test designed to disprove it.
4. **Dry-Run Never Counts as Live Success**: A dry-run or static script generation must NEVER return `status: "success"` or register as `REAL_SUCCESS`.
5. **Swallowed Exceptions Never Count as Success**: Any silent catch (`except Exception: pass`) or fallback returning dummy success is classified as P0 fraud.
6. **Explicit Gating for Absent Providers**: Missing dependencies must raise `ProviderUnavailableError` or return `PROVIDER_UNAVAILABLE`, never fabricate success or dummy responses.
7. **Strict RNG Determinism**: Any method accepting `seed: int` must deterministically control all internal stochastic processes using isolated instances (`random.Random(traj_seed)`), never leaking to or from global state.
8. **No Metric Impersonation**: Distinct mathematical metrics must never be conflated, substituted, or approximated.
9. **Mutation Score Hurdle**: Test suites must achieve $\ge 85\%$ kill rate against in-memory adversarial mutations before production approval ($\ge 95\%$ for release, $100\%$ achieved in Phase 8).
10. **Zero Raw SQL / In-Memory O(1) Lookups**: In-memory lookups must be strictly $O(1)$ (`dict`/`set`); zero quadratic scans.
11. **Non-Destructive Observability**: Sniffers and metrics collectors must never alter intercepted response streams or introduce memory leaks.
12. **Double-Entry Auditing for State**: State storage must record timestamps, depths, and statuses without mutating historical audit records.
13. **Mandatory Terminal Verification**: Every gate run must execute cleanly from the terminal and output unambiguous metrics (exit code 0).
14. **Phased Lifecycle**: The repository must follow `RED -> REVIEW -> LOCK -> FIX -> GREEN`. No code fixing is permitted before baseline review.
15. **Decoupled Out-of-Process External Verification**: In-memory verification is untrusted; final release verification must execute via isolated OS subprocess pipes (`IndependentExternalVerifier`) to protect against single-process memory patching.
16. **Live Physical OS & Artifact Hashing**: Claims of browser execution require verified live OS PIDs (`OpenProcess`/`os.kill`) in the OS process table and live filesystem SHA-256 byte recalculation of all generated artifacts.
17. **Cryptographic HMAC Provenance Chains**: Observation bundles must be sealed at capture time with HMAC-SHA256 signatures binding execution IDs, session IDs, PIDs, and artifact hashes.
18. **Anti-Replay Nonce & Freshness Boundaries**: Previously verified evidence tokens cannot be replayed across runs; evidence must enforce strict timestamp freshness ($\Delta t < 60\text{s}$), out-of-process replay registries, and future-timestamp rejection.
19. **Strict Prohibition of Arbitrary Sleeps**: `time.sleep`, `asyncio.sleep` with magic numbers, and `page.wait_for_timeout` are strictly banned; dynamic DOM mutation checks and event listeners are mandatory.
20. **Zero Tautological Tests & Environment-Aware Provider Assertions**: Tautologies like `assert True` are classified as P0 fraud; optional modular providers must verify dynamic environment availability (`is Provider().is_available()`).
21. **Session & Workflow Identity Binding**: Workflows and PageSessions must be explicitly bound. Mismatched session IDs (`workflow.session_id != session.session_id`) or session-less execution must immediately fail with `WorkflowIntegrityError`.
22. **Zero Positional Ambiguity & Fallbacks**: Positional fallbacks (`.first()`, `.nth(0)`, `elements[0]`) on multi-element queries without explicit ranking metrics are strictly prohibited. Multi-match ambiguity must trigger resolution disambiguation or structured error.
23. **Anti-Loop & Zero-Progress Protection**: Execution pipelines must enforce strict loop protection (`LoopProtector`, `RunawayLoopError`). Repeated identical action sequences ($N \ge 3$) or zero DOM state hash mutation windows ($M \ge 4$) must trip fail-safes immediately.
24. **Mandatory Post-Recovery Live Verification**: Recovery attempts must actively verify the viability of the recovered target. A closed or dead session cannot be marked `RECOVERED`; it must terminate as `TERMINAL_FAILURE`.
25. **100% Adversarial Mutation Hurdle**: The complete system must achieve 100% kill score against external adversarial mutants (including state bypass, signature forgery, silent exception masking, and identity spoofing).
26. **Complete Phased Regression Invariant**: Across all phases (Phase 1 through Phase 8), all 560+ test suites and 140+ independent verification suites must run concurrently or in sequence with zero regressions, zero skipped required checks, and zero mocked core logic.

---

## 5. Machine Learning Mathematical Rigor & Catastrophic Loss Prevention
1. **Zero Hardcoded Conformal Coverage**: Conformal prediction sets must be calibrated on a disjoint calibration set and empirically validated on an untouched holdout set with actual realized empirical coverage ($P(y \in C(x))$).
2. **True Binning ECE**: ECE must strictly use true binning ($\sum_{m=1}^{M} \frac{|B_m|}{N} |\text{acc}(B_m) - \text{conf}(B_m)|$).
3. **Nested Cross-Validation**: Outer $K$-folds for honest evaluation $\times$ Inner $k$-folds for hyperparameter tuning. Zero in-sample tuning reporting.
4. **No Zombie Models**: Serialized models must be fully fitted Scikit-Learn estimators. No silent exception masking with dummy fallbacks.

---

## 6. Adversarial Attack Battery & Hardened Defenses (The 15 Fraud Attacks)

| Attack ID | Attack Vector | Vulnerability / Malpractice | Hardened Architectural Countermeasure |
| :--- | :--- | :--- | :--- |
| **ATTACK-P8-001** | Return `True` without execution | Empty workflow declaring success | `WorkflowOrchestrator` checks `not workflow.steps` and raises `ExecutionError`. |
| **ATTACK-P8-002** | Forge `WorkflowResult` | Synthetic `WorkflowResult` with fake `is_verified=True` | `validate_integrity()` checks non-empty provenance & step results; `WorkflowVerifier` audits HMAC signatures. |
| **ATTACK-P8-003** | Forge verification result | Altering evidence payload while claiming verified | `WorkflowProvenanceChain.verify_chain_integrity()` recalculates SHA-256 evidence digests against signed HMAC. |
| **ATTACK-P8-004** | Stale evidence replay | Reusing old tokens from previous workflows | `WorkflowVerifier` computes `freshness_delta_s = abs(now - ev_time)`; rejects if $> 60\text{s}$. |
| **ATTACK-P8-005** | Forge session identity | Executing Workflow A on Session B | `WorkflowOrchestrator` verifies `session.session_id == workflow.session_id`; raises `PolicyViolationError`. |
| **ATTACK-P8-006** | Forge workflow identity | Injecting step record from Workflow X into Workflow Y | `verify_chain_integrity()` strictly verifies `rec.workflow_id == self.workflow_id`. |
| **ATTACK-P8-007** | Replace evidence artifact | Modifying JSON evidence after step execution | Cryptographic hash binding in provenance record invalidates chain on any modified key/value. |
| **ATTACK-P8-008** | Modify DOM after capture | Zero-progress state mutation | `WorkflowVerifier` verifies that state-mutating actions produce non-zero DOM hash or URL delta. |
| **ATTACK-P8-009** | Fake browser/page object | Passing `session=None` or unbacked mock | `WorkflowExecutor` checks session presence and interfaces; raises typed `ExecutionError`. |
| **ATTACK-P8-010** | Forge MCP response | External client fabricating MCP result | MCP tool handler executes through authoritative framework and serializes verified result. |
| **ATTACK-P8-011** | Planner declares success | Planner trying to mark steps as `COMPLETED` | Planner only returns proposals with `StepStatus.PENDING`; has zero authority to set execution status. |
| **ATTACK-P8-012** | Executor declares success | Step with `None` result claiming verified | `WorkflowVerifier` explicitly rejects `result is None` or empty payloads without `allow_empty=True`. |
| **ATTACK-P8-013** | Recovery declares success | Dead dummy session recovery attempt | Dead session recovery fails live verification and enters `RecoveryState.TERMINAL_FAILURE` (never fake True). |
| **ATTACK-P8-014** | Direct tool bypass of policies | Invoking high-impact side effects directly | `ApprovalManager` forces approval ticket generation; execution halts with `ApprovalRequiredError`. |
| **ATTACK-P8-015** | Cross-session evidence substitution | Substituting Session B proof into Session A | `verify_workflow_result()` evaluates `result.session_id == expected_session_id`. |
