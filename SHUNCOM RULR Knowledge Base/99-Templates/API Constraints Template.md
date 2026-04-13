# API Constraints Template

## Overview
- API group: `<api-group>`
- Endpoint / Channel: ``<method path or ws-channel>``
- Canonical topic: `<topic>`
- Confidence: High / Medium / Low

## Provenance
> Copy from [Source Provenance Template](Source%20Provenance%20Template.md)

## Purpose
- <what this interface is for>

## Auth and scope
- Authentication: Public / Bearer / Session / Device-auth
- Permission: `<permission>`
- Scope rules: `<project/group/device scope>`

## Request shape
```yaml
Path params:
  <field>: <type>
Query params:
  <field>: <type>
Body:
  <field>: <type>
```

## Request field constraints
| Field | Required | Type | Rules | Evidence |
|---|---|---|---|---|
| `<field>` | Yes | string | `<validation>` | `[SRC:...]` |

## Business constraints
- <constraint 1>
- <constraint 2>
- <constraint 3>

## Side effects
- creates / updates / deletes `<entity>`
- triggers `<rule / sync / command>`
- emits `<websocket event>`
- writes `<system log / audit log>`

## Success response
```json
{
  "success": true,
  "data": {}
}
```

## Error model
| Code | Scenario | Notes |
|---|---|---|
| 400 | Validation error | <notes> |
| 401 | Auth failed | <notes> |
| 403 | Scope / permission denied | <notes> |
| 409 | Business conflict | <notes> |
| 422 | Semantic validation failed | <notes> |

## Logging and observability
- Audit fields: actor, target, action, status, timestamp
- Operational logs: request outcome, sync status, retries
- Metrics: latency / throughput / failure count if relevant

## Related docs
- [Documentation Standards](Documentation%20Standards.md)
- [System Flow Template](System%20Flow%20Template.md)
- [Source Provenance Template](Source%20Provenance%20Template.md)

## Open questions
- <question 1>
- <question 2>
