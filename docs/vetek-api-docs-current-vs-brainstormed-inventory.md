# Vetek API docs hiện tại vs API inventory đã brainstorm

## Nguồn kiểm tra
- Swagger UI: `https://api.vetek.vn/docs`
- OpenAPI schema thực tế: `https://api.vetek.vn/openapi.json`
- Tài liệu brainstorm nội bộ đã so: `SHUNCOM RULR Knowledge Base/02-System-Architecture/API Endpoints Map.md`

## Kết luận nhanh
Hiện tại docs API của Vetek **đã có 48 paths** trong OpenAPI `Vsense IoT Management API 1.0.0`.

Có một phần trùng với API inventory đã brainstorm, nhưng mô hình hiện tại của Vetek đang nghiêng về:
- `customers`
- `zones`
- `gateways`
- `nodes`
- `rules`
- `scripts`
- `gateway commands`
- `dashboard overview/detail`
- các master data như `data-types`, `state-types`, `config-types`, `physical-types`, `gateway-types`, `map-models`

Trong khi inventory brainstorm trước đó thiên về mô hình rộng hơn cho SHUNCOM/RULR:
- auth, users, roles, organizations
- projects, groups, devices
- platform/local/alarm rules
- alarms, reports, settings, recycle-bin, audit, realtime

## 1. Những gì docs API Vetek hiện tại đã có

### 1.1 Auth
- `POST /auth/register` — Register
- `POST /auth/login` — Login
- `POST /auth/check-token` — Check Token

### 1.2 User login
- `POST /user_login/` — Create User Login
- `GET /user_login/{user_id}` — Get User Login

### 1.3 Customers
- `POST /customers/` — Create Customer
- `GET /customers/` — List Customers
- `GET /customers/{customer_id}` — Get Customer

### 1.4 Zones
- `POST /zones/` — Create a new zone
- `GET /zones/` — List all zones
- `GET /zones/{zone_id}` — Get zone details
- `PUT /zones/{zone_id}` — Update a zone
- `DELETE /zones/{zone_id}` — Delete a zone

### 1.5 Gateways
- `POST /gateways/` — Create Gateway
- `GET /gateways/` — Get Gateways
- `GET /gateways/{gateway_id}` — Get Gateway
- `PUT /gateways/{gateway_id}` — Update Gateway
- `DELETE /gateways/{gateway_id}` — Delete Gateway

### 1.6 Nodes
- `POST /nodes/` — Create Node
- `GET /nodes/` — Get Nodes
- `GET /nodes/{node_id}` — Get Node
- `PUT /nodes/{node_id}` — Update Node
- `DELETE /nodes/{node_id}` — Delete Node

### 1.7 Rules
- `POST /rules/` — Create a new rule
- `GET /rules/` — List all rules
- `GET /rules/{rule_id}` — Get rule details
- `PUT /rules/{rule_id}` — Update a rule
- `DELETE /rules/{rule_id}` — Delete a rule

### 1.8 Scripts
- `POST /scripts/` — Create a new script
- `GET /scripts/` — List all scripts
- `GET /scripts/{script_id}` — Get script details
- `PUT /scripts/{script_id}` — Update a script
- `DELETE /scripts/{script_id}` — Delete a script

### 1.9 Gateway Commands
- `POST /gateways/{gateway_id}/cmd/config` — Send Config
- `POST /gateways/{gateway_id}/cmd/suspend` — Send Suspend
- `POST /gateways/{gateway_id}/cmd/control` — Send Control
- `POST /gateways/{gateway_id}/cmd/auto` — Send Auto Rules
- `POST /gateways/{gateway_id}/cmd/add` — Send Add Nodes
- `POST /gateways/{gateway_id}/cmd/remove` — Send Remove Nodes
- `POST /gateways/{gateway_id}/cmd/pair` — Send Pair Command
- `POST /gateways/{gateway_id}/cmd/refresh` — Send Refresh
- `POST /gateways/{gateway_id}/cmd/ota` — Send Ota
- `POST /gateways/{gateway_id}/cmd/transfer` — Send Transfer
- `POST /gateways/{gateway_id}/cmd/backdoor/refresh-config` — Backdoor Refresh Config
- `POST /gateways/{gateway_id}/cmd/backdoor/provision` — Backdoor Provision

### 1.10 Logs
- `POST /logs/publish` — Get Publish Logs
- `POST /logs/subscribe` — Get Subscribe Logs

### 1.11 Dashboard Overview
- `GET /dashboard_overview/gateways` — Gateways Overview
- `GET /dashboard_overview/nodes` — Nodes Overview
- `GET /dashboard_overview/commands-notify` — Commands Notify
- `GET /dashboard_overview/alerts` — Serious Alerts

### 1.12 Dashboard Detail
- `GET /dashboard_detail/dashboard/detail` — Dashboard Detail

### 1.13 Gateway Types
- `GET /gateway-types/` — List Gateway Types
- `POST /gateway-types/` — Create Gateway Type
- `GET /gateway-types/{gateway_type_id}` — Get Gateway Type
- `PUT /gateway-types/{gateway_type_id}` — Update Gateway Type
- `DELETE /gateway-types/{gateway_type_id}` — Delete Gateway Type

### 1.14 Data Types
- `GET /data-types/` — Get Data Types
- `POST /data-types/` — Create Data Type
- `GET /data-types/{id}` — Get Data Type
- `PUT /data-types/{id}` — Update Data Type
- `DELETE /data-types/{id}` — Delete Data Type

### 1.15 State Types
- `GET /state-types/` — Get State Types
- `POST /state-types/` — Create State Type
- `GET /state-types/{id}` — Get State Type
- `PUT /state-types/{id}` — Update State Type
- `DELETE /state-types/{id}` — Delete State Type

### 1.16 Config Types
- `GET /config-types/` — Get Config Types
- `POST /config-types/` — Create Config Type
- `GET /config-types/{id}` — Get Config Type
- `PUT /config-types/{id}` — Update Config Type
- `DELETE /config-types/{id}` — Delete Config Type

### 1.17 Physical Types
- `GET /physical-types/` — Get Physical Types
- `POST /physical-types/` — Create Physical Type
- `GET /physical-types/{id}` — Get Physical Type
- `PUT /physical-types/{id}` — Update Physical Type
- `DELETE /physical-types/{id}` — Delete Physical Type

### 1.18 Map Models
- `POST /map-models/` — Create Map Model
- `GET /map-models/` — Get Map Models
- `GET /map-models/{model_id}` — Get Map Model
- `PUT /map-models/{model_id}` — Update Map Model
- `DELETE /map-models/{model_id}` — Delete Map Model

## 2. Mapping với API đã brainstorm trước đó

| Nhóm brainstorm | Trong Vetek docs hiện tại | Mức khớp | Ghi chú |
|---|---|---|---|
| Authentication APIs | `/auth/register`, `/auth/login`, `/auth/check-token` | Khớp một phần | Có auth cơ bản, chưa thấy refresh/logout/me/password reset như brainstorm |
| User management APIs | `/user_login/`, `/user_login/{user_id}` | Khớp rất ít | Chưa thấy CRUD users đầy đủ, roles, permissions, scope |
| Organization APIs | `/customers/` | Khớp một phần | `customers` có thể gần với tenant/org layer hơn là `organizations` |
| Role APIs | Không thấy | Thiếu | Chưa có `roles`, `permissions` |
| Project APIs | `/zones/` | Khớp một phần | `zones` có vẻ đang đóng vai gần `projects` hoặc khu vực quản lý |
| Device management APIs | `/gateways/`, `/nodes/` | Khớp một phần | Vetek tách gateway/node, chưa có `devices` aggregate API như brainstorm |
| Device actions | `POST /gateways/{gateway_id}/cmd/*` | Khớp một phần | Có command layer rất mạnh ở gateway, nhưng chưa theo form `/devices/{id}/actions/*` |
| Device groups | Không thấy | Thiếu | Chưa có `device-groups` |
| Device types | `gateway-types`, `data-types`, `state-types`, `config-types`, `physical-types` | Khác mô hình | Có master-data types, nhưng không phải `device-types` như brainstorm |
| Rule management | `/rules/` | Khớp một phần | Có CRUD rule tổng quát, chưa tách `platform/local/alarm` |
| Alarm APIs | `/dashboard_overview/alerts` | Khớp rất ít | Có alert summary, chưa thấy CRUD alarm, acknowledge, resolve |
| Dashboard APIs | `/dashboard_overview/*`, `/dashboard_detail/dashboard/detail` | Khớp một phần | Có overview/detail, nhưng chưa thấy map-data, energy, reports rõ ràng |
| Logs / audit | `/logs/publish`, `/logs/subscribe` | Khớp một phần | Có logs nhưng chưa thấy audit logs/user activity như brainstorm |
| Reports APIs | Không thấy | Thiếu | Chưa thấy `/reports/*` |
| Settings APIs | Không thấy | Thiếu | Chưa thấy `/settings/*` |
| Recycle Bin APIs | Không thấy | Thiếu | Chưa thấy `/recycle-bin/*` |
| Realtime / WebSocket | Không thấy trong OpenAPI | Thiếu trong docs | Có thể tồn tại ngoài OpenAPI, hiện chưa thấy trong `/docs` |

## 3. Những phần Vetek docs đã có mà brainstorm trước đó chưa nhấn mạnh

Các nhóm sau hiện có trong Vetek docs nhưng inventory brainstorm trước đó chưa tách rõ:
- `scripts`
- `gateway-types`
- `data-types`
- `state-types`
- `config-types`
- `physical-types`
- `map-models`
- `gateway command backdoor endpoints`

Điều này cho thấy API Vetek hiện tại đang có xu hướng:
- quản lý master data khá rõ
- command gateway mạnh
- mô hình runtime xoay quanh `gateways` + `nodes`
- zone/customer-based hơn là project/group/device abstraction kiểu SHUNCOM brainstorm

## 4. Những phần brainstorm có nhưng Vetek docs hiện tại chưa thấy

### Chưa thấy rõ trong docs hiện tại
- `POST /auth/refresh`
- `POST /auth/logout`
- `GET /auth/me`
- full `users` CRUD
- `roles`, `permissions`, `management scope`
- `organizations` CRUD đúng nghĩa
- `projects/tree`, `sub-projects`
- `device-groups`
- `device-types` inventory theo business type
- `rules/platform`, `rules/local`, `rules/alarm`
- `alarms/{id}/acknowledge`
- `alarms/{id}/resolve`
- `settings/system`, `settings/timezone`, `settings/notifications`
- `reports/*`
- `recycle-bin/*`
- `audit/logs`
- WebSocket/realtime topics

## 5. Nhận định kiến trúc ngắn

Nếu lấy Vetek docs hiện tại làm nguồn thật đang có, thì backend hiện tại gần với mô hình sau hơn:
- `customers` = tenant/customer layer
- `zones` = vùng/khu vực quản lý
- `gateways` = thiết bị cấp hub
- `nodes` = thiết bị con hoặc endpoint field
- `rules` = rule CRUD tổng quát
- `gateway commands` = control plane chính
- `dashboard_overview/detail` = read model cho dashboard
- nhiều bảng master-data = chuẩn hóa model/runtime/config

Tức là nó **không hoàn toàn khớp 1:1** với bộ API brainstorm trước đó. Bộ brainstorm trước đó vẫn hữu ích để thiết kế API domain-level đẹp hơn, nhưng nếu bám vào docs thật hiện tại thì nên map lại theo mô hình `customer -> zone -> gateway -> node`.

## 6. Gợi ý sử dụng tiếp

### Nếu mục tiêu là bám đúng backend hiện tại
Nên viết lại inventory API theo các nhóm sau:
- Auth
- Customers
- Zones
- Gateways
- Nodes
- Rules
- Scripts
- Gateway Commands
- Dashboard Overview / Detail
- Logs
- Master Data Types

### Nếu mục tiêu là thiết kế target architecture tương lai
Có thể giữ inventory brainstorm cũ như một **target API model**, nhưng cần note rõ:
- đây là domain-driven inventory
- chưa phản ánh đúng hoàn toàn OpenAPI đang public ở `api.vetek.vn`
- cần mapping layer từ target model sang current implementation

## 7. Kết luận
Hiện tại `https://api.vetek.vn/docs` đã có khá nhiều API thật, nhưng chúng đang theo mô hình thực thi của Vetek/VSense chứ chưa trùng hoàn toàn với bộ API brainstorm trước đó.

Tóm gọn:
- **Đã có thật:** auth cơ bản, customers, zones, gateways, nodes, rules, scripts, dashboard, logs, gateway commands, nhiều master-data types
- **Khớp một phần với brainstorm:** auth, devices, rules, dashboard, logs
- **Chưa thấy trong docs hiện tại:** users/roles/scope đầy đủ, projects tree, groups, alarms workflow đầy đủ, reports, settings, recycle-bin, audit logs, websocket topics
