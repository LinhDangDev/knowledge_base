# SHUNCOM RULR IoT Platform Knowledge Base

Bộ knowledge base này mô tả hệ thống SHUNCOM RULR ở mức high-level, business flow, domain behavior, API inventory, và operational knowledge cho BA, PM, QA, Dev, và Ops.

## Mục tiêu
- Chuẩn hóa tri thức hệ thống ở mức business + system level
- Mô tả các flow chính: project, device, rules, scheduling, dashboard, GIS, logs
- Giữ một canonical doc cho mỗi chủ đề quan trọng
- Bảo đảm mọi claim quan trọng có provenance rõ ràng trong canonical docs đang còn sử dụng

## Chuẩn đang áp dụng
- Ngôn ngữ mặc định: **Vietnamese-first**
- Link chuẩn: **markdown links**
- Canonical strategy: **1 chủ đề = 1 canonical document**
- Supporting docs không được tranh nội dung với canonical docs

## Canonical navigation
### 01. Overview
- [01-System Overview](01-Overview/01-System%20Overview.md)

### 02. System Architecture
- [02-Authentication System](02-System-Architecture/02-Authentication%20System.md)
- [API Endpoints Map](02-System-Architecture/API%20Endpoints%20Map.md)

### 03. Device Management
- [03-Device Management Hub](03-Device-Management/03-Device%20Management%20Hub.md)
- [Device Types Reference](03-Device-Management/Device%20Types%20Reference.md)
- [Device Troubleshooting](03-Device-Management/Device%20Troubleshooting.md)
- [Protocol Guides](03-Device-Management/Protocol%20Guides.md)

### 04. Rule Management
- [04-Rule Engine System](04-Rule-Management/04-Rule%20Engine%20System.md)
- [Rule Configuration Patterns](04-Rule-Management/Rule%20Configuration%20Patterns.md)
- [Local Rules Best Practices](04-Rule-Management/Local%20Rules%20Best%20Practices.md)

### 05. User and Project Scope
- [05-Project Management](05-User-Management/05-Project%20Management.md)
- [Permission Matrices](05-User-Management/Permission%20Matrices.md)
- [Role Design Patterns](05-User-Management/Role%20Design%20Patterns.md)
- [User Onboarding Guide](05-User-Management/User%20Onboarding%20Guide.md)

### 06. Project Dashboard and GIS
- [06-Dashboard Interface](06-Project-Management/06-Dashboard%20Interface.md)
- [GIS Setup Guide](06-Project-Management/GIS%20Setup%20Guide.md)

### 07. Dashboard and Planning Support
- [07-Development Roadmap](07-Dashboard/07-Development%20Roadmap.md)
- [Customization Guide](07-Dashboard/Customization%20Guide.md)
- [Widget Reference](07-Dashboard/Widget%20Reference.md)

### 08. Development Guide
- [API Design Patterns](08-Development-Guide/API%20Design%20Patterns.md)
- [Automated Testing Setup Guide](08-Development-Guide/Automated%20Testing%20Setup%20Guide.md)
- [Feature Requirements Checklist](08-Development-Guide/Feature%20Requirements%20Checklist.md)
- [Knowledge Base Setup Guide](08-Development-Guide/Knowledge%20Base%20Setup%20Guide.md)
- [Performance Benchmarks](08-Development-Guide/Performance%20Benchmarks.md)
- [Security Architecture](08-Development-Guide/Security%20Architecture.md)
- [Testing Scenarios](08-Development-Guide/Testing%20Scenarios.md)
- [Troubleshooting Guide](08-Development-Guide/Troubleshooting%20Guide.md)
- [UI Component Library](08-Development-Guide/UI%20Component%20Library.md)
- [UI Design Guidelines](08-Development-Guide/UI%20Design%20Guidelines.md)

## Tài liệu liên quan ngoài KB
- [BRD Overview](../docs/shuncom-iot-brd-overview.md)
- [Business Requirements Document](../docs/shuncom-iot-business-requirements-document.md)
- [Software Requirements Specification](../docs/shuncom-iot-software-requirements-specification.md)
- [Non-Functional Requirements](../docs/shuncom-iot-non-functional-requirements.md)
- [User Stories BA](../docs/shuncom-iot-ba-user-stories.md)
- [Screen Flows](../docs/shuncom-iot-screen-flows.md)
- [Story ↔ Flow ↔ Screen ↔ Module Mapping](../docs/shuncom-iot-story-flow-screen-module-mapping.md)
- [System Analysis](../SHUNCOM_RULR_IoT_Platform_Analysis.md)

## Cách dùng bộ KB này
1. Đọc [01-System Overview](01-Overview/01-System%20Overview.md) để nắm hệ thống.
2. Đọc nhóm tài liệu trong `../docs/` khi cần trace nguồn BA, flow, requirements, và mapping.
3. Cập nhật trực tiếp canonical doc nếu nội dung chủ đề thay đổi.
4. Chỉ giữ supporting docs nếu chúng giúp đọc nhanh hơn nhưng không cạnh tranh canonical source.
