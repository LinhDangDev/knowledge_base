# Rule Engine System

## Overview
- Canonical topic: Rule domain
- Goal: Chuẩn hóa tri thức về platform rules, local rules, alarm rules, update rules, trigger/action logic, sync behavior, và các constraint vận hành chính.
- Primary users: BA, PM, QA, Dev, Ops, automation operator

## Provenance
### Source summary
```yaml
Document status: Canonical draft
Confidence: Medium
Last validated: 2026-04-12
Validated by: Claude Code
Primary source type: screenshot
Canonical topic: rule-engine
```

### Primary sources used
| Source | Path | Why it matters |
|---|---|---|
| Manual screenshot | `manual-images/p52_Image352.jpg` | platform rule builder, conditions/actions, rule metadata |
| Manual screenshot | `manual-images/p45_Image333.jpg` | alarm rules list tabs/status/actions |
| Flow doc | `docs/shuncom-iot-screen-flows.md` | flows 15-19 cho platform/local/alarm/receiving-group/sync |
| BA doc | `docs/shuncom-iot-ba-user-stories.md` | business intent cho rule creation và alarm handling |
| Traceability map | `docs/shuncom-iot-story-flow-screen-module-mapping.md` | rule story-flow-screen mapping |
| Analysis doc | `SHUNCOM_RULR_IoT_Platform_Analysis.md` | platform/local/alarm/update-rule architecture và constraints |

### Validation gaps
- Payload/request schema chi tiết cho từng rule API chưa được xác nhận từ backend source code.
- Một số constraint chi tiết về unsupported condition combinations vẫn là manual-derived, chưa phải backend contract.

## Scope
### In scope
- Platform rules
- Local rules
- Alarm rules
- Receiving groups, alarm levels, update rules
- Trigger/action logic, silent periods, sync results, timezone dependencies

### Out of scope
- Rule engine implementation internals ở mức code
- Job scheduler/database schema chi tiết
- Notification provider integration chi tiết ngoài phạm vi manual-derived sources

## Traceability
### Related stories
- `US-RULE-02` - Tạo Platform Rule
- `US-RULE-03` - Tạo Local Rule
- `US-RULE-04` - Đồng bộ local rule xuống thiết bị
- `US-RULE-05` - Tạo Alarm Rule
- `US-RULE-06` - Tạo Receiving Group
- `US-DASH-02` - Cấu hình Lighting schedules today

### Related flows
- Flow 15 - Tạo Platform Rule
- Flow 16 - Tạo Local Rule
- Flow 17 - Xem Kết quả Đồng bộ Local Rule
- Flow 18 - Tạo Alarm Rule
- Flow 19 - Tạo Receiving Group

### Main screens / contexts
| Screen / Context | Purpose | Evidence |
|---|---|---|
| Platform Rule form | define metadata, conditions, actions, target devices | `[SRC:IMG-p52_Image352.jpg]` |
| Alarm rules list | list/alarm tabs/status/actions | `[SRC:IMG-p45_Image333.jpg]` |
| Local rule sync result dialog | monitor sync success/failure per device | `[SRC:FLOW-17]` |
| Other Configurations | receiving groups, alarm levels, update rules | `[SRC:ANALYSIS-rule-config]` |

## Business responsibilities
- Tự động hóa thiết bị ở mức cloud hoặc device-side.
- Quản lý cảnh báo, notification, silent period, và auto-handle logic.
- Tạo rule-scoped behavior theo product/category/group/project.
- Đồng bộ local rules xuống thiết bị và theo dõi kết quả sync.

## Rule families
### Platform rules
- Chạy ở platform/cloud side.
- Hỗ trợ multiple sub-rules, nhiều trigger conditions, nhiều execute actions.
- Dùng cho logic phức tạp, group-level orchestration, và rule-based control tập trung.

### Local rules
- Chạy ở device/gateway side sau khi sync xuống thiết bị.
- Simple hơn platform rules: thường 1 condition + 1 action per sub-rule theo nguồn hiện có.
- Dùng để giảm phụ thuộc mạng cho automation cơ bản.

### Alarm rules
- Dùng để tạo cảnh báo từ attribute/event/offline/device alarm conditions.
- Kèm severity, silent period, recipient groups, auto-handle behavior.

### Update rules
- Dùng để cấu hình chu kỳ refresh/read data từ thiết bị theo product type.
- Có tác động tới freshness của dashboard và monitoring data.

## Platform rule structure
### Rule metadata
Các field nhìn thấy từ nguồn hiện có:
- Rule name
- Rule type
- Product category
- Effective date / Forever
- Repeat period
- Remarks

### Trigger conditions
| Trigger type | Description | Important constraints |
|---|---|---|
| Attribute trigger | trigger từ attribute do device report | một số flow giới hạn 1 attribute trigger device = 1 device |
| Time trigger | timing / sunrise / sunset / interval | timezone và coordinates có thể ảnh hưởng |
| Time range | giới hạn execution window | theo nguồn hiện có, không nên đứng một mình trong một số tổ hợp |
| Online/offline | trigger theo connectivity | thường dùng kết hợp trigger khác |
| Trigger times | trigger nếu condition xảy ra N lần trong X phút | cần count/time-window logic |

### Condition logic
- `Meet all conditions` / AND
- `Meet any condition` / OR
- Một số tổ hợp trigger bị hạn chế theo nguồn manual-derived.

### Execute actions
| Action family | Examples |
|---|---|
| Device control | turn on/off/dim lights |
| Loop control | open/close circuits |
| Invoke service | device/product-specific operations |
| Notification / alarm action | recipient groups, silent-period behavior |

### Target selection
- Select device
- Select group
- Với một số loại thiết bị có thể chọn sub-components như fixtures hoặc circuits
- Same-batch / same-category constraint xuất hiện trong nhiều mô tả rule

## Local rule behavior
### Supported patterns
- Scheduled trigger
- Sunrise/sunset trigger
- Light sensitivity / sensor-based trigger
- Single action execution per simple rule pattern

### Sync lifecycle
1. User tạo local rule trên platform.
2. Platform gửi rule xuống device/gateway.
3. Thiết bị trả sync result.
4. UI hiển thị success/failure per device.
5. User có thể retry/resend failed sync.

### Local-rule value
- Giảm phụ thuộc mạng cho các automation cơ bản.
- Cho phép autonomous behavior khi platform/network không ổn định.

## Alarm rule behavior
### Alarm types
- Platform alarms
- Offline alarms
- Device alarms

### Core concepts
| Concept | Meaning |
|---|---|
| Silent period | chống alarm spam trong khoảng thời gian ngắn |
| Alarm level | phân mức severity |
| Receiving group | nhóm nhận cảnh báo |
| Auto-handle | tự process alarm cũ nếu điều kiện phục hồi đạt |
| Device exclusions | loại trừ một số thiết bị khỏi rule |

### Offline alarms
- Offline threshold không nên đặt quá ngắn nếu không muốn false alarms nhiều.
- Effective time, silent period, recipient groups, exclusion list là những setting quan trọng.

### Device alarms
- Dựa trên event từ thiết bị.
- Có thể gắn threshold/config theo loại controller/device hỗ trợ.

## Business constraints
- Timezone là constraint trọng yếu cho mọi rule time-based.
- Sunrise/sunset cần coordinates hợp lệ.
- Local rules cần sync thành công xuống device thì mới có hiệu lực ở device-side.
- Alarm rules cần silent period hợp lý để tránh spam.
- Một số trigger combinations có restriction theo manual-derived sources.
- Rule scope phụ thuộc product/category/project/group/device selection.

## Logging and audit implications
- Audit log: create/edit/enable/disable/copy/delete rule.
- Operational log: sync result, trigger evaluation result, execution result, retry result.
- Alarm log: generated / processed / auto-handled / acknowledged notifications.
- Update-rule log: read/refresh cycle outcome nếu hệ thống hỗ trợ ghi nhận.

## API contract posture
- Các API touchpoints dưới đây là inventory-level references để nối domain doc với API map.
- Contract chính thức phải defer về [API Endpoints Map](../02-System-Architecture/API%20Endpoints%20Map.md) và backend/OpenAPI source nếu có.

## Data and integration touchpoints
| Type | Item | Purpose |
|---|---|---|
| API | `GET /rules/platform` | list platform rules |
| API | `POST /rules/platform` | create platform rule |
| API | `POST /rules/local` | create local rule |
| API | `POST /rules/local/:ruleId/sync` | sync local rule |
| API | `GET /rules/alarms` | list alarm rules |
| Realtime | rule execution events | dashboard status / monitoring |
| Realtime | alarm notifications | ops + maintenance views |

## Related docs
- [03-Device Management Hub](../03-Device-Management/03-Device%20Management%20Hub.md)
- [05-Project Management](../05-User-Management/05-Project%20Management.md)
- [06-Dashboard Interface](../06-Project-Management/06-Dashboard%20Interface.md)
- [API Endpoints Map](../02-System-Architecture/API%20Endpoints%20Map.md)
- [Rule Configuration Patterns](Rule%20Configuration%20Patterns.md)

## Open questions
- Giới hạn chính xác của rule combination validation trong backend chưa được xác nhận từ source code.
- Notification channels, escalation workflow, và retry policy chi tiết cần backend/spec confirmation nếu dùng làm contract chính thức.
