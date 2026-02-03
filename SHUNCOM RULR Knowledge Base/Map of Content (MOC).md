# 🗺️ Map of Content (MOC)

> Central navigation hub for SHUNCOM RULR IoT Platform Knowledge Base

{% hint style="info" %}
**Platform:** SHUNCOM RULR IoT Platform v1.1 | **Last Updated:** January 2025
{% endhint %}

{% hint style="info" %}
**Platform:** SHUNCOM RULR IoT Platform v1.1 | **Last Updated:** January 22, 2025
{% endhint %}

---

## 🚀 Getting Started Fast Track

### For New Team Members
```mermaid
graph LR
    A[Start Here] --> B[System Overview]
    B --> C[Device Types Reference]
    C --> D[Development Roadmap]
    D --> E[Begin Implementation]
```

1. **[01-System Overview](01-Overview/01-System%20Overview.md)** - Understand the platform architecture
2. **[Device Types Reference](Device%20Types%20Reference.md)** - Learn supported devices  
3. **[07-Development Roadmap](07-Dashboard/07-Development%20Roadmap.md)** - See implementation plan
4. **[Feature Requirements Checklist](Feature%20Requirements%20Checklist.md)** - Track development progress

### For Project Managers
1. **[Project Scope Summary](01-Overview/Project%20Scope%20Summary.md)** - Complete project overview
2. **[Performance Benchmarks](08-Development-Guide/Performance%20Benchmarks.md)** - System requirements
3. **[Testing Scenarios](08-Development-Guide/Testing%20Scenarios.md)** - QA planning
4. **[UI Design Guidelines](08-Development-Guide/UI%20Design%20Guidelines.md)** - Design standards
5. **[Feature Requirements Checklist](Feature%20Requirements%20Checklist.md)** - Track development progress

---

## 📚 Core Knowledge Areas

### 🏗️ System Architecture
```mermaid
mindmap
  root((SHUNCOM RULR))
    System Architecture
      Authentication System
        User Management
        Role-Based Access Control
        Organization Management
      Device Management
        7 Device Categories
        Batch Operations  
        GIS Integration
      Rule Engine
        Platform Rules
        Local Rules
        Alarm Rules
      Dashboard
        Real-time Monitoring
        Statistical Analysis
        Operation Control
```

#### Foundation Documents
- **[01-System Overview](01-Overview/01-System%20Overview.md)** - Complete architectural overview
- **[02-Authentication System](02-System-Architecture/02-Authentication%20System.md)** - User management and security
- **[API Endpoints Map](02-System-Architecture/API%20Endpoints%20Map.md)** - System integration points
- **[Database Schema](02-System-Architecture/Database%20Schema.md)** - Data model relationships

#### Technical Deep Dives  
- **[Performance Benchmarks](08-Development-Guide/Performance%20Benchmarks.md)** - System performance requirements
- **[Security Architecture](08-Development-Guide/Security%20Architecture.md)** - Security implementation details
- **[[Integration Patterns]]** - Third-party integration guide
- **[[Scalability Planning]]** - Growth and scaling strategies

### 🔧 Device Management
#### Quick References
- **[Device Types Reference](Device%20Types%20Reference.md)** - 7 device categories overview
- **[Device Troubleshooting](03-Device-Management/Device%20Troubleshooting.md)** - Common problems and solutions
- **[Protocol Guides](03-Device-Management/Protocol%20Guides.md)** - Zigbee, LoRa, NB-IoT, CAT.1, MQTT

#### Detailed Guides
- **[03-Device Management Hub](03-Device-Management/03-Device%20Management%20Hub.md)** - Complete device lifecycle
- **[[Gateway Configuration Guide]]** - Smart gateway setup
- **[[Light Controller Setup]]** - All controller types
- **[[Batch Operations Manual]]** - Import/export procedures

### ⚙️ Automation & Rules
#### Rule System Overview
- **[04-Rule Engine System](04-Rule-Management/04-Rule%20Engine%20System.md)** - Complete rule system guide
- **[Rule Configuration Patterns](04-Rule-Management/Rule%20Configuration%20Patterns.md)** - Common automation patterns
- **[[Alarm Management Guide]]** - Comprehensive alarm handling
- **[Local Rules Best Practices](04-Rule-Management/Local%20Rules%20Best%20Practices.md)** - Device-level automation

#### Implementation Examples
- **[[Platform Rules Examples]]** - Real-world automation scenarios
- **[[Alarm Configuration Examples]]** - Practical alarm setups
- **[[Rule Testing Procedures]]** - Validation and testing
- **[[Rule Performance Optimization]]** - Efficiency guidelines

### 👥 User & Project Management
#### User Management
- **[02-Authentication System](02-System-Architecture/02-Authentication%20System.md)** - User lifecycle management
- **[Role Design Patterns](05-User-Management/Role%20Design%20Patterns.md)** - RBAC implementation
- **[Permission Matrices](05-User-Management/Permission%20Matrices.md)** - Access control mapping
- **[User Onboarding Guide](05-User-Management/User%20Onboarding%20Guide.md)** - New user procedures

#### Project Structure
- **[05-Project Management](05-User-Management/05-Project%20Management.md)** - Project hierarchy design
- **[GIS Setup Guide](06-Project-Management/GIS%20Setup%20Guide.md)** - Map and location features
- **[Customization Guide](07-Dashboard/Customization%20Guide.md)** - Custom dashboard setup
- **[[Multi-tenant Architecture]]** - Organization isolation

---

## 🎯 Development Resources

### 💻 Development Guides
```mermaid
graph TB
    A[Development Roadmap] --> B[Phase 1: Core]
    A --> C[Phase 2: Advanced]
    A --> D[Phase 3: Analytics]
    
    B --> E[Authentication]
    B --> F[Device Management]
    B --> G[Basic Rules]
    
    C --> H[Complex Rules]
    C --> I[GIS Integration]
    C --> J[Real-time Features]
    
    D --> K[Analytics Dashboard]
    D --> L[Performance Optimization]
    D --> M[Advanced Integrations]
```

#### Planning & Architecture
- **[07-Development Roadmap](07-Dashboard/07-Development%20Roadmap.md)** - Complete implementation timeline
- **[Feature Requirements Checklist](Feature%20Requirements%20Checklist.md)** - Development tracking
- **[[Technical Debt Management]]** - Code quality maintenance
- **[[Architecture Decision Records]]** - Design decision history

#### Frontend Development  
- **[UI Component Library](08-Development-Guide/UI%20Component%20Library.md)** - Reusable UI components
- **[06-Dashboard Interface](06-Project-Management/06-Dashboard%20Interface.md)** - Frontend implementation guide
- **[UI Design Guidelines](08-Development-Guide/UI%20Design%20Guidelines.md)** - Design system standards
- **[Widget Reference](07-Dashboard/Widget%20Reference.md)** - Dashboard widget catalog
- **[Customization Guide](07-Dashboard/Customization%20Guide.md)** - Dashboard customization
- **[[Responsive Design Patterns]]** - Multi-device support

#### Backend Development
- **[API Design Patterns](08-Development-Guide/API%20Design%20Patterns.md)** - RESTful API standards
- **[[Database Design Guide]]** - Data model implementation
- **[[Real-time Architecture]]** - WebSocket implementation
- **[[Microservices Patterns]]** - Service architecture

### 🧪 Quality Assurance
#### Testing Framework
- **[Testing Scenarios](08-Development-Guide/Testing%20Scenarios.md)** - Comprehensive test cases
- **[[Automated Testing Guide]]** - CI/CD integration
- **[[Performance Testing]]** - Load and stress testing
- **[[Security Testing]]** - Vulnerability assessment

#### Quality Standards
- **[[Code Review Guidelines]]** - Code quality standards
- **[[Documentation Standards]]** - Technical writing guide
- **[[Release Procedures]]** - Deployment workflows
- **[[Monitoring & Alerting]]** - Production monitoring

---

## 🔗 Cross-Reference Maps

### Feature Dependencies Map
```mermaid
graph TD
    A[Authentication] --> B[Project Management]
    B --> C[Device Management]
    C --> D[Rule Engine]
    D --> E[Dashboard]
    
    F[User Roles] --> G[Device Access]
    G --> H[Rule Permissions]
    H --> I[Dashboard Views]
    
    J[GIS Integration] --> K[Device Distribution]
    K --> L[Location-based Rules]
    L --> M[Map Visualization]
```

### Technology Stack Map
```yaml
Frontend:
  Framework: React/Vue.js (TBD)
  State Management: Redux/Vuex
  UI Components: Custom component library
  Maps: GIS integration service
  Real-time: WebSocket client
  
Backend:  
  API: RESTful + GraphQL (optional)
  Real-time: WebSocket server
  Database: PostgreSQL/MongoDB (TBD)
  Authentication: JWT + RBAC
  Device Communication: MQTT/HTTP
  
Infrastructure:
  Hosting: Cloud platform (AWS/Azure/GCP)
  CDN: Static asset delivery
  Monitoring: Application performance monitoring
  Logging: Centralized logging system
```

### Integration Points Map
```yaml
External Integrations:
  GIS Services: Map data and geocoding
  Weather Services: Sunrise/sunset calculations
  SMS/Email: Notification delivery
  Mobile Apps: Push notifications
  
Internal Integrations:
  Device Protocols: Zigbee, LoRa, NB-IoT, CAT.1
  Database Systems: User data, device data, metrics
  File Systems: Document storage, exports
  Caching Systems: Performance optimization
```

---

## 📊 Progress Tracking

### Implementation Status
| Component | Status | Priority | Complexity | Dependencies |
|-----------|--------|----------|------------|--------------|
| **Authentication** | 🔄 Planning | High | Medium | None |
| **Device Management** | 📋 Designed | High | High | Authentication |
| **Rule Engine** | 📋 Designed | High | High | Device Management |
| **Dashboard** | 🔄 Planning | High | Medium | All above |
| **GIS Integration** | 📅 Future | Medium | High | Device Management |
| **Analytics** | 📅 Future | Low | Medium | Dashboard |

**Legend**: 📅 Not Started | 🔄 In Progress | 📋 Designed | ✅ Complete | ⚠️ Blocked

### Knowledge Base Health
```yaml
Documentation Coverage:
  Core Systems: ✅ 95% Complete
  API Documentation: 🔄 70% Complete  
  User Guides: 🔄 75% Complete
  Troubleshooting: ✅ 80% Complete
  
Link Health:
  Internal Links: ✅ All functional
  External Links: ⚠️ Need validation
  Bi-directional Links: ✅ Properly structured
  
Maintenance Status:
  Last Updated: 2025-01-23
  Next Review: Weekly
  Ownership: Development Team
  Total Files: 41 markdown documents
```

---

## 🏷️ Tag Directory

### System Tags
- `#shuncom-rulr` - Main platform content
- `#system-architecture` - Architecture documentation  
- `#development-guide` - Implementation guides
- `#quick-reference` - Quick lookup documents

### Feature Tags
- `#device-management` - Device lifecycle and configuration
- `#rule-engine` - Automation and rule processing
- `#user-management` - Authentication and authorization  
- `#dashboard` - Frontend interface components
- `#gis-integration` - Mapping and location services
- `#alarm-system` - Notification and alerting
- `#real-time` - Live monitoring and WebSocket features

### Development Tags
- `#ui-requirements` - Frontend development needs
- `#backend-api` - Server-side implementation
- `#database-schema` - Data model design
- `#performance` - Optimization and scaling
- `#security` - Security implementation
- `#testing` - Quality assurance procedures

---

## 🔍 Search Strategies

### Finding Information Quickly
```yaml
By Role:
  Developer: Search #development-guide + #ui-requirements
  DevOps: Search #performance + #security + #monitoring  
  Product Manager: Search #feature-requirements + #roadmap
  QA: Search #testing + #troubleshooting
  
By Feature:
  Authentication: Search #user-management + #security
  Devices: Search #device-management + #iot-devices
  Automation: Search #rule-engine + #automation
  UI: Search #dashboard + #ui-requirements
  
By Status:
  Planning: Search #roadmap + #requirements
  Implementation: Search #development-guide + #patterns
  Testing: Search #testing + #validation
  Deployment: Search #performance + #monitoring
```

### Obsidian-Specific Features
```yaml
Graph View: Visualize knowledge connections
Tags Pane: Browse by tag categories  
Search: Use boolean operators (AND, OR, NOT)
Backlinks: See incoming references
Local Graph: Focused connection view
Query Blocks: Dynamic content embedding
```

---

**Navigation Tips**: 
- Use `Ctrl/Cmd + O` to quick-open any file
- Use `Ctrl/Cmd + Shift + F` for global search
- Click any `[[Link]]` to navigate instantly
- Use graph view to explore connections visually