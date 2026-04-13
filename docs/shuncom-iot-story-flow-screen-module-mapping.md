# SHUNCOM IoT — Mapping Story ↔ Flow ↔ Screen ↔ Module

## Tổng quan
Bảng này dùng để traceability giữa user story, flow nghiệp vụ, màn hình, và module hệ thống.

| Module                 | Screen / Context                         | Flow ID | Flow Name                              | Story ID    | Story Name                             |
| ---------------------- | ---------------------------------------- | ------: | -------------------------------------- | ----------- | -------------------------------------- |
| Auth & Access          | Login                                    |       1 | Đăng nhập                              | US-AUTH-01  | Đăng nhập hệ thống                     |
| Auth & Access          | User Management                          |       2 | Tạo User                               | US-ADM-03   | Tạo user                               |
| Auth & Access          | Permission Management / Management Scope |       3 | Cấu hình Management Scope              | US-ADM-06   | Cấu hình phạm vi quản lý               |
| Project & GIS          | Project tab / Add Project                |       4 | Tạo Project                            | US-PRJ-02   | Tạo project                            |
| Project & GIS          | Project / Associated devices             |       5 | Gán Thiết bị vào Project               | US-PRJ-04   | Gán thiết bị vào project               |
| Device Configuration   | Type list / Add device                   |       6 | Tạo Thiết bị theo Type                 | US-DEV-03   | Tạo thiết bị                           |
| Device Configuration   | Smart Gateway form                       |       7 | Tạo Smart Gateway                      | US-GW-02    | Tạo Smart Gateway                      |
| Device Configuration   | Configure circuits                       |       8 | Cấu hình Gateway Circuits              | US-GW-03    | Cấu hình gateway circuits              |
| Device Configuration   | Smart Light Controller form              |       9 | Tạo Smart Light Controller             | US-LC-02    | Tạo controller theo subtype            |
| Device Configuration   | Associated luminaires selector           |      10 | Chọn Associated Luminaires             | US-LC-03    | Gán luminaires cho controller          |
| Device Configuration   | Loop Control form                        |      11 | Tạo Loop Control                       | US-LOOP-01  | Tạo Loop Control                       |
| Device Configuration   | Smart Electric Meter form                         |      12 | Tạo Smart Electric Meter                        | US-METER-01 | Tạo Smart Electric Meter                        |
| Group & Lifecycle      | Group form                               |      13 | Tạo Device Group                       | US-GRP-01   | Tạo device group                       |
| Group & Lifecycle      | Group / Associated devices               |      14 | Gán Thiết bị vào Group                 | US-GRP-02   | Gán thiết bị vào group                 |
| Rule Management        | Platform Rule form                       |      15 | Tạo Platform Rule                      | US-RULE-02  | Tạo Platform Rule                      |
| Rule Management        | Local Rule form                          |      16 | Tạo Local Rule                         | US-RULE-03  | Tạo Local Rule                         |
| Rule Management        | Sync Result dialog                       |      17 | Xem Kết quả Đồng bộ Local Rule         | US-RULE-04  | Đồng bộ local rule xuống thiết bị      |
| Rule Management        | Alarm Rule form                          |      18 | Tạo Alarm Rule                         | US-RULE-05  | Tạo Alarm Rule                         |
| Rule Management        | Receiving Group form                     |      19 | Tạo Receiving Group                    | US-RULE-06  | Tạo receiving group                    |
| Project & GIS          | Project edit / Display Information       |      20 | Cấu hình Display Information           | US-DASH-01  | Cấu hình Display Information           |
| Project & GIS          | Lighting schedules today                 |      21 | Cấu hình Lighting Schedules Today      | US-DASH-02  | Cấu hình Lighting schedules today      |
| Project & GIS          | Electricity consumption plan             |      22 | Cấu hình Electricity Consumption Plan  | US-DASH-03  | Cấu hình Electricity Consumption Plan  |
| Operations & Analytics | Operation Control                        |      23 | Thao tác Thiết bị từ Operation Control | US-OPS-01   | Thao tác thiết bị từ Operation Control |
| Operations & Analytics | Device Detail                            |      24 | Xem Chi tiết Thiết bị                  | US-OPS-02   | Xem device detail                      |
| Operations & Analytics | Statistical Analysis                     |      25 | Xem Thống kê / Phân tích               | US-OPS-03   | Xem thống kê và xu hướng thiết bị      |

---

## Mapping theo Module

### Auth & Access
- Screens: Login, User Management, Permission Management, Management Scope
- Stories: US-AUTH-01, US-ADM-03, US-ADM-04, US-ADM-06
- Flows: 1, 2, 3

### Project & GIS
- Screens: Project tree, Add/Edit Project, Associated devices, Display Information, Lighting schedules today, Electricity consumption plan
- Stories: US-PRJ-02, US-PRJ-04, US-PRJ-06, US-DASH-01, US-DASH-02, US-DASH-03
- Flows: 4, 5, 20, 21, 22

### Device Configuration
- Screens: Type list, Smart Gateway form, Configure circuits, Smart Light Controller form, Associated luminaires, Loop Control form, Smart Electric Meter form
- Stories: US-DEV-03, US-DEV-08, US-DEV-09, US-GW-02, US-GW-03, US-LC-02, US-LC-03, US-LOOP-01, US-METER-01, US-POLE-01
- Flows: 6, 7, 8, 9, 10, 11, 12

### Group & Lifecycle
- Screens: Group form, Group selector, Recycle Bin, Batch Import / Export
- Stories: US-GRP-01, US-GRP-02, US-GRP-03, US-BATCH-01, US-BATCH-02, US-LIFE-01, US-LIFE-02, US-LIFE-03
- Flows: 13, 14

### Rule Management
- Screens: Platform Rule, Local Rule, Sync Result, Alarm Rule, Receiving Group, Running Rules, Other Configurations
- Stories: US-RULE-02, US-RULE-03, US-RULE-04, US-RULE-05, US-RULE-06, US-RULE-07, US-RULE-08
- Flows: 15, 16, 17, 18, 19

### Operations & Analytics
- Screens: Operation Control, Device Detail, Statistical Analysis
- Stories: US-OPS-01, US-OPS-02, US-OPS-03
- Flows: 23, 24, 25

---

## Ghi chú
- Một screen có thể map tới nhiều story.
- Một story có thể dùng nhiều flow nếu có create/edit/sync/delete riêng.
- Bảng này là đầu vào tốt cho BA traceability và test scenario mapping.