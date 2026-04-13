# Map of Content (MOC)

Bản MOC này là navigation hub chính cho bộ tài liệu SHUNCOM RULR theo hướng canonical docs + traceability sources.

## 1. Start here
- [Knowledge Base README](README.md)
- [01-System Overview](01-Overview/01-System%20Overview.md)
- [BRD Overview](../docs/shuncom-iot-brd-overview.md)
- [Business Requirements Document](../docs/shuncom-iot-business-requirements-document.md)
- [Software Requirements Specification](../docs/shuncom-iot-software-requirements-specification.md)
- [Non-Functional Requirements](../docs/shuncom-iot-non-functional-requirements.md)
- [User Stories BA](../docs/shuncom-iot-ba-user-stories.md)
- [Screen Flows](../docs/shuncom-iot-screen-flows.md)
- [Story ↔ Flow ↔ Screen ↔ Module Mapping](../docs/shuncom-iot-story-flow-screen-module-mapping.md)

## 2. Theo mục tiêu đọc
### Nếu cần hiểu hệ thống ở mức high-level
- [01-System Overview](01-Overview/01-System%20Overview.md)

### Nếu cần hiểu kiến trúc và integration posture
- [02-Authentication System](02-System-Architecture/02-Authentication%20System.md)
- [API Endpoints Map](02-System-Architecture/API%20Endpoints%20Map.md)

### Nếu cần hiểu device lifecycle
- [03-Device Management Hub](03-Device-Management/03-Device%20Management%20Hub.md)
- [Device Types Reference](03-Device-Management/Device%20Types%20Reference.md)
- [Device Troubleshooting](03-Device-Management/Device%20Troubleshooting.md)
- [Protocol Guides](03-Device-Management/Protocol%20Guides.md)

### Nếu cần hiểu rules, schedules, alarms
- [04-Rule Engine System](04-Rule-Management/04-Rule%20Engine%20System.md)
- [Rule Configuration Patterns](04-Rule-Management/Rule%20Configuration%20Patterns.md)
- [Local Rules Best Practices](04-Rule-Management/Local%20Rules%20Best%20Practices.md)
- [Screen Flows](../docs/shuncom-iot-screen-flows.md)

### Nếu cần hiểu project, dashboard, GIS, analytics
- [05-Project Management](05-User-Management/05-Project%20Management.md)
- [06-Dashboard Interface](06-Project-Management/06-Dashboard%20Interface.md)
- [GIS Setup Guide](06-Project-Management/GIS%20Setup%20Guide.md)
- [Widget Reference](07-Dashboard/Widget%20Reference.md)
- [Customization Guide](07-Dashboard/Customization%20Guide.md)

### Nếu cần trace nguồn nghiệp vụ
- [BRD Overview](../docs/shuncom-iot-brd-overview.md)
- [Business Requirements Document](../docs/shuncom-iot-business-requirements-document.md)
- [Software Requirements Specification](../docs/shuncom-iot-software-requirements-specification.md)
- [Non-Functional Requirements](../docs/shuncom-iot-non-functional-requirements.md)
- [User Stories BA](../docs/shuncom-iot-ba-user-stories.md)
- [Screen Flows](../docs/shuncom-iot-screen-flows.md)
- [Story ↔ Flow ↔ Screen ↔ Module Mapping](../docs/shuncom-iot-story-flow-screen-module-mapping.md)
- [System Analysis](../SHUNCOM_RULR_IoT_Platform_Analysis.md)

### Nếu cần maintain bộ knowledge base
- [Knowledge Base Setup Guide](08-Development-Guide/Knowledge%20Base%20Setup%20Guide.md)
- [Feature Requirements Checklist](08-Development-Guide/Feature%20Requirements%20Checklist.md)

## 3. Canonical topic map
| Topic | Canonical document |
|---|---|
| System overview | [01-System Overview](01-Overview/01-System%20Overview.md) |
| Authentication and access | [02-Authentication System](02-System-Architecture/02-Authentication%20System.md) |
| API reference | [API Endpoints Map](02-System-Architecture/API%20Endpoints%20Map.md) |
| Device domain | [03-Device Management Hub](03-Device-Management/03-Device%20Management%20Hub.md) |
| Rule domain | [04-Rule Engine System](04-Rule-Management/04-Rule%20Engine%20System.md) |
| Project domain | [05-Project Management](05-User-Management/05-Project%20Management.md) |
| Dashboard domain | [06-Dashboard Interface](06-Project-Management/06-Dashboard%20Interface.md) |

## 4. Required checks for active docs
- Có provenance nếu là canonical doc
- Có confidence level nếu doc chứa assumption lớn
- Có open questions nếu còn giả định
- Có traceability phù hợp cho business/system docs
- Dùng markdown links
- Không tạo thêm duplicate canonical doc cho cùng chủ đề
