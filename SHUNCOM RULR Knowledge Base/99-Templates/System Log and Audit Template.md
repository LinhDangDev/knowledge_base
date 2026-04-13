# System Log and Audit Template

## Overview
- Domain: `<auth | device | project | rule | dashboard | gis | analytics>`
- Log type: `audit | operational | device-event | sync-result`
- Goal: `<why these logs exist>`

## Provenance
> Copy from [Source Provenance Template](Source%20Provenance%20Template.md)

## Logging scope
- What actions must be logged
- What actions should not be logged
- Which fields may contain sensitive data

## Event catalog
| Event ID | Event name | Trigger | Actor | Target | Result |
|---|---|---|---|---|---|
| `LOG-001` | `<event-name>` | `<when fired>` | `<actor>` | `<target>` | `<result>` |

## Required fields
| Field | Required | Description |
|---|---|---|
| `timestamp` | Yes | event time |
| `actorId` | Yes | user/system/device |
| `actorType` | Yes | user / system / device |
| `action` | Yes | operation performed |
| `targetType` | Yes | device / rule / project / user |
| `targetId` | Yes | target identifier |
| `status` | Yes | success / failed / queued |
| `details` | Optional | structured payload |

## Retention and visibility
- Retention period: `<duration or TBD>`
- Viewer roles / reader roles: `<roles>`
- Export capability: Yes / No
- Masking requirement: `<fields to mask>`

## Query and filtering needs
- By project
- By group
- By device
- By actor
- By time range
- By result status

## Alerting / escalation links
- Which log events should trigger alarms or notifications
- Which events are for audit only

## Related APIs / screens
- `<system-log-screen>`
- `GET /logs/...`
- export flow / filter flow

## Open questions
- <question 1>
- <question 2>
