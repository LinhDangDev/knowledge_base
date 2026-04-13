# SHUNCOM IoT — Software Requirements Specification (SRS)

## 1. Mục đích
Tài liệu SRS này mô tả các yêu cầu hệ thống/functional requirements chính cho SHUNCOM IoT dựa trên manual, screenshots, checklist, user stories, và screen flows đã được tổng hợp.

## 2. Phạm vi hệ thống
Hệ thống hỗ trợ quản lý người dùng, project, thiết bị IoT, rules, cảnh báo, dashboard, và vận hành thiết bị trong một nền tảng tập trung.

## 3. Yêu cầu chức năng theo module

## 3.1 Authentication & Access
### FR-AUTH-01
Hệ thống phải cho phép user đăng nhập bằng credential hợp lệ.

### FR-AUTH-02
Hệ thống phải từ chối đăng nhập với tài khoản sai thông tin hoặc bị disable.

### FR-AUTH-03
Hệ thống phải hỗ trợ quản lý user, role, permission, và management scope.

### FR-AUTH-04
Hệ thống phải áp dụng management scope theo product category, project, và group khi hiển thị dữ liệu.

## 3.2 Project & GIS
### FR-PRJ-01
Hệ thống phải hiển thị project theo cấu trúc cây.

### FR-PRJ-02
Hệ thống phải cho phép tạo project với name, manager, address, coordinates, và map background khi hỗ trợ.

### FR-PRJ-03
Hệ thống phải cho phép gán thiết bị vào project.

### FR-PRJ-04
Hệ thống phải hỗ trợ phân bố thiết bị trên GIS/map context.

### FR-PRJ-05
Hệ thống phải cho phép cấu hình display information theo project.

## 3.3 Device Configuration
### FR-DEV-01
Hệ thống phải cho phép quản lý thiết bị theo 3 góc nhìn: Project, Type, Group.

### FR-DEV-02
Hệ thống phải hỗ trợ nhiều loại thiết bị trong Type view.

### FR-DEV-03
Hệ thống phải cho phép tạo thiết bị với form động theo category/product/subtype.

### FR-DEV-04
Hệ thống phải lưu Device information, Product Information, và Asset Info theo khả năng của từng loại thiết bị.

### FR-DEV-05
Hệ thống phải hỗ trợ search, column settings, pagination, import, export trong context thích hợp.

## 3.4 Smart Gateway
### FR-GW-01
Hệ thống phải cho phép tạo/sửa Smart Gateway.

### FR-GW-02
Hệ thống phải hỗ trợ các trường association như distribution box, circuit control, electricity meter khi áp dụng.

### FR-GW-03
Hệ thống phải hỗ trợ cấu hình gateway circuits theo nhiều dòng loop mapping.

### FR-GW-04
Hệ thống phải hỗ trợ các action vận hành như synchronization, configure circuits, set screen password, three-phase electric ratio, clear local rules khi thiết bị hỗ trợ.

## 3.5 Smart Light Controller
### FR-LC-01
Hệ thống phải cho phép tạo Smart Light Controller theo subtype.

### FR-LC-02
Hệ thống phải render field theo subtype đã chọn.

### FR-LC-03
Hệ thống phải hỗ trợ association giữa controller và luminaires.

### FR-LC-04
Hệ thống phải hỗ trợ các action vận hành phù hợp với loại controller.

## 3.6 Other Device Types
### FR-OD-01
Hệ thống phải hỗ trợ tạo và quản lý Lighting Pole.

### FR-OD-02
Hệ thống phải hỗ trợ tạo và quản lý Loop Control với các thông số kỹ thuật liên quan.

### FR-OD-03
Hệ thống phải hỗ trợ tạo và quản lý Smart Electric Meter với gateway association và meter-related fields.

## 3.7 Group & Lifecycle
### FR-GRP-01
Hệ thống phải cho phép tạo device group theo product category.

### FR-GRP-02
Hệ thống phải cho phép gán thiết bị vào group.

### FR-GRP-03
Hệ thống phải hỗ trợ đồng bộ group/multicast configuration khi applicable.

### FR-LIFE-01
Hệ thống phải hỗ trợ batch import thiết bị.

### FR-LIFE-02
Hệ thống phải hỗ trợ batch export thiết bị.

### FR-LIFE-03
Hệ thống phải kiểm tra dependency trước khi xóa thiết bị.

### FR-LIFE-04
Hệ thống phải hỗ trợ Recycle Bin, restore, và permanent delete.

## 3.8 Rule Management
### FR-RULE-01
Hệ thống phải cho phép tạo platform rules.

### FR-RULE-02
Hệ thống phải cho phép tạo local rules.

### FR-RULE-03
Hệ thống phải hỗ trợ đồng bộ local rules tới thiết bị và trả về sync result.

### FR-RULE-04
Hệ thống phải cho phép tạo alarm rules.

### FR-RULE-05
Hệ thống phải hỗ trợ receiving groups.

### FR-RULE-06
Hệ thống phải hỗ trợ alarm levels và update rules.

## 3.9 Dashboard & Display
### FR-DASH-01
Hệ thống phải cho phép cấu hình display information theo project.

### FR-DASH-02
Hệ thống phải cho phép cấu hình lighting schedules today.

### FR-DASH-03
Hệ thống phải cho phép cấu hình electricity consumption plan.

## 3.10 Operations & Analytics
### FR-OPS-01
Hệ thống phải cho phép thao tác thiết bị trong operation control context.

### FR-OPS-02
Hệ thống phải hiển thị device detail với thông tin và telemetry liên quan.

### FR-OPS-03
Hệ thống phải cung cấp statistical analysis/trend data khi dữ liệu sẵn có.

## 4. Module summary mapping
### Auth & Access
- Screens: Login, User Management, Permission Management, Management Scope
- Stories/flows: login, create user, configure scope

### Project & GIS
- Screens: Project tree, Add/Edit Project, Associated devices, map placement, Display Information
- Stories/flows: create project, assign devices, GIS distribution, dashboard config

### Device Configuration
- Screens: Type list, Add/Edit Device, Smart Gateway, Configure Circuits, Smart Light Controller, Luminaire Selector, Loop Control, Smart Electric Meter
- Stories/flows: create devices by type and manage key associations

### Group & Lifecycle
- Screens: Group view, Associated devices selector, Sync result, Batch Import/Export, Recycle Bin
- Stories/flows: group membership, multicast sync, import/export, recycle lifecycle

### Rule Management
- Screens: Running Rules, Local Rules, Sync Result, Alarm Rules, Other Configurations, Receiving Group
- Stories/flows: platform/local/alarm/receiving group flows

### Operations & Analytics
- Screens: Operation Control, Device Detail, Statistical Analysis
- Stories/flows: operations, detail, analytics

## 5. Traceability
Để traceability đầy đủ, tham chiếu tới:
- [User Stories BA](./shuncom-iot-ba-user-stories.md)
- [Luồng Màn Hình](./shuncom-iot-screen-flows.md)
- [Story ↔ Flow ↔ Screen ↔ Module Mapping](./shuncom-iot-story-flow-screen-module-mapping.md)

## 6. Giả định và giới hạn
- Tài liệu này được trích xuất từ UI/manual, chưa phải reverse-engineering từ code triển khai thực tế.
- Một số tên trường đã được chuẩn hóa theo ngữ nghĩa BA/SA.
- Các yêu cầu kỹ thuật sâu hơn cần được chốt ở tài liệu thiết kế solution/API/database.

## 7. Ghi chú
- SRS này là lớp cầu nối giữa BRD và implementation design.
- Khi vào phase phát triển, nên tiếp tục bổ sung endpoint specs, entity specs, state transitions, validation matrix, và error catalog.