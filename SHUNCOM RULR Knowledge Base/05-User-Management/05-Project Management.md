# Project Management

## Overview
- Canonical topic: Project domain
- Goal: Chuẩn hóa tri thức về project hierarchy, project-device association, display information, lighting schedules, electricity consumption plan, và GIS distribution.
- Primary users: BA, PM, QA, Dev, Ops, project admin, GIS operator

## Provenance
### Source summary
```yaml
Document status: Canonical draft
Confidence: Medium
Last validated: 2026-04-12
Validated by: Claude Code
Primary source type: screenshot
Canonical topic: project-management
```

### Primary sources used
| Source | Path | Why it matters |
|---|---|---|
| Manual screenshot | `manual-images/p20_Image256.png` | Display information > energy saving overview / energy composition |
| Flow doc | `docs/shuncom-iot-screen-flows.md` | flows 4, 5, 20, 21, 22 |
| BA doc | `docs/shuncom-iot-ba-user-stories.md` | project creation, GIS, display-info, schedule, ECP intent |
| Traceability map | `docs/shuncom-iot-story-flow-screen-module-mapping.md` | project/dashboard flow mapping |
| Analysis doc | `SHUNCOM_RULR_IoT_Platform_Analysis.md` | project hierarchy, GIS distribution methods, ECP, display modules |

### Validation gaps
- Tên đầy đủ của tất cả 8 dashboard modules có thể khác nhẹ giữa manual screenshot và tài liệu cũ.
- Polygon/boundary backend schema cho GIS chưa được xác nhận từ code.

## Scope
### In scope
- Project hierarchy và default project buckets
- Project creation / edit / association
- Display information configuration
- Lighting schedules today
- Electricity consumption plan (ECP)
- GIS map distribution

### Out of scope
- GIS provider integration implementation chi tiết
- Database geometry schema chi tiết
- Dashboard widget rendering internals

## Traceability
### Related stories
- `US-PRJ-02` - Tạo project
- `US-PRJ-04` - Gán thiết bị vào project
- `US-PRJ-06` - Phân bố thiết bị trên GIS
- `US-DASH-01` - Cấu hình Display Information
- `US-DASH-02` - Cấu hình Lighting schedules today
- `US-DASH-03` - Cấu hình Electricity Consumption Plan

### Related flows
- Flow 4 - Tạo Project
- Flow 5 - Gán Thiết bị vào Project
- Flow 20 - Cấu hình Display Information
- Flow 21 - Cấu hình Lighting Schedules Today
- Flow 22 - Cấu hình Electricity Consumption Plan

### Main screens / contexts
| Screen / Context | Purpose | Evidence |
|---|---|---|
| `Device configuration > Project` | create/edit project và hierarchy | `[SRC:FLOW-4]` |
| Associated devices | bind thiết bị vào project | `[SRC:FLOW-5]` |
| Display information | chọn module/style/content cho project dashboard | `[SRC:FLOW-20]` |
| Energy saving overview | chọn energy composition / data source | `[SRC:IMG-p20_Image256.png]` |
| GIS distribution screen | đặt thiết bị lên bản đồ / path distribution | `[SRC:ANALYSIS-gis]` |

## Business responsibilities
- Tổ chức thiết bị theo project hierarchy.
- Cung cấp scope chính cho dashboard, GIS, rules, và access control.
- Quản lý display information cho homepage theo project.
- Quản lý lịch chiếu sáng và ECP ở cấp project.

## Project hierarchy model
| Level | Role |
|---|---|
| Top-level project | root container / organization grouping |
| Sub-project | operational scope chính cho device distribution và GIS |
| Associated devices | thiết bị thuộc project |
| Unassigned project | bucket mặc định cho thiết bị chưa gán project |

## Core capabilities
### 1. Create and maintain projects
- Tạo project với tên, manager, mô tả, địa chỉ, coordinates, map/background mode.
- Sửa/xóa/move project theo hierarchy nếu quyền cho phép.

### 2. Associate devices
- Project là context để nhìn thấy và vận hành thiết bị.
- Thiết bị có thể được gán vào project từ project page hoặc trong onboarding/import flow.

### 3. Configure display information
- Chọn style, usage scenario, title settings, modules bật/tắt.
- Có preview và có thể batch-apply cho project khác theo nguồn hiện có.

### 4. Configure lighting schedules
- Hỗ trợ fixed time hoặc sunrise/sunset hoặc sensor threshold based logic.
- Cấu hình này liên kết chặt với dashboard và rule/schedule behavior.

### 5. Configure ECP
- Kế hoạch điện năng năm/tháng/ngày.
- Dùng cho dashboard energy overview và cảnh báo vượt ngưỡng.

### 6. GIS distribution
- Đặt thiết bị theo tọa độ cụ thể hoặc phân bố hàng loạt theo path.
- Có fine-tuning coordinates sau khi đã lên map.

## Display information model
### Common display configuration areas
| Area | Purpose |
|---|---|
| Style / theme | hình thức hiển thị homepage |
| Title settings | tên project / màu / font |
| Module switches | bật tắt module thống kê / hiển thị |
| Usage scenario | ngữ cảnh vận hành như smart lighting |
| Preview | xem trước layout |
| Batch apply | copy config sang project khác |

### Energy saving overview
- Screenshot xác nhận lựa chọn `energy consumption composition` theo source như Smart Electric Meter hoặc Smart light controller `[SRC:IMG-p20_Image256.png]`.
- Điều này cho thấy analytics/data-source configuration là một phần của project display settings.

## GIS distribution behavior
### Preconditions
- Thường cần second-level project theo analysis doc.
- Thiết bị phải có hoặc được gán coordinates.
- Project phải dùng GIS environment nếu muốn map distribution đầy đủ.

### Distribution methods
| Method | Summary |
|---|---|
| Single device | chọn 1 device rồi đặt vị trí trực tiếp |
| Batch by path | chọn nhiều device rồi phân bố dọc path |
| Fine-tune | kéo/thả để chỉnh tọa độ |

## Business constraints
- Unassigned project là bucket mặc định nhưng có thể tạo rủi ro visibility nếu thiết bị chưa gán đúng project.
- GIS distribution thường chỉ có ý nghĩa đầy đủ ở sub-project / second-level project.
- Sunrise/sunset schedule phụ thuộc coordinates hợp lệ.
- Dashboard và analytics phụ thuộc data-source composition được chọn ở display information.
- ECP cần annual/monthly/daily target hợp lý; warning ratio ảnh hưởng hiển thị cảnh báo.
- Project scope ảnh hưởng user visibility, dashboard data, và rule targeting.

## Logging and audit implications
- Audit log: create/edit/delete/move project, device association/disassociation.
- Operational log: display-info updates, GIS redistribution, schedule/ECP changes.
- Analytics dependency log: thay đổi data source có thể ảnh hưởng dashboard interpretation.

## API contract posture
- Các API touchpoints dưới đây là inventory-level references để nối domain doc với API map.
- Contract chính thức phải defer về [API Endpoints Map](../02-System-Architecture/API%20Endpoints%20Map.md) và backend/OpenAPI source nếu có.

## Data and integration touchpoints
| Type | Item | Purpose |
|---|---|---|
| API | `GET /projects` | list project hierarchy and summary |
| API | `POST /projects` | create project |
| API | device/project association flows | bind devices |
| Data | project, group, coordinates, boundary | GIS and scope |
| Dashboard | project-based statistics | homepage / analytics |

## Related docs
- [03-Device Management Hub](../03-Device-Management/03-Device%20Management%20Hub.md)
- [06-Dashboard Interface](../06-Project-Management/06-Dashboard%20Interface.md)
- [04-Rule Engine System](../04-Rule-Management/04-Rule%20Engine%20System.md)
- [GIS Setup Guide](../06-Project-Management/GIS%20Setup%20Guide.md)
- [API Endpoints Map](../02-System-Architecture/API%20Endpoints%20Map.md)

## Open questions
- Boundary/polygon data contract và validation rules cho GIS chưa được xác nhận từ source code/backend.
- Rule precedence giữa project-level display schedule, local rules, và platform rules cần thêm confirmation nếu dùng làm contract nghiệp vụ chính thức.
