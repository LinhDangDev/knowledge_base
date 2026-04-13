# Dashboard Interface

## Overview
- Canonical topic: Dashboard domain
- Goal: Chuẩn hóa tri thức về homepage dashboard, operation control, statistical analysis, alarm handling, rule view, và system log trong trải nghiệm vận hành.
- Primary users: Manufacturer, Project Admin, Project Member, maintenance team, BA, QA, Dev

## Provenance
### Source summary
```yaml
Document status: Canonical draft
Confidence: Medium
Last validated: 2026-04-12
Validated by: Claude Code
Primary source type: screenshot
Canonical topic: dashboard-interface
```

### Primary sources used
| Source | Path | Why it matters |
|---|---|---|
| Manual screenshot | `manual-images/p20_Image256.png` | project display info / energy composition source |
| Manual screenshot | `manual-images/p45_Image333.jpg` | alarm rules list/status/actions used by operations context |
| Flow doc | `docs/shuncom-iot-screen-flows.md` | flows 20-25 for display info, operation control, detail, stats |
| BA doc | `docs/shuncom-iot-ba-user-stories.md` | dashboard/project analytics intent |
| Traceability map | `docs/shuncom-iot-story-flow-screen-module-mapping.md` | dashboard/ops/analysis mapping |
| Analysis doc | `SHUNCOM_RULR_IoT_Platform_Analysis.md` | homepage sections, GIS, stats, alarm processing, system log |

### Validation gaps
- Exact widget naming/quantity across all project scenarios chưa được xác nhận hoàn toàn từ UI source hiện tại.
- WebSocket/channel implementation details là inferred system behavior, chưa phải code-level contract.

## Scope
### In scope
- Homepage dashboard sections
- Operation control via GIS map và device list
- Device detail and statistical analysis
- Operation & maintenance alarm handling
- Rule management view trong dashboard context
- System log view trong operational context

### Out of scope
- Frontend component implementation chi tiết
- Chart library / rendering internals
- Backend analytics computation internals

## Traceability
### Related stories
- `US-DASH-01` - Cấu hình Display Information
- `US-DASH-02` - Cấu hình Lighting schedules today
- `US-DASH-03` - Cấu hình Electricity Consumption Plan
- `US-OPS-01` - Thao tác thiết bị từ Operation Control
- `US-OPS-02` - Xem device detail
- `US-OPS-03` - Xem thống kê và xu hướng thiết bị

### Related flows
- Flow 20 - Cấu hình Display Information
- Flow 21 - Cấu hình Lighting Schedules Today
- Flow 22 - Cấu hình Electricity Consumption Plan
- Flow 23 - Thao tác Thiết bị từ Operation Control
- Flow 24 - Xem Chi tiết Thiết bị
- Flow 25 - Xem Thống kê / Phân tích

### Main screens / contexts
| Screen / Context | Purpose | Evidence |
|---|---|---|
| Homepage dashboard | thống kê + điều hướng chính | `[SRC:ANALYSIS-dashboard]` |
| Operation Control > GIS Map | thao tác thiết bị trên bản đồ | `[SRC:FLOW-23]` |
| Operation Control > Device List | list/filter/view details | `[SRC:FLOW-23]` |
| Device Detail | data overview, rules, alarms, records, statistics | `[SRC:FLOW-24]` |
| Statistical Analysis | charts/trends/export | `[SRC:FLOW-25]` |
| Operation & Maintenance | alarm processing | `[SRC:ANALYSIS-ops]` |
| System Log | log view by project/type/group | `[SRC:ANALYSIS-system-log]` |

## Business responsibilities
- Cung cấp snapshot vận hành của project hiện tại.
- Hỗ trợ điều khiển thiết bị trực tiếp hoặc theo nhóm từ operational views.
- Hỗ trợ phân tích thống kê, energy consumption, và trend views.
- Hiển thị alarms, rule status, system logs phục vụ vận hành hàng ngày.

## Dashboard structure
### Main homepage sections
| Section | Purpose |
|---|---|
| Statistical Data Overview | KPI/tổng quan thiết bị, trạng thái, energy, alarms |
| Operation Control | map + device list + quick actions |
| Statistical Analysis | charts, trends, export |
| Operation & Maintenance | alarm management, batch processing |
| Rule Management View | xem trạng thái rules trong ngữ cảnh dashboard |
| System Log | xem operation records/logs |

### Display configuration dependency
- Dashboard phụ thuộc cấu hình project `Display Information`.
- Module hiển thị khác nhau theo project.
- Energy-saving/consumption modules phụ thuộc source composition configuration `[SRC:IMG-p20_Image256.png]`.

## Operation control
### GIS map mode
- Yêu cầu project có GIS context và device có coordinates.
- Hỗ trợ icon theo loại thiết bị và trạng thái.
- Hỗ trợ quick actions trên controller/gateway theo scope.

### Device list mode
- Xem toàn bộ thiết bị hoặc theo product type.
- Có search, filter, pagination, và mở device detail.

## Device detail model
### Common sections
| Section | Purpose |
|---|---|
| Data Overview | trạng thái hiện tại / quick actions |
| Historical Data | dữ liệu theo thời gian |
| All Rules | platform + local rules liên quan |
| Alarm Information | alarm history / current state |
| Operation Records | command/action history |
| Statistical Analysis | trend và comparison |

### Rule/device interactions
- Từ device detail có thể đọc/clear/sync local rules theo nguồn phân tích.
- Điều này nối trực tiếp dashboard operational view với rule subsystem.

## Statistical analysis
### Core behaviors
- Filter theo thời gian: day/week/month/year.
- Xem trends về energy, performance, usage patterns.
- Export dữ liệu từ module hoặc enlarged view.
- Scope là selected project hoặc context hiện tại.

## Operation and maintenance
### Alarm management
- Hiển thị alarms theo project/type/group dimensions.
- Hỗ trợ individual processing và batch processing.
- Có filter theo severity/type/status và export.
- Có thể liên quan dispatch/work-order flow theo analysis doc.

## Rule management view
- Là operational projection của rule status trong dashboard.
- Chủ yếu để xem và đổi status; không phải nơi chính để edit content rule.

## System log view
- Tổ chức log theo project/type/group.
- Dùng để xem operation records và lịch sử tác động vận hành.
- Là điểm quan trọng cho audit/troubleshooting.

## Business constraints
- Dashboard data là project-scoped; user scope quyết định những gì nhìn thấy.
- Real-time behavior phụ thuộc device status updates và communication layer.
- GIS mode chỉ có giá trị khi coordinates và project GIS setup đã đúng.
- Statistical widgets phụ thuộc data-source configuration ở project display settings.
- Large datasets cần pagination/filtering/clustering theo phân tích hiện có.

## Logging and audit implications
- Audit log: dashboard configuration changes, alarm status changes, operational actions.
- Operational log: command execution results, map actions, export actions, device-detail operations.
- System log view là consumer của nhiều event từ auth/device/rule/project subsystems.

## API contract posture
- Các API touchpoints dưới đây là inventory-level references để nối domain doc với API map.
- Contract chính thức phải defer về [API Endpoints Map](../02-System-Architecture/API%20Endpoints%20Map.md) và backend/OpenAPI source nếu có.

## Data and integration touchpoints
| Type | Item | Purpose |
|---|---|---|
| API | `GET /dashboard/statistics` | overview KPIs |
| API | `GET /analytics/energy` | energy analysis |
| Realtime | device status updates | live dashboard refresh |
| Realtime | alarm notifications | ops visibility |
| Realtime | rule execution events | rule status feedback |

## Related docs
- [05-Project Management](../05-User-Management/05-Project%20Management.md)
- [03-Device Management Hub](../03-Device-Management/03-Device%20Management%20Hub.md)
- [04-Rule Engine System](../04-Rule-Management/04-Rule%20Engine%20System.md)
- [API Endpoints Map](../02-System-Architecture/API%20Endpoints%20Map.md)
- [Widget Reference](../07-Dashboard/Widget%20Reference.md)

## Open questions
- Exact realtime transport/channel contract và fallback behavior chưa được xác nhận từ source code.
- KPI aggregation precedence giữa project-level filtering, group-level filtering, và device-level overrides cần thêm backend confirmation.
