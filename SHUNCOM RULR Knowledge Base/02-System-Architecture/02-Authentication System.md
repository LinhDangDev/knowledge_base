# Authentication System

## Overview
- Canonical topic: Authentication and access control
- Goal: Chuẩn hóa tri thức về login, user lifecycle, role model, management scope, và access decision logic theo model Manufacturer / Project Admin / Project Member.
- Primary users: BA, PM, QA, Dev, security reviewer, Manufacturer, Project Admin

## Provenance
### Source summary
```yaml
Document status: Canonical draft
Confidence: Medium
Last validated: 2026-04-12
Validated by: Claude Code
Primary source type: user-confirmed-business-rule
Canonical topic: authentication-system
```

### Primary sources used
| Source | Path | Why it matters |
|---|---|---|
| User instruction in chat | current conversation | canonical role model |
| Existing KB doc | `02-System-Architecture/02-Authentication System.md` | previous auth baseline |
| Existing KB doc | `05-User-Management/Permission Matrices.md` | permission posture |
| Existing KB doc | `05-User-Management/Role Design Patterns.md` | role semantics |
| Flow doc | `docs/shuncom-iot-screen-flows.md` | login, user create, scope flows |
| BA doc | `docs/shuncom-iot-ba-user-stories.md` | auth/user/scope stories |
| Analysis doc | `SHUNCOM_RULR_IoT_Platform_Analysis.md` | auth and scope context |

### Validation gaps
- Token/session implementation details remain backend-dependent and not fully source-verified.
- Exact permission-key names and claim shape in tokens remain implementation-specific.

## Scope
### In scope
- Login and access decision
- User state
- Role model
- Management scope
- Permission + scope interplay

### Out of scope
- Detailed JWT/refresh-token implementation contract
- MFA provider specifics
- Password storage implementation internals

## Standard role model
### Manufacturer
- Highest authority role.
- Scope: toàn hệ thống, tất cả area, tất cả project.
- Permissions: full.

### Project Admin
- Full authority inside managed project scope.
- Can manage project-level resources and configure Project Member permissions within that scope.

### Project Member
- Delegated role envelope.
- Permissions are configured by Project Admin.
- Scope remains bounded to delegated project/sub-scope.

## User lifecycle
| State | Meaning |
|---|---|
| Active / enabled | can login and use assigned scope |
| Disabled | login blocked |
| Deleted / removed | no longer active in system lifecycle |

## Authentication flow
1. User submits credentials.
2. System validates account.
3. System verifies active/disabled state.
4. System resolves role.
5. System resolves scope.
6. System grants session/access only within allowed scope.

## Access decision model
### Required checks
1. User identity valid
2. User state active
3. Role permits action
4. Scope includes target resource

### Practical effect
- Manufacturer bypasses project boundary restrictions by design.
- Project Admin gets full control only inside managed project(s).
- Project Member sees/does only what Project Admin configured.

## Management scope model
| Scope model | Typical role |
|---|---|
| Global all-area scope | Manufacturer |
| Managed project scope | Project Admin |
| Delegated project/sub-scope | Project Member |

### Supported scope dimensions
- project
- group
- device
- product category (if UI/implementation supports)

## Business constraints
- Manufacturer is the only global all-area/all-permission role.
- Project Admin must not gain authority outside managed projects.
- Project Member must not exceed delegated project scope.
- Visibility and action rights depend on both role and scope.
- Disabled users cannot login even if role/scope are otherwise valid.
- Time zone preference can influence time-based feature behavior but does not change authorization boundaries.

## API contract posture
- Auth and user endpoints remain inventory-level references unless verified with backend/OpenAPI source.
- Do not treat token claim examples or permission strings from docs as final implementation contract.

## Data and integration touchpoints
| Type | Item | Purpose |
|---|---|---|
| API | `/auth/*` | login/session lifecycle |
| API | `/users` | user creation/update |
| Data | users / roles / scopes / orgs | access model |
| Audit | login, role change, scope change | traceability |

## Logging and audit implications
- Log successful and failed login attempts.
- Log user creation, disable/enable, role assignment, and scope changes.
- Log delegated permission changes for Project Member.
- Log access denials where security/audit policy requires it.

## Related docs
- [Permission Matrices](../05-User-Management/Permission%20Matrices.md)
- [Role Design Patterns](../05-User-Management/Role%20Design%20Patterns.md)
- [User Onboarding Guide](../05-User-Management/User%20Onboarding%20Guide.md)
- [Security Architecture](../08-Development-Guide/Security%20Architecture.md)

## Open questions
- Exact token/session/MFA behaviors need backend confirmation if used for implementation contract.
- Fine-grained sub-scope dimensions for Project Member need UI/backend verification if the product exposes them explicitly.
