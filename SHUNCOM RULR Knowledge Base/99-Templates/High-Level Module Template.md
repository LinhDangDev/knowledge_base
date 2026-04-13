# High-Level Module Template

## Overview
- Module name: `<module-name>`
- Domain: `<domain>`
- Primary users: `<users>`
- Goal: `<why this module exists>`
- Canonical status: Draft / Review / Canonical

## Provenance
> Copy from [Source Provenance Template](Source%20Provenance%20Template.md)

## Scope
### In scope
- <item>
- <item>

### Out of scope
- <item>
- <item>

## Business responsibilities
- <responsibility 1>
- <responsibility 2>
- <responsibility 3>

## Actors
| Actor | Role in module | Notes |
|---|---|---|
| Manufacturer | <action> | <notes> |
| Project Admin | <action> | <notes> |
| Project Member | <action> | <notes> |
| System | <action> | <notes> |
| Device | <action> | <notes> |

## Main screens / contexts
| Screen / Context | Purpose | Evidence |
|---|---|---|
| `<screen-name>` | `<purpose>` | `[SRC:IMG-...]` |

## Traceability
### Related stories
- `US-...` - <story name>

### Related flows
- `Flow ...` - <flow name>

### Related APIs / channels
- `GET /...`
- `POST /...`
- `WS ...`

## Main entities
| Entity | Description | Key relationships |
|---|---|---|
| `<entity>` | `<description>` | `<relations>` |

## Core behaviors
### Behavior 1
1. <step>
2. <step>
3. <step>

### Behavior 2
1. <step>
2. <step>
3. <step>

## Business constraints
- <constraint 1>
- <constraint 2>
- <constraint 3>

## Permissions and scope rules
- Required roles / permissions: `<permission-list>`
- Project scope rules: `<rules>`
- Group / device scope rules: `<rules>`

## Data and integration touchpoints
| Type | Item | Purpose |
|---|---|---|
| API | `<endpoint>` | `<purpose>` |
| Realtime | `<channel>` | `<purpose>` |
| Data | `<entity/table>` | `<purpose>` |

## Logging and audit implications
- Audit log should capture: <events>
- Operational log should capture: <events>
- Failure events should capture: <events>

## Edge cases
- <edge case 1>
- <edge case 2>
- <edge case 3>

## Related docs
- [System Overview](../01-Overview/01-System%20Overview.md)
- [API Endpoints Map](../02-System-Architecture/API%20Endpoints%20Map.md)
- [Testing Scenarios](../08-Development-Guide/Testing%20Scenarios.md)

## Open questions
- <question 1>
- <question 2>
