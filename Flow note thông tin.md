



Add device
- Setting -> Equipment Management -> Device Configuration -> Type Device -> (Choose device in list) -> Add device
- More 
	- Set screen password
	- Device Synchorminizattion 
	- 

- Gateway 
	- Device name
	- Product name
	- Device Number
	- Lat and Long (Địa chỉ kinh độ vĩ độ của vị trí )
	- Mac Address
	- Project 
	- Group = Zone
	- Product information (Thông tin chi tiết của device có thể import từ excel hoặc add feild từng cái để làm )
		- Device Manufacturer - Text
		- Prodcut model - Text
		- Supply Voltage - Text
		- Overall Power Consumption - Text
		- Product Image - image 
		- Product Introduction - Text
		Action để xóa các fill, select all field
- Industrial Controller = information Gateway
- Smart Light Controller:
	- 1. Device Type  
	- `device_type` (enum, required)  
	- `zigbee_v3`  
	- `dual_way_zigbee_v3`  
	- `nb_iot`  
	- `cat1`  
	- `lora`  
  
---  
  
## 2. Common Fields (áp dụng cho tất cả device)  
  
| Field                 | Type            | Required | Description            |     |
| --------------------- | --------------- | -------- | ---------------------- | --- |
| device_name           | string (max 50) | optional | Tên thiết bị           |     |
| product_name          | string          | required | Tên sản phẩm           |     |
| light_pole_id         | string          | optional | ID cột đèn             |     |
| associated_luminaires | string[]        | optional | Danh sách đèn liên kết |     |
| project_id            | string          | optional | ID project             |     |
| latitude              | number          | optional | Vĩ độ                  |     |
| longitude             | number          | optional | Kinh độ                |     |
| altitude              | number          | optional | Độ cao (m)             |     |
| belonging_group       | string          | optional | Nhóm                   |     |
  
---  
  
## 3. Pass-through Devices (Zigbee)  
  
### Condition  
`device_type IN (zigbee_v3, dual_way_zigbee_v3)`  
  
| Field | Type | Required | Description |  
|------|------|----------|------------|  
| device_number | string | required | Số thiết bị |  
| gateway_id | string | required | Gateway quản lý |  
  
---  
  
## 4. Directly-communicated Devices (NB-IoT / CAT.1)  
  
### Condition  
`device_type IN (nb_iot, cat1)`  
  
| Field | Type | Required | Description |  
|------|------|----------|------------|  
| device_number | string | required | Số thiết bị |  
  
👉 Note:  
- Không có `gateway_id`  
  
---  
  
## 5. LoRa Light Controller  
  
### Condition  
`device_type = lora`  
  
### 5.1 Common LoRa Fields  
  
| Field | Type | Required | Description |  
|------|------|----------|------------|  
| devui | string (16 hex) | required | Device EUI |  
| dev_profile | string | required | Profile (e.g. ClassC_EU868) |  
| access_mode | enum | required | `OTAA` hoặc `ABP` |  
  
---  
  
## 5.2 OTAA Mode  
  
### Condition  
`access_mode = OTAA`  
  
| Field | Type | Required | Description |  
|------|------|----------|------------|  
| appkey | string (32 hex) | required | App Key |  
  
---  
  
## 5.3 ABP Mode  
  
### Condition  
`access_mode = ABP`  
  
| Field | Type | Required | Description |  
|------|------|----------|------------|  
| devaddr | string (8 hex) | required | Device Address |  
| nwkskey | string (32 hex) | required | Network Session Key |  
  
---  
  
## 6. Asset Information (Optional)  
  
| Field                | Type          | Required | Description  |     |
| -------------------- | ------------- | -------- | ------------ | --- |
| manufacturer         | string        | optional | Nhà sản xuất |     |
| price                | number        | optional | Giá          |     |
| purchase_date        | string (date) | optional | Ngày mua     |     |
| installation_date    | string (date) | optional | Ngày lắp     |     |
| expiration_date      | string (date) | optional | Ngày hết hạn |     |
| expiration_of_tariff | string (date) | optional | Hết hạn gói  |     |
| service_life         | number        | optional | Tuổi thọ     |     |
| type                 | string        | optional | Loại         |     |
| function             | string        | optional | Chức năng    |     |
  
---







- Power Distribution Control (PDC)
- Weather Sensor
- Environmental Sensor
- Smart Electric Meter

- Lighting Pole
- Lighting Fixture
- Loop Control
- Smart Water Meter
- Leakage Monitoring
- Indoor Light Controller
- Scene Panel
- Accessory Device

Device Information


Batch import device (Import excel )



## Project management

Project 
- Sub project
Type Hiển thị tất cả các thiết bị dù là có thuộc project hay group nào nếu có thì hiển thị số không thì thôi
Group: Thuộc Zone quản lý Khu vực
	- Nhiều node
		- Device
- 



Conbime lại protocal smart light controller




Hiện tại có thể brainstorm các flow action user có thể có e2e về UI và backend các endpoint api như nào cho toàn bộ các flow đó và mermaid kiến trúc tổng quan và chi tiết từng cũng như là khi connect các thiết bị với platform và có thể mở rộng ra  sau này nữa 