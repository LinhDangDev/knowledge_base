# Device Management Hub

## Overview
- Canonical topic: Device domain
- Goal: Chuẩn hóa tri thức về vòng đời thiết bị, cấu hình theo loại, association, import/export, và các ràng buộc vận hành chính của SHUNCOM RULR.
- Primary users: BA, PM, QA, Dev, Ops, field operator

## Provenance
### Source summary
```yaml
Document status: Canonical draft
Confidence: Medium
Last validated: 2026-04-12
Validated by: Claude Code
Primary source type: screenshot
Canonical topic: device-management
```

### Primary sources used
| Source | Path | Why it matters |
|---|---|---|
| Manual screenshot | `manual-images/p61_Image376.jpg` | form Smart Gateway, loop configuration, project/group/location fields |
| Manual screenshot | `manual-images/p33_Image301.png` | form Smart Meter và required fields nhìn thấy trên UI |
| Flow doc | `docs/shuncom-iot-screen-flows.md` | flow 6-12 cho create/configuration flows |
| BA doc | `docs/shuncom-iot-ba-user-stories.md` | business intent cho device onboarding |
| Traceability map | `docs/shuncom-iot-story-flow-screen-module-mapping.md` | story-flow-screen mapping |
| Analysis doc | `SHUNCOM_RULR_IoT_Platform_Analysis.md` | 7 device categories, sync/import/recycle-bin constraints |

### Validation gaps
- Một số field labels trong tài liệu cũ bị lẫn hoặc không đồng nhất giữa các loại thiết bị.
- Payload API chi tiết cho device operations chưa được xác nhận từ backend source code.

## Scope
### In scope
- Device categories và subtype logic
- Device creation / edit / association / sync
- Product information và asset info
- Import/export / recycle bin / group-project associations
- Operational constraints nhìn thấy từ manual-derived sources

### Out of scope
- Database column-level schema chi tiết
- Device protocol electrical specification ở mức firmware bit-level
- Backend implementation internals

## Traceability
### Related stories
- `US-DEV-03` - Tạo thiết bị
- `US-GW-02` - Tạo Smart Gateway
- `US-GW-03` - Cấu hình gateway circuits
- `US-LC-02` - Tạo controller theo subtype
- `US-LC-03` - Gán luminaires cho controller
- `US-METER-01` - Tạo Smart Meter
- `US-POLE-01` - Tạo Lighting Pole
- `US-BATCH-01` - Import thiết bị hàng loạt

### Related flows
- Flow 6 - Tạo Thiết bị theo Type
- Flow 7 - Tạo Smart Gateway
- Flow 8 - Cấu hình Gateway Circuits
- Flow 9 - Tạo Smart Light Controller
- Flow 10 - Chọn Associated Luminaires
- Flow 11 - Tạo Loop Control
- Flow 12 - Tạo Smart Meter
- Lighting Pole hiện đang được trace gián tiếp qua story `US-POLE-01` và device-type flow chung; chưa có flow canonical riêng trong bộ nguồn hiện tại.

### Main screens / contexts
| Screen / Context                                     | Purpose                                     | Evidence                     |
| ---------------------------------------------------- | ------------------------------------------- | ---------------------------- |
| `Equipment management > Device configuration > Type` | list theo category + add device             | `[SRC:FLOW-6]`               |
| Smart Gateway form                                   | onboard gateway và cấu hình associations    | `[SRC:IMG-p61_Image376.jpg]` |
| Smart Meter form                                     | onboard meter với gateway/downlink/protocol | `[SRC:IMG-p33_Image301.png]` |
| Associated luminaires selector                       | bind controller với luminaires              | `[SRC:FLOW-10]`              |
| Configure circuits                                   | mapping loop/circuit cho gateway            | `[SRC:FLOW-8]`               |

## Business responsibilities
- Quản lý vòng đời thiết bị từ onboard tới recycle bin.
- Áp dụng form động theo device category / product subtype.
- Quản lý quan hệ gateway-subdevice, controller-fixture, project-group-device.
- Cung cấp dữ liệu đầu vào cho rules, dashboard, GIS, analytics, và logs.

## Supported device set
| Device Type                      | Main purpose                         | Important constraints                                                                              |
| -------------------------------- | ------------------------------------ | -------------------------------------------------------------------------------------------------- |
| Gateway                          | hub quản lý sub-devices              | device number/product required; có sync/local-rule ops                                             |
| Industrial Controller            | industrial control endpoint          | field model cần bám product/subtype thực tế                                                        |
| Smart Light Controller           | điều khiển đèn theo nhiều subtype    | field bắt buộc thay đổi theo subtype; một số subtype cần gateway; thường cần associated luminaires |
| Power Distribution Control (PDC) | quản lý tủ điện / power distribution | thường liên kết gateway / circuit / meter                                                          |
| Weather Sensor                   | weather telemetry source             | phụ thuộc telemetry/threshold use cases                                                            |
| Environmental Sensor             | environment telemetry source         | phụ thuộc telemetry/threshold use cases                                                            |
| Smart Electric Meter             | đo điện năng / thống kê điện         | thường gắn gateway, protocol, downlink channel                                                     |
| Lighting Pole                    | thực thể hạ tầng vật lý              | dùng cho association/visual organization                                                           |
| Lighting Fixture                 | đại diện bộ đèn / tải chiếu sáng     | cần cho một số controller use case; thiếu association có thể làm đèn không điều khiển được         |
| Smart Water Meter                | water metering device                | schema/association chi tiết cần verify thêm                                                        |
| Leakage Monitoring               | leakage detection / alarm device     | alarm/safety-oriented use case                                                                     |
| Indoor Light Controller          | indoor lighting control device       | có thể có subtype riêng, hiện giữ như supported type riêng                                         |
| Scene Panel                      | scene/interaction control panel      | control/UI linkage device                                                                          |
| Accessory Device                 | supporting accessory device          | normalized spelling from previous 'Accessary'                                                      |

## Common data structure
### Device information
| Field family | Notes |
|---|---|
| Device name | có thể optional ở một số form |
| Product name / subtype | thường là required |
| Device number | required cho nhiều thiết bị, có thể là MAC/IMEI/identifier |
| Project / Belonging group | ảnh hưởng scope, dashboard, GIS, rules |
| Latitude / Longitude / Altitude | cần cho GIS, sunrise/sunset, map placement |

### Product information
- Metadata sản phẩm theo model/device type
- Có thể mang tính động theo product
- Là nơi chứa thông tin kỹ thuật hoặc giới thiệu sản phẩm

### Asset info
- Manufacturer
- Price
- Purchase date
- Installation date
- Expiration / tariff expiration
- Service life

## Type-specific configuration patterns
### Smart Gateway
- Có thể liên kết distribution box, circuit control, electricity meter.
- Có `Loop configuration / Configure Now` trên form `[SRC:IMG-p61_Image376.jpg]`.
- Có các operation thường gặp: sync, clear local rules, set ratios, screen password.

### Smart Light Controller
- Nhóm subtype chính theo nguồn hiện có:
  - pass-through / Zigbee
  - direct communication / NB-IoT / CAT.1
  - LoRa OTAA / ABP
- Với LoRa, trường cấu hình thay đổi theo access mode.
- Với một số use case lighting, associated luminaires là constraint quan trọng.

### Smart Electric Meter
- UI hiện có cho thấy các field: gateway, downlink channel, sub-device protocol, location, project, group `[SRC:IMG-p33_Image301.png]`.
- Dùng cho energy analytics và dashboard statistics.

## Core flows
### 1. Create by type
1. User chọn category ở Type list.
2. User nhấn `Add device`.
3. Form render theo loại / subtype.
4. User nhập device information, product information, asset info.
5. Hệ thống validate theo loại.
6. Record được tạo và xuất hiện trong list.

### 2. Association flow
- Device có thể được gán vào project.
- Device có thể được gán vào group.
- Một số thiết bị có association thiết bị-cha / thiết bị-con.
- Controller có thể cần gán luminaires.

### 3. Sync and lifecycle flow
- Gateway / local-rule capable devices có sync behavior.
- Batch import hỗ trợ onboarding số lượng lớn.
- Recycle bin giữ basic info nhưng historical data có thể mất theo analysis doc.

## Business constraints
- Bắt buộc field thay đổi theo device type và subtype.
- Project/group binding ảnh hưởng trực tiếp visibility và scope.
- Device có tọa độ mới dùng tốt cho GIS distribution và sunrise/sunset based logic.
- Batch import có giới hạn `5000` devices mỗi lần theo analysis doc.
- Delete/recycle-bin behavior phải cân nhắc dependency bindings và historical data loss.
- Một số subtype controller cần gateway; một số subtype direct communication thì không.
- Fixture association là constraint quan trọng cho một số luồng điều khiển đèn.

## API contract posture
- Các API touchpoints dưới đây là inventory-level references để nối domain doc với API map.
- Contract chính thức phải defer về [API Endpoints Map](../02-System-Architecture/API%20Endpoints%20Map.md) và backend/OpenAPI source nếu có.

## Data and integration touchpoints
| Type     | Item                                      | Purpose                            |
| -------- | ----------------------------------------- | ---------------------------------- |
| API      | `GET /devices`                            | list/filter devices                |
| API      | `POST /devices`                           | register device                    |
| API      | `PUT /devices/:deviceId`                  | update configuration               |
| API      | `POST /devices/:deviceId/control`         | command/control                    |
| API      | `POST /devices/batch/import`              | bulk import                        |
| API      | `DELETE /devices/:deviceId`               | recycle/delete flow                |
| Realtime | device status updates                     | dashboard and operation feedback   |
| Data     | device, gateway, group, project relations | rule/dashboard/GIS source-of-truth |

## Logging and audit implications
- Audit log: create/edit/delete/import/restore device actions.
- Operational log: sync result, command result, batch import result, validation failures.
- Analytics/log dependency: meter/light controller data feeds dashboard và energy statistics.

## Related docs
- [API Endpoints Map](../02-System-Architecture/API%20Endpoints%20Map.md)
- [05-Project Management](../05-User-Management/05-Project%20Management.md)
- [04-Rule Engine System](../04-Rule-Management/04-Rule%20Engine%20System.md)
- [06-Dashboard Interface](../06-Project-Management/06-Dashboard%20Interface.md)
- [Device Troubleshooting](Device%20Troubleshooting.md)

## Open questions
- Exact validation regex/range cho từng protocol-specific field chưa được xác nhận từ source code/backend.
- Delete flow thực tế giữa hard delete, recycle bin, và dependency resolution cần backend confirmation chi tiết hơn.
