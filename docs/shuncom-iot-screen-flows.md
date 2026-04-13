# SHUNCOM IoT — Luồng Màn Hình

## 1. Tổng quan
- Nguồn tổng hợp: checklist Excel, manual PDF/text, toàn bộ ảnh trong `manual-images/`
- Trọng tâm của bản này: làm rõ các **luồng tạo mới (create flows)** bằng markdown chi tiết
- Phạm vi: luồng theo từng màn hình cho BA, thiết kế, và căn chỉnh triển khai
- Trạng thái: Bản nháp

## 2. Chỉ mục flow
1. Đăng nhập
2. Tạo User
3. Cấu hình Management Scope
4. Tạo Project
5. Gán Thiết bị vào Project
6. Tạo Thiết bị theo Type
7. Tạo Smart Gateway
8. Cấu hình Gateway Circuits
9. Tạo Smart Light Controller
10. Chọn Associated Luminaires
11. Tạo Loop Control
12. Tạo Smart Electric Meter
13. Tạo Device Group
14. Gán Thiết bị vào Group
15. Tạo Platform Rule
16. Tạo Local Rule
17. Xem Kết quả Đồng bộ Local Rule
18. Tạo Alarm Rule
19. Tạo Receiving Group
20. Cấu hình Display Information
21. Cấu hình Lighting Schedules Today
22. Cấu hình Electricity Consumption Plan
23. Thao tác Thiết bị từ Operation Control
24. Xem Chi tiết Thiết bị
25. Xem Thống kê / Phân tích

---

## 1. Đăng nhập
- **Điểm vào:** Trang landing của hệ thống
- **Tác nhân:** Người dùng
- **Kích hoạt:** Người dùng muốn vào hệ thống
- **Điều kiện tiên quyết:** Tài khoản tồn tại và đang active

### Luồng chính
1. Người dùng mở trang đăng nhập.
2. Người dùng nhập username.
3. Người dùng nhập password.
4. Người dùng nhấn đăng nhập.
5. Hệ thống xác thực thông tin.
6. Hệ thống tải màn hình khởi đầu theo quyền.

### Quy tắc kiểm tra
- Username là bắt buộc.
- Password là bắt buộc.
- User bị disable không được phép đăng nhập.

### Trạng thái thành công
- Phiên đăng nhập được tạo.
- Header và menu điều hướng xuất hiện.

### Trạng thái thất bại
- Đăng nhập bị từ chối.
- Hệ thống hiển thị thông báo lỗi.

---

## 2. Tạo User
- **Điểm vào:** Basic settings → User management
- **Tác nhân:** Quản trị viên hệ thống
- **Kích hoạt:** Có người mới cần được cấp quyền truy cập
- **Điều kiện tiên quyết:** Admin có quyền quản lý user

### Các trường dữ liệu
- Account / username
- Password hoặc credential khởi tạo
- Role
- Department
- Status
- Thông tin liên hệ nếu màn hình hỗ trợ

### Luồng chính
1. Admin mở User Management.
2. Admin nhấn **Add User**.
3. Hệ thống mở form tạo user.
4. Admin nhập các trường định danh.
5. Admin chọn role và department.
6. Admin đặt trạng thái user.
7. Admin nhấn **Save**.
8. Hệ thống kiểm tra form.
9. Hệ thống tạo user.
10. Hệ thống refresh danh sách user.

### Luồng thay thế
- Admin lưu không gán role khi role là tùy chọn → hệ thống vẫn tạo user và cho phép gán role sau.
- Admin tạo user ở trạng thái disabled → user được lưu nhưng chưa thể đăng nhập.

### Luồng ngoại lệ
- Trùng username → hệ thống chặn lưu.
- Thiếu trường bắt buộc → hệ thống highlight trường lỗi.

### Hậu điều kiện
- User mới xuất hiện trong danh sách user.
- User sẵn sàng cho bước gán scope.

---

## 3. Cấu hình Management Scope
- **Điểm vào:** Basic settings → Permission Management → Management scope
- **Tác nhân:** Quản trị viên hệ thống
- **Kích hoạt:** Role hoặc user cần bị giới hạn dữ liệu
- **Điều kiện tiên quyết:** Role/user đã tồn tại

### Các trường dữ liệu
- Product category selections
- Project selections
- Group selections

### Luồng chính
1. Admin mở Permission Management.
2. Admin chọn role hoặc đối tượng scope cần cấu hình.
3. Admin mở **Management scope**.
4. Admin chọn các product category được phép.
5. Admin chọn các project được phép.
6. Admin chọn các group được phép.
7. Admin nhấn **Save**.
8. Hệ thống lưu cấu hình scope.

### Quy tắc nghiệp vụ
- Scope có thể giới hạn phạm vi thiết bị, project, và group.
- Scope chỉ có hiệu lực sau khi lưu thành công.

### Hậu điều kiện
- Quyền hiển thị dữ liệu của đối tượng đích được cập nhật.

---

## 4. Tạo Project
- **Điểm vào:** Equipment management → Device configuration → Project
- **Tác nhân:** Quản trị viên project
- **Kích hoạt:** Cần tạo ngữ cảnh project mới
- **Điều kiện tiên quyết:** Người dùng có quyền quản lý project

### Các trường dữ liệu
- Project name
- Manager
- Project description
- Contact address
- Detailed address
- Latitude
- Longitude
- Chế độ nền bản đồ: GIS / Custom upload

### Luồng chính
1. Người dùng mở tab Project.
2. Người dùng nhấn **Add project**.
3. Hệ thống mở modal tạo project.
4. Người dùng nhập project name.
5. Người dùng chọn manager.
6. Người dùng nhập description và address.
7. Người dùng nhập latitude/longitude hoặc dùng **Locate in map**.
8. Người dùng chọn GIS hoặc custom background.
9. Người dùng nhấn **Save**.
10. Hệ thống kiểm tra trường bắt buộc và định dạng tọa độ.
11. Hệ thống tạo project.
12. Hệ thống refresh cây project.

### Luồng thay thế
- Người dùng bỏ qua description vì là tùy chọn → project vẫn được tạo.
- Người dùng chọn vị trí bằng map picker thay vì nhập tay tọa độ.

### Luồng ngoại lệ
- Thiếu project name → không cho lưu.
- Tọa độ không hợp lệ → hiển thị lỗi validation.

### Hậu điều kiện
- Project xuất hiện trong cây project.
- Project có thể được chọn trong form thiết bị và cấu hình scope.

---

## 5. Gán Thiết bị vào Project
- **Điểm vào:** Project node → Associated devices
- **Tác nhân:** Quản trị viên project
- **Kích hoạt:** Thiết bị hiện có cần được gắn vào project
- **Điều kiện tiên quyết:** Project đã tồn tại; thiết bị đã tồn tại

### Luồng chính
1. Người dùng chọn một project.
2. Người dùng nhấn **Associated devices**.
3. Hệ thống mở bộ chọn thiết bị.
4. Người dùng tìm danh sách thiết bị khả dụng.
5. Người dùng chọn một hoặc nhiều thiết bị.
6. Người dùng xác nhận.
7. Hệ thống tạo liên kết project-device.
8. Hệ thống refresh context project.

### Luồng ngoại lệ
- Không chọn thiết bị → không cho xác nhận.
- Thiết bị đang bị ràng buộc xung đột → hiển thị cảnh báo validation.

### Hậu điều kiện
- Thiết bị đã chọn thuộc project hiện tại.

---

## 6. Tạo Thiết bị theo Type
- **Điểm vào:** Device configuration → Type → Add device
- **Tác nhân:** Quản trị viên thiết bị
- **Kích hoạt:** Cần onboard thiết bị mới
- **Điều kiện tiên quyết:** Người dùng có quyền tạo; category mục tiêu tồn tại

### Các khu vực form dùng chung
- Device information
- Product Information
- Asset Info

### Luồng chính dùng chung
1. Người dùng mở tab Type.
2. Người dùng chọn category thiết bị trong sidebar.
3. Người dùng nhấn **Add device**.
4. Hệ thống mở form tạo theo category.
5. Người dùng nhập Device information.
6. Người dùng cập nhật Product Information nếu cần.
7. Người dùng cập nhật Asset Info nếu cần.
8. Người dùng nhấn **Save**.
9. Hệ thống kiểm tra các quy tắc theo loại.
10. Hệ thống tạo bản ghi và refresh danh sách.

### Quy tắc kiểm tra dùng chung
- Product là bắt buộc.
- Device number là bắt buộc trừ khi logic sản phẩm tự sinh.
- Quy tắc project/group/location phụ thuộc từng type.

### Hậu điều kiện
- Thiết bị xuất hiện trong danh sách type đã chọn.

---

## 7. Tạo Smart Gateway
- **Điểm vào:** Type → Smart Gateway → Add device
- **Tác nhân:** Quản trị viên gateway
- **Kích hoạt:** Cần onboard gateway mới
- **Điều kiện tiên quyết:** Các master records liên quan tồn tại nếu association là bắt buộc

### Các trường dữ liệu
- Device name
- Product name
- Device number
- Associated distribution box
- Associated circuit control
- Select electricity meter
- Latitude / Longitude
- Altitude
- Project
- Belonging group

### Luồng chính
1. Người dùng chọn **Smart Gateway**.
2. Người dùng nhấn **Add device**.
3. Hệ thống mở form tạo Smart Gateway.
4. Người dùng nhập device name.
5. Người dùng chọn product name.
6. Người dùng nhập device number.
7. Người dùng chọn distribution box, circuit control và electricity meter nếu áp dụng.
8. Người dùng nhập tọa độ và altitude.
9. Người dùng chọn project và group.
10. Người dùng chỉnh Product Information nếu cần.
11. Người dùng chỉnh Asset Info nếu cần.
12. Người dùng nhấn **Save**.
13. Hệ thống kiểm tra form.
14. Hệ thống tạo Smart Gateway.
15. Hệ thống refresh danh sách gateway.

### Quy tắc kiểm tra
- Product và device number là bắt buộc.
- Association phải trỏ đến bản ghi hợp lệ.
- Tọa độ phải là số hợp lệ.

### Trạng thái thành công
- Gateway xuất hiện trong danh sách Smart Gateway.
- Các action nâng cao bắt đầu khả dụng.

---

## 8. Cấu hình Gateway Circuits
- **Điểm vào:** Smart Gateway list → More → Configure circuits
- **Tác nhân:** Quản trị viên gateway
- **Kích hoạt:** Cần định nghĩa loop/circuit mapping của gateway
- **Điều kiện tiên quyết:** Gateway đã tồn tại

### Các trường theo từng dòng
- Loop control
- Loop serial number
- Control remark name
- Associated devices
- Loop collection
- Collection attributes
- Phase
- Collection remark name
- Displayed flag

### Luồng chính
1. Người dùng chọn một gateway có sẵn.
2. Người dùng mở **More > Configure circuits**.
3. Hệ thống mở màn cấu hình circuit.
4. Người dùng điền giá trị cho từng dòng.
5. Người dùng thêm dòng mới khi cần.
6. Người dùng xóa dòng sai khi cần.
7. Người dùng nhấn **Save**.
8. Hệ thống kiểm tra trùng lặp, trường bắt buộc, và quan hệ hợp lệ.
9. Hệ thống lưu cấu hình circuit.

### Luồng ngoại lệ
- Trùng loop serial → chặn lưu.
- Thiếu trường bắt buộc → chặn lưu.

### Hậu điều kiện
- Circuit definitions của gateway được lưu.

---

## 9. Tạo Smart Light Controller
- **Điểm vào:** Type → Smart Light Controller → Add device
- **Tác nhân:** Quản trị viên chiếu sáng
- **Kích hoạt:** Cần onboard controller mới
- **Điều kiện tiên quyết:** Subtype hỗ trợ đang tồn tại

### Các trường dữ liệu
- Device name
- Product name / subtype
- Device number
- Gateway (nếu subtype cần)
- Light pole
- Associated luminaires
- Latitude / Longitude
- Altitude
- Project
- Belonging group

### Luồng chính
1. Người dùng chọn **Smart Light Controller**.
2. Người dùng nhấn **Add device**.
3. Hệ thống mở form tạo controller.
4. Người dùng chọn product subtype.
5. Hệ thống render các trường riêng theo subtype.
6. Người dùng nhập các trường thiết bị cơ bản.
7. Người dùng chọn gateway nếu subtype yêu cầu.
8. Người dùng chọn light pole nếu cần.
9. Người dùng mở selector của luminaires nếu áp dụng.
10. Người dùng nhập project/group/location.
11. Người dùng nhấn **Save**.
12. Hệ thống kiểm tra dữ liệu theo subtype.
13. Hệ thống tạo controller.

### Quy tắc kiểm tra
- Trường bắt buộc khác nhau theo subtype.
- Gateway có thể bắt buộc với một số subtype.
- Associated luminaires có thể bắt buộc với subtype điều khiển đèn.

### Hậu điều kiện
- Controller xuất hiện trong danh sách Smart Light Controller.

---

## 10. Chọn Associated Luminaires
- **Điểm vào:** Form Smart Light Controller → Associated luminaires
- **Tác nhân:** Quản trị viên chiếu sáng
- **Kích hoạt:** Controller cần được gán bộ đèn
- **Điều kiện tiên quyết:** Đã có các bản ghi luminaire

### Luồng chính
1. Người dùng nhấn **Associated luminaires**.
2. Hệ thống mở drawer/modal selector.
3. Người dùng tìm danh sách luminaire.
4. Người dùng chọn một hoặc nhiều luminaire.
5. Người dùng xác nhận.
6. Hệ thống lưu association và quay lại form.

### Luồng ngoại lệ
- Không có luminaire phù hợp → hiển thị empty state.
- Lựa chọn không hợp lệ theo subtype → chặn xác nhận.

### Hậu điều kiện
- Quan hệ luminaire hiển thị trên form controller.

---

## 11. Tạo Loop Control
- **Điểm vào:** Type → Loop Control → Add device
- **Tác nhân:** Gateway operator
- **Kích hoạt:** Cần tạo loop control mới
- **Điều kiện tiên quyết:** Gateway mục tiêu tồn tại nếu bắt buộc

### Các trường dữ liệu
- Device name
- Product name
- Device number
- Gateway
- Downlink channel
- Sub-device protocol
- Latitude / Longitude
- Altitude
- Project
- Belonging group

### Luồng chính
1. Người dùng chọn **Loop Control**.
2. Người dùng nhấn **Add device**.
3. Người dùng nhập device name/product/device number.
4. Người dùng chọn gateway.
5. Người dùng nhập downlink channel.
6. Người dùng chọn sub-device protocol.
7. Người dùng nhập location/project/group.
8. Người dùng nhấn **Save**.
9. Hệ thống kiểm tra các ràng buộc kỹ thuật.
10. Hệ thống tạo bản ghi Loop Control.

### Hậu điều kiện
- Loop Control xuất hiện trong danh sách.

---

## 12. Tạo Smart Electric Meter
- **Điểm vào:** Type → Smart Electric Meter → Add device
- **Tác nhân:** Metering operator
- **Kích hoạt:** Cần onboard smart meter mới
- **Điều kiện tiên quyết:** Gateway tồn tại nếu association là bắt buộc

### Các trường dữ liệu
- Device name
- Product name
- Device number
- Associated gateway
- Meter no.
- Total account number
- Latitude / Longitude
- Altitude
- Project
- Belonging group

### Luồng chính
1. Người dùng chọn **Smart Electric Meter**.
2. Người dùng nhấn **Add device**.
3. Hệ thống mở form Smart Electric Meter.
4. Người dùng nhập các trường định danh meter.
5. Người dùng chọn associated gateway.
6. Người dùng nhập project/group/location.
7. Người dùng nhấn **Save**.
8. Hệ thống kiểm tra các trường kỹ thuật.
9. Hệ thống tạo Smart Electric Meter.

### Hậu điều kiện
- Smart Electric Meter xuất hiện trong danh sách.

---

## 13. Tạo Device Group
- **Điểm vào:** Device configuration → Group → Add Group
- **Tác nhân:** Quản trị viên vận hành
- **Kích hoạt:** Cần nhóm thiết bị phục vụ vận hành
- **Điều kiện tiên quyết:** Các product category đã tồn tại

### Các trường dữ liệu
- Group name
- Product category
- Location / tọa độ nếu áp dụng
- Frequency / multicast settings nếu áp dụng
- Description / remarks nếu hỗ trợ

### Luồng chính
1. Người dùng mở tab Group.
2. Người dùng nhấn **Add Group**.
3. Hệ thống mở form group.
4. Người dùng nhập metadata của group.
5. Người dùng chọn product category.
6. Người dùng nhập location/frequency config nếu áp dụng.
7. Người dùng nhấn **Save** hoặc **Save and associate devices**.
8. Hệ thống kiểm tra form.
9. Hệ thống tạo group.

### Hậu điều kiện
- Group xuất hiện trong Group view.

---

## 14. Gán Thiết bị vào Group
- **Điểm vào:** Group create/edit flow → Associate devices
- **Tác nhân:** Quản trị viên vận hành
- **Kích hoạt:** Cần chỉ định membership cho group
- **Điều kiện tiên quyết:** Group đã tồn tại; thiết bị đã tồn tại

### Luồng chính
1. Người dùng mở flow associate devices.
2. Hệ thống mở bộ chọn thiết bị.
3. Người dùng tìm và chọn thiết bị.
4. Người dùng xác nhận membership.
5. Hệ thống lưu quan hệ group-device.
6. Hệ thống refresh context group.

### Hậu điều kiện
- Group chứa các thiết bị đã chọn.

---

## 15. Tạo Platform Rule
- **Điểm vào:** Rule Management → Running Rules → Add Rule
- **Tác nhân:** Operator
- **Kích hoạt:** Cần automation trung tâm
- **Điều kiện tiên quyết:** Product category và target devices đã tồn tại

### Các trường dữ liệu
- Rule name
- Rule type
- Product category
- Effective date / forever
- Repeat period
- Remarks
- Trigger conditions
- Execute actions
- Devices to be operated

### Luồng chính
1. Người dùng mở Platform Rules.
2. Người dùng nhấn **Add Rule**.
3. Hệ thống mở form rule.
4. Người dùng nhập metadata.
5. Người dùng thêm một hoặc nhiều trigger conditions.
6. Người dùng thêm một hoặc nhiều actions.
7. Người dùng chọn target devices.
8. Người dùng nhấn **Save**.
9. Hệ thống kiểm tra tính đầy đủ của rule.
10. Hệ thống tạo platform rule.

### Hậu điều kiện
- Rule xuất hiện trong danh sách running rules.

---

## 16. Tạo Local Rule
- **Điểm vào:** Rule Management → Local Rules → Add Local Rule
- **Tác nhân:** Operator
- **Kích hoạt:** Cần automation chạy ở tầng thiết bị
- **Điều kiện tiên quyết:** Có category hỗ trợ local rule

### Các trường dữ liệu
- Rule name
- Rule type = Local Rules
- Product category
- Effective date / forever
- Repeat period
- Remarks
- Trigger conditions
- Execute actions
- Devices to be operated

### Luồng chính
1. Người dùng mở Local Rules.
2. Người dùng nhấn **Add Local Rule**.
3. Hệ thống mở form local rule.
4. Người dùng nhập metadata.
5. Người dùng thêm trigger conditions như time, sunrise/sunset, light sensor threshold.
6. Người dùng thêm actions.
7. Người dùng chọn target devices.
8. Người dùng nhấn **Save**.
9. Hệ thống kiểm tra và tạo local rule.

### Hậu điều kiện
- Rule xuất hiện trong Local Rules list.

---

## 17. Xem Kết quả Đồng bộ Local Rule
- **Điểm vào:** Action của local rule → Send rules synchronously / Verify synchronization
- **Tác nhân:** Operator
- **Kích hoạt:** Người dùng cần biết kết quả sau khi sync local rule
- **Điều kiện tiên quyết:** Local rule đã tồn tại; có target devices

### Luồng chính
1. Người dùng kích hoạt đồng bộ.
2. Hệ thống gửi rule xuống thiết bị.
3. Hệ thống mở dialog Sync Result.
4. Người dùng xem kết quả theo từng thiết bị, thời gian sync và remarks.
5. Người dùng có thể retry hoặc verify lại.

### Hậu điều kiện
- Trạng thái sync sẵn sàng cho mục đích troubleshooting và audit.

---

## 18. Tạo Alarm Rule
- **Điểm vào:** Rule Management → Alarm Rules → Add Rule
- **Tác nhân:** Operator
- **Kích hoạt:** Cần cấu hình cảnh báo cho điều kiện bất thường
- **Điều kiện tiên quyết:** Alarm level và receiving group tồn tại nếu bắt buộc

### Các trường dữ liệu
- Rule name
- Product / category
- Effective date / forever
- Repeat period
- Effective time
- Trigger conditions
- Silence period
- Alarm/reminder behavior
- Notification / receiving group
- Remarks

### Luồng chính
1. Người dùng mở Alarm Rules.
2. Người dùng nhấn **Add Rule**.
3. Hệ thống mở form alarm rule.
4. Người dùng nhập metadata.
5. Người dùng định nghĩa trigger conditions.
6. Người dùng đặt silence period và severity behavior.
7. Người dùng chọn receiving group / notification behavior.
8. Người dùng nhấn **Save**.
9. Hệ thống kiểm tra và tạo alarm rule.

### Hậu điều kiện
- Alarm rule xuất hiện trong danh sách Alarm Rules.

---

## 19. Tạo Receiving Group
- **Điểm vào:** Rule Management → Other Configurations → Receiving Group
- **Tác nhân:** Operator
- **Kích hoạt:** Alarm rules cần đối tượng nhận cảnh báo
- **Điều kiện tiên quyết:** Người dùng có quyền cấu hình

### Các trường dữ liệu
- Group name
- Notification method
- Notification interval/window
- Remarks

### Luồng chính
1. Người dùng mở Other Configurations.
2. Người dùng chọn khu vực Receiving Group.
3. Người dùng nhấn **Add**.
4. Người dùng nhập các trường của receiving group.
5. Người dùng nhấn **Save**.
6. Hệ thống kiểm tra và tạo receiving group.

### Hậu điều kiện
- Receiving group có thể chọn được trong form alarm rule.

---

## 20. Cấu hình Display Information
- **Điểm vào:** Project edit → Display Information
- **Tác nhân:** Quản trị viên project
- **Kích hoạt:** Dashboard của project cần được tùy chỉnh
- **Điều kiện tiên quyết:** Project đã tồn tại

### Luồng chính
1. Người dùng mở màn chỉnh project.
2. Người dùng vào tab **Display Information**.
3. Người dùng chọn presentation style và usage scenario.
4. Người dùng bật/tắt các modules.
5. Người dùng preview layout.
6. Người dùng lưu hoặc batch apply cấu hình.

### Hậu điều kiện
- Dashboard settings của project được cập nhật.

---

## 21. Cấu hình Lighting Schedules Today
- **Điểm vào:** Display Information → Lighting schedules today → Set
- **Tác nhân:** Quản trị viên project
- **Kích hoạt:** Cần cấu hình lịch chiếu sáng hằng ngày
- **Điều kiện tiên quyết:** Smart lighting scenario đã được bật

### Các trường dữ liệu
- Associated sensor
- Light on threshold
- Light off threshold
- Schedule source
- Sunrise/sunset offset
- Final time

### Luồng chính
1. Người dùng mở phần cài đặt lighting schedule.
2. Người dùng chọn nguồn lịch hoặc sensor.
3. Người dùng nhập threshold hoặc giá trị thời gian.
4. Người dùng đặt sunrise/sunset offset nếu áp dụng.
5. Người dùng lưu cấu hình.

### Hậu điều kiện
- Lịch chiếu sáng được lưu cho project.

---

## 22. Cấu hình Electricity Consumption Plan
- **Điểm vào:** Display Information → Electricity consumption plan → Set
- **Tác nhân:** Energy manager / Quản trị viên project
- **Kích hoạt:** Cần cấu hình chỉ tiêu điện năng cho project
- **Điều kiện tiên quyết:** Project đã tồn tại

### Các trường dữ liệu
- Year
- Annual planned value
- Warning ratio
- Monthly plan values
- Daily plan values

### Luồng chính
1. Người dùng mở cài đặt electricity plan.
2. Người dùng chọn year.
3. Người dùng nhập annual planned value.
4. Người dùng nhập warning ratio.
5. Người dùng cấu hình monthly values.
6. Người dùng cấu hình daily values nếu áp dụng.
7. Người dùng lưu plan.

### Hậu điều kiện
- Kế hoạch điện năng sẵn sàng cho dashboard và cảnh báo.

---

## 23. Thao tác Thiết bị từ Operation Control
- **Điểm vào:** Dashboard / operation control screen
- **Tác nhân:** Operator
- **Kích hoạt:** Cần thao tác vận hành tức thời
- **Điều kiện tiên quyết:** Thiết bị nằm trong scope nhìn thấy của user

### Luồng chính
1. Người dùng mở operation control.
2. Người dùng chọn project/device context.
3. Người dùng chọn device hoặc group.
4. Người dùng chạy quick action phù hợp.
5. Hệ thống thực thi lệnh và trả feedback.

### Hậu điều kiện
- Kết quả command được hiển thị cho operator.

---

## 24. Xem Chi tiết Thiết bị
- **Điểm vào:** Device list / operation control → Detail
- **Tác nhân:** Operator
- **Kích hoạt:** Người dùng cần xem đầy đủ thông tin thiết bị
- **Điều kiện tiên quyết:** Thiết bị tồn tại và user có quyền truy cập

### Luồng chính
1. Người dùng mở device detail.
2. Hệ thống tải basic info.
3. Hệ thống tải Product Information và Asset Info.
4. Hệ thống tải telemetry/platform data nếu có.
5. Người dùng xem state hiện tại và các association liên quan.

### Hậu điều kiện
- Operator nhìn thấy toàn bộ context của thiết bị trong một màn.

---

## 25. Xem Thống kê / Phân tích
- **Điểm vào:** Device detail / analysis screen
- **Tác nhân:** Operator
- **Kích hoạt:** Người dùng cần xem xu hướng hoặc biểu đồ
- **Điều kiện tiên quyết:** Có dữ liệu lịch sử / thống kê

### Luồng chính
1. Người dùng mở màn statistical analysis.
2. Hệ thống tải charts và trends.
3. Người dùng đổi bộ lọc thời gian nếu có.
4. Người dùng export kết quả khi hỗ trợ.

### Hậu điều kiện
- Operator nhận được insight xu hướng hành vi thiết bị.

---

## Ghi chú
- Giả định: tên trường đã được chuẩn hóa từ UI hiển thị và ngữ cảnh manual.
- Rủi ro: một số label trong ảnh có độ phân giải thấp; khi implement cần xác nhận lại tên và constraint chính xác.
- Câu hỏi mở: API contracts chính xác, regex/range validation chính xác, format import/export, và cơ chế retry của device synchronization.