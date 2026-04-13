# System Flow Template

## Overview
- Flow name: `<flow-name>`
- Flow ID: `FLOW-...`
- Module: `<module-name>`
- Goal: `<what this flow achieves>`

## Provenance
> Copy from [Source Provenance Template](Source%20Provenance%20Template.md)

## Trigger
- `<what starts the flow>`

## Preconditions
- <condition 1>
- <condition 2>
- <condition 3>

## Actors
- User / Manufacturer / Project Admin / Project Member
- System
- Device / Gateway / Scheduler / Rule Engine

## Main flow
1. <step>
2. <step>
3. <step>
4. <step>

## Alternate flows
### A1
1. <step>
2. <step>

### A2
1. <step>
2. <step>

## Failure flows
### F1
- Cause: <cause>
- System response: <response>
- Recovery: <recovery>

### F2
- Cause: <cause>
- System response: <response>
- Recovery: <recovery>

## Validation and decision rules
- <validation 1>
- <validation 2>
- <validation 3>

## Result states
### Success
- <success result>

### Failure
- <failure result>

## Related APIs / channels
| Step | Interface | Purpose |
|---|---|---|
| 1 | `POST /...` | `<purpose>` |
| 2 | `WS ...` | `<purpose>` |

## Logs and audit
- Audit events: <events>
- Operational logs: <events>
- Error logs: <events>

## Traceability
- Story IDs: `US-...`
- Screen / Context: `<screen-name>`
- Related module doc: `<relative-path-to-module-doc>`

## Edge cases
- <edge case 1>
- <edge case 2>

## Open questions
- <question 1>
- <question 2>
