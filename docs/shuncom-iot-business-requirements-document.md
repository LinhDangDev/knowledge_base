# SHUNCOM IoT — Business Requirements Document (BRD)

## 1. Mục đích
Tài liệu BRD này mô tả các yêu cầu nghiệp vụ cấp cao của SHUNCOM IoT, tập trung vào mục tiêu kinh doanh, phạm vi, actor chính, năng lực nghiệp vụ cần có, và kết quả mong đợi của hệ thống.

## 2. Mục tiêu kinh doanh
- Tạo một nền tảng quản lý IoT tập trung cho nhiều loại thiết bị
- Hỗ trợ smart lighting và các kịch bản điều khiển/giám sát liên quan
- Quản trị người dùng và dữ liệu theo role, permission, và management scope
- Cấu hình automation, cảnh báo, và vận hành theo project / group / type
- Hỗ trợ dashboard và phân tích phục vụ điều hành

## 3. Stakeholders chính
- Chủ đầu tư / business owner
- Product owner
- Operations team
- System administrators
- Project administrators
- Device / lighting / gateway operators
- QA / developers / analysts

## 4. Actors nghiệp vụ
- Người dùng hệ thống
- Quản trị viên hệ thống
- Quản trị viên project
- Quản trị viên thiết bị
- Gateway operator
- Lighting operator
- Metering operator
- Network operator
- Energy manager

## 5. Năng lực nghiệp vụ bắt buộc
### 5.1 Authentication & Access
- Đăng nhập hệ thống
- Quản lý user
- Quản lý role
- Quản lý permission
- Quản lý management scope

### 5.2 Project & GIS
- Quản lý project theo cây
- Gán thiết bị vào project
- Phân bố thiết bị trên GIS
- Cấu hình dashboard theo project

### 5.3 Device Configuration
- Quản lý thiết bị theo Project / Type / Group
- Tạo và cấu hình nhiều loại thiết bị
- Lưu product information và asset information
- Hỗ trợ configuration riêng cho gateway/controller/meter/loop

### 5.4 Group & Lifecycle
- Tạo group thiết bị
- Gán thiết bị vào group
- Hỗ trợ multicast/group sync
- Import/export thiết bị
- Recycle bin và xóa có dependency check

### 5.5 Rule Management
- Tạo platform rule
- Tạo local rule
- Đồng bộ local rule
- Tạo alarm rule
- Quản lý receiving groups
- Quản lý alarm levels và update rules

### 5.6 Operations & Analytics
- Thao tác thiết bị từ operation control
- Xem chi tiết thiết bị
- Xem phân tích và thống kê

## 6. Phạm vi nghiệp vụ theo module
### Auth & Access
Tập trung vào ai được truy cập hệ thống và nhìn thấy dữ liệu nào.

Các màn hình/chức năng chính:
- Login
- User Management
- Permission / Scope Management

Phạm vi nghiệp vụ:
- Đăng nhập
- Tạo user
- Gán role chuẩn
- Cấu hình management scope

### Project & GIS
Tập trung vào cấu trúc project, vị trí địa lý, và context vận hành.

Các màn hình/chức năng chính:
- Project tree
- Add/Edit Project
- Associated devices
- Distributed devices / map placement
- Display Information

Phạm vi nghiệp vụ:
- Tạo project
- Gán thiết bị vào project
- Phân bố thiết bị trên GIS
- Cấu hình dashboard theo project

### Device Configuration
Tập trung vào onboarding và cấu hình thiết bị theo từng loại.

Các màn hình/chức năng chính:
- Type list
- Add/Edit device
- Smart Gateway form
- Configure circuits
- Smart Light Controller form
- Luminaire selector
- Loop Control form
- Smart Electric Meter form

Phạm vi nghiệp vụ:
- Tạo thiết bị theo type
- Tạo/cấu hình gateway
- Tạo controller và gán luminaires
- Tạo loop control, smart meter, lighting pole
- Quản lý Product Information / Asset Info

### Group & Lifecycle
Tập trung vào tổ chức thiết bị theo nhóm và quản lý vòng đời.

Các màn hình/chức năng chính:
- Group view
- Associated devices selector
- Sync result
- Batch Import / Batch Export
- Recycle Bin

Phạm vi nghiệp vụ:
- Tạo device group
- Gán thiết bị vào group
- Đồng bộ group/multicast
- Import/export hàng loạt
- Recycle bin và vòng đời xóa/khôi phục

### Rule Management
Tập trung vào rule-based automation và cảnh báo.

Các màn hình/chức năng chính:
- Running Rules
- Local Rules
- Sync Result dialog
- Alarm Rules
- Other Configurations
- Receiving Group

Phạm vi nghiệp vụ:
- Tạo platform rule
- Tạo local rule
- Đồng bộ local rule
- Tạo alarm rule
- Tạo receiving group
- Quản lý alarm levels / update rules / running rules

### Operations & Analytics
Tập trung vào điều hành thực tế và khai thác dữ liệu.

Các màn hình/chức năng chính:
- Operation Control
- Device Detail
- Statistical Analysis

Phạm vi nghiệp vụ:
- Thao tác thiết bị từ operation control
- Xem chi tiết thiết bị
- Xem thống kê và xu hướng thiết bị

## 7. Business Rules cấp cao
- Chỉ user hợp lệ và active mới được đăng nhập
- Dữ liệu hiển thị phụ thuộc vào role và management scope
- Thiết bị nên được gán project/group đúng context quản lý
- Một số loại thiết bị yêu cầu association bắt buộc như gateway hoặc luminaires
- Xóa thiết bị phải đi kèm dependency check
- Local rules phải có cơ chế sync và phản hồi kết quả
- Dashboard/project display là một phần của cấu hình nghiệp vụ, không chỉ là UI preference

## 8. Thành công mong đợi
- Thiết bị được onboarding và quản lý tập trung
- Người dùng nhìn đúng dữ liệu theo phạm vi
- Rule và alert hoạt động đúng ngữ cảnh thiết bị
- Operations team có đủ màn hình để giám sát và thao tác
- Business team có đủ dashboard và dữ liệu phân tích

## 9. Tài liệu chi tiết tham chiếu
- [BRD Overview](./shuncom-iot-brd-overview.md)
- [User Stories BA](./shuncom-iot-ba-user-stories.md)
- [Luồng Màn Hình](./shuncom-iot-screen-flows.md)
- [Story/Flow/Screen/Module Mapping](./shuncom-iot-story-flow-screen-module-mapping.md)

## 10. Ghi chú
- BRD này là mức nghiệp vụ, chưa đi sâu vào giải pháp kỹ thuật cụ thể.
- Khi làm việc với vendor/dev team, tài liệu này nên đi kèm SRS để chốt rõ các yêu cầu hệ thống.