# System Requirements Specification

**Document Version**: 1.0
**Date**: January 27, 2026
**Project**: SHUNCOM RULR IoT Platform
**Related Documents**: [01-Executive Summary](./01-executive-summary.md)

---

## 1. Functional Requirements

### 1.1 Authentication & User Management

#### FR-AUTH-001: User Authentication System
**Priority**: Critical ⭐⭐⭐⭐⭐
**Phase**: 1

**Requirements**:
- System SHALL support username/password authentication
- System SHALL implement JWT token-based session management
- System SHALL support "Remember Me" functionality with secure token storage
- System SHALL provide password reset workflow via email
- System SHALL implement account lockout after 5 failed login attempts
- System SHALL enforce minimum password requirements (8+ characters, mixed case, numbers, special chars)
- System SHALL support Google Chrome (recommended browser)
- System SHALL maintain session for 24 hours or until explicit logout

**Acceptance Criteria**:
- ✅ User can login with valid credentials
- ✅ Invalid login shows clear error message
- ✅ Account locks after 5 failed attempts
- ✅ Password reset email sent within 60 seconds
- ✅ Session expires after 24 hours of inactivity

---

#### FR-AUTH-002: Role-Based Access Control (RBAC)
**Priority**: Critical ⭐⭐⭐⭐⭐
**Phase**: 1

**Requirements**:
- System SHALL support custom role creation with granular permissions
- System SHALL implement page-level AND function-level permission controls
- System SHALL allow users to have multiple roles simultaneously
- System SHALL support role templates for common use cases (Admin, Manager, Operator, Viewer)
- System SHALL enforce permissions at API endpoint level
- System SHALL dynamically show/hide UI elements based on user permissions
- System SHALL log all permission changes for audit purposes

**Permission Categories**:
1. **Page Access**: Dashboard, Device Management, Rules, Alarms, Analytics, Settings
2. **Function Access**: Create, Read, Update, Delete, Export, Import
3. **Data Scope**: Project-level, Group-level, Device-level access

**Acceptance Criteria**:
- ✅ Admin can create custom roles with specific permissions
- ✅ User with "Viewer" role cannot modify devices
- ✅ UI hides inaccessible features based on permissions
- ✅ API returns 403 Forbidden for unauthorized actions
- ✅ Permission changes logged in audit trail

---

#### FR-AUTH-003: Management Scope System
**Priority**: Critical ⭐⭐⭐⭐⭐
**Phase**: 1

**Requirements**:
- System SHALL support hierarchical management scopes: Organization → Project → Group → Device
- System SHALL allow administrators to assign project-level access to users
- System SHALL support group-level management rights
- System SHALL support product category restrictions
- System SHALL apply scope inheritance (parent scope grants child access)
- System SHALL resolve scope conflicts (most restrictive wins)
- Tenant administrators SHALL have access to all scopes by default
- System SHALL display only authorized data to scoped users

**Scope Types**:
1. **Project Management Rights**: Access to specific projects and sub-projects
2. **Group Management Rights**: Access to device groups within authorized projects
3. **Product Category Rights**: Access to specific device types (e.g., Gateways only)

**Acceptance Criteria**:
- ✅ User assigned "Project A" scope only sees Project A devices
- ✅ User cannot access devices outside assigned scope
- ✅ Scope inheritance works correctly (Project scope grants Group access)
- ✅ Tenant admin sees all projects by default

---

#### FR-AUTH-004: Organization Management
**Priority**: High ⭐⭐⭐⭐
**Phase**: 1

**Requirements**:
- System SHALL support multi-tenant architecture with organization isolation
- System SHALL allow organization logo upload (PNG/JPG, max 2MB)
- System SHALL display organization logo in upper-left corner of dashboard
- System SHALL support organization profile management (name, contact, branding)
- System SHALL ensure complete data isolation between organizations
- System SHALL support white-label customization per tenant

**Acceptance Criteria**:
- ✅ Organization logo displayed correctly after upload
- ✅ Different organizations cannot see each other's data
- ✅ Branding settings persist across user sessions

---

#### FR-AUTH-005: Time Zone Management
**Priority**: Critical ⭐⭐⭐⭐⭐
**Phase**: 1

**Critical Importance**: Time zone affects ALL rule executions (Platform Rules, Local Rules, Alarm Rules)

**Requirements**:
- System SHALL support time zone selection via My Account → Preferences
- System SHALL apply selected time zone globally to all rules and schedules
- System SHALL synchronize device local time with platform time zone
- System SHALL display prominent time zone indicator in dashboard header
- System SHALL show impact assessment when user changes time zone
- System SHALL convert all timestamps to UTC for storage
- System SHALL support all IANA time zones (e.g., America/New_York, Asia/Shanghai)

**Affected Features**:
- Platform Rule scheduling
- Local Rule execution times
- Alarm Rule effective time ranges
- Sunrise/sunset calculations
- Device local time synchronization
- Historical data timestamps

**Acceptance Criteria**:
- ✅ Time zone selection persists across sessions
- ✅ Rules execute at correct local time
- ✅ Dashboard displays times in user's selected time zone
- ✅ Warning shown when changing time zone (affects rules)
- ✅ Device sync updates device local time correctly

---

### 1.2 Device Management

#### FR-DEV-001: Device Registration System
**Priority**: Critical ⭐⭐⭐⭐⭐
**Phase**: 1

**Requirements**:
- System SHALL support 7 device categories:
  1. Smart Gateway
  2. Smart Light Controller (6 sub-types)
  3. Lighting Fixture
  4. Lighting Pole
  5. Power Distribution Control
  6. Loop Control (Built-in + Extended)
  7. Smart Meter (485 three-phase)

- System SHALL enforce mandatory field validation per device type
- System SHALL support device-specific configuration forms
- System SHALL validate device associations before saving
- System SHALL support coordinate management (latitude/longitude)
- System SHALL assign devices to projects and groups
- System SHALL prevent duplicate device numbers within same product type

**Acceptance Criteria**:
- ✅ All 7 device categories can be registered
- ✅ Mandatory fields enforced (prevents save without required data)
- ✅ Device appears in device list after registration
- ✅ Duplicate device number shows error message
- ✅ Coordinates validated (lat: -90 to 90, long: -180 to 180)

---

#### FR-DEV-002: Smart Gateway Configuration
**Priority**: Critical ⭐⭐⭐⭐⭐
**Phase**: 1

**Requirements**:
- System SHALL support gateway configuration with mandatory fields:
  - Device Name (unique identifier)
  - Product Name (from product catalog)
  - Device Number (MAC address format: AA:BB:CC:DD:EE:FF)

- System SHALL support optional fields:
  - Associated distribution box
  - Associated circuit control
  - GPS coordinates (lat/long/altitude)
  - Parent project
  - Belonging group

- System SHALL support circuit configuration in bulk:
  1. Add gateway with basic info
  2. Import/add circuit controllers
  3. Select gateway → Configure Circuits
  4. Generate corresponding circuits in batch
  5. Individual circuit configuration (optional)

- System SHALL support gateway operations:
  - Set 6-digit numeric screen password
  - Synchronize sub-device information
  - Configure circuits in bulk
  - Clear local rules
  - Set three-phase electric ratio

**Display Information**:
- Device Name, Device Number, Product Name
- Online Status
- Three-Phase Electricity Information
- Loop Collection Status
- Local Time
- Screen Password Status
- Last Update Time

**Acceptance Criteria**:
- ✅ Gateway registered with valid MAC address
- ✅ Circuit configuration generates batch circuits
- ✅ Screen password set successfully (6 digits)
- ✅ Sub-device sync status displayed
- ✅ Online/offline status updates in real-time

---

#### FR-DEV-003: Smart Light Controller Configuration
**Priority**: Critical ⭐⭐⭐⭐⭐
**Phase**: 1

**Requirements**:
- System SHALL support 6 light controller communication types:

**Pass-through Devices** (Gateway Required):
1. **Zigbee V3**: Requires gateway, automatic network activation
2. **Dual-way Zigbee V3**: Requires gateway, automatic network activation

**Direct Communication Devices** (No Gateway):
3. **NB-IoT**: Direct platform communication, carrier network activation
4. **CAT.1**: Direct platform communication, carrier network activation

**LoRaWAN Devices** (No Gateway):
5. **LoRa OTAA Mode**: Over-the-Air Activation
   - DEVEUI (Device unique identifier)
   - DEV_PROFILE (LoRaWAN profile)
   - APPEUI (Application identifier)
   - APPKEY (Application key)

6. **LoRa ABP Mode**: Activation by Personalization
   - DEVEUI (Device unique identifier)
   - DEV_PROFILE (LoRaWAN profile)
   - DEVADDR (Device address)
   - APPSKEY (Application session key)
   - NWKSKEY (Network session key)

**Critical Association Requirement**:
- System SHALL enforce lighting fixture association before controller is operational
- System SHALL display "Lamp uncontrollable in list" if fixture association missing
- System SHALL support flexible association order (fixture first OR controller first)

**Monitoring Capabilities**:
System SHALL display real-time data:
- **Electrical**: Voltage, Current, Active Power, Power Factor, Active Energy
- **Environmental**: Illuminance, Color Temperature
- **Network**: Signal Strength, Connection Status, IMSI, Connected Base Station
- **Performance**: Run Time, Frequency, Version, Local Time

**Configuration Commands**:
- Clear configuration
- Timing calibration
- Enable/disable local rules
- Read data
- Device synchronization
- GPS switch control

**Acceptance Criteria**:
- ✅ All 6 controller types can be configured
- ✅ Zigbee controller associates with gateway correctly
- ✅ NB-IoT controller connects without gateway
- ✅ LoRa OTAA activation successful with valid keys
- ✅ Controller without fixture shows warning message
- ✅ Real-time data updates displayed in UI

---

#### FR-DEV-004: Lighting Fixture Management
**Priority**: Critical ⭐⭐⭐⭐⭐
**Phase**: 1

**Critical Role**: Fixture MUST exist before light controller association

**Requirements**:
- System SHALL allow lighting fixture creation independently
- System SHALL support flexible creation order:
  - Create fixture first → then controller → then associate
  - Create controller first → then fixture → then associate
- System SHALL prevent light control without fixture association
- System SHALL display clear warning when association missing
- System SHALL track fixture-controller relationships

**Acceptance Criteria**:
- ✅ Fixture can be created before controller
- ✅ Controller can be created before fixture
- ✅ Association works in both creation orders
- ✅ Lamp control fails gracefully without fixture
- ✅ Warning message displayed when association missing

---

#### FR-DEV-005: Device Relationship Management
**Priority**: Critical ⭐⭐⭐⭐⭐
**Phase**: 1

**Critical Associations** (System MUST enforce):

1. **Light Controller ↔ Lighting Fixture**
   - Impact: Without association → lamp uncontrollable
   - Validation: Show warning if missing

2. **Sub-devices ↔ Gateway**
   - Impact: Without association → device always offline
   - Validation: Verify gateway exists before association

3. **Device ↔ Project**
   - Impact: Unassigned devices visible to ALL users (security risk)
   - Recommendation: Assign all devices to specific projects

4. **Device ↔ Group**
   - Impact: Organizational requirement for group operations
   - Default: "Ungrouped" group available

**Requirements**:
- System SHALL validate all associations before saving
- System SHALL display association warnings prominently
- System SHALL track association history for audit
- System SHALL prevent deletion of devices with active associations
- System SHALL provide bulk association tools

**Acceptance Criteria**:
- ✅ Controller without fixture shows warning
- ✅ Sub-device without gateway shows offline
- ✅ Unassigned device accessible to all users
- ✅ Cannot delete device with active associations
- ✅ Bulk association updates multiple devices

---

#### FR-DEV-006: Device Status Monitoring
**Priority**: Critical ⭐⭐⭐⭐⭐
**Phase**: 1

**Requirements**:
- System SHALL display real-time online/offline status
- System SHALL show device communication health indicators
- System SHALL use status indicator system:
  - ✅ **Green**: Online and communicating
  - ⚠️ **Yellow**: Online but warning conditions
  - ❌ **Red**: Offline or error state
  - ❗ **Exclamation Mark**: Unaddressed alarms
  - ⚙️ **Special Symbol**: Unavailable/misconfigured

- System SHALL display last seen timestamp
- System SHALL show connection quality metrics (signal strength)
- System SHALL update status within 60 seconds of device state change
- System SHALL display dash "-" for unavailable data fields

**Acceptance Criteria**:
- ✅ Status indicator matches actual device state
- ✅ Online status updates within 60 seconds
- ✅ Alarm indicator appears for unaddressed alarms
- ✅ Last seen timestamp accurate
- ✅ Unavailable data shows dash "-" instead of error

---

#### FR-DEV-007: Batch Operations
**Priority**: High ⭐⭐⭐⭐
**Phase**: 2

**Requirements**:
- System SHALL support batch import via template (5,000 device limit)
- System SHALL provide device-specific import templates
- System SHALL validate data during import process
- System SHALL report import errors with row numbers
- System SHALL support import recovery (fix errors and re-import)
- System SHALL support filtered device export (5,000 limit)
- System SHALL track progress for large operations
- System SHALL support background processing for bulk operations

**Template Types**:
1. Smart Gateway template
2. Light Controller templates (6 sub-types)
3. Lighting Fixture template
4. Lighting Pole template
5. Power Distribution template
6. Loop Control template
7. Smart Meter template

**Acceptance Criteria**:
- ✅ Import succeeds with valid template data
- ✅ Import shows clear error messages for invalid data
- ✅ Progress indicator displays for large imports
- ✅ Export generates correct data for selected filters
- ✅ 5,000 device limit enforced

---

#### FR-DEV-008: Device Lifecycle Management
**Priority**: High ⭐⭐⭐⭐
**Phase**: 1

**Requirements**:
- System SHALL check device bindings before deletion
- System SHALL implement recycle bin system:
  - Basic information retained
  - Historical data marked for deletion
  - Recovery within 30 days
  - Permanent deletion after recycle bin clear

- System SHALL clean up device relationships on deletion
- System SHALL support bulk device operations
- System SHALL log all lifecycle events for audit

**Deletion Checks**:
- Associated lighting fixtures
- Active rules referencing device
- Group memberships
- Project assignments
- User favorites/bookmarks

**Acceptance Criteria**:
- ✅ Cannot delete device with active associations
- ✅ Deleted device moves to recycle bin
- ✅ Recovered device restores to original location
- ✅ Permanent deletion irreversible
- ✅ Lifecycle events logged

---

### 1.3 Device Group Management

#### FR-GROUP-001: Device Group Types
**Priority**: High ⭐⭐⭐⭐
**Phase**: 1

**Requirements**:
- System SHALL support 4 group types:

1. **Regular Groups**
   - General device organization
   - No hardware limitations
   - Unlimited group size

2. **Hardware Multicast Groups**
   - **Zigbee Multicast**: Group numbers 1-255, manual entry
   - **LoRa Multicast**: Group numbers 1, 2, 3 with frequency bands
   - Hardware synchronization required
   - Failed sync retry support

3. **Luminaire Groups**
   - Light controller grouping
   - Scene control support

4. **Loop Groups**
   - Circuit controller grouping
   - Batch circuit operations

**Acceptance Criteria**:
- ✅ All 4 group types can be created
- ✅ Zigbee multicast sync to hardware
- ✅ LoRa multicast frequency configured
- ✅ Failed sync devices identified for retry

---

### 1.4 Project Management

#### FR-PROJ-001: Project Hierarchy
**Priority**: Critical ⭐⭐⭐⭐⭐
**Phase**: 1

**Requirements**:
- System SHALL support hierarchical project structure:
  - **Top-level Projects**: Auto-generated, cannot delete
  - **Sub-projects**: Unlimited nesting levels
  - **Unassigned Project**: Auto-generated for unassigned devices

- System SHALL support project-level device association
- System SHALL recommend associating all devices to specific projects
- System SHALL support add/delete/modify per project level
- System SHALL enforce project isolation for scoped users

**Acceptance Criteria**:
- ✅ Top-level project auto-created
- ✅ Sub-projects can be nested
- ✅ Unassigned project contains unassociated devices
- ✅ Project deletion checks for sub-projects and devices

---

#### FR-PROJ-002: Dashboard Display Configuration
**Priority**: High ⭐⭐⭐⭐
**Phase**: 2

**Requirements**:
- System SHALL support 8 customizable dashboard modules per project:
  1. Basic Settings (Technology vs Future style)
  2. Title Settings (name, font, color)
  3. Lighting Distribution (GIS map)
  4. Device Status Overview
  5. Energy Consumption
  6. Alarm Summary
  7. Statistical Charts
  8. Custom Widgets

- System SHALL support drag-and-drop module arrangement
- System SHALL allow module enable/disable per project
- System SHALL support batch apply (copy config to other projects)
- System SHALL provide preview before applying settings

**Acceptance Criteria**:
- ✅ All 8 modules configurable
- ✅ Drag-and-drop rearrangement works
- ✅ Module settings saved per project
- ✅ Batch apply copies config correctly
- ✅ Preview shows changes before save

---

#### FR-PROJ-003: Lighting Schedules
**Priority**: High ⭐⭐⭐⭐
**Phase**: 2

**Requirements**:
- System SHALL support illuminance sensor association
- System SHALL configure light on/off thresholds
- System SHALL support time options:
  - **Preset Fixed Time**: User-defined times
  - **Sunrise/Sunset Time**: Calculated from device GPS coordinates

- System SHALL display configured schedules on homepage
- System SHALL update sunrise/sunset times daily
- System SHALL respect time zone settings

**Acceptance Criteria**:
- ✅ Illuminance threshold triggers light control
- ✅ Fixed time schedule executes correctly
- ✅ Sunrise/sunset times calculated from coordinates
- ✅ Schedule displayed on dashboard
- ✅ Time zone changes update schedule execution

---

#### FR-PROJ-004: Electricity Consumption Plan (ECP)
**Priority**: Medium ⭐⭐⭐
**Phase**: 3

**Requirements**:
- System SHALL support annual consumption plan input
- System SHALL divide plan by month and day
- System SHALL calculate energy saving rate:
  ```
  Energy Saving Rate = [(Planned - Actual) / Planned] × 100%
  ```
- System SHALL display warning (red) when consumption exceeds threshold
- System SHALL display normal (green) when within acceptable range
- System SHALL track actual vs. planned consumption daily

**Acceptance Criteria**:
- ✅ Annual plan input accepted
- ✅ Monthly/daily division calculated
- ✅ Energy saving rate displayed correctly
- ✅ Warning color triggers at threshold
- ✅ Dashboard shows plan vs. actual comparison

---

**Next Document**: [03-Device Specifications](./03-device-specifications.md)

---

## Document Revision History

| Version | Date | Changes | Author |
|---------|------|---------|--------|
| 1.0 | 2026-01-27 | Initial system requirements | AI Assistant |
