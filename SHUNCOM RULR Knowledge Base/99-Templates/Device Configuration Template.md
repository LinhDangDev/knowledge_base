# Device Configuration Template

## Overview
- Device type: `<gateway | industrial-controller | smart-light-controller | pdc | weather-sensor | environmental-sensor | smart-electric-meter | lighting-pole | lighting-fixture | loop-control | smart-water-meter | leakage-monitoring | indoor-light-controller | scene-panel | accessory-device>`
- Product / subtype: `<product-name>`
- Canonical topic: `<device-topic>`
- Status: Draft / Review / Canonical

## Provenance
> Copy from [Source Provenance Template](Source%20Provenance%20Template.md)

## Purpose
- Thiết bị này dùng để làm gì.
- Thiết bị này thuộc domain nào.
- Thiết bị này liên kết với module nào.

## Traceability
### Related stories
- `US-...` - <story>

### Related flows
- `Flow ...` - <flow>

### Related screens / contexts
- `<screen-name>`

## Device information
| Field | Required | Type | Description | Evidence |
|---|---|---|---|---|
| `deviceName` | Yes/No | string | <description> | `[SRC:IMG-...]` |
| `productName` | Yes | string | <description> | `[SRC:IMG-...]` |
| `deviceNumber` | Yes/No | string | <description> | `[SRC:IMG-...]` |

## Associations
| Field | Required | Description | Constraint |
|---|---|---|---|
| Gateway | Yes/No | parent gateway | <constraint> |
| Project | Yes/No | project binding | <constraint> |
| Group | Yes/No | group binding | <constraint> |
| Related devices | Yes/No | fixtures / circuits / meters / panels / accessories | <constraint> |

## Location fields
| Field | Required | Type | Description |
|---|---|---|---|
| Latitude | Yes/No | number | <description> |
| Longitude | Yes/No | number | <description> |
| Altitude | Yes/No | number | <description> |

## Type-specific notes
### Smart Light Controller / Indoor Light Controller
- Có thể có subtype/protocol-specific fields.
- Có thể cần gateway hoặc direct communication tùy subtype.
- Có thể cần association với lighting fixture.

### Metering and monitoring devices
- Smart Electric Meter
- Smart Water Meter
- Leakage Monitoring
- Weather Sensor
- Environmental Sensor

Ghi rõ telemetry fields, communication method, và any required parent relation nếu có.

### Infrastructure/control devices
- Gateway
- Power Distribution Control (PDC)
- Loop Control
- Industrial Controller
- Scene Panel
- Accessory Device

Ghi rõ control capability, parent-child relation, và required associations nếu có.

## Product information
| Field | Required | Type | Description |
|---|---|---|---|
| `<field>` | Yes/No | `<type>` | <description> |

## Asset info
| Field | Required | Type | Description |
|---|---|---|---|
| Manufacturer | No | string | <description> |
| Price | No | number | <description> |
| Purchase date | No | date | <description> |
| Installation date | No | date | <description> |

## Business constraints
- <constraint 1>
- <constraint 2>
- <constraint 3>

## Supported operations
- <operation 1>
- <operation 2>
- <operation 3>

## Logging and sync implications
- Device creation log: <details>
- Device update log: <details>
- Sync / command result log: <details>

## Validation checklist
- [ ] Required fields confirmed from source
- [ ] Association rules confirmed
- [ ] Protocol-specific rules confirmed if relevant
- [ ] Scope / project / group behavior confirmed
- [ ] Open questions listed

## Related docs
- [Documentation Standards](Documentation%20Standards.md)
- [Source Provenance Template](Source%20Provenance%20Template.md)
- [High-Level Module Template](High-Level%20Module%20Template.md)

## Open questions
- <question 1>
- <question 2>
