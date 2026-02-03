# 🗺️ API Endpoints Map

> Complete reference of all API endpoints for SHUNCOM RULR IoT Platform

{% hint style="info" %}
**Platform:** SHUNCOM RULR IoT Platform v1.1 | **Last Updated:** January 2025
{% endhint %}


---

## 📋 Endpoint Overview

### Base URLs
```yaml
Production: https://api.shuncom-rulr.com/v1
Staging: https://api-staging.shuncom-rulr.com/v1
Development: http://localhost:3000/api/v1
WebSocket: wss://api.shuncom-rulr.com/ws/v1
```

### Authentication
All endpoints (except `/auth/login`) require:
```
Authorization: Bearer {access_token}
```

---

## 🔐 Authentication Endpoints

| Method | Endpoint | Description | Auth Required |
|--------|----------|-------------|---------------|
| POST | `/auth/login` | User login | No |
| POST | `/auth/refresh` | Refresh access token | No (uses refresh token) |
| POST | `/auth/logout` | Logout and invalidate tokens | Yes |
| GET | `/auth/me` | Get current user profile | Yes |
| POST | `/auth/password/change` | Change password | Yes |
| POST | `/auth/password/reset-request` | Request password reset | No |
| POST | `/auth/password/reset` | Reset password with token | No |
| POST | `/auth/mfa/enable` | Enable MFA | Yes |
| POST | `/auth/mfa/disable` | Disable MFA | Yes |
| POST | `/auth/mfa/verify` | Verify MFA code | Yes |

### Login Request/Response
```yaml
POST /auth/login:
  Request:
    {
      "username": "string",
      "password": "string",
      "mfaCode": "string"  # Optional, if MFA enabled
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

---

## 👥 User Management Endpoints

| Method | Endpoint | Description | Permission |
|--------|----------|-------------|------------|
| GET | `/users` | List users | users.read |
| GET | `/users/{id}` | Get user details | users.read |
| POST | `/users` | Create user | users.write |
| PUT | `/users/{id}` | Update user | users.write |
| DELETE | `/users/{id}` | Delete user | users.delete |
| PATCH | `/users/{id}/status` | Enable/disable user | users.write |
| GET | `/users/{id}/permissions` | Get user permissions | users.read |
| PUT | `/users/{id}/roles` | Assign roles | users.admin |
| PUT | `/users/{id}/scope` | Set management scope | users.admin |

### User Filters
```yaml
GET /users?page=1&limit=20&status=active&role=operator&search=john
```

---

## 🏢 Organization Endpoints

| Method | Endpoint | Description | Permission |
|--------|----------|-------------|------------|
| GET | `/organizations` | List organizations | org.read |
| GET | `/organizations/{id}` | Get organization | org.read |
| POST | `/organizations` | Create organization | org.write |
| PUT | `/organizations/{id}` | Update organization | org.write |
| DELETE | `/organizations/{id}` | Delete organization | org.delete |
| GET | `/organizations/{id}/users` | List org users | org.read |
| GET | `/organizations/{id}/projects` | List org projects | org.read |

---

## 👤 Role Endpoints

| Method | Endpoint | Description | Permission |
|--------|----------|-------------|------------|
| GET | `/roles` | List roles | roles.read |
| GET | `/roles/{id}` | Get role details | roles.read |
| POST | `/roles` | Create custom role | roles.write |
| PUT | `/roles/{id}` | Update role | roles.write |
| DELETE | `/roles/{id}` | Delete role | roles.delete |
| GET | `/roles/permissions` | List all permissions | roles.read |

---

## 📁 Project Endpoints

| Method | Endpoint | Description | Permission |
|--------|----------|-------------|------------|
| GET | `/projects` | List projects | projects.read |
| GET | `/projects/{id}` | Get project details | projects.read |
| POST | `/projects` | Create project | projects.write |
| PUT | `/projects/{id}` | Update project | projects.write |
| DELETE | `/projects/{id}` | Delete project | projects.delete |
| GET | `/projects/{id}/devices` | List project devices | projects.read |
| GET | `/projects/{id}/children` | List sub-projects | projects.read |
| GET | `/projects/tree` | Get project hierarchy | projects.read |

---

## 🔧 Device Endpoints

### Device CRUD
| Method | Endpoint | Description | Permission |
|--------|----------|-------------|------------|
| GET | `/devices` | List devices | devices.read |
| GET | `/devices/{id}` | Get device details | devices.read |
| POST | `/devices` | Create device | devices.write |
| PUT | `/devices/{id}` | Update device | devices.write |
| PATCH | `/devices/{id}` | Partial update | devices.write |
| DELETE | `/devices/{id}` | Delete device (recycle) | devices.delete |

### Device Filters
```yaml
GET /devices?page=1&limit=20&type=gateway&status=online&projectId=uuid&groupId=uuid&search=north
```

### Device Actions
| Method | Endpoint | Description | Permission |
|--------|----------|-------------|------------|
| POST | `/devices/{id}/actions/power-on` | Turn on device | devices.execute |
| POST | `/devices/{id}/actions/power-off` | Turn off device | devices.execute |
| POST | `/devices/{id}/actions/dim` | Set brightness | devices.execute |
| POST | `/devices/{id}/actions/sync` | Sync device | devices.execute |
| POST | `/devices/{id}/actions/reboot` | Reboot device | devices.execute |
| POST | `/devices/{id}/actions/read-data` | Read current data | devices.read |

### Dim Action Request
```yaml
POST /devices/{id}/actions/dim:
  Request:
    {
      "brightness": 80,
      "transitionTime": 1000  # milliseconds, optional
    }
```

### Bulk Operations
| Method | Endpoint | Description | Permission |
|--------|----------|-------------|------------|
| POST | `/devices/batch` | Batch create devices | devices.write |
| POST | `/devices/batch/import` | Import from file | devices.write |
| GET | `/devices/batch/export` | Export to file | devices.read |
| DELETE | `/devices/batch` | Batch delete | devices.delete |
| POST | `/devices/actions/bulk` | Bulk control | devices.execute |

### Device Data
| Method | Endpoint | Description | Permission |
|--------|----------|-------------|------------|
| GET | `/devices/{id}/metrics` | Get device metrics | devices.read |
| GET | `/devices/{id}/metrics/history` | Historical metrics | devices.read |
| GET | `/devices/{id}/alarms` | Device alarms | devices.read |
| GET | `/devices/{id}/operations` | Operation history | devices.read |

### Metrics Query
```yaml
GET /devices/{id}/metrics/history?from=2025-01-01&to=2025-01-31&interval=hour&metrics=voltage,current,power
```

---

## 📦 Device Group Endpoints

| Method | Endpoint | Description | Permission |
|--------|----------|-------------|------------|
| GET | `/device-groups` | List groups | devices.read |
| GET | `/device-groups/{id}` | Get group details | devices.read |
| POST | `/device-groups` | Create group | devices.write |
| PUT | `/device-groups/{id}` | Update group | devices.write |
| DELETE | `/device-groups/{id}` | Delete group | devices.delete |
| POST | `/device-groups/{id}/devices` | Add devices to group | devices.write |
| DELETE | `/device-groups/{id}/devices` | Remove devices | devices.write |
| POST | `/device-groups/{id}/sync` | Sync multicast group | devices.execute |
| POST | `/device-groups/{id}/actions/{action}` | Group control | devices.execute |

---

## 📋 Device Type Endpoints

| Method | Endpoint | Description | Permission |
|--------|----------|-------------|------------|
| GET | `/device-types` | List device types | devices.read |
| GET | `/device-types/{code}` | Get type details | devices.read |
| GET | `/device-types/{code}/template` | Get import template | devices.read |

---

## ⚙️ Rule Endpoints

### Platform Rules
| Method | Endpoint | Description | Permission |
|--------|----------|-------------|------------|
| GET | `/rules/platform` | List platform rules | rules.read |
| GET | `/rules/platform/{id}` | Get rule details | rules.read |
| POST | `/rules/platform` | Create rule | rules.write |
| PUT | `/rules/platform/{id}` | Update rule | rules.write |
| DELETE | `/rules/platform/{id}` | Delete rule | rules.delete |
| POST | `/rules/platform/{id}/enable` | Enable rule | rules.write |
| POST | `/rules/platform/{id}/disable` | Disable rule | rules.write |
| POST | `/rules/platform/{id}/execute` | Execute manually | rules.execute |
| GET | `/rules/platform/{id}/executions` | Execution history | rules.read |

### Local Rules
| Method | Endpoint | Description | Permission |
|--------|----------|-------------|------------|
| GET | `/rules/local` | List local rules | rules.read |
| GET | `/rules/local/{id}` | Get rule details | rules.read |
| POST | `/rules/local` | Create rule | rules.write |
| PUT | `/rules/local/{id}` | Update rule | rules.write |
| DELETE | `/rules/local/{id}` | Delete rule | rules.delete |
| POST | `/rules/local/{id}/sync` | Sync to gateway | rules.execute |
| DELETE | `/rules/local/gateway/{gatewayId}` | Clear gateway rules | rules.delete |

### Alarm Rules
| Method | Endpoint | Description | Permission |
|--------|----------|-------------|------------|
| GET | `/rules/alarm` | List alarm rules | rules.read |
| GET | `/rules/alarm/{id}` | Get rule details | rules.read |
| POST | `/rules/alarm` | Create rule | rules.write |
| PUT | `/rules/alarm/{id}` | Update rule | rules.write |
| DELETE | `/rules/alarm/{id}` | Delete rule | rules.delete |

---

## 🚨 Alarm Endpoints

| Method | Endpoint | Description | Permission |
|--------|----------|-------------|------------|
| GET | `/alarms` | List alarms | alarms.read |
| GET | `/alarms/{id}` | Get alarm details | alarms.read |
| POST | `/alarms/{id}/acknowledge` | Acknowledge alarm | alarms.write |
| POST | `/alarms/{id}/resolve` | Resolve alarm | alarms.write |
| POST | `/alarms/batch/acknowledge` | Batch acknowledge | alarms.write |
| POST | `/alarms/batch/resolve` | Batch resolve | alarms.write |
| GET | `/alarms/statistics` | Alarm statistics | alarms.read |

### Alarm Filters
```yaml
GET /alarms?status=active&severity=critical&deviceId=uuid&from=2025-01-01&to=2025-01-31
```

---

## 📊 Dashboard Endpoints

| Method | Endpoint | Description | Permission |
|--------|----------|-------------|------------|
| GET | `/dashboard/statistics` | Device statistics | dashboard.read |
| GET | `/dashboard/energy` | Energy consumption | dashboard.read |
| GET | `/dashboard/alarms/summary` | Alarm summary | dashboard.read |
| GET | `/dashboard/devices/status` | Device status distribution | dashboard.read |
| GET | `/dashboard/map-data` | GIS map data | dashboard.read |

### Statistics Response
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

---

## 🗑️ Recycle Bin Endpoints

| Method | Endpoint | Description | Permission |
|--------|----------|-------------|------------|
| GET | `/recycle-bin` | List deleted items | devices.read |
| POST | `/recycle-bin/{id}/restore` | Restore item | devices.write |
| DELETE | `/recycle-bin/{id}` | Permanent delete | devices.delete |
| DELETE | `/recycle-bin/clear` | Clear all | devices.delete |

---

## ⚙️ Settings Endpoints

| Method | Endpoint | Description | Permission |
|--------|----------|-------------|------------|
| GET | `/settings/system` | Get system settings | settings.read |
| PUT | `/settings/system` | Update system settings | settings.write |
| GET | `/settings/timezone` | Get timezone | settings.read |
| PUT | `/settings/timezone` | Set timezone | settings.write |
| GET | `/settings/notifications` | Notification settings | settings.read |
| PUT | `/settings/notifications` | Update notifications | settings.write |

---

## 📈 Reports Endpoints

| Method | Endpoint | Description | Permission |
|--------|----------|-------------|------------|
| GET | `/reports/energy` | Energy report | reports.read |
| GET | `/reports/device-status` | Device status report | reports.read |
| GET | `/reports/alarms` | Alarm report | reports.read |
| GET | `/reports/operations` | Operations report | reports.read |
| POST | `/reports/generate` | Generate custom report | reports.write |
| GET | `/reports/{id}/download` | Download report | reports.read |

---

## 📝 Audit Endpoints

| Method | Endpoint | Description | Permission |
|--------|----------|-------------|------------|
| GET | `/audit/logs` | List audit logs | audit.read |
| GET | `/audit/logs/{id}` | Get log details | audit.read |
| GET | `/audit/user/{userId}` | User activity | audit.read |

---

## 🔌 WebSocket Topics

### Subscribe Message
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

### Available Topics
| Topic | Description | Payload |
|-------|-------------|---------|
| `devices.status` | All device status changes | `{deviceId, status, timestamp}` |
| `devices.{id}.status` | Specific device status | `{status, timestamp}` |
| `devices.{id}.metrics` | Device metrics update | `{metrics, timestamp}` |
| `alarms.new` | New alarm notifications | `{alarm object}` |
| `alarms.{severity}` | Alarms by severity | `{alarm object}` |
| `rules.execution` | Rule execution events | `{ruleId, status, timestamp}` |
| `dashboard.statistics` | Stats updates | `{statistics object}` |

---

## 🔗 Related Documentation

- **[API Design Patterns](API%20Design%20Patterns.md)**: API standards and conventions
- **[02-Authentication System](../02-System-Architecture/02-Authentication%20System.md)**: Authentication details
- **[Database Schema](../02-System-Architecture/Database%20Schema.md)**: Data models

---

**Usage:** Use this as a quick reference when implementing API integrations or debugging API issues.
