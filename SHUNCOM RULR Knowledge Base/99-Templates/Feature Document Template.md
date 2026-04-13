# Feature Document Template

## Overview
- Feature name: `<feature-name>`
- Feature ID: `FEAT-...`
- Module: `<module-name>`
- Priority: Critical / High / Medium / Low
- Status: Draft / Review / Approved / In Progress / Complete
- Owner: `<owner>`

## Provenance
> Copy from [Source Provenance Template](Source%20Provenance%20Template.md)

## Summary
- Mô tả ngắn gọn feature này làm gì.
- Vì sao feature này cần tồn tại.
- Giá trị nghiệp vụ chính.

## Scope
### In scope
- <item>
- <item>

### Out of scope
- <item>
- <item>

## Business goals
- <goal 1>
- <goal 2>
- <goal 3>

## Traceability
### Related stories
- `US-...` - <story name>

### Related flows
- `Flow ...` - <flow name>

### Related screens / contexts
- `<screen-name>`

## Functional requirements
| ID | Requirement | Priority | Notes |
|---|---|---|---|
| `FR-001` | <requirement> | High | <notes> |
| `FR-002` | <requirement> | Medium | <notes> |

## Non-functional requirements
| ID | Requirement | Target / Constraint |
|---|---|---|
| `NFR-001` | Performance | <target> |
| `NFR-002` | Security | <constraint> |
| `NFR-003` | Reliability | <constraint> |

## Main behavior
### Main scenario
1. <step>
2. <step>
3. <step>

### Alternate / exception scenarios
- <scenario 1>
- <scenario 2>

## Data and interfaces
### Entities touched
- <entity>
- <entity>

### APIs / channels touched
- `GET /...`
- `POST /...`
- `WS ...`

## Business constraints
- <constraint 1>
- <constraint 2>
- <constraint 3>

## Logging and audit implications
- Audit events: <events>
- Operational logs: <events>
- Failure logs: <events>

## Testing checklist
- [ ] Main scenario covered
- [ ] Validation errors covered
- [ ] Permission/scope covered
- [ ] Failure/retry behavior covered
- [ ] Logging/audit behavior covered

## Related docs
- [Documentation Standards](Documentation%20Standards.md)
- [High-Level Module Template](High-Level%20Module%20Template.md)
- [System Flow Template](System%20Flow%20Template.md)
- [API Constraints Template](API%20Constraints%20Template.md)

## Open questions
- <question 1>
- <question 2>
