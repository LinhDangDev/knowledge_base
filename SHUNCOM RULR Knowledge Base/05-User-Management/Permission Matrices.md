# Permission Matrices

## Overview
- Canonical topic: Role and permission matrix
- Goal: Định nghĩa matrix quyền chuẩn cho 3 role chính của SHUNCOM RULR: Manufacturer, Project Admin, Project Member.
- Primary users: BA, PM, QA, Dev, security reviewer, Manufacturer, Project Admin

## Provenance
### Source summary
```yaml
Document status: Canonical draft
Confidence: Medium
Last validated: 2026-04-12
Validated by: Claude Code
Primary source type: user-confirmed-business-rule
Canonical topic: permission-matrices
```

### Primary sources used
| Source | Path | Why it matters |
|---|---|---|
| User instruction in chat | current conversation | canonical role model confirmed by user |
| Existing KB doc | `05-User-Management/Permission Matrices.md` | previous matrix baseline to replace |
| Existing KB doc | `05-User-Management/Role Design Patterns.md` | old role hierarchy to refactor |
| Existing KB doc | `02-System-Architecture/02-Authentication System.md` | auth/scope architecture context |
| BA doc | `docs/shuncom-iot-ba-user-stories.md` | role/user/scope stories needing updates |
| Flow doc | `docs/shuncom-iot-screen-flows.md` | login/user/scope flows |

### Validation gaps
- Exact permission-key naming in backend/API still needs source verification.
- Delegation model for Project Member is business-confirmed, but UI granularity for every permission toggle still needs implementation verification.

## Scope
### In scope
- Standard roles
- Permission families
- Scope behavior
- Management responsibility boundaries

### Out of scope
- Backend permission engine implementation
- Token/session claims format
- Legacy role migration playbook

## Standard roles
### 1. Manufacturer
- Scope: toàn hệ thống
- Visibility: tất cả area / project / group / device
- Permission posture: toàn quyền
- Use case: platform owner / manufacturer-level operator

### 2. Project Admin
- Scope: project đang được giao quản lý
- Visibility: toàn bộ resource trong project đó
- Permission posture: toàn quyền trong project scope
- Use case: người vận hành/quản lý dự án

### 3. Project Member
- Scope: project hoặc phần resource do Project Admin gán
- Visibility: theo cấu hình của Project Admin
- Permission posture: configurable by Project Admin
- Use case: member/operator/view-only/technician trong phạm vi project

## Scope behavior
| Role | Scope model | Notes |
|---|---|---|
| Manufacturer | all areas / all projects / all resources | global top-level role |
| Project Admin | assigned managed project(s) | full control only inside managed project scope |
| Project Member | subset of project scope | quyền và visibility do Project Admin cấu hình |

## Master permission matrix
### Device permissions
| Permission family | Manufacturer | Project Admin | Project Member |
|---|:---:|:---:|:---:|
| View devices | ✅ | ✅ | Configurable |
| Create devices | ✅ | ✅ | Configurable |
| Update devices | ✅ | ✅ | Configurable |
| Delete / recycle devices | ✅ | ✅ | Configurable |
| Execute device commands | ✅ | ✅ | Configurable |
| Import / export devices | ✅ | ✅ | Configurable |

### Rule permissions
| Permission family | Manufacturer | Project Admin | Project Member |
|---|:---:|:---:|:---:|
| View rules | ✅ | ✅ | Configurable |
| Create / edit rules | ✅ | ✅ | Configurable |
| Delete rules | ✅ | ✅ | Configurable |
| Enable / disable / execute rules | ✅ | ✅ | Configurable |
| Manage local-rule sync | ✅ | ✅ | Configurable |
| Manage alarm rules | ✅ | ✅ | Configurable |

### Alarm permissions
| Permission family | Manufacturer | Project Admin | Project Member |
|---|:---:|:---:|:---:|
| View alarms | ✅ | ✅ | Configurable |
| Acknowledge / process alarms | ✅ | ✅ | Configurable |
| Resolve alarms | ✅ | ✅ | Configurable |
| Configure alarm settings | ✅ | ✅ | Configurable |

### Project permissions
| Permission family | Manufacturer | Project Admin | Project Member |
|---|:---:|:---:|:---:|
| View projects | ✅ | ✅ | Configurable |
| Create / edit projects | ✅ | ✅ | Configurable if allowed |
| Delete projects | ✅ | ✅ | Typically restricted; configurable only if business allows |
| Configure display information | ✅ | ✅ | Configurable |
| Configure GIS / schedule / ECP | ✅ | ✅ | Configurable |

### User and membership permissions
| Permission family | Manufacturer | Project Admin | Project Member |
|---|:---:|:---:|:---:|
| View users in scope | ✅ | ✅ | Typically no |
| Create project members | ✅ | ✅ | No |
| Update project member permissions | ✅ | ✅ | No |
| Remove project members | ✅ | ✅ | No |
| Create new top-level role types | No standard need | No | No |

### Dashboard / report / log permissions
| Permission family | Manufacturer | Project Admin | Project Member |
|---|:---:|:---:|:---:|
| View dashboard | ✅ | ✅ | Configurable |
| Configure dashboard | ✅ | ✅ | Configurable |
| View reports | ✅ | ✅ | Configurable |
| Generate / export reports | ✅ | ✅ | Configurable |
| View system logs / audit in scope | ✅ | ✅ | Configurable |

## Delegation model for Project Member
### Project Admin can configure
- feature visibility
- read/write/execute scope inside project
- device/rule/dashboard/report visibility
- optional narrower sub-scope by group/device/category if UI supports it

### Project Admin cannot grant
- authority outside managed project
- Manufacturer-equivalent global access
- permissions on projects they do not manage

## Recommended permission-set patterns for Project Member
| Pattern | Typical permissions |
|---|---|
| Viewer Member | read-only dashboard/devices/rules/reports |
| Operator Member | view + execute commands + acknowledge alarms |
| Engineer Member | operator rights + rule editing + selected config rights |
| Analyst Member | read dashboards/reports/exports without control actions |

## Business constraints
- Manufacturer is the only global all-area/all-permission role.
- Project Admin is powerful only within managed project boundaries.
- Project Member is not a fixed low-power role; it is a configurable permission envelope.
- Project Member permissions must always remain bounded by Project Admin project scope.
- User visibility and operation rights depend on both role and scope.

## Logging and audit implications
- Audit log must capture: member creation, permission changes, scope changes, removal from project.
- Sensitive operations must record actor, target member, changed permission set, and timestamp.
- Manufacturer and Project Admin changes should be especially visible in audit trails.

## Related docs
- [Role Design Patterns](Role%20Design%20Patterns.md)
- [User Onboarding Guide](User%20Onboarding%20Guide.md)
- [02-Authentication System](../02-System-Architecture/02-Authentication%20System.md)
- [Security Architecture](../08-Development-Guide/Security%20Architecture.md)

## Open questions
- Exact permission-key names for Project Member delegation need backend/UI verification.
- Whether Project Admin can create/edit/delete project records themselves in every deployment should be revalidated with product owner if needed.
