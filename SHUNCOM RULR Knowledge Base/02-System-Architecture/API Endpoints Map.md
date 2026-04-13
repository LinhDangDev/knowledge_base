# API Endpoints Map

## Overview
- Canonical topic: API inventory and constraints
- Goal: Tập trung hóa inventory endpoint/channel chính của SHUNCOM RULR, giữ được mức chi tiết đủ dùng cho BA/QA/Dev/Integration, nhưng không xem đây là backend contract cuối cùng nếu chưa có source-code/OpenAPI verification.
- Primary users: BA, PM, QA, Dev, integration team

## Provenance
### Source summary
```yaml
Document status: Canonical draft
Confidence: Medium
Last validated: 2026-04-12
Validated by: Claude Code
Primary source type: kb
Canonical topic: api-endpoints-map
```

### Primary sources used
| Source | Path | Why it matters |
|---|---|---|
| Existing KB doc | `02-System-Architecture/API Endpoints Map.md` (previous content) | canonical inventory baseline |
| Historical KB content | merged from previous development-guide API map | richer endpoint grouping and example payloads |
| Flow doc | `docs/shuncom-iot-screen-flows.md` | maps UI flows needing API support |
| BA doc | `docs/shuncom-iot-ba-user-stories.md` | business operations needing interfaces |
| Traceability map | `docs/shuncom-iot-story-flow-screen-module-mapping.md` | story-screen-module coverage |
| Analysis doc | `SHUNCOM_RULR_IoT_Platform_Analysis.md` | platform/device/rule/dashboard behaviors that imply API needs |
| Manual screenshots | `manual-images/p52_Image352.jpg`, `manual-images/p45_Image333.jpg`, `manual-images/p61_Image376.jpg`, `manual-images/p33_Image301.png` | UI evidence for rule/device/project operations |

### Validation gaps
- Endpoint list hiện tại vẫn chủ yếu là documentation-derived, chưa được đối chiếu với backend source code.
- Payload examples và response schemas nên xem là working draft cho integration/analysis, không phải contract cuối cùng.
- Permission strings, exact path naming, và websocket topics cần backend/source verification trước khi dùng làm production contract.

## Scope
### In scope
- API groups chính theo module
- WebSocket/realtime channels ở mức inventory
- Request/response examples ở mức docs-derived working draft
- Cross-cutting auth/scope/error/rate-limit/business constraints
- Mapping giữa UI/business flow và interface groups

### Out of scope
- OpenAPI/Swagger final contract
- Backend implementation details
- Internal service-to-service interfaces

## Traceability
### Related stories and flows
- Auth & access: Flow 1-3
- Project & GIS: Flow 4-5, 20-22
- Device domain: Flow 6-14
- Rule domain: Flow 15-19
- Operations & analytics: Flow 23-25

### Main module dependencies
- [02-Authentication System](02-Authentication%20System.md)
- [03-Device Management Hub](../03-Device-Management/03-Device%20Management%20Hub.md)
- [04-Rule Engine System](../04-Rule-Management/04-Rule%20Engine%20System.md)
- [05-Project Management](../05-User-Management/05-Project%20Management.md)
- [06-Dashboard Interface](../06-Project-Management/06-Dashboard%20Interface.md)

## Contract posture
- Tài liệu này là **canonical API inventory**.
- Base URLs, endpoint names, permission names, request/response examples có thể hữu ích cho thiết kế và integration discussion, nhưng vẫn là **documentation-derived working assumptions** nếu chưa có backend verification.
- Không nên copy nguyên các ví dụ ở đây sang production contract hoặc source code mà không revalidate.

## Base interface model
```yaml
REST Base URL: https://rulr-aiot.com/api/v1   # documentation-derived working assumption, not backend-verified contract
Realtime Base URL: wss://rulr-aiot.com/ws/v1  # documentation-derived working assumption, not backend-verified contract
Default auth model: Bearer token for protected resources
Default scope model: role + management scope + project/group/device visibility
```

## API groups
### 1. Authentication APIs
| Method | Path                           | Purpose                   |
| ------ | ------------------------------ | ------------------------- |
| POST   | `/auth/login`                  | login bằng credentials    |
| POST   | `/auth/refresh`                | refresh access token      |
| POST   | `/auth/logout`                 | invalidate session        |
| GET    | `/auth/me`                     | current user profile      |
| POST   | `/auth/password/change`        | change password           |
| POST   | `/auth/password/reset-request` | request password reset    |
| POST   | `/auth/password/reset`         | reset password with token |
| POST   | `/auth/mfa/enable`             | enable MFA                |
| POST   | `/auth/mfa/disable`            | disable MFA               |
| POST   | `/auth/mfa/verify`             | verify MFA code           |

#### Example login payload (working draft)
```yaml
POST /auth/login:
  Request:
    {
      "username": "string",
      "password": "string",
      "mfaCode": "string"  # optional if MFA enabled
    }
  Response:
    {
      "success": true,
      "data": {
        "accessToken": "jwt_token",
        "refreshToken": "refresh_token",
        "expiresIn": 3600,
        "user": {
          "id": "uuid",
          "username": "string",
          "displayName": "string",
          "role": "string",
          "permissions": ["array"]
        }
      }
    }
```

#### Core constraints
- Login là public endpoint.
- Sai credentials phải trả về auth failure rõ ràng, không mở rộng visibility quá mức.
- Session/token behavior ảnh hưởng toàn bộ scope và rule/dashboard access.

### 2. User management APIs
| Method | Path                                | Purpose              |     |
| ------ | ----------------------------------- | -------------------- | --- |
| GET    | `/users`                            | list/filter users    |     |
| GET    | `/users/{id}` hoặc `/users/:userId` | get user details     |     |
| POST   | `/users`                            | create user          |     |
| PUT    | `/users/{id}` hoặc `/users/:userId` | update user          |     |
| DELETE | `/users/{id}` hoặc `/users/:userId` | soft-delete user     |     |
| PATCH  | `/users/{id}/status`                | enable/disable user  |     |
| GET    | `/users/{id}/permissions`           | get user permissions |     |
| PUT    | `/users/{id}/roles`                 | assign roles         |     |
| PUT    | `/users/{id}/scope`                 | set management scope |     |

#### Working-draft filter example
```yaml
GET /users?page=1&limit=20&status=active&role=operator&search=john
```

#### Core constraints
- Permission-based access (`user.view`, `user.create`, `user.edit`, `user.delete`) are working-draft names only.
- Management scope phải được áp dụng ở data visibility level.
- Disabled users không được phép login.

### 3. Organization and role APIs
| Method | Path                           | Purpose                    |
| ------ | ------------------------------ | -------------------------- |
| GET    | `/organizations`               | list organizations         |
| GET    | `/organizations/{id}`          | get organization           |
| POST   | `/organizations`               | create organization        |
| PUT    | `/organizations/{id}`          | update organization        |
| DELETE | `/organizations/{id}`          | delete organization        |
| GET    | `/organizations/{id}/users`    | list org users             |
| GET    | `/organizations/{id}/projects` | list org projects          |
| GET    | `/roles`                       | list roles                 |
| GET    | `/roles/{id}`                  | role details               |
| POST   | `/roles`                       | create role                |
| PUT    | `/roles/{id}`                  | update role                |
| DELETE | `/roles/{id}`                  | delete role                |
| GET    | `/roles/permissions`           | list available permissions |

#### Core constraints
- Org/role endpoints govern tenant-level access boundaries.
- Role + scope together determine effective resource visibility.

### 4. Project APIs
| Method | Path                      | Purpose                    |
| ------ | ------------------------- | -------------------------- |
| GET    | `/projects`               | list project hierarchy     |
| GET    | `/projects/{id}`          | get project details        |
| POST   | `/projects`               | create project             |
| PUT    | `/projects/{id}`          | update project             |
| DELETE | `/projects/{id}`          | delete project             |
| GET    | `/projects/{id}/devices`  | list project devices       |
| GET    | `/projects/{id}/children` | list sub-projects          |
| GET    | `/projects/tree`          | get project hierarchy tree |

#### Core constraints
- Project là scope chính cho dashboard, GIS, rules, visibility.
- GIS/boundary/location contract cần backend confirmation chi tiết hơn.
- Unassigned/default project behavior cần được hiểu như một special scope bucket.

### 5. Device management APIs
| Method | Path                                      | Purpose                     |
| ------ | ----------------------------------------- | --------------------------- |
| GET    | `/devices`                                | list/filter devices         |
| GET    | `/devices/{id}` hoặc `/devices/:deviceId` | get device details          |
| POST   | `/devices`                                | register/create device      |
| PUT    | `/devices/{id}` hoặc `/devices/:deviceId` | update device configuration |
| PATCH  | `/devices/{id}`                           | partial update              |
| DELETE | `/devices/{id}` hoặc `/devices/:deviceId` | recycle/delete device       |

#### Working-draft filter example
```yaml
GET /devices?page=1&limit=20&type=gateway&status=online&projectId=uuid&groupId=uuid&search=north
```

### Device action APIs
| Method | Path | Purpose |
|---|---|---|
| POST | `/devices/{id}/actions/power-on` | turn on device |
| POST | `/devices/{id}/actions/power-off` | turn off device |
| POST | `/devices/{id}/actions/dim` | set brightness |
| POST | `/devices/{id}/actions/sync` | sync device |
| POST | `/devices/{id}/actions/reboot` | reboot device |
| POST | `/devices/{id}/actions/read-data` | read current data |
| POST | `/devices/:deviceId/control` | unified control command variant seen in docs |

#### Dim action example (working draft)
```yaml
POST /devices/{id}/actions/dim:
  Request:
    {
      "brightness": 80,
      "transitionTime": 1000
    }
```

### Bulk and lifecycle APIs
| Method | Path | Purpose |
|---|---|---|
| POST | `/devices/batch` | batch create devices |
| POST | `/devices/batch/import` | import from file |
| GET | `/devices/batch/import/:jobId` | import status |
| GET | `/devices/batch/export` | export devices |
| DELETE | `/devices/batch` | batch delete |
| POST | `/devices/actions/bulk` | bulk control |

### Device data APIs
| Method | Path | Purpose |
|---|---|---|
| GET | `/devices/{id}/metrics` | current device metrics |
| GET | `/devices/{id}/metrics/history` | historical metrics |
| GET | `/devices/{id}/alarms` | device alarms |
| GET | `/devices/{id}/operations` | operation history |

#### Metrics query example (working draft)
```yaml
GET /devices/{id}/metrics/history?from=2025-01-01&to=2025-01-31&interval=hour&metrics=voltage,current,power
```

#### Core constraints
- Device fields và validation thay đổi theo type/subtype.
- Batch import có giới hạn 5000 records theo tài liệu hiện có.
- Delete có thể bị chặn bởi bindings/rules/associations.
- Project/group/coordinate data ảnh hưởng dashboard, GIS, schedules, rules.

### 6. Device group and type APIs
| Method | Path                                   | Purpose                   |
| ------ | -------------------------------------- | ------------------------- |
| GET    | `/device-groups`                       | list groups               |
| GET    | `/device-groups/{id}`                  | group details             |
| POST   | `/device-groups`                       | create group              |
| PUT    | `/device-groups/{id}`                  | update group              |
| DELETE | `/device-groups/{id}`                  | delete group              |
| POST   | `/device-groups/{id}/devices`          | add devices to group      |
| DELETE | `/device-groups/{id}/devices`          | remove devices from group |
| POST   | `/device-groups/{id}/sync`             | sync multicast group      |
| POST   | `/device-groups/{id}/actions/{action}` | group control             |
| GET    | `/device-types`                        | list device types         |
| GET    | `/device-types/{code}`                 | type details              |
| GET    | `/device-types/{code}/template`        | import template           |

#### Core constraints
- Group/device membership affects operations, scope, and sometimes rules.
- Multicast/sync behaviors may be type/protocol specific.

### 7. Rule management APIs
| Method | Path                                | Purpose                |
| ------ | ----------------------------------- | ---------------------- |
| GET    | `/rules/platform`                   | list platform rules    |
| GET    | `/rules/platform/{id}`              | platform rule details  |
| POST   | `/rules/platform`                   | create platform rule   |
| PUT    | `/rules/platform/{id}`              | update platform rule   |
| DELETE | `/rules/platform/{id}`              | delete platform rule   |
| POST   | `/rules/platform/{id}/enable`       | enable rule            |
| POST   | `/rules/platform/{id}/disable`      | disable rule           |
| POST   | `/rules/platform/{id}/execute`      | execute manually       |
| GET    | `/rules/platform/{id}/executions`   | execution history      |
| GET    | `/rules/local`                      | list local rules       |
| GET    | `/rules/local/{id}`                 | local rule details     |
| POST   | `/rules/local`                      | create local rule      |
| PUT    | `/rules/local/{id}`                 | update local rule      |
| DELETE | `/rules/local/{id}`                 | delete local rule      |
| POST   | `/rules/local/{id}/sync`            | sync to gateway/device |
| DELETE | `/rules/local/gateway/{gatewayId}`  | clear gateway rules    |
| GET    | `/rules/alarms` hoặc `/rules/alarm` | list alarm rules       |
| GET    | `/rules/alarm/{id}`                 | alarm rule details     |
| POST   | `/rules/alarm`                      | create alarm rule      |
| PUT    | `/rules/alarm/{id}`                 | update alarm rule      |
| DELETE | `/rules/alarm/{id}`                 | delete alarm rule      |

#### Core constraints
- Platform rules và local rules có model hành vi khác nhau.
- Local rules cần sync result tracking.
- Alarm rules cần silent period, recipients, severity, và possibly auto-handle logic.
- Timezone và coordinates ảnh hưởng sunrise/sunset/time-based rules.

### 8. Alarm and notification APIs
| Method | Path | Purpose |
|---|---|---|
| GET | `/alarms` | list alarms |
| GET | `/alarms/{id}` | alarm details |
| POST | `/alarms/{id}/acknowledge` | acknowledge alarm |
| POST | `/alarms/{id}/resolve` | resolve alarm |
| POST | `/alarms/batch/acknowledge` | batch acknowledge |
| POST | `/alarms/batch/resolve` | batch resolve |
| GET | `/alarms/statistics` | alarm statistics |

#### Working-draft filter example
```yaml
GET /alarms?status=active&severity=critical&deviceId=uuid&from=2025-01-01&to=2025-01-31
```

#### Core constraints
- Alarm handling flows tie strongly to ops dashboards and rule engine.
- Status transitions and notification behaviors need backend verification if used as hard contract.

### 9. Dashboard, analytics, recycle-bin, settings, reports, audit
| Method | Path                                         | Purpose                    |
| ------ | -------------------------------------------- | -------------------------- |
| GET    | `/dashboard/statistics`                      | overview KPIs              |
| GET    | `/dashboard/energy` hoặc `/analytics/energy` | energy analytics           |
| GET    | `/dashboard/alarms/summary`                  | alarm summary              |
| GET    | `/dashboard/devices/status`                  | device status distribution |
| GET    | `/dashboard/map-data`                        | GIS map data               |
| GET    | `/recycle-bin`                               | deleted items              |
| POST   | `/recycle-bin/{id}/restore`                  | restore item               |
| DELETE | `/recycle-bin/{id}`                          | permanent delete           |
| DELETE | `/recycle-bin/clear`                         | clear all                  |
| GET    | `/settings/system`                           | system settings            |
| PUT    | `/settings/system`                           | update settings            |
| GET    | `/settings/timezone`                         | timezone setting           |
| PUT    | `/settings/timezone`                         | update timezone            |
| GET    | `/settings/notifications`                    | notification settings      |
| PUT    | `/settings/notifications`                    | update notifications       |
| GET    | `/reports/energy`                            | energy report              |
| GET    | `/reports/device-status`                     | device status report       |
| GET    | `/reports/alarms`                            | alarm report               |
| GET    | `/reports/operations`                        | operations report          |
| POST   | `/reports/generate`                          | generate custom report     |
| GET    | `/reports/{id}/download`                     | download report            |
| GET    | `/audit/logs`                                | audit logs                 |
| GET    | `/audit/logs/{id}`                           | audit log detail           |
| GET    | `/audit/user/{userId}`                       | user activity              |

#### Example dashboard response (working draft)
```yaml
GET /dashboard/statistics?projectId=uuid:
  Response:
    {
      "devices": {
        "total": 1000,
        "online": 950,
        "offline": 45,
        "alarm": 5
      },
      "byType": {
        "gateway": 50,
        "lightController": 800,
        "fixture": 800,
        "meter": 100
      },
      "energy": {
        "today": 1500.5,
        "month": 45000.0,
        "unit": "kWh"
      }
    }
```

#### Core constraints
- Analytics phải tôn trọng project scope.
- Energy source composition có thể phụ thuộc project display configuration.
- Recycle-bin behavior must align with lifecycle and binding rules.
- Settings like timezone have cross-cutting impact on rules and displays.

## Realtime / WebSocket inventory
### Connection
| Interface | Purpose |
|---|---|
| `wss://rulr-aiot.com/ws/v1` | realtime updates cho dashboard/ops |

### Subscribe example (working draft)
```json
{
  "type": "subscribe",
  "topics": [
    "devices.status",
    "devices.{deviceId}.metrics",
    "alarms.new",
    "rules.execution"
  ]
}
```

### Message/channel groups
| Topic / message type | Purpose |
|---|---|
| `device.status` / `device.status.update` | cập nhật trạng thái thiết bị |
| `devices.{id}.metrics` | metrics updates |
| `alarms` / `alarm.triggered` / `alarms.new` | thông báo alarm realtime |
| `rules` / `rule.executed` / `rules.execution` | phản hồi rule execution |
| `dashboard.statistics` | stats updates |

#### Core constraints
- Realtime visibility phải tuân theo scope.
- Client có thể subscribe theo project/device filters.
- Fallback polling behavior chưa được xác nhận từ source code.

## Cross-cutting constraints
### Auth and scope
- Hầu hết endpoints ngoài auth đều là protected.
- Access phụ thuộc role permissions và management scope.
- Project/group/device visibility phải được áp dụng nhất quán.

### Validation and business rules
- Type-specific device validation.
- Rule-condition compatibility validation.
- Timezone-sensitive scheduling.
- Coordinate-dependent GIS/sunrise-sunset logic.
- Binding conflict checks trước delete/move/disassociate quan trọng.

### Error model
| Code | Typical meaning |
|---|---|
| 400 | malformed request / validation format issue |
| 401 | auth failed / token invalid |
| 403 | permission or scope denied |
| 404 | target resource not found |
| 409 | business conflict (bindings, state conflict) |
| 422 | semantic validation failed |
| 429 | rate limit exceeded |
| 500+ | server/platform error |

### Rate-limit and bulk-processing notes
- Authentication endpoints thường có rate limits thấp hơn.
- Bulk import là async/batch behavior.
- Large list/analytics endpoints cần pagination/filtering support.

## Logging and observability implications
- Audit log: user actions on auth, device, project, rule, alarm processing.
- Operational log: command results, sync status, batch import results, export requests.
- Realtime events: device updates, alarms, rule execution.

## Related docs
- [02-Authentication System](02-Authentication%20System.md)
- [03-Device Management Hub](../03-Device-Management/03-Device%20Management%20Hub.md)
- [04-Rule Engine System](../04-Rule-Management/04-Rule%20Engine%20System.md)
- [05-Project Management](../05-User-Management/05-Project%20Management.md)
- [06-Dashboard Interface](../06-Project-Management/06-Dashboard%20Interface.md)
- [API Design Patterns](../08-Development-Guide/API%20Design%20Patterns.md)

## Recommended usage
- Dùng tài liệu này như **canonical API inventory**.
- Nếu cần contract chính thức để dev/integration, phải verify lại với backend code hoặc OpenAPI source.
- Không nên copy payload examples, permission strings, topic names, hoặc base URLs từ đây sang contract production mà không revalidate.

## Open questions
- Endpoint payloads/responses, exact path naming, và permission strings cuối cùng cần backend/source confirmation.
- Realtime subscription auth/filter semantics cần code-level verification trước khi dùng làm integration contract chính thức.
