# Role Design Patterns

## Overview
- Canonical topic: Role design guidance
- Goal: Mô tả cách áp dụng model 3 role chuẩn của SHUNCOM RULR và cách thiết kế permission patterns cho Project Member mà không tạo thêm top-level role trùng nghĩa.
- Primary users: BA, PM, QA, Dev, project admin

## Provenance
### Source summary
```yaml
Document status: Canonical draft
Confidence: Medium
Last validated: 2026-04-12
Validated by: Claude Code
Primary source type: user-confirmed-business-rule
Canonical topic: role-design-patterns
```

### Primary sources used
| Source | Path | Why it matters |
|---|---|---|
| User instruction in chat | current conversation | new role model confirmed |
| Existing KB doc | `05-User-Management/Role Design Patterns.md` | previous role hierarchy to replace |
| Existing KB doc | `05-User-Management/Permission Matrices.md` | matrix baseline |
| Existing KB doc | `02-System-Architecture/02-Authentication System.md` | auth/scope context |

### Validation gaps
- Exact UI mechanics for Project Member permission configuration still need implementation verification.
- Legacy role migration behavior is not defined here.

## Scope
### In scope
- Standard roles
- Permission pattern design
- Scope-aware delegation
- Least-privilege guidance within the new model

### Out of scope
- Custom top-level role proliferation
- Backend RBAC engine internals
- Historical legacy-role mapping policy

## Standard role model
### Manufacturer
- Global platform role
- Sees all areas and has all permissions
- Used only for platform/manufacturer-level governance

### Project Admin
- Full control within managed project scope
- Responsible for project-level configuration, membership, device/rule/dashboard control

### Project Member
- Permission set is delegated by Project Admin
- Exists inside project scope only
- Can be configured as viewer/operator/engineer/analyst style member without creating a new top-level role

## Design principle
### Do not create parallel top-level roles
Thay vì duy trì các role như Project Manager / Operator / Viewer như top-level roles riêng, chuẩn mới dùng:
- 2 fixed authority roles: Manufacturer, Project Admin
- 1 delegated role family: Project Member

Project Member sẽ mang các permission-set pattern khác nhau.

## Permission-set patterns for Project Member
### Pattern 1 — Viewer Member
Use when user chỉ cần giám sát.

Typical rights:
- view dashboard
- view devices
- view rules
- view reports
- view logs if allowed
- no control / no configuration

### Pattern 2 — Operator Member
Use when user cần vận hành hằng ngày.

Typical rights:
- viewer rights
- execute device commands
- acknowledge/process alarms
- limited group-level operations
- no project governance

### Pattern 3 — Engineer Member
Use when user cần cấu hình kỹ thuật trong project.

Typical rights:
- operator rights
- create/edit selected rules
- update selected device configuration
- manage local-rule sync if needed
- still no cross-project authority

### Pattern 4 — Analyst Member
Use when user cần báo cáo/phân tích.

Typical rights:
- view dashboards/reports/logs
- export reports
- no control actions
- no write access to operational settings

## Scope-aware role rules
- Manufacturer vượt qua mọi area/project boundary.
- Project Admin chỉ có toàn quyền trong managed project(s).
- Project Member luôn bị chặn ngoài project được cấp.
- Nếu UI hỗ trợ finer-grained scope, Project Member có thể bị giới hạn thêm theo group/device/category.

## Least-privilege guidance
- Bắt đầu Project Member từ read-only rồi mở thêm quyền thật cần thiết.
- Tránh cấp delete/configure rộng nếu chỉ cần vận hành.
- Tách người điều khiển thiết bị khỏi người chỉnh rule nếu dự án yêu cầu phân tách trách nhiệm.

## Example role design matrix
| Pattern                 | Read            | Execute         | Configure       | Member management |
| ----------------------- | --------------- | --------------- | --------------- | ----------------- |
| Manufacturer            | Full            | Full            | Full            | Full              |
| Project Admin           | Full in project | Full in project | Full in project | Full in project   |
| Project Member Viewer   | Configurable    | No              | No              | No                |
| Project Member Operator | Configurable    | Configurable    | Limited         | No                |
| Project Member Engineer | Configurable    | Configurable    | Configurable    | No                |

## Anti-patterns to avoid
- Tạo thêm role top-level mới để mô phỏng viewer/operator nếu Project Member đã đủ linh hoạt.
- Cho Project Admin quyền ngoài project quản lý.
- Cho Project Member chỉnh membership hoặc cấp quyền vượt ra ngoài delegated scope.
- Diễn đạt role names cũ như Project Manager/Operator/Viewer như thể chúng vẫn là chuẩn chính thức.

## Logging and audit implications
- Permission delegation changes by Project Admin must be audited.
- Any elevation to Manufacturer or Project Admin should be tightly controlled and logged.
- Project Member permission-set changes should be traceable per project.

## Related docs
- [Permission Matrices](Permission%20Matrices.md)
- [User Onboarding Guide](User%20Onboarding%20Guide.md)
- [02-Authentication System](../02-System-Architecture/02-Authentication%20System.md)
- [Security Architecture](../08-Development-Guide/Security%20Architecture.md)

## Open questions
- Whether Project Member presets should be formalized in UI as templates or configured fully manually is not yet verified.
- Legacy role names may still appear in historical docs and need phased cleanup.
