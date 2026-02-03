# 🔌 API Endpoints Map

> Comprehensive API reference for SHUNCOM RULR IoT Platform

{% hint style="info" %}
**Platform:** SHUNCOM RULR IoT Platform v1.1 | **Last Updated:** January 2025
{% endhint %}

**API Version**: v1.0
**Base URL**: `https://rulr-aiot.com/api/v1`

---

## 📋 Table of Contents

1. [Authentication APIs](#authentication-apis)
2. [User Management APIs](#user-management-apis)
3. [Device Management APIs](#device-management-apis)
4. [Rule Engine APIs](#rule-engine-apis)
5. [Project Management APIs](#project-management-apis)
6. [Dashboard & Analytics APIs](#dashboard--analytics-apis)
7. [Real-time WebSocket APIs](#real-time-websocket-apis)
8. [Common Response Codes](#common-response-codes)

---

## 🔐 Authentication APIs

### POST /auth/login
**Description**: User authentication with username/password
**Authentication**: None (Public endpoint)
**Rate Limit**: 5 requests per minute per IP

**Request Body**:
```json
{
  "username": "admin@shuncom.com",
  "password": "SecurePassword123!",
  "rememberMe": true
}
```

**Success Response (200)**:
```json
{
  "success": true,
  "data": {
    "accessToken": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...",
    "refreshToken": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...",
    "expiresIn": 3600,
    "user": {
      "id": "usr_12345",
      "username": "admin@shuncom.com",
      "displayName": "System Administrator",
      "role": {
        "id": "role_001",
        "name": "Super Admin",
        "permissions": ["*"]
      },
      "organization": {
        "id": "org_001",
        "name": "Shanghai Shuncom AIOT Co., Ltd",
        "logo": "https://cdn.rulr-aiot.com/logos/org_001.png"
      },
      "timezone": "Asia/Shanghai",
      "preferences": {
        "language": "zh-CN",
        "theme": "light"
      }
    }
  }
}
```

**Error Response (401)**:
```json
{
  "success": false,
  "error": {
    "code": "AUTH_INVALID_CREDENTIALS",
    "message": "Invalid username or password",
    "details": {
      "attemptsRemaining": 3,
      "lockoutThreshold": 5
    }
  }
}
```

### POST /auth/refresh
**Description**: Refresh access token using refresh token
**Authentication**: Refresh Token Required

**Request Body**:
```json
{
  "refreshToken": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9..."
}
```

**Success Response (200)**:
```json
{
  "success": true,
  "data": {
    "accessToken": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...",
    "expiresIn": 3600
  }
}
```

### POST /auth/logout
**Description**: Invalidate current session
**Authentication**: Bearer Token Required

**Request Headers**:
```
Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...
```

**Success Response (200)**:
```json
{
  "success": true,
  "message": "Logged out successfully"
}
```

### POST /auth/password/reset-request
**Description**: Request password reset email
**Authentication**: None (Public endpoint)

**Request Body**:
```json
{
  "email": "admin@shuncom.com"
}
```

**Success Response (200)**:
```json
{
  "success": true,
  "message": "Password reset instructions sent to email"
}
```

---

## 👥 User Management APIs

### GET /users
**Description**: List all users with pagination and filtering
**Authentication**: Bearer Token + Permission: `user.view`
**Rate Limit**: 100 requests per minute

**Query Parameters**:
```
?page=1
&limit=20
&search=admin
&role=role_001
&status=active
&organizationId=org_001
&sortBy=createdAt
&sortOrder=desc
```

**Success Response (200)**:
```json
{
  "success": true,
  "data": {
    "users": [
      {
        "id": "usr_12345",
        "username": "admin@shuncom.com",
        "displayName": "System Administrator",
        "email": "admin@shuncom.com",
        "phone": "+86 138 1234 5678",
        "role": {
          "id": "role_001",
          "name": "Super Admin"
        },
        "status": "active",
        "organization": {
          "id": "org_001",
          "name": "Shanghai Shuncom AIOT Co., Ltd"
        },
        "managementScope": {
          "projects": ["*"],
          "deviceGroups": ["*"],
          "productCategories": ["*"]
        },
        "lastLogin": "2025-01-26T10:30:00Z",
        "createdAt": "2024-01-01T00:00:00Z",
        "updatedAt": "2025-01-26T08:00:00Z"
      }
    ],
    "pagination": {
      "page": 1,
      "limit": 20,
      "total": 150,
      "totalPages": 8
    }
  }
}
```

### POST /users
**Description**: Create a new user
**Authentication**: Bearer Token + Permission: `user.create`

**Request Body**:
```json
{
  "username": "operator@shuncom.com",
  "displayName": "Device Operator",
  "email": "operator@shuncom.com",
  "phone": "+86 138 8888 9999",
  "password": "TempPassword123!",
  "roleId": "role_003",
  "organizationId": "org_001",
  "managementScope": {
    "projects": ["prj_001", "prj_002"],
    "deviceGroups": ["grp_lighting_zone_a"],
    "productCategories": ["smart_gateway", "light_controller"]
  },
  "timezone": "Asia/Shanghai",
  "preferences": {
    "language": "zh-CN",
    "emailNotifications": true,
    "smsNotifications": false
  }
}
```

**Success Response (201)**:
```json
{
  "success": true,
  "data": {
    "id": "usr_67890",
    "username": "operator@shuncom.com",
    "displayName": "Device Operator",
    "createdAt": "2025-01-26T11:00:00Z"
  }
}
```

### PUT /users/:userId
**Description**: Update user information
**Authentication**: Bearer Token + Permission: `user.edit`

**Request Body** (partial update supported):
```json
{
  "displayName": "Senior Device Operator",
  "phone": "+86 138 8888 8888",
  "roleId": "role_002",
  "status": "active"
}
```

**Success Response (200)**:
```json
{
  "success": true,
  "data": {
    "id": "usr_67890",
    "updatedAt": "2025-01-26T11:30:00Z"
  }
}
```

### DELETE /users/:userId
**Description**: Delete user (soft delete)
**Authentication**: Bearer Token + Permission: `user.delete`

**Success Response (200)**:
```json
{
  "success": true,
  "message": "User deleted successfully"
}
```

---

## 🔧 Device Management APIs

### GET /devices
**Description**: List devices with advanced filtering
**Authentication**: Bearer Token + Permission: `device.view`
**Rate Limit**: 200 requests per minute

**Query Parameters**:
```
?page=1
&limit=50
&projectId=prj_001
&deviceType=light_controller
&status=online
&groupId=grp_lighting_zone_a
&search=LED-001
&hasCoordinates=true
&boundingBox=31.2,121.4,31.3,121.5
&sortBy=name
&sortOrder=asc
```

**Success Response (200)**:
```json
{
  "success": true,
  "data": {
    "devices": [
      {
        "id": "dev_lc_001",
        "name": "LED-CTRL-Zone-A-001",
        "deviceType": "light_controller",
        "subType": "zigbee_controller",
        "status": "online",
        "project": {
          "id": "prj_001",
          "name": "Smart Street Lighting Project"
        },
        "group": {
          "id": "grp_lighting_zone_a",
          "name": "Zone A Lighting"
        },
        "gateway": {
          "id": "dev_gw_001",
          "name": "Gateway-001"
        },
        "associatedDevices": {
          "fixtures": ["dev_fix_001", "dev_fix_002"],
          "pole": "dev_pole_001"
        },
        "coordinates": {
          "latitude": 31.2304,
          "longitude": 121.4737,
          "address": "Nanjing Road, Shanghai"
        },
        "attributes": {
          "brightness": 75,
          "power": "on",
          "voltage": 220.5,
          "current": 1.2,
          "temperature": 45.5,
          "signalStrength": -65
        },
        "communication": {
          "protocol": "zigbee",
          "lastSeen": "2025-01-26T11:45:00Z",
          "uptime": 864000
        },
        "metadata": {
          "manufacturer": "Shuncom",
          "model": "ZB-LC-2000",
          "firmwareVersion": "v2.1.5",
          "installationDate": "2024-06-15"
        },
        "createdAt": "2024-06-15T09:00:00Z",
        "updatedAt": "2025-01-26T11:45:00Z"
      }
    ],
    "pagination": {
      "page": 1,
      "limit": 50,
      "total": 2340,
      "totalPages": 47
    },
    "statistics": {
      "online": 2180,
      "offline": 160,
      "total": 2340
    }
  }
}
```

### POST /devices
**Description**: Register a new device
**Authentication**: Bearer Token + Permission: `device.create`

**Request Body**:
```json
{
  "name": "LED-CTRL-Zone-B-050",
  "deviceType": "light_controller",
  "subType": "zigbee_controller",
  "projectId": "prj_001",
  "groupId": "grp_lighting_zone_b",
  "gatewayId": "dev_gw_002",
  "coordinates": {
    "latitude": 31.2350,
    "longitude": 121.4800,
    "address": "West Nanjing Road, Shanghai"
  },
  "configuration": {
    "manufacturer": "Shuncom",
    "model": "ZB-LC-2000",
    "serialNumber": "ZB-LC-2000-050",
    "installationDate": "2025-01-26"
  },
  "associatedDevices": {
    "fixtures": ["dev_fix_150", "dev_fix_151"],
    "pole": "dev_pole_050"
  }
}
```

**Success Response (201)**:
```json
{
  "success": true,
  "data": {
    "id": "dev_lc_050",
    "name": "LED-CTRL-Zone-B-050",
    "deviceType": "light_controller",
    "createdAt": "2025-01-26T12:00:00Z"
  }
}
```

### PUT /devices/:deviceId
**Description**: Update device configuration
**Authentication**: Bearer Token + Permission: `device.edit`

**Request Body**:
```json
{
  "name": "LED-CTRL-Zone-B-050-Updated",
  "groupId": "grp_lighting_zone_c",
  "coordinates": {
    "latitude": 31.2351,
    "longitude": 121.4801
  },
  "associatedDevices": {
    "fixtures": ["dev_fix_150", "dev_fix_151", "dev_fix_152"]
  }
}
```

### POST /devices/:deviceId/control
**Description**: Send control command to device
**Authentication**: Bearer Token + Permission: `device.control`

**Request Body**:
```json
{
  "command": "setBrightness",
  "parameters": {
    "brightness": 80,
    "transitionTime": 5
  }
}
```

**Success Response (200)**:
```json
{
  "success": true,
  "data": {
    "commandId": "cmd_12345",
    "status": "pending",
    "sentAt": "2025-01-26T12:05:00Z"
  }
}
```

### POST /devices/batch/import
**Description**: Batch import devices from CSV/Excel
**Authentication**: Bearer Token + Permission: `device.import`
**Rate Limit**: 5 requests per hour
**Max Devices**: 5000 per request

**Request Body** (multipart/form-data):
```
file: devices_import.csv
projectId: prj_001
validateOnly: false
```

**Success Response (202)**:
```json
{
  "success": true,
  "data": {
    "jobId": "import_job_789",
    "status": "processing",
    "totalRecords": 1500,
    "estimatedCompletionTime": "2025-01-26T12:30:00Z"
  }
}
```

### GET /devices/batch/import/:jobId
**Description**: Check batch import status
**Authentication**: Bearer Token

**Success Response (200)**:
```json
{
  "success": true,
  "data": {
    "jobId": "import_job_789",
    "status": "completed",
    "startedAt": "2025-01-26T12:00:00Z",
    "completedAt": "2025-01-26T12:25:00Z",
    "results": {
      "total": 1500,
      "successful": 1480,
      "failed": 20,
      "errors": [
        {
          "row": 45,
          "error": "Invalid gateway ID: dev_gw_999",
          "deviceName": "LED-CTRL-Invalid-001"
        }
      ]
    }
  }
}
```

### DELETE /devices/:deviceId
**Description**: Delete device (with binding check)
**Authentication**: Bearer Token + Permission: `device.delete`

**Query Parameters**:
```
?force=false
&moveToRecycleBin=true
```

**Success Response (200)**:
```json
{
  "success": true,
  "message": "Device moved to recycle bin",
  "data": {
    "recycleId": "recycle_123",
    "recoveryDeadline": "2025-02-26T12:00:00Z"
  }
}
```

**Error Response (409)** - Device has bindings:
```json
{
  "success": false,
  "error": {
    "code": "DEVICE_HAS_BINDINGS",
    "message": "Cannot delete device with active bindings",
    "details": {
      "rules": ["rule_001", "rule_045"],
      "alarms": ["alarm_003"],
      "associatedDevices": ["dev_fix_001", "dev_fix_002"]
    }
  }
}
```

---

## ⚙️ Rule Engine APIs

### GET /rules/platform
**Description**: List platform rules
**Authentication**: Bearer Token + Permission: `rule.view`

**Query Parameters**:
```
?page=1
&limit=20
&projectId=prj_001
&status=enabled
&ruleType=scheduled
```

**Success Response (200)**:
```json
{
  "success": true,
  "data": {
    "rules": [
      {
        "id": "rule_001",
        "name": "Evening Light Activation",
        "description": "Turn on street lights at sunset",
        "type": "platform",
        "status": "enabled",
        "project": {
          "id": "prj_001",
          "name": "Smart Street Lighting Project"
        },
        "conditions": [
          {
            "type": "time",
            "operator": "equals",
            "value": "sunset",
            "logic": "AND"
          },
          {
            "type": "attribute",
            "deviceId": "dev_sensor_001",
            "attribute": "illuminance",
            "operator": "lessThan",
            "value": 50,
            "logic": "AND"
          }
        ],
        "actions": [
          {
            "type": "deviceControl",
            "targetType": "group",
            "targetId": "grp_all_street_lights",
            "command": "setBrightness",
            "parameters": {
              "brightness": 100,
              "transitionTime": 10
            }
          }
        ],
        "schedule": {
          "timezone": "Asia/Shanghai",
          "enabledDays": ["monday", "tuesday", "wednesday", "thursday", "friday", "saturday", "sunday"]
        },
        "statistics": {
          "executionCount": 180,
          "lastExecuted": "2025-01-25T18:30:00Z",
          "successRate": 99.4
        },
        "createdBy": "usr_12345",
        "createdAt": "2024-06-15T10:00:00Z",
        "updatedAt": "2025-01-20T14:30:00Z"
      }
    ],
    "pagination": {
      "page": 1,
      "limit": 20,
      "total": 45,
      "totalPages": 3
    }
  }
}
```

### POST /rules/platform
**Description**: Create platform rule
**Authentication**: Bearer Token + Permission: `rule.create`

**Request Body**:
```json
{
  "name": "Midnight Energy Saving",
  "description": "Reduce brightness to 50% after midnight",
  "projectId": "prj_001",
  "status": "enabled",
  "conditions": [
    {
      "type": "time",
      "operator": "between",
      "value": {
        "start": "00:00",
        "end": "05:00"
      },
      "logic": "AND"
    }
  ],
  "actions": [
    {
      "type": "deviceControl",
      "targetType": "group",
      "targetId": "grp_all_street_lights",
      "command": "setBrightness",
      "parameters": {
        "brightness": 50,
        "transitionTime": 30
      }
    }
  ],
  "schedule": {
    "timezone": "Asia/Shanghai",
    "enabledDays": ["monday", "tuesday", "wednesday", "thursday", "friday", "saturday", "sunday"]
  }
}
```

**Success Response (201)**:
```json
{
  "success": true,
  "data": {
    "id": "rule_046",
    "name": "Midnight Energy Saving",
    "createdAt": "2025-01-26T12:30:00Z"
  }
}
```

### POST /rules/local
**Description**: Create local rule (gateway-based)
**Authentication**: Bearer Token + Permission: `rule.create`

**Request Body**:
```json
{
  "name": "Motion Sensor Light Activation",
  "description": "Turn on light when motion detected",
  "gatewayId": "dev_gw_001",
  "status": "enabled",
  "condition": {
    "type": "attribute",
    "deviceId": "dev_sensor_005",
    "attribute": "motion",
    "operator": "equals",
    "value": true
  },
  "action": {
    "type": "deviceControl",
    "deviceId": "dev_lc_001",
    "command": "setPower",
    "parameters": {
      "power": "on",
      "brightness": 100
    }
  },
  "autoSync": true
}
```

**Success Response (201)**:
```json
{
  "success": true,
  "data": {
    "id": "rule_local_001",
    "name": "Motion Sensor Light Activation",
    "syncStatus": "pending",
    "createdAt": "2025-01-26T12:35:00Z"
  }
}
```

### POST /rules/local/:ruleId/sync
**Description**: Synchronize local rule to gateway
**Authentication**: Bearer Token + Permission: `rule.sync`

**Success Response (200)**:
```json
{
  "success": true,
  "data": {
    "syncJobId": "sync_job_456",
    "status": "in_progress",
    "gatewayId": "dev_gw_001"
  }
}
```

### GET /rules/alarms
**Description**: List alarm rules
**Authentication**: Bearer Token + Permission: `alarm.view`

**Success Response (200)**:
```json
{
  "success": true,
  "data": {
    "alarms": [
      {
        "id": "alarm_001",
        "name": "Device Offline Alert",
        "type": "offline_alarm",
        "status": "enabled",
        "conditions": [
          {
            "type": "status",
            "operator": "equals",
            "value": "offline",
            "duration": 300
          }
        ],
        "notifications": {
          "channels": ["email", "sms"],
          "recipients": {
            "groups": ["grp_admins", "grp_operators"],
            "users": ["usr_12345"]
          },
          "silentPeriod": {
            "start": "23:00",
            "end": "07:00"
          }
        },
        "escalation": {
          "enabled": true,
          "levels": [
            {
              "threshold": 600,
              "recipients": ["usr_12345"]
            },
            {
              "threshold": 1800,
              "recipients": ["usr_00001"]
            }
          ]
        },
        "statistics": {
          "triggeredCount": 23,
          "lastTriggered": "2025-01-26T08:15:00Z"
        }
      }
    ]
  }
}
```

---

## 🏢 Project Management APIs

### GET /projects
**Description**: List all projects
**Authentication**: Bearer Token + Permission: `project.view`

**Success Response (200)**:
```json
{
  "success": true,
  "data": {
    "projects": [
      {
        "id": "prj_001",
        "name": "Smart Street Lighting Project",
        "description": "City-wide intelligent street lighting system",
        "organization": {
          "id": "org_001",
          "name": "Shanghai Shuncom AIOT Co., Ltd"
        },
        "location": {
          "city": "Shanghai",
          "district": "Huangpu",
          "address": "Nanjing Road Area"
        },
        "boundary": {
          "type": "Polygon",
          "coordinates": [
            [[121.4700, 31.2300], [121.4800, 31.2300], [121.4800, 31.2400], [121.4700, 31.2400], [121.4700, 31.2300]]
          ]
        },
        "statistics": {
          "totalDevices": 2340,
          "onlineDevices": 2180,
          "deviceTypes": {
            "smart_gateway": 15,
            "light_controller": 800,
            "lighting_fixture": 1500
          }
        },
        "status": "active",
        "createdAt": "2024-01-15T00:00:00Z",
        "updatedAt": "2025-01-26T10:00:00Z"
      }
    ]
  }
}
```

### POST /projects
**Description**: Create new project
**Authentication**: Bearer Token + Permission: `project.create`

**Request Body**:
```json
{
  "name": "Smart Park Lighting",
  "description": "Intelligent lighting for central park",
  "organizationId": "org_001",
  "location": {
    "city": "Shanghai",
    "district": "Pudong",
    "address": "Century Park"
  },
  "boundary": {
    "type": "Polygon",
    "coordinates": [
      [[121.5500, 31.2200], [121.5600, 31.2200], [121.5600, 31.2300], [121.5500, 31.2300], [121.5500, 31.2200]]
    ]
  }
}
```

**Success Response (201)**:
```json
{
  "success": true,
  "data": {
    "id": "prj_002",
    "name": "Smart Park Lighting",
    "createdAt": "2025-01-26T13:00:00Z"
  }
}
```

---

## 📊 Dashboard & Analytics APIs

### GET /dashboard/statistics
**Description**: Get dashboard statistics
**Authentication**: Bearer Token + Permission: `dashboard.view`

**Query Parameters**:
```
?projectId=prj_001
&timeRange=last_24h
```

**Success Response (200)**:
```json
{
  "success": true,
  "data": {
    "overview": {
      "totalDevices": 2340,
      "onlineDevices": 2180,
      "offlineDevices": 160,
      "onlineRate": 93.16,
      "activeAlarms": 5,
      "activeRules": 45
    },
    "devicesByType": {
      "smart_gateway": 15,
      "light_controller": 800,
      "lighting_fixture": 1500,
      "lighting_pole": 800,
      "power_distribution": 12,
      "loop_control": 200,
      "smart_meter": 13
    },
    "devicesByStatus": {
      "online": 2180,
      "offline": 160,
      "maintenance": 0,
      "error": 0
    },
    "energyConsumption": {
      "today": 1850.5,
      "yesterday": 1920.3,
      "thisMonth": 52340.8,
      "lastMonth": 54210.2,
      "unit": "kWh",
      "savings": 3.45
    },
    "recentAlarms": [
      {
        "id": "alarm_evt_001",
        "deviceId": "dev_lc_045",
        "deviceName": "LED-CTRL-Zone-C-045",
        "alarmType": "offline",
        "severity": "high",
        "message": "Device offline for 10 minutes",
        "triggeredAt": "2025-01-26T12:50:00Z",
        "status": "unhandled"
      }
    ],
    "timestamp": "2025-01-26T13:00:00Z"
  }
}
```

### GET /analytics/energy
**Description**: Energy consumption analytics
**Authentication**: Bearer Token + Permission: `analytics.view`

**Query Parameters**:
```
?projectId=prj_001
&startDate=2025-01-01
&endDate=2025-01-26
&granularity=daily
&groupBy=deviceType
```

**Success Response (200)**:
```json
{
  "success": true,
  "data": {
    "summary": {
      "totalConsumption": 52340.8,
      "averageDaily": 2013.1,
      "peakConsumption": 2450.2,
      "peakDate": "2025-01-15",
      "unit": "kWh"
    },
    "timeSeries": [
      {
        "date": "2025-01-01",
        "consumption": 1920.5,
        "deviceTypes": {
          "light_controller": 1450.2,
          "power_distribution": 470.3
        }
      }
    ],
    "comparison": {
      "previousPeriod": 54210.2,
      "change": -3.45,
      "changeType": "decrease"
    }
  }
}
```

---

## 🔄 Real-time WebSocket APIs

### WebSocket Connection
**Endpoint**: `wss://rulr-aiot.com/ws/v1`
**Authentication**: Token-based authentication

**Connection Example**:
```javascript
const ws = new WebSocket('wss://rulr-aiot.com/ws/v1?token=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...');

ws.onopen = () => {
  console.log('WebSocket connected');

  // Subscribe to device updates
  ws.send(JSON.stringify({
    type: 'subscribe',
    channel: 'device.status',
    filter: {
      projectId: 'prj_001',
      deviceTypes: ['light_controller']
    }
  }));
};

ws.onmessage = (event) => {
  const message = JSON.parse(event.data);
  console.log('Received:', message);
};
```

### Message Types

#### Subscribe to Channel
**Client → Server**:
```json
{
  "type": "subscribe",
  "channel": "device.status",
  "filter": {
    "projectId": "prj_001",
    "deviceIds": ["dev_lc_001", "dev_lc_002"]
  }
}
```

**Server → Client (Confirmation)**:
```json
{
  "type": "subscribed",
  "channel": "device.status",
  "subscriptionId": "sub_12345"
}
```

#### Device Status Update
**Server → Client**:
```json
{
  "type": "device.status.update",
  "channel": "device.status",
  "data": {
    "deviceId": "dev_lc_001",
    "status": "online",
    "attributes": {
      "brightness": 80,
      "power": "on",
      "temperature": 46.2
    },
    "timestamp": "2025-01-26T13:05:00Z"
  }
}
```

#### Alarm Notification
**Server → Client**:
```json
{
  "type": "alarm.triggered",
  "channel": "alarms",
  "data": {
    "alarmId": "alarm_evt_002",
    "ruleId": "alarm_001",
    "ruleName": "Device Offline Alert",
    "deviceId": "dev_lc_045",
    "deviceName": "LED-CTRL-Zone-C-045",
    "severity": "high",
    "message": "Device offline for 10 minutes",
    "triggeredAt": "2025-01-26T13:05:00Z"
  }
}
```

#### Rule Execution Event
**Server → Client**:
```json
{
  "type": "rule.executed",
  "channel": "rules",
  "data": {
    "ruleId": "rule_001",
    "ruleName": "Evening Light Activation",
    "status": "success",
    "affectedDevices": 800,
    "executedAt": "2025-01-26T18:30:00Z"
  }
}
```

---

## 📋 Common Response Codes

### Success Codes
| Code | Meaning | Description |
|------|---------|-------------|
| 200 | OK | Request successful |
| 201 | Created | Resource created successfully |
| 202 | Accepted | Request accepted for processing |
| 204 | No Content | Request successful, no content to return |

### Client Error Codes
| Code | Meaning | Description |
|------|---------|-------------|
| 400 | Bad Request | Invalid request parameters |
| 401 | Unauthorized | Authentication required or failed |
| 403 | Forbidden | Insufficient permissions |
| 404 | Not Found | Resource not found |
| 409 | Conflict | Resource conflict (e.g., device has bindings) |
| 422 | Unprocessable Entity | Validation failed |
| 429 | Too Many Requests | Rate limit exceeded |

### Server Error Codes
| Code | Meaning | Description |
|------|---------|-------------|
| 500 | Internal Server Error | Unexpected server error |
| 502 | Bad Gateway | Gateway or proxy error |
| 503 | Service Unavailable | Service temporarily unavailable |
| 504 | Gateway Timeout | Gateway timeout |

---

## 🔒 Security & Rate Limiting

### Authentication
All authenticated endpoints require a JWT Bearer token in the Authorization header:
```
Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...
```

### Rate Limits
| Endpoint Category | Rate Limit | Window |
|-------------------|------------|--------|
| Authentication | 5 requests | 1 minute |
| User Management | 100 requests | 1 minute |
| Device Management | 200 requests | 1 minute |
| Batch Operations | 5 requests | 1 hour |
| Analytics | 50 requests | 1 minute |

### Rate Limit Headers
```
X-RateLimit-Limit: 100
X-RateLimit-Remaining: 85
X-RateLimit-Reset: 1706270400
```

---

## 📚 Related Documentation

- [Database Schema](Database%20Schema.md) - Database structure and relationships
- [02-Authentication System](02-Authentication%20System.md) - Authentication flow details
- [03-Device Management Hub](../03-Device-Management/03-Device%20Management%20Hub.md) - Device management workflows
- [04-Rule Engine System](../04-Rule-Management/04-Rule%20Engine%20System.md) - Rule engine implementation
- [API Design Patterns](../08-Development-Guide/API%20Design%20Patterns.md) - RESTful API best practices
- [Security Architecture](../08-Development-Guide/Security%20Architecture.md) - Security implementation details

---

**API Version**: v1.0
**Maintained by**: Backend Development Team
