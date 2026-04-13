# GIS Setup Guide

## Overview
- Canonical topic: GIS setup and location management
- Goal: Chuẩn hóa tri thức về GIS prerequisites, device coordinates, distribution behavior, zone/boundary concepts, và location-based operational constraints trong SHUNCOM RULR.
- Primary users: BA, PM, QA, Dev, GIS operator, project admin

## Provenance
### Source summary
```yaml
Document status: Canonical draft
Confidence: Medium
Last validated: 2026-04-12
Validated by: Claude Code
Primary source type: analysis
Canonical topic: gis-setup-guide
```

### Primary sources used
| Source | Path | Why it matters |
|---|---|---|
| Flow doc | `docs/shuncom-iot-screen-flows.md` | project creation and GIS-related user flows |
| BA doc | `docs/shuncom-iot-ba-user-stories.md` | GIS distribution business intent |
| Analysis doc | `SHUNCOM_RULR_IoT_Platform_Analysis.md` | GIS distribution methods and dashboard integration |
| Existing KB doc | `06-Project-Management/GIS Setup Guide.md` | previous GIS guide content |
| Related project doc | `05-User-Management/05-Project Management.md` | project hierarchy and display context |

### Validation gaps
- Map provider specifics (OpenStreetMap/Google/Mapbox) trong version cũ là design suggestions, chưa được xác nhận từ platform source hiện tại.
- Boundary schema và geofence implementation chi tiết chưa được xác nhận từ code/backend.

## Scope
### In scope
- GIS prerequisites ở cấp project
- Device coordinates
- GIS distribution flows
- Zone/boundary concepts ở mức logical guidance
- Dashboard/rule integration implications ở mức tài liệu định hướng, không phải contract backend cuối cùng

### Out of scope
- Vendor-specific production map integration contract
- Physical GIS schema cuối cùng
- Frontend map rendering implementation chi tiết

## Traceability
### Related stories
- `US-PRJ-02` - Tạo project
- `US-PRJ-04` - Gán thiết bị vào project
- `US-PRJ-06` - Phân bố thiết bị trên GIS
- `US-OPS-01` - Thao tác thiết bị từ Operation Control

### Related flows
- Flow 4 - Tạo Project
- Flow 5 - Gán Thiết bị vào Project
- Flow 23 - Thao tác Thiết bị từ Operation Control

### Main screens / contexts
| Screen / Context | Purpose | Evidence |
|---|---|---|
| Project creation/edit | chọn GIS/map environment và location basics | `[SRC:FLOW-4]` |
| GIS distribution view | đặt thiết bị trên bản đồ | `[SRC:ANALYSIS-gis]` |
| Operation Control > GIS Map | xem và thao tác thiết bị theo vị trí | `[SRC:ANALYSIS-dashboard]` |

## Core prerequisites
- Project nên có ngữ cảnh GIS/map phù hợp nếu muốn dùng map-based operations.
- Thiết bị cần có coordinates hoặc được phân bố lên map để hiển thị chính xác.
- Project/device scope phải cho phép user nhìn thấy đối tượng trên map.
- Một số use case location-based scheduling/rules phụ thuộc coordinates hợp lệ.

## Core capabilities
### 1. Project GIS enablement
- Project có thể được tạo với location/address/coordinates.
- GIS environment là phần của project setup/display context.
- GIS usefulness tăng mạnh ở sub-project / operational project level.

### 2. Device coordinate management
- Coordinates có thể đến từ manual entry, map selection, import, hoặc GPS-capable devices theo hướng dẫn cũ.
- Nhưng các cơ chế cụ thể này cần xem là setup options/guidance, không phải contract chắc chắn nếu chưa verify từ code.

### 3. Device distribution on map
| Mode | Meaning |
|---|---|
| Single distribution | đặt 1 thiết bị vào vị trí cụ thể |
| Batch path distribution | đặt nhiều thiết bị theo path |
| Fine-tuning | chỉnh marker sau khi đã đặt |

### 4. Geographic grouping concepts
- Zones / boundaries / project extents là logical concepts hữu ích cho quản lý khu vực.
- Tuy nhiên zone implementation cụ thể trong hệ thống hiện tại chưa được xác nhận đầy đủ từ source thật.

## Business constraints
- Coordinates là điều kiện gần như bắt buộc cho GIS distribution và sunrise/sunset-based logic.
- GIS distribution thường được mô tả là meaningful ở second-level/sub-project contexts.
- Data visibility trên map vẫn phải tuân theo project/group/device scope.
- Nếu device chưa gán đúng project hoặc chưa có location, dashboard/GIS experience sẽ không đầy đủ.

## Map/provider posture
Version cũ có mô tả OpenStreetMap / Google Maps / Mapbox và nhiều config rất chi tiết. Hiện các phần này nên được xem là:
- implementation options
- design suggestions
- not verified product contract
- không nên dùng làm căn cứ duy nhất để chốt provider production nếu chưa có source/deploy verification

Nếu sau này tìm được source code hoặc deployment config xác nhận provider thật, nên tách ra một doc `Map Provider Integration` riêng đã verify.

## Rule and dashboard implications
- GIS hỗ trợ dashboard operation control theo vị trí.
- Coordinates ảnh hưởng location-based schedules và sunrise/sunset logic.
- Geofence/proximity/zone-based rules là khả năng hợp lý theo hướng kiến trúc, nhưng cần verify trước khi coi là product contract.

## Logging and audit implications
- Audit log: thay đổi project GIS config, device coordinate updates, distribution actions.
- Operational log: batch distribution, fine-tuning results, location-related command context.
- Troubleshooting cần nhìn thấy vấn đề: missing coordinates, out-of-bound placement, wrong project context.

## Related docs
- [05-Project Management](../05-User-Management/05-Project%20Management.md)
- [06-Dashboard Interface](06-Dashboard%20Interface.md)
- [03-Device Management Hub](../03-Device-Management/03-Device%20Management%20Hub.md)
- [04-Rule Engine System](../04-Rule-Management/04-Rule%20Engine%20System.md)
- [API Endpoints Map](../02-System-Architecture/API%20Endpoints%20Map.md)

## Open questions
- Map provider thực tế của production/staging chưa được xác nhận từ source/deploy config.
- Boundary/polygon data contract, geofence support, và zone automation behavior cần backend/source confirmation trước khi dùng làm contract chính thức.
