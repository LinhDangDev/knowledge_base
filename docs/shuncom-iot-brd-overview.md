# SHUNCOM IoT — BRD Overview

## 1. Mục tiêu tài liệu
Tài liệu này là điểm vào tổng quan cho bộ BRD/SRS của SHUNCOM IoT. Nó tóm tắt mục tiêu nghiệp vụ, phạm vi hệ thống, các phân hệ chính, và liên kết đến các tài liệu chi tiết hơn trong `docs/`.

## 2. Bối cảnh nghiệp vụ
SHUNCOM IoT là nền tảng quản lý thiết bị IoT tập trung, hướng đến các kịch bản như smart lighting, gateway control, metering, rule automation, cảnh báo, và vận hành theo project/group/scope.

Hệ thống phục vụ các nhu cầu chính:
- Quản trị truy cập và phân quyền theo role/scope
- Quản lý project và phân bố GIS
- Quản lý nhiều loại thiết bị theo Type
- Tổ chức thiết bị theo Group và vòng đời thiết bị
- Cấu hình automation bằng platform rules / local rules / alarm rules
- Vận hành thiết bị, xem chi tiết, và phân tích dữ liệu

## 3. Mục tiêu nghiệp vụ
- Chuẩn hóa onboarding và quản trị thiết bị
- Giới hạn dữ liệu theo đúng phạm vi quản lý
- Hỗ trợ vận hành tập trung theo project, type, group
- Cho phép rule-based automation và alerting
- Hỗ trợ dashboard và phân tích phục vụ điều hành

## 4. Phạm vi cấp cao
### Trong phạm vi
- Authentication và access control
- Organization / user / role / permission / management scope
- Project management và GIS
- Device configuration theo nhiều loại thiết bị
- Group management, import/export, recycle bin
- Rule management
- Dashboard / display information
- Operation control / device detail / statistical analysis

### Ngoài phạm vi hiện tại
- Thiết kế API chi tiết mức endpoint
- Thiết kế database schema chi tiết mức bảng/cột
- Triển khai kỹ thuật frontend/backend cụ thể
- Tích hợp hạ tầng third-party chi tiết chưa thấy rõ trong manual hiện tại

## 5. Các phân hệ chính
- Auth & Access
- Project & GIS
- Device Configuration
- Group & Lifecycle
- Rule Management
- Operations & Analytics

## 6. Tài liệu liên quan
### Tài liệu tổng
- [SHUNCOM IoT — User Stories BA](./shuncom-iot-ba-user-stories.md)
- [SHUNCOM IoT — Luồng Màn Hình](./shuncom-iot-screen-flows.md)
- [SHUNCOM IoT — Mapping Story ↔ Flow ↔ Screen ↔ Module](./shuncom-iot-story-flow-screen-module-mapping.md)

### Tài liệu theo module
- [Business Requirements Document (BRD)](./shuncom-iot-business-requirements-document.md) — tóm tắt nghiệp vụ theo module
- [Software Requirements Specification (SRS)](./shuncom-iot-software-requirements-specification.md) — yêu cầu hệ thống theo module
- [User Stories BA](./shuncom-iot-ba-user-stories.md) — user stories theo module
- [Luồng Màn Hình](./shuncom-iot-screen-flows.md) — flow theo màn hình/module
- [Story ↔ Flow ↔ Screen ↔ Module Mapping](./shuncom-iot-story-flow-screen-module-mapping.md) — traceability chéo

## 7. Đối tượng đọc
- Business Analyst
- Product Owner
- System Analyst
- Solution Architect
- UI/UX Designer
- QA / Tester
- Development team

## 8. Ghi chú
- Bộ tài liệu này được dựng lại từ manual, checklist, và ảnh hệ thống.
- Tên trường hiển thị và hành vi cụ thể cần được revalidate khi bước sang thiết kế kỹ thuật/triển khai.
- Nếu cần BRD/SRS chính thức cho bàn giao, nên dùng tài liệu này làm base line rồi review với stakeholder.