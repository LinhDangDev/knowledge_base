# 📋 Device Types Reference

> Supporting quick reference for the current supported device set in SHUNCOM RULR.
>
> Canonical lifecycle/configuration contracts live in [03-Device Management Hub](03-Device%20Management%20Hub.md) and related canonical domain docs.

## Overview
Danh sách thiết bị hỗ trợ hiện tại dùng chuẩn hóa theo business truth mới.

## Supported device set
| Device Type | Role / Function | Notes |
|---|---|---|
| Gateway | Hub / parent communication device | top-level gateway role |
| Industrial Controller | Industrial control endpoint | current supported set |
| Smart Light Controller | Lighting control device | gồm nhiều communication/subtype patterns |
| Power Distribution Control (PDC) | Power distribution management | distribution cabinet / power control |
| Weather Sensor | Weather/environment feed | telemetry source |
| Environmental Sensor | Environment telemetry | sensor device |
| Smart Electric Meter | Energy metering | normalized name replacing generic “Smart Meter” |
| Lighting Pole | Physical infrastructure container | support association / location context |
| Lighting Fixture | Logical/physical lighting asset | critical for some controller use cases |
| Loop Control | Circuit / loop control | gateway-related in many cases |
| Smart Water Meter | Water metering device | current supported set |
| Leakage Monitoring | Leakage detection device | alarm/safety-oriented device |
| Indoor Light Controller | Indoor lighting control | kept as explicit supported type |
| Scene Panel | Scene/interaction control panel | current supported set |
| Accessory Device | Supporting accessory device | normalized spelling from “Accessary Device” |

## Quick grouping view
### Core infrastructure
- Gateway
- Power Distribution Control (PDC)
- Loop Control
- Lighting Pole

### Lighting control and lighting assets
- Smart Light Controller
- Indoor Light Controller
- Lighting Fixture
- Scene Panel

### Sensors and metering
- Weather Sensor
- Environmental Sensor
- Smart Electric Meter
- Smart Water Meter
- Leakage Monitoring

### Other operational devices
- Industrial Controller
- Accessory Device

## Important notes
- Một số thiết bị có thể có subtype/protocol-specific configuration, nhưng ở quick reference này ưu tiên top-level supported set.
- Nếu có khác biệt giữa file này và canonical domain docs, luôn tin canonical docs.
- `Accessory Device` là spelling chuẩn hóa dùng cho tài liệu hiện tại.

## Configuration references
- [03-Device Management Hub](03-Device%20Management%20Hub.md) — canonical lifecycle and configuration reference
- [05-Project Management](../05-User-Management/05-Project%20Management.md) — project assignment and GIS dependency
- [Device Troubleshooting Guide](Device%20Troubleshooting.md) — common device-side issues
- [Feature Requirements Checklist](../08-Development-Guide/Feature%20Requirements%20Checklist.md) — rollout/coverage cross-check
