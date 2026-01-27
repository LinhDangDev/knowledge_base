# Technical Architecture & System Design

**Document Version**: 1.0
**Date**: January 27, 2026
**Project**: SHUNCOM RULR IoT Platform
**Related Documents**: [03-Device Specifications](./03-device-specifications.md)

---

## 1. System Architecture Overview

### 1.1 High-Level Architecture

```
┌─────────────────────────────────────────────────────────────────┐
│                     Presentation Layer                          │
│  ┌──────────────┐  ┌──────────────┐  ┌──────────────┐         │
│  │ Web Dashboard│  │  GIS Map UI  │  │ Mobile Web   │         │
│  │   (React)    │  │  (Leaflet)   │  │ (Responsive) │         │
│  └──────┬───────┘  └──────┬───────┘  └──────┬───────┘         │
└─────────┼──────────────────┼──────────────────┼────────────────┘
          │                  │                  │
          └──────────────────┴──────────────────┘
                             │
          ┌──────────────────▼──────────────────┐
          │         API Gateway Layer           │
          │  - Authentication (JWT)             │
          │  - Rate Limiting                    │
          │  - Request Validation               │
          │  - Load Balancing                   │
          └──────────────┬──────────────────────┘
                         │
          ┌──────────────▼──────────────────────┐
          │      Application Services Layer      │
          │  ┌──────────┐  ┌──────────┐         │
          │  │  Auth    │  │  Device  │         │
          │  │ Service  │  │ Service  │         │
          │  └──────────┘  └──────────┘         │
          │  ┌──────────┐  ┌──────────┐         │
          │  │   Rule   │  │  Alarm   │         │
          │  │  Engine  │  │ Service  │         │
          │  └──────────┘  └──────────┘         │
          │  ┌──────────┐  ┌──────────┐         │
          │  │ Project  │  │Analytics │         │
          │  │ Service  │  │ Service  │         │
          │  └──────────┘  └──────────┘         │
          └──────────────┬──────────────────────┘
                         │
          ┌──────────────▼──────────────────────┐
          │         Data Layer                   │
          │  ┌──────────┐  ┌──────────┐         │
          │  │PostgreSQL│  │  Redis   │         │
          │  │(Primary) │  │ (Cache)  │         │
          │  └──────────┘  └──────────┘         │
          │  ┌──────────┐  ┌──────────┐         │
          │  │TimeSeries│  │  S3/Blob │         │
          │  │   DB     │  │ Storage  │         │
          │  └──────────┘  └──────────┘         │
          └──────────────┬──────────────────────┘
                         │
          ┌──────────────▼──────────────────────┐
          │      IoT Communication Layer         │
          │  ┌──────────┐  ┌──────────┐         │
          │  │  MQTT    │  │  CoAP    │         │
          │  │  Broker  │  │ Server   │         │
          │  └──────────┘  └──────────┘         │
          │  ┌──────────┐  ┌──────────┐         │
          │  │ WebSocket│  │  HTTP    │         │
          │  │  Server  │  │  API     │         │
          │  └──────────┘  └──────────┘         │
          └──────────────┬──────────────────────┘
                         │
          ┌──────────────▼──────────────────────┐
          │         IoT Device Layer             │
          │  ┌──────────┐  ┌──────────┐         │
          │  │ Gateways │  │NB-IoT/   │         │
          │  │ (Zigbee) │  │CAT.1     │         │
          │  └──────────┘  └──────────┘         │
          │  ┌──────────┐  ┌──────────┐         │
          │  │   LoRa   │  │  Meters  │         │
          │  │ Devices  │  │ Sensors  │         │
          │  └──────────┘  └──────────┘         │
          └──────────────────────────────────────┘
```

### 1.2 Technology Stack

#### Frontend Technologies
```yaml
Framework: React 18+ with TypeScript
State Management: Redux Toolkit + RTK Query
UI Components:
  - Ant Design / Material-UI
  - Custom component library
Mapping: Leaflet.js with OpenStreetMap
Charts: Apache ECharts / Recharts
Build Tool: Vite
Testing: Jest + React Testing Library
```

#### Backend Technologies
```yaml
Runtime: Node.js 18+ LTS
Framework: NestJS (TypeScript)
Alternative: Fastify / Express
API Style: RESTful + GraphQL (optional)
Authentication: Passport.js + JWT
Validation: class-validator + class-transformer
Documentation: Swagger/OpenAPI 3.0
Testing: Jest + Supertest
```

#### Database Technologies
```yaml
Primary Database: PostgreSQL 15+
  - ACID transactions
  - JSONB support
  - Full-text search
  - Spatial data (PostGIS)

Cache Layer: Redis 7+
  - Session storage
  - Real-time data cache
  - Rate limiting
  - Pub/Sub messaging

Time-Series: TimescaleDB (PostgreSQL extension)
  - Device metrics
  - Energy consumption
  - Performance monitoring

Object Storage: MinIO / AWS S3
  - File uploads
  - Export files
  - Backup storage
```

#### IoT Communication
```yaml
MQTT Broker: EMQX / Mosquitto
  - QoS 0, 1, 2 support
  - TLS/SSL encryption
  - ACL authentication
  - Clustering support

WebSocket: Socket.IO
  - Real-time dashboard updates
  - Alarm notifications
  - Device status streaming

Protocol Adapters:
  - Zigbee: zigbee2mqtt / Zigbee-herdsman
  - LoRaWAN: ChirpStack server integration
  - Modbus: node-modbus
  - DLT645: Custom implementation
```

#### Infrastructure
```yaml
Containerization: Docker + Docker Compose
Orchestration: Kubernetes (production) / Docker Swarm
CI/CD: GitHub Actions / GitLab CI
Monitoring:
  - Prometheus + Grafana
  - ELK Stack (Elasticsearch, Logstash, Kibana)
  - Sentry (error tracking)
Load Balancer: Nginx / Traefik
Reverse Proxy: Nginx
```

---

## 2. Database Schema Design

### 2.1 Core Entities

#### Users & Authentication
```sql
-- Users table
CREATE TABLE users (
  id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  username VARCHAR(50) UNIQUE NOT NULL,
  email VARCHAR(255) UNIQUE NOT NULL,
  password_hash VARCHAR(255) NOT NULL,
  first_name VARCHAR(100),
  last_name VARCHAR(100),
  phone VARCHAR(20),
  timezone VARCHAR(50) DEFAULT 'UTC',
  locale VARCHAR(10) DEFAULT 'en',
  is_active BOOLEAN DEFAULT true,
  is_locked BOOLEAN DEFAULT false,
  failed_login_attempts INT DEFAULT 0,
  last_login_at TIMESTAMP,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  deleted_at TIMESTAMP -- Soft delete
);

-- Organizations table
CREATE TABLE organizations (
  id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  name VARCHAR(255) NOT NULL,
  logo_url VARCHAR(500),
  contact_email VARCHAR(255),
  contact_phone VARCHAR(20),
  address TEXT,
  is_active BOOLEAN DEFAULT true,
  settings JSONB, -- Branding, custom configs
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Roles table
CREATE TABLE roles (
  id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  organization_id UUID REFERENCES organizations(id),
  name VARCHAR(100) NOT NULL,
  description TEXT,
  permissions JSONB NOT NULL, -- Page & function permissions
  is_system_role BOOLEAN DEFAULT false, -- Admin, Manager, Operator, Viewer
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- User-Role association (many-to-many)
CREATE TABLE user_roles (
  user_id UUID REFERENCES users(id) ON DELETE CASCADE,
  role_id UUID REFERENCES roles(id) ON DELETE CASCADE,
  assigned_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  assigned_by UUID REFERENCES users(id),
  PRIMARY KEY (user_id, role_id)
);

-- Management scopes
CREATE TABLE management_scopes (
  id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  user_id UUID REFERENCES users(id) ON DELETE CASCADE,
  scope_type VARCHAR(20) NOT NULL, -- 'project', 'group', 'product_category'
  scope_value UUID NOT NULL, -- Reference to project/group/product ID
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
```

#### Projects & Groups
```sql
-- Projects table (hierarchical)
CREATE TABLE projects (
  id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  organization_id UUID REFERENCES organizations(id),
  parent_id UUID REFERENCES projects(id), -- Self-reference for hierarchy
  name VARCHAR(255) NOT NULL,
  description TEXT,
  is_system_project BOOLEAN DEFAULT false, -- Top-level, Unassigned
  gis_enabled BOOLEAN DEFAULT false,
  dashboard_config JSONB, -- Module configuration
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  deleted_at TIMESTAMP
);

-- Device groups table
CREATE TABLE device_groups (
  id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  organization_id UUID REFERENCES organizations(id),
  project_id UUID REFERENCES projects(id),
  name VARCHAR(255) NOT NULL,
  description TEXT,
  group_type VARCHAR(30) NOT NULL, -- 'regular', 'zigbee_multicast', 'lora_multicast', 'luminaire', 'loop'
  multicast_config JSONB, -- Group number, frequency (for hardware multicast)
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
```

#### Devices
```sql
-- Product catalog
CREATE TABLE products (
  id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  category VARCHAR(50) NOT NULL, -- 'gateway', 'light_controller', 'fixture', etc.
  name VARCHAR(255) NOT NULL,
  manufacturer VARCHAR(255),
  model VARCHAR(100),
  communication_type VARCHAR(50), -- 'zigbee', 'nb-iot', 'lora_otaa', etc.
  specifications JSONB,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Devices table (all device types)
CREATE TABLE devices (
  id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  organization_id UUID REFERENCES organizations(id),
  project_id UUID REFERENCES projects(id),
  group_id UUID REFERENCES device_groups(id),
  product_id UUID REFERENCES products(id) NOT NULL,

  -- Basic info
  device_name VARCHAR(255) NOT NULL,
  device_number VARCHAR(100) NOT NULL, -- MAC, IMEI, DEVEUI, etc.

  -- Location
  latitude DECIMAL(10, 8),
  longitude DECIMAL(11, 8),
  altitude DECIMAL(8, 2),
  address TEXT,

  -- Status
  online_status VARCHAR(20) DEFAULT 'offline', -- 'online', 'offline', 'unknown'
  last_seen_at TIMESTAMP,

  -- Associations (device-specific)
  parent_device_id UUID REFERENCES devices(id), -- For sub-devices (gateway relationship)
  associated_fixture_id UUID REFERENCES devices(id), -- For light controllers
  associated_pole_id UUID REFERENCES devices(id), -- For multiple device types

  -- Configuration
  device_config JSONB, -- Device-specific configurations

  -- Metadata
  installation_date DATE,
  warranty_expiry DATE,
  maintenance_interval INT, -- Days
  notes TEXT,

  -- Timestamps
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  deleted_at TIMESTAMP,

  -- Indexes
  CONSTRAINT unique_device_number UNIQUE (organization_id, product_id, device_number)
);

CREATE INDEX idx_devices_online_status ON devices(online_status);
CREATE INDEX idx_devices_project ON devices(project_id);
CREATE INDEX idx_devices_group ON devices(group_id);
CREATE INDEX idx_devices_parent ON devices(parent_device_id);
CREATE INDEX idx_devices_location ON devices USING GIST (
  ST_SetSRID(ST_MakePoint(longitude, latitude), 4326)
); -- PostGIS spatial index
```

#### Device Data (Time-Series)
```sql
-- Device metrics (TimescaleDB hypertable)
CREATE TABLE device_metrics (
  time TIMESTAMPTZ NOT NULL,
  device_id UUID NOT NULL REFERENCES devices(id),
  metric_name VARCHAR(50) NOT NULL, -- 'voltage', 'current', 'power', etc.
  metric_value DOUBLE PRECISION,
  metric_unit VARCHAR(20),

  PRIMARY KEY (device_id, metric_name, time)
);

-- Convert to hypertable (TimescaleDB)
SELECT create_hypertable('device_metrics', 'time');

-- Create compression policy (keep 7 days uncompressed, compress older)
SELECT add_compression_policy('device_metrics', INTERVAL '7 days');

-- Create retention policy (keep 1 year)
SELECT add_retention_policy('device_metrics', INTERVAL '1 year');

-- Device events log
CREATE TABLE device_events (
  id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  device_id UUID REFERENCES devices(id),
  event_type VARCHAR(50) NOT NULL, -- 'online', 'offline', 'alarm', 'command', etc.
  event_data JSONB,
  severity VARCHAR(20), -- 'info', 'warning', 'error', 'critical'
  occurred_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE INDEX idx_device_events_device ON device_events(device_id);
CREATE INDEX idx_device_events_time ON device_events(occurred_at DESC);
```

---

### 2.2 Rule Engine Schema

```sql
-- Platform rules
CREATE TABLE platform_rules (
  id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  organization_id UUID REFERENCES organizations(id),
  name VARCHAR(255) NOT NULL,
  description TEXT,
  rule_type VARCHAR(50), -- 'schedule', 'automation', 'scene'
  is_enabled BOOLEAN DEFAULT true,
  effective_date_start DATE,
  effective_date_end DATE,
  repeat_period VARCHAR(20), -- 'daily', 'weekly', 'monthly'
  created_by UUID REFERENCES users(id),
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Platform rule sub-rules
CREATE TABLE platform_rule_subrules (
  id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  rule_id UUID REFERENCES platform_rules(id) ON DELETE CASCADE,
  subrule_order INT NOT NULL,

  -- Trigger conditions (JSONB array)
  trigger_conditions JSONB NOT NULL,
  -- Example: [
  --   {"type": "attribute", "device_id": "...", "property": "voltage", "operator": ">", "value": 220},
  --   {"type": "time", "mode": "fixed", "time": "18:00"},
  --   {"type": "time_range", "start": "17:00", "end": "22:00"}
  -- ]

  condition_logic VARCHAR(10) DEFAULT 'AND', -- 'AND', 'OR'

  -- Execute actions (JSONB array)
  execute_actions JSONB NOT NULL,
  -- Example: [
  --   {"type": "control_lamp", "device_ids": [...], "operation": "turn_on", "brightness": 80},
  --   {"type": "invoke_service", "service": "gateway.close_circuit", "params": {...}}
  -- ]

  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Local rules (device-level)
CREATE TABLE local_rules (
  id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  organization_id UUID REFERENCES organizations(id),
  device_id UUID REFERENCES devices(id) ON DELETE CASCADE,
  name VARCHAR(255) NOT NULL,
  is_enabled BOOLEAN DEFAULT true,

  -- Trigger condition (single condition for local rules)
  trigger_condition JSONB NOT NULL,

  -- Execute action (single action for local rules)
  execute_action JSONB NOT NULL,

  -- Synchronization status
  sync_status VARCHAR(20) DEFAULT 'pending', -- 'pending', 'synced', 'failed'
  last_sync_at TIMESTAMP,
  sync_error TEXT,

  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Rule execution history
CREATE TABLE rule_executions (
  id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  rule_id UUID, -- Reference to platform_rules or local_rules
  rule_type VARCHAR(20), -- 'platform', 'local'
  executed_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  execution_status VARCHAR(20), -- 'success', 'failed', 'partial'
  trigger_details JSONB,
  action_results JSONB,
  error_message TEXT
);

CREATE INDEX idx_rule_executions_time ON rule_executions(executed_at DESC);
```

---

### 2.3 Alarm System Schema

```sql
-- Alarm rules (platform alarms)
CREATE TABLE alarm_rules (
  id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  organization_id UUID REFERENCES organizations(id),
  product_id UUID REFERENCES products(id), -- Device type this alarm applies to
  name VARCHAR(255) NOT NULL,
  description TEXT,
  is_enabled BOOLEAN DEFAULT true,

  effective_date_start DATE,
  effective_date_end DATE,
  repeat_period VARCHAR(20),
  effective_time_start TIME,
  effective_time_end TIME,

  -- Alarm configuration
  alarm_level_id UUID REFERENCES alarm_levels(id),
  silent_period_minutes INT DEFAULT 30,
  auto_handle_condition JSONB, -- Condition for automatic alarm resolution

  -- Notification
  send_notification BOOLEAN DEFAULT true,
  recipient_group_ids UUID[], -- Array of recipient group IDs

  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Alarm rule sub-rules (conditions)
CREATE TABLE alarm_rule_subrules (
  id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  alarm_rule_id UUID REFERENCES alarm_rules(id) ON DELETE CASCADE,

  trigger_conditions JSONB NOT NULL,
  condition_logic VARCHAR(10) DEFAULT 'AND',

  custom_alarm_name VARCHAR(255), -- Override default alarm name

  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Offline alarms configuration
CREATE TABLE offline_alarm_configs (
  id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  organization_id UUID REFERENCES organizations(id),
  product_id UUID REFERENCES products(id),

  offline_threshold_minutes INT DEFAULT 30,
  is_enabled BOOLEAN DEFAULT true,

  effective_time_start TIME,
  effective_time_end TIME,
  silent_period_minutes INT DEFAULT 30,

  alarm_level_id UUID REFERENCES alarm_levels(id),
  send_notification BOOLEAN DEFAULT true,
  recipient_group_ids UUID[],

  excluded_device_ids UUID[], -- Devices that won't trigger this alarm

  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Device alarms configuration
CREATE TABLE device_alarm_configs (
  id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  organization_id UUID REFERENCES organizations(id),
  product_id UUID REFERENCES products(id),

  alarm_event_type VARCHAR(100), -- Device-reported alarm type
  is_enabled BOOLEAN DEFAULT true,

  effective_time_start TIME,
  effective_time_end TIME,
  silent_period_minutes INT DEFAULT 30,

  alarm_level_id UUID REFERENCES alarm_levels(id),
  send_notification BOOLEAN DEFAULT true,
  recipient_group_ids UUID[],

  excluded_device_ids UUID[],
  threshold_config JSONB, -- Threshold settings for alarm trigger

  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Alarm instances (generated alarms)
CREATE TABLE alarms (
  id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  organization_id UUID REFERENCES organizations(id),
  device_id UUID REFERENCES devices(id),
  alarm_rule_id UUID REFERENCES alarm_rules(id), -- NULL for offline/device alarms

  alarm_type VARCHAR(50) NOT NULL, -- 'platform', 'offline', 'device'
  alarm_name VARCHAR(255) NOT NULL,
  alarm_level_id UUID REFERENCES alarm_levels(id),

  alarm_data JSONB, -- Alarm-specific data (values, thresholds, etc.)

  status VARCHAR(20) DEFAULT 'pending', -- 'pending', 'processing', 'resolved', 'auto_resolved'

  triggered_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  acknowledged_at TIMESTAMP,
  acknowledged_by UUID REFERENCES users(id),
  resolved_at TIMESTAMP,
  resolved_by UUID REFERENCES users(id),
  resolution_notes TEXT,

  auto_handle_at TIMESTAMP, -- When auto-handle should occur
  is_auto_handled BOOLEAN DEFAULT false,

  notification_sent BOOLEAN DEFAULT false,
  notification_sent_at TIMESTAMP,

  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE INDEX idx_alarms_device ON alarms(device_id);
CREATE INDEX idx_alarms_status ON alarms(status);
CREATE INDEX idx_alarms_triggered ON alarms(triggered_at DESC);

-- Alarm levels
CREATE TABLE alarm_levels (
  id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  organization_id UUID REFERENCES organizations(id),
  name VARCHAR(100) NOT NULL,
  severity INT NOT NULL, -- 1 (lowest) to 5 (highest)
  color VARCHAR(20), -- Display color
  is_system_level BOOLEAN DEFAULT false,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Notification recipient groups
CREATE TABLE recipient_groups (
  id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  organization_id UUID REFERENCES organizations(id),
  name VARCHAR(255) NOT NULL,
  description TEXT,

  notification_channels JSONB, -- email, sms, push, webhook
  notification_interval_minutes INT,
  notification_times INT, -- How many times to send

  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Recipient group members
CREATE TABLE recipient_group_members (
  group_id UUID REFERENCES recipient_groups(id) ON DELETE CASCADE,
  user_id UUID REFERENCES users(id) ON DELETE CASCADE,
  PRIMARY KEY (group_id, user_id)
);
```

---

## 3. API Architecture

### 3.1 RESTful API Design

#### Authentication Endpoints
```yaml
POST   /api/v1/auth/login
POST   /api/v1/auth/logout
POST   /api/v1/auth/refresh
POST   /api/v1/auth/forgot-password
POST   /api/v1/auth/reset-password
GET    /api/v1/auth/me
PATCH  /api/v1/auth/me/timezone
```

#### User Management
```yaml
GET    /api/v1/users                # List users (paginated)
POST   /api/v1/users                # Create user
GET    /api/v1/users/:id            # Get user details
PATCH  /api/v1/users/:id            # Update user
DELETE /api/v1/users/:id            # Delete user
PATCH  /api/v1/users/:id/status     # Enable/disable user
POST   /api/v1/users/:id/roles      # Assign roles
DELETE /api/v1/users/:id/roles/:roleId  # Remove role
```

#### Device Management
```yaml
GET    /api/v1/devices              # List devices (filtered, paginated)
POST   /api/v1/devices              # Create device
GET    /api/v1/devices/:id          # Get device details
PATCH  /api/v1/devices/:id          # Update device
DELETE /api/v1/devices/:id          # Delete device (move to recycle bin)

GET    /api/v1/devices/:id/metrics  # Get device metrics (time-series)
GET    /api/v1/devices/:id/events   # Get device events
POST   /api/v1/devices/:id/commands # Send command to device

POST   /api/v1/devices/batch-import # Batch import devices
GET    /api/v1/devices/export       # Export devices
GET    /api/v1/devices/recycle-bin  # List deleted devices
POST   /api/v1/devices/:id/restore  # Restore from recycle bin

# Gateway-specific
POST   /api/v1/devices/:id/configure-circuits  # Bulk circuit config
POST   /api/v1/devices/:id/sync-subdevices     # Sync sub-devices
POST   /api/v1/devices/:id/clear-local-rules   # Clear local rules
```

#### Rule Management
```yaml
# Platform Rules
GET    /api/v1/rules/platform       # List platform rules
POST   /api/v1/rules/platform       # Create platform rule
GET    /api/v1/rules/platform/:id   # Get rule details
PATCH  /api/v1/rules/platform/:id   # Update rule
DELETE /api/v1/rules/platform/:id   # Delete rule
PATCH  /api/v1/rules/platform/:id/status  # Enable/disable

# Local Rules
GET    /api/v1/rules/local          # List local rules
POST   /api/v1/rules/local          # Create local rule
POST   /api/v1/rules/local/sync     # Sync rules to devices
GET    /api/v1/rules/local/:id/sync-status  # Check sync status

# Rule Execution History
GET    /api/v1/rules/executions     # Rule execution logs
```

#### Alarm Management
```yaml
# Alarm Rules
GET    /api/v1/alarms/rules         # List alarm rules
POST   /api/v1/alarms/rules         # Create alarm rule
PATCH  /api/v1/alarms/rules/:id     # Update alarm rule

# Alarm Instances
GET    /api/v1/alarms               # List alarms (filtered)
GET    /api/v1/alarms/:id           # Get alarm details
PATCH  /api/v1/alarms/:id/status    # Update alarm status (processing, resolved)
POST   /api/v1/alarms/batch-process # Batch update alarm status
POST   /api/v1/alarms/batch-dispatch # Batch create work orders
GET    /api/v1/alarms/export        # Export alarms

# Alarm Configuration
GET    /api/v1/alarms/levels        # List alarm levels
GET    /api/v1/alarms/recipient-groups  # List recipient groups
```

#### Project & Group Management
```yaml
# Projects
GET    /api/v1/projects             # List projects (tree)
POST   /api/v1/projects             # Create project
PATCH  /api/v1/projects/:id         # Update project
DELETE /api/v1/projects/:id         # Delete project
PATCH  /api/v1/projects/:id/dashboard-config  # Update dashboard
POST   /api/v1/projects/:id/batch-apply  # Copy config to other projects

# Groups
GET    /api/v1/groups               # List groups
POST   /api/v1/groups               # Create group
POST   /api/v1/groups/:id/sync      # Sync multicast group to hardware
```

#### Analytics & Reporting
```yaml
GET    /api/v1/analytics/dashboard  # Dashboard statistics
GET    /api/v1/analytics/energy     # Energy consumption analysis
GET    /api/v1/analytics/devices    # Device performance metrics
POST   /api/v1/analytics/export     # Export report
```

### 3.2 WebSocket Events

```yaml
# Client subscribes to channels
SUBSCRIBE device:{device_id}           # Device status updates
SUBSCRIBE project:{project_id}         # Project-wide updates
SUBSCRIBE alarms                       # New alarm notifications
SUBSCRIBE rule-executions              # Rule execution events

# Server events
EVENT device.status.changed            # Device online/offline
EVENT device.data.updated              # Device metric update
EVENT alarm.triggered                  # New alarm created
EVENT alarm.resolved                   # Alarm resolved
EVENT rule.executed                    # Rule executed
```

---

## 4. Security Architecture

### 4.1 Authentication & Authorization

```yaml
Authentication:
  Method: JWT (JSON Web Tokens)
  Token Types:
    Access Token:
      Expiry: 1 hour
      Storage: HTTP-only cookie (recommended) or localStorage
      Claims: user_id, organization_id, roles, scopes

    Refresh Token:
      Expiry: 7 days
      Storage: HTTP-only cookie
      Rotation: New refresh token on each use

  Session Management:
    - Redis-backed session store
    - Concurrent session limit: 5 per user
    - Auto-logout on inactivity: 24 hours

Authorization:
  RBAC Implementation:
    - Permission check on every API endpoint
    - Dynamic permission evaluation
    - Scope-based data filtering (SQL WHERE clause injection)

  Permission Format:
    - Pattern: resource:action
    - Examples:
        "devices:read"
        "devices:write"
        "rules:execute"
        "alarms:resolve"
```

### 4.2 Data Security

```yaml
Encryption:
  Data at Rest:
    - Database: AES-256 encryption
    - Object Storage: Server-side encryption
    - Secrets: AWS Secrets Manager / HashiCorp Vault

  Data in Transit:
    - TLS 1.2+ for all connections
    - Certificate pinning for IoT devices
    - MQTT over TLS
    - WebSocket Secure (WSS)

Sensitive Data Handling:
  Passwords:
    - Hashing: bcrypt (cost factor 12)
    - No password storage in logs

  API Keys:
    - HMAC-SHA256 signed
    - Rotation every 90 days
    - Rate-limited

  Personal Data:
    - GDPR compliance
    - Data anonymization for analytics
    - Right to deletion
```

### 4.3 API Security

```yaml
Rate Limiting:
  Anonymous: 100 requests/hour
  Authenticated: 1,000 requests/hour
  Premium: 10,000 requests/hour

  Per Endpoint:
    POST /auth/login: 5 attempts/15 minutes
    POST /devices: 100/hour
    GET /devices: 500/hour

Input Validation:
  - Request payload validation (class-validator)
  - SQL injection prevention (parameterized queries)
  - XSS prevention (input sanitization)
  - CSRF protection (CSRF tokens)

CORS Policy:
  Allowed Origins:
    - https://dashboard.rulr-aiot.com
    - https://*.rulr-aiot.com
  Allowed Methods: GET, POST, PATCH, DELETE
  Credentials: true
```

### 4.4 Audit Logging

```yaml
Logged Events:
  - User authentication (login, logout, failed attempts)
  - Permission changes (role assignment, scope updates)
  - Device operations (create, update, delete, commands)
  - Rule executions (trigger, actions, results)
  - Alarm status changes (triggered, resolved)
  - Data exports (user, timestamp, data scope)

Log Format:
  timestamp: ISO 8601
  user_id: UUID
  organization_id: UUID
  action: string (CRUD operation)
  resource_type: string (device, rule, alarm, etc.)
  resource_id: UUID
  ip_address: string
  user_agent: string
  request_payload: JSONB (sanitized)
  response_status: int

Retention: 2 years
Storage: Elasticsearch (searchable) + S3 (archive)
```

---

## 5. Scalability & Performance

### 5.1 Horizontal Scaling

```yaml
Application Layer:
  - Stateless services (horizontally scalable)
  - Load balancer: Nginx / AWS ALB
  - Auto-scaling: Based on CPU/Memory/Request rate
  - Minimum instances: 2 (high availability)
  - Maximum instances: 20 (cost optimization)

Database Layer:
  PostgreSQL:
    - Read replicas: 2-4 (for read-heavy operations)
    - Connection pooling: PgBouncer
    - Partitioning: Time-based partitioning for metrics

  Redis:
    - Redis Cluster mode (16 shards)
    - Persistence: RDB + AOF
    - Sentinel: High availability

Message Broker:
  MQTT:
    - EMQX cluster (3-5 nodes)
    - Session persistence
    - Message queue for offline devices
```

### 5.2 Caching Strategy

```yaml
Cache Layers:
  L1 (Application Memory):
    - In-memory cache for hot data
    - LRU eviction policy
    - TTL: 1-5 minutes

  L2 (Redis):
    - User sessions
    - Device status (online/offline)
    - Recent metrics (last 10 readings)
    - TTL: 5-60 minutes

  CDN (Static Assets):
    - Frontend bundles
    - Images, icons
    - Map tiles
    - CloudFlare / AWS CloudFront

Cache Invalidation:
  - On device update: Invalidate device cache
  - On rule execution: Clear rule cache
  - On alarm trigger: Refresh alarm cache
```

### 5.3 Performance Optimization

```yaml
Database Optimization:
  - Indexing strategy (B-tree, GiST, Hash)
  - Query optimization (EXPLAIN ANALYZE)
  - Materialized views for complex aggregations
  - Partial indexes for filtered queries
  - Connection pooling (max 100 connections)

API Optimization:
  - Response compression (gzip, brotli)
  - Pagination (cursor-based for large datasets)
  - Field filtering (GraphQL-like field selection)
  - Eager loading (avoid N+1 queries)
  - API response caching (ETag, Last-Modified)

Frontend Optimization:
  - Code splitting (lazy loading)
  - Tree shaking (remove unused code)
  - Image optimization (WebP, lazy loading)
  - Service workers (offline capability)
  - Virtual scrolling (large device lists)
```

---

## 6. Deployment Architecture

### 6.1 Development Environment

```yaml
Local Development:
  - Docker Compose for all services
  - Hot reload for frontend & backend
  - Mock MQTT broker
  - Seed data for testing

Tech Stack:
  - Frontend: Vite dev server (port 5173)
  - Backend: NestJS dev mode (port 3000)
  - PostgreSQL: Docker container (port 5432)
  - Redis: Docker container (port 6379)
  - MQTT: Mosquitto (port 1883)
```

### 6.2 Staging Environment

```yaml
Infrastructure:
  - Kubernetes cluster (3 nodes)
  - Managed PostgreSQL (AWS RDS)
  - Managed Redis (AWS ElastiCache)
  - MQTT cluster (EMQX 3 nodes)

Purpose:
  - QA testing
  - Performance testing
  - UAT (User Acceptance Testing)
  - Integration testing with real devices
```

### 6.3 Production Environment

```yaml
Infrastructure:
  Cloud Provider: AWS / Azure / Google Cloud

  Compute:
    - Kubernetes: EKS / AKS / GKE
    - Node pools:
        - Frontend: 3 nodes (4 vCPU, 8GB RAM)
        - Backend: 5 nodes (8 vCPU, 16GB RAM)
        - Workers: 3 nodes (4 vCPU, 8GB RAM)

  Database:
    - PostgreSQL: Multi-AZ deployment
      - Instance: db.r5.2xlarge (8 vCPU, 64GB RAM)
      - Read replicas: 2
      - Automated backups: Daily

    - Redis: Cluster mode
      - Instance: cache.r5.xlarge (4 vCPU, 26GB RAM)
      - Nodes: 6 (3 primary + 3 replica)

  Storage:
    - S3 buckets: Device data, exports, backups
    - EBS volumes: Persistent storage for Kubernetes

  Networking:
    - VPC with private subnets
    - Application Load Balancer (ALB)
    - CloudFront CDN
    - Route 53 DNS

High Availability:
  - Multi-AZ deployment
  - Auto-scaling groups
  - Health checks
  - Automatic failover
  - Disaster recovery plan (RTO: 1 hour, RPO: 15 minutes)
```

---

**Next Document**: [05-Functional Requirements (Detailed)](./05-functional-requirements.md)

---

## Document Revision History

| Version | Date | Changes | Author |
|---------|------|---------|--------|
| 1.0 | 2026-01-27 | Initial technical architecture | AI Assistant |
