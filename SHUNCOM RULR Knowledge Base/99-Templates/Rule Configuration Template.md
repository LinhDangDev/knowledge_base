# Rule Configuration Template

## Overview
- Rule name: `<rule-name>`
- Rule ID: `RULE-...`
- Rule type: `platform | local | alarm`
- Product / category: `<category>`
- Status: Draft / Review / Enabled / Disabled

## Provenance
> Copy from [Source Provenance Template](Source%20Provenance%20Template.md)

## Purpose
- Rule này giải quyết bài toán gì.
- Rule này tác động tới domain nào.
- Rule này là cloud-side hay device-side.

## Traceability
### Related stories
- `US-...` - <story>

### Related flows
- `Flow ...` - <flow>

### Related screens / contexts
- `<screen-name>`

## Rule metadata
| Field | Required | Description | Evidence |
|---|---|---|---|
| Rule name | Yes | <description> | `[SRC:IMG-...]` |
| Rule type | Yes | <description> | `[SRC:IMG-...]` |
| Effective date | Yes/No | <description> | `[SRC:IMG-...]` |
| Repeat period | Yes/No | <description> | `[SRC:IMG-...]` |
| Remarks | No | <description> | `[SRC:IMG-...]` |

## Trigger conditions
### Trigger list
| Trigger type | Required | Description | Constraints |
|---|---|---|---|
| Attribute trigger | Yes/No | <description> | <constraint> |
| Time trigger | Yes/No | <description> | <constraint> |
| Time range | Yes/No | <description> | <constraint> |
| Event trigger | Yes/No | <description> | <constraint> |
| Online/offline | Yes/No | <description> | <constraint> |

### Logic rules
- Meet all conditions / Meet any condition
- Max / min condition combinations if known
- Unsupported combinations if known

## Execute actions
| Action type | Target | Description | Constraints |
|---|---|---|---|
| Device control | Device / Group | <description> | <constraint> |
| Loop control | Gateway / Circuit | <description> | <constraint> |
| Notification | Group / User | <description> | <constraint> |

## Scope and target selection
- Triggered device rules: <rules>
- Devices to be operated: <rules>
- Group selection behavior: <rules>
- Same-batch / same-category constraints: <rules>

## Sync and execution behavior
### Platform rule
- Execution location: cloud/platform
- Runtime implications: <notes>

### Local rule
- Sync to device required: Yes/No
- Retry / resend behavior: <notes>
- Sync result visibility: <notes>

### Alarm rule
- Silent period: <notes>
- Auto-handle logic: <notes>
- Notification recipients: <notes>

## Business constraints
- <constraint 1>
- <constraint 2>
- <constraint 3>

## Logging and audit implications
- Rule create/update/enable/disable logs
- Sync result logs
- Alarm processing logs
- Notification delivery logs if applicable

## Testing checklist
- [ ] Trigger validation covered
- [ ] Unsupported condition combinations covered
- [ ] Scope and permission behavior covered
- [ ] Sync/retry behavior covered
- [ ] Logging behavior covered

## Related docs
- [Documentation Standards](Documentation%20Standards.md)
- [System Flow Template](System%20Flow%20Template.md)
- [API Constraints Template](API%20Constraints%20Template.md)

## Open questions
- <question 1>
- <question 2>
