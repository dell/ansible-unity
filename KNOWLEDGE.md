# KNOWLEDGE.md — ansible-unity

<!-- yaml-metadata-start -->
scope_paths: ["./"]
capture_git_sha: "301cd2815f4477fae7d9e39b9a973792df25b1b6"
status: "current"
auto_update: false
preview_before_apply: true
scaffold_version: "1.0"
# session_state: { is_complete: true }
<!-- yaml-metadata-end -->

<!-- quick-reference-start -->
## Agent Quick Reference

| Section | Heading | Summary | never_again_count |
|---------|---------|---------|-------------------|
| Component Overview | `## Component Overview` | dellemc.unity collection for Unity | — |
| Architectural Rationale | `## Architectural Rationale` | storops SDK; Ansible collection pattern | — |
| Failure Modes & Gotchas | `## Failure Modes & Gotchas` | SDK coupling, idempotency, verify_ssl | 0 |
| Implicit Contracts | `## Implicit Contracts` | Connection params, ordering, action groups | — |
<!-- quick-reference-end -->

## Five Questions Quick Reference

### What does it do?
Ansible Galaxy collection `dellemc.unity` (v2.1.0). Provides 18 modules for declarative, idempotent management of Dell Unity storage arrays. Uses `storops` (>=1.2.12) Python SDK.

### How do you modify it?
Create module file in `plugins/modules/`, add example playbook in `playbooks/modules/`, add unit test in `tests/unit/plugins/modules/`, append module FQCN to `meta/runtime.yml` action group.

### What breaks?
SDK version mismatch is a blocking defect. Missing action group entry causes `module_defaults` to silently skip the module. `verifycert: false` in production violates security constitution.

### What depends on it?
`storops` >=1.2.12, Ansible >= 2.15.0. Ordering: dependent resources must exist before referencing them.

### What's undocumented?
No shared base — modules call `utils.get_unity_connection()` directly. Uses `logging.basicConfig` with `CustomRotatingFileHandler`. Writes `ansible_unity.log` by default (5 MB rotate, 5 backups).

---

## Component Overview

Ansible Galaxy collection `dellemc.unity` (v2.1.0) for Dell Unity storage arrays. 18 modules covering volumes (LUNs), storage pools, hosts, host groups, snapshots, snapshot schedules, NAS servers, NFS exports, SMB shares, file systems, consistency groups, interfaces, and more.

---

## Architectural Rationale

Standard Ansible Galaxy collection layout. Each module is a self-contained Python file under `plugins/modules/` that communicates with the Unity REST API through the `storops` SDK.

**SDK strategy:** Static import. Version pinned at `>=1.2.12` in `requirements.txt`.

---

## Failure Modes & Gotchas

### 1. SDK version coupling

Each collection release is tested against exactly one SDK version (or tight range for PyU4V). A mismatch between collection and SDK version is a blocking defect. Never update `requirements.txt` SDK versions without verifying against the corresponding collection release notes.

### 2. Idempotency assumptions

Modules are designed to be idempotent but some parameters may be accepted by the module yet ignored by the underlying API. Always verify with a second run.

### 3. Verify SSL setting

`verifycert: false` is used in example playbooks but is a lab-only setting. Production requires `true`. Modules must not default to skipping verification.

### 4. Acceptance test cleanup

If tests fail mid-run, resources may be left on the array. Clean up manually before re-running.

### No Base Class

Like PowerMax, Unity does **not** have a `libraries/` or `shared_library/` directory. Module classes call `utils.get_unity_connection()` directly. There is no `UnityBase` to subclass.

### SDK Floor-Only Pin

`storops` uses a floor-only pin (`>=1.2.12`) with no ceiling. This is the loosest version constraint among all storage collections.

### Never Again

No incident-derived constraints recorded.

---

## Performance Characteristics

TBD — requires SME input.

---

## Implicit Contracts

**Connection parameters required:** All modules require `unispherehost`, `username`, `password`, `verifycert` — these are not optional.

**Resource ordering:** Dependent resources must exist before being referenced (e.g., filesystem before snapshot, volume group before volumes, policies before assignment).

**Action group registration:** Every new module must be appended to the `dellemc.unity.all` action group in `meta/runtime.yml`.

---

## Threading & Synchronization

Ansible handles concurrency via forks at the play level. Individual module executions are single-threaded.

---

## Build System & Configuration

| Command | Description |
|---------|-------------|
| `ansible-galaxy collection build` | Build collection tarball |
| `ansible-galaxy collection install <tarball>` | Install locally |
| `pytest tests/unit/` | Run unit tests |
| `ansible-playbook --syntax-check` | Validate playbook syntax |

---

## Operational Knowledge

Uses `logging.basicConfig` with `CustomRotatingFileHandler`. Writes `ansible_unity.log` by default (5 MB rotate, 5 backups).

---

## General Context

No additional context beyond what has been captured.

---

## References

- [Ansible Galaxy — dellemc.unity](https://galaxy.ansible.com/dellemc/unity)
- [Ansible Collection Developer Guide](https://docs.ansible.com/ansible/latest/dev_guide/developing_collections.html)

---

## Governance Spec Discrepancies

No discrepancies detected.
