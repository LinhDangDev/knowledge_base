# User Onboarding Guide

## Overview
- Canonical topic: User onboarding and member assignment
- Goal: Hướng dẫn tạo user mới, gán đúng role chuẩn, và cấu hình đúng project/member permissions theo model hiện tại.
- Primary users: Manufacturer, Project Admin, onboarding/support staff

## Provenance
### Source summary
```yaml
Document status: Canonical draft
Confidence: Medium
Last validated: 2026-04-12
Validated by: Claude Code
Primary source type: user-confirmed-business-rule
Canonical topic: user-onboarding-guide
```

### Primary sources used
| Source | Path | Why it matters |
|---|---|---|
| User instruction in chat | current conversation | role model and responsibility boundaries |
| Existing KB doc | `05-User-Management/User Onboarding Guide.md` | prior onboarding process |
| Existing KB doc | `05-User-Management/Permission Matrices.md` | permission model baseline |
| Existing KB doc | `05-User-Management/Role Design Patterns.md` | delegated role guidance |
| Flow doc | `docs/shuncom-iot-screen-flows.md` | user creation / scope flow |

### Validation gaps
- UI wording for permission delegation to Project Member may differ in implementation.
- Invite flow/email delivery specifics may vary by deployment.

## Scope
### In scope
- Create user
- Assign Manufacturer / Project Admin / Project Member
- Configure project-bound permissions for Project Member
- Verify login and scope visibility

### Out of scope
- HR/offboarding policy at enterprise level
- SSO/LDAP deep integration specifics
- Legacy role migration details

## Onboarding checklist
### Pre-onboarding
- [ ] Xác định user thuộc Manufacturer, Project Admin, hay Project Member
- [ ] Xác định project scope cần cấp
- [ ] Nếu là Project Member: xác định permission-set cụ thể do Project Admin cấu hình
- [ ] Chuẩn bị credential delivery method an toàn

### Account creation
- [ ] Tạo user account
- [ ] Gán role chuẩn
- [ ] Gán scope phù hợp
- [ ] Nếu là Project Member: cấu hình permissions cụ thể
- [ ] Cấp credential tạm thời

### Post-creation verification
- [ ] Verify user login được
- [ ] Verify user chỉ thấy đúng scope
- [ ] Verify user làm được đúng actions được cấp
- [ ] Verify user không làm được actions ngoài quyền

## Standard onboarding paths
### 1. Manufacturer onboarding
Use when user cần toàn quyền toàn platform.

Typical setup:
- role: Manufacturer
- scope: all areas / all projects / all resources
- permissions: full

### 2. Project Admin onboarding
Use when user quản lý một hoặc nhiều project cụ thể.

Typical setup:
- role: Project Admin
- scope: managed project(s)
- permissions: full within managed project scope

### 3. Project Member onboarding
Use when user là member trong project do Project Admin quản lý.

Typical setup:
- role: Project Member
- scope: project hoặc subset trong project
- permissions: configured by Project Admin

## Step-by-step onboarding flow
### Step 1: Access user management
```yaml
Navigation:
  Settings > User Management > Users > Add User

Required authority:
  Manufacturer or Project Admin (within managed project scope)
```

### Step 2: Enter basic information
```yaml
Typical fields:
  Username / account
  Email
  Display name
  Phone (optional)
  Initial password or invite method
  Status
```

### Step 3: Assign standard role
```yaml
Role selection:
  - Manufacturer
  - Project Admin
  - Project Member
```

### Step 4: Configure scope
```yaml
Manufacturer:
  - All areas / all resources

Project Admin:
  - Select managed project(s)

Project Member:
  - Select project scope
  - Optional narrower scope by group/device/category if UI supports it
```

### Step 5: Configure Project Member permissions
```yaml
Permission-set examples:
  Viewer-like:
    - dashboard.read
    - devices.read
    - rules.read
    - reports.read

  Operator-like:
    - Viewer-like rights
    - devices.execute
    - alarms.acknowledge
    - alarms.resolve

  Engineer-like:
    - Operator-like rights
    - rules.write
    - selected device config rights
```

### Step 6: Review and create
Review before create:
- correct role
- correct project scope
- correct delegated permissions
- no accidental over-scope access

## Verification steps
### Basic verification
- [ ] User can login
- [ ] User sees expected dashboard context
- [ ] User sees only allowed project scope

### Role-specific verification
#### Manufacturer
- [ ] Can see all project areas
- [ ] Can access all core modules

#### Project Admin
- [ ] Can fully manage assigned project(s)
- [ ] Cannot exceed non-managed projects
- [ ] Can configure Project Member permissions inside managed scope

#### Project Member
- [ ] Can see only delegated scope
- [ ] Can execute only delegated actions
- [ ] Cannot self-elevate or manage membership

## Common issues
| Issue | Likely cause | Fix direction |
|---|---|---|
| User cannot login | wrong credentials / disabled state | reset credential or enable account |
| User sees no devices | wrong project scope | adjust scope |
| Project Member can do too much | over-granted delegated permissions | reduce permission set |
| Project Admin cannot manage member | wrong role or wrong project ownership | verify managed project binding |

## Logging and audit implications
- User creation, role assignment, scope assignment, and delegated-permission changes should all be audited.
- Project Admin changes to Project Member permissions are especially important to track.

## Related docs
- [Permission Matrices](Permission%20Matrices.md)
- [Role Design Patterns](Role%20Design%20Patterns.md)
- [02-Authentication System](../02-System-Architecture/02-Authentication%20System.md)
- [Security Architecture](../08-Development-Guide/Security%20Architecture.md)

## Open questions
- Whether Project Admin can create other Project Admins in the same project should be verified with product owner if needed.
- Invite email / temporary password / SSO onboarding specifics may vary by deployment.
