# SHUNCOM IoT — User Stories BA

## 1. Tổng quan
- Nguồn tổng hợp: checklist Excel, manual PDF/text, toàn bộ ảnh trong `manual-images/`
- Trọng tâm của bản này: làm rõ các **user stories** chính theo format markdown cho BA
- Phạm vi: backlog toàn hệ thống, ưu tiên các luồng tạo mới/cấu hình
- Trạng thái: Bản nháp

## 2. Bản đồ story

| Epic                        | Các story tạo mới chính                                    |
| --------------------------- | ---------------------------------------------------------- |
| Xác thực & Truy cập         | Đăng nhập                                                  |
| Tổ chức / Vai trò / Phạm vi | Tạo user, tạo role, cấu hình phạm vi                       |
| Quản lý Project & GIS       | Tạo project, gán thiết bị, phân bố GIS                     |
| Cấu hình Thiết bị           | Tạo thiết bị theo loại                                     |
| Smart Gateway               | Tạo gateway, cấu hình circuits                             |
| Smart Light Controller      | Tạo controller, gán bộ đèn                                 |
| Thiết bị khác               | Tạo loop control, tạo smart meter, tạo lighting pole       |
| Quản lý Nhóm                | Tạo group, gán thiết bị, đồng bộ group                     |
| Quản lý Rule                | Tạo platform rule, local rule, alarm rule, receiving group |
| Dashboard / Hiển thị        | Cấu hình display info, lịch chiếu sáng, kế hoạch điện năng |

---

## 3. Các story tạo mới chi tiết

### Epic 01 — Xác thực & Truy cập

### US-AUTH-01 — Đăng nhập hệ thống
- **Mức ưu tiên:** Critical
- **Trạng thái:** Bản nháp

**User Story**  
Là một **người dùng**,  
tôi muốn **đăng nhập bằng thông tin hợp lệ**,  
để **truy cập hệ thống theo đúng quyền được cấp**.

**Vấn đề nghiệp vụ**
- Điểm đau hiện tại: truy cập chưa xác thực phải bị chặn.
- Tại sao quan trọng: mọi module phía sau đều phụ thuộc vào danh tính đã xác thực.
- Giá trị kinh doanh: tạo điểm vào an toàn cho toàn bộ hệ thống.

**Tiêu chí chấp nhận**
- [ ] Người dùng có thể nhập username/password và gửi form.
- [ ] Hệ thống xác thực thông tin hợp lệ.
- [ ] Hệ thống mở ứng dụng chính khi đăng nhập thành công.
- [ ] Hệ thống hiển thị lỗi rõ ràng khi thông tin sai.
- [ ] User bị disable không thể đăng nhập.

**Điều kiện tiên quyết**
- Tài khoản người dùng đã tồn tại.
- Tài khoản đang active.
- Dịch vụ xác thực đang khả dụng.

**Luồng chính**
1. Người dùng mở trang đăng nhập.
2. Người dùng nhập username và password.
3. Người dùng gửi form.
4. Hệ thống xác thực thông tin đăng nhập.
5. Hệ thống xác định role và scope của user.
6. Hệ thống tạo phiên đăng nhập.
7. Hệ thống điều hướng đến màn hình khởi đầu phù hợp quyền.

**Tình huống biên**
- Bỏ trống username/password.
- Sai thông tin đăng nhập.
- User bị disable.
- Dịch vụ xác thực timeout.

---

### Epic 02 — Tổ chức / User / Role / Scope

### US-ADM-03 — Tạo user
- **Mức ưu tiên:** High
- **Trạng thái:** Bản nháp

**User Story**  
Là một **quản trị viên hệ thống**,  
tôi muốn **tạo user mới**,  
để **nhân sự được cấp quyền có thể truy cập nền tảng**.

**Vấn đề nghiệp vụ**
- Điểm đau hiện tại: operator và admin cần được onboard có kiểm soát.
- Tại sao quan trọng: tạo account là tiền đề để gán role/scope.
- Giá trị kinh doanh: kiểm soát vòng đời danh tính người dùng.

**Tiêu chí chấp nhận**
- [ ] Admin có thể mở form thêm user.
- [ ] Admin có thể nhập đầy đủ thông tin bắt buộc.
- [ ] Admin có thể gán role trong lúc tạo hoặc sau khi tạo.
- [ ] Hệ thống kiểm tra duy nhất và các trường bắt buộc.
- [ ] User mới xuất hiện trong danh sách user.

**Điều kiện tiên quyết**
- Admin có quyền quản lý user.
- Có ít nhất một role nếu role là bắt buộc khi tạo user.

**Luồng tạo mới chi tiết**
1. Admin mở User Management.
2. Admin nhấn **Add User**.
3. Hệ thống mở form tạo user.
4. Admin nhập thông tin định danh user.
5. Admin chọn role, department, và trạng thái nếu màn hình hỗ trợ.
6. Admin lưu form.
7. Hệ thống kiểm tra trường bắt buộc và ràng buộc trùng tài khoản.
8. Hệ thống tạo bản ghi user.
9. Hệ thống refresh danh sách và hiển thị thông báo thành công.

**Quy tắc kiểm tra**
- Username/account phải là duy nhất.
- Không được bỏ trống trường bắt buộc.
- Không được dùng trạng thái disabled để bỏ qua các bước bắt buộc.

### US-ADM-04 — Tạo role
- **Mức ưu tiên:** High
- **Trạng thái:** Bản nháp

**User Story**  
Là một **quản trị viên hệ thống**,  
tôi muốn **tạo role mới**,  
để **gom nhóm quyền theo trách nhiệm nghiệp vụ**.

**Tiêu chí chấp nhận**
- [ ] Admin có thể mở form thêm role.
- [ ] Admin có thể nhập tên role và mô tả.
- [ ] Admin có thể lưu role.
- [ ] Role mới sẵn sàng để gán permission và gán user.

**Luồng tạo mới chi tiết**
1. Admin mở Role Management.
2. Admin nhấn **Add Role**.
3. Hệ thống mở form tạo role.
4. Admin nhập metadata của role.
5. Admin lưu role.
6. Hệ thống kiểm tra tính duy nhất và trường bắt buộc.
7. Hệ thống tạo role và quay lại danh sách role.

### US-ADM-06 — Cấu hình phạm vi quản lý
- **Mức ưu tiên:** Critical
- **Trạng thái:** Bản nháp

**User Story**  
Là một **quản trị viên hệ thống**,  
tôi muốn **cấu hình phạm vi quản lý theo product category, project và group**,  
để **user chỉ làm việc với dữ liệu thuộc phạm vi được cấp**.

**Tiêu chí chấp nhận**
- [ ] Admin có thể chọn product categories.
- [ ] Admin có thể chọn projects.
- [ ] Admin có thể chọn groups.
- [ ] Phạm vi được lưu và áp dụng cho role/user đích.

**Luồng tạo mới chi tiết**
1. Admin mở Permission Management.
2. Admin chọn role hoặc đối tượng scope cần cấu hình.
3. Admin vào tab **Management scope**.
4. Admin chọn các product category được phép.
5. Admin chọn các project được phép.
6. Admin chọn các group được phép.
7. Admin lưu cấu hình scope.
8. Hệ thống cập nhật ranh giới truy cập dữ liệu cho role/user đó.

---

### Epic 03 — Quản lý Project & GIS

### US-PRJ-02 — Tạo project
- **Mức ưu tiên:** Critical
- **Trạng thái:** Bản nháp

**User Story**  
Là một **quản trị viên project**,  
tôi muốn **tạo project mới**,  
để **thiết bị và dashboard được quản lý trong một ngữ cảnh rõ ràng**.

**Vấn đề nghiệp vụ**
- Điểm đau hiện tại: thiết bị cần ngữ cảnh project cho scope, GIS và hiển thị dashboard.
- Tại sao quan trọng: project là một trục tổ chức chính trong Device Configuration.
- Giá trị kinh doanh: hỗ trợ vận hành theo phạm vi, cấu hình hiển thị và phân bố bản đồ.

**Tiêu chí chấp nhận**
- [ ] Admin có thể nhập tên project.
- [ ] Admin có thể chọn manager.
- [ ] Admin có thể nhập địa chỉ liên hệ và địa chỉ chi tiết.
- [ ] Admin có thể nhập latitude và longitude.
- [ ] Admin có thể dùng locate in map.
- [ ] Admin có thể chọn GIS map hoặc custom upload nếu có hỗ trợ.
- [ ] Project mới xuất hiện trong cây project sau khi lưu.

**Điều kiện tiên quyết**
- Người dùng có quyền quản lý project.
- Cây project đang khả dụng.

**Luồng tạo mới chi tiết**
1. Người dùng mở `Equipment management > Device configuration > Project`.
2. Người dùng nhấn **Add project**.
3. Hệ thống mở modal tạo project.
4. Người dùng nhập **Project name**.
5. Người dùng chọn **Manager**.
6. Người dùng nhập **Project description** nếu cần.
7. Người dùng nhập **Contact address**.
8. Người dùng nhập **Latitude** và **Longitude** hoặc dùng **Locate in map**.
9. Người dùng chọn **Environmental background** là GIS map hoặc custom upload.
10. Người dùng nhấn **Save**.
11. Hệ thống kiểm tra các trường bắt buộc.
12. Hệ thống tạo bản ghi project.
13. Hệ thống refresh cây project và hiển thị trạng thái thành công.

**Quy tắc kiểm tra**
- Tên project là bắt buộc.
- Tọa độ phải nằm trong khoảng số hợp lệ.
- Manager có thể là bắt buộc tùy cấu hình nghiệp vụ.

**Kết quả thành công**
- Project có thể chọn được trong cây project.
- Project có thể dùng trong form thiết bị và cấu hình scope.

### US-PRJ-04 — Gán thiết bị vào project
- **Mức ưu tiên:** High
- **Trạng thái:** Bản nháp

**User Story**  
Là một **quản trị viên project**,  
tôi muốn **gán thiết bị vào project**,  
để **thiết bị thuộc đúng phạm vi quản lý**.

**Tiêu chí chấp nhận**
- [ ] Project có action **Associated devices**.
- [ ] Người dùng có thể chọn một hoặc nhiều thiết bị.
- [ ] Thiết bị sau khi xác nhận sẽ được liên kết với project đã chọn.

**Luồng tạo mới chi tiết**
1. Người dùng chọn một project trong cây.
2. Người dùng nhấn **Associated devices**.
3. Hệ thống mở bộ chọn thiết bị.
4. Người dùng tìm kiếm và lọc các thiết bị khả dụng.
5. Người dùng chọn các thiết bị cần gán.
6. Người dùng xác nhận thao tác.
7. Hệ thống tạo liên kết project-device.
8. Hệ thống refresh danh sách thiết bị thuộc project.

### US-PRJ-06 — Phân bố thiết bị trên GIS
- **Mức ưu tiên:** High
- **Trạng thái:** Bản nháp

**User Story**  
Là một **GIS operator**,  
tôi muốn **đặt thiết bị lên bản đồ**,  
để **vị trí địa lý của thiết bị được quản lý trực quan**.

**Tiêu chí chấp nhận**
- [ ] Context project/device có action phân bố.
- [ ] Operator có thể gán/cập nhật tọa độ.
- [ ] Tọa độ được lưu sau khi save.

**Luồng tạo mới chi tiết**
1. Người dùng mở context phân bố bản đồ của project hoặc thiết bị.
2. Người dùng chọn một hoặc nhiều thiết bị.
3. Người dùng chọn action phân bố hoặc locate.
4. Người dùng nhấn vị trí mục tiêu trên bản đồ hoặc kéo marker.
5. Người dùng lưu vị trí bản đồ.
6. Hệ thống cập nhật tọa độ.
7. Hệ thống refresh marker trên bản đồ.

---

### Epic 04 — Cấu hình Thiết bị Cốt lõi

### US-DEV-03 — Tạo thiết bị
- **Mức ưu tiên:** Critical
- **Trạng thái:** Bản nháp

**User Story**  
Là một **quản trị viên thiết bị**,  
tôi muốn **thêm thiết bị mới**,  
để **thiết bị được onboard vào nền tảng**.

**Vấn đề nghiệp vụ**
- Điểm đau hiện tại: rules, groups và dashboards phía sau đều phụ thuộc vào bản ghi thiết bị.
- Tại sao quan trọng: tạo thiết bị là hành động nền tảng của vòng đời Equipment Management.
- Giá trị kinh doanh: cho phép onboarding và điều khiển tài sản vật lý.

**Tiêu chí chấp nhận**
- [ ] Hệ thống có action **Add device** trong Type view.
- [ ] Form tạo thay đổi theo category và product.
- [ ] Các trường bắt buộc được kiểm tra trước khi lưu.
- [ ] Thiết bị mới xuất hiện trong danh sách.

**Điều kiện tiên quyết**
- Người dùng có quyền quản lý thiết bị.
- Type list và các category thiết bị đang khả dụng.

**Luồng tạo mới chi tiết**
1. Người dùng mở `Equipment management > Device configuration > Type`.
2. Người dùng chọn category thiết bị từ sidebar trái.
3. Người dùng nhấn **Add device**.
4. Hệ thống mở form tạo thiết bị theo loại đã chọn.
5. Người dùng nhập **Device information**.
6. Người dùng nhập hoặc chỉnh **Product Information** nếu áp dụng.
7. Người dùng nhập hoặc chỉnh **Asset Info** nếu áp dụng.
8. Người dùng nhấn **Save**.
9. Hệ thống kiểm tra tất cả trường bắt buộc và các ràng buộc theo loại.
10. Hệ thống tạo bản ghi thiết bị.
11. Hệ thống quay lại danh sách và hiển thị thiết bị mới.

**Yêu cầu dữ liệu**
- Input: device name, product name, device number, project/group, vị trí, dữ liệu kỹ thuật theo loại.
- Output: bản ghi thiết bị mới, thông báo thành công/thất bại.
- Validation: trường bắt buộc phụ thuộc vào từng loại thiết bị.

### US-DEV-08 — Quản lý Product Information
- **Mức ưu tiên:** Medium
- **Trạng thái:** Bản nháp

**User Story**  
Là một **configurator**,  
tôi muốn **chỉnh các thuộc tính Product Information**,  
để **metadata sản phẩm phù hợp loại thiết bị**.

**Tiêu chí chấp nhận**
- [ ] Product Information có action chỉnh sửa.
- [ ] Người dùng có thể thêm/sửa/xóa thuộc tính sản phẩm.
- [ ] Hỗ trợ kiểu thuộc tính text/image khi UI cho phép.

**Luồng tạo mới chi tiết**
1. Người dùng mở form tạo hoặc sửa thiết bị.
2. Người dùng nhấn **Edit** tại Product Information.
3. Hệ thống mở trình chỉnh thuộc tính sản phẩm.
4. Người dùng thêm dòng mới hoặc xóa dòng cũ.
5. Người dùng chọn kiểu thuộc tính như text hoặc image.
6. Người dùng nhập nội dung cho từng thuộc tính.
7. Người dùng xác nhận cập nhật.
8. Hệ thống lưu cấu hình thuộc tính và quay về form thiết bị.

### US-DEV-09 — Quản lý Asset Info
- **Mức ưu tiên:** Medium
- **Trạng thái:** Bản nháp

**User Story**  
Là một **quản trị viên tài sản**,  
tôi muốn **chỉnh Asset Info**,  
để **dữ liệu vòng đời tài sản được ghi nhận**.

**Tiêu chí chấp nhận**
- [ ] Asset Info có action chỉnh sửa.
- [ ] Hệ thống lưu được manufacturer, price, purchase date, installation date, service life và expiration data nếu có hỗ trợ.

**Luồng tạo mới chi tiết**
1. Người dùng mở form tạo hoặc sửa thiết bị.
2. Người dùng nhấn **Edit** tại Asset Info.
3. Người dùng nhập các trường tài sản.
4. Người dùng xác nhận thay đổi.
5. Hệ thống kiểm tra định dạng và lưu dữ liệu tài sản.

---

### Epic 05 — Quản lý Smart Gateway

### US-GW-02 — Tạo Smart Gateway
- **Mức ưu tiên:** Critical
- **Trạng thái:** Bản nháp

**User Story**  
Là một **quản trị viên gateway**,  
tôi muốn **cấu hình Smart Gateway**,  
để **gateway sẵn sàng quản lý các thiết bị con**.

**Tiêu chí chấp nhận**
- [ ] Form hỗ trợ device name, product name và device number.
- [ ] Form hỗ trợ associated distribution box.
- [ ] Form hỗ trợ associated circuit control.
- [ ] Form hỗ trợ associated electricity meter.
- [ ] Form hỗ trợ project, group, location và altitude.
- [ ] Save thành công khi dữ liệu hợp lệ.

**Điều kiện tiên quyết**
- Người dùng có quyền tạo Smart Gateway.
- Các thiết bị liên kết tồn tại nếu association là bắt buộc.

**Luồng tạo mới chi tiết**
1. Người dùng chọn **Smart Gateway** từ Type sidebar.
2. Người dùng nhấn **Add device**.
3. Hệ thống mở form tạo Smart Gateway.
4. Người dùng nhập **Device name**.
5. Người dùng chọn **Product name**.
6. Người dùng nhập **Device number**.
7. Người dùng chọn **Associated distribution box** nếu áp dụng.
8. Người dùng chọn **Associated circuit control** nếu áp dụng.
9. Người dùng chọn **Electricity meter** nếu áp dụng.
10. Người dùng nhập **Latitude/Longitude** hoặc chọn từ bản đồ.
11. Người dùng nhập **Altitude** nếu cần.
12. Người dùng chọn **Project** và **Belonging group**.
13. Người dùng xem lại **Product Information** và **Asset Info**.
14. Người dùng nhấn **Save**.
15. Hệ thống kiểm tra trường bắt buộc và quy tắc association.
16. Hệ thống tạo gateway.
17. Hệ thống refresh danh sách Smart Gateway.

**Quy tắc kiểm tra**
- Device number là bắt buộc.
- Product selection là bắt buộc.
- Các trường association phải tham chiếu đến bản ghi hợp lệ.
- Tọa độ phải là số nếu được nhập.

### US-GW-03 — Cấu hình gateway circuits
- **Mức ưu tiên:** High
- **Trạng thái:** Bản nháp

**User Story**  
Là một **quản trị viên gateway**,  
tôi muốn **cấu hình gateway circuits và loop mappings**,  
để **các circuit khớp với thiết bị ngoài field và quy tắc thu thập**.

**Tiêu chí chấp nhận**
- [ ] Gateway có action **Configure circuits**.
- [ ] Màn circuit hỗ trợ nhiều dòng.
- [ ] Mỗi dòng hỗ trợ loop control, serial number, associated device, collection settings, phase và display flag.
- [ ] Người dùng có thể thêm/xóa dòng và lưu cấu hình.

**Luồng tạo mới chi tiết**
1. Người dùng mở danh sách Smart Gateway.
2. Người dùng chọn một gateway.
3. Người dùng mở **More > Configure circuits**.
4. Hệ thống mở màn hình cấu hình circuit.
5. Người dùng điền từng dòng loop control.
6. Người dùng chọn associated device và collection attributes.
7. Người dùng đặt phase và display toggle.
8. Người dùng thêm dòng nếu cần.
9. Người dùng lưu cấu hình.
10. Hệ thống kiểm tra tính đầy đủ của từng dòng và quy tắc trùng lặp.
11. Hệ thống lưu mapping circuit.

### US-GW-04 — Đồng bộ gateway
- **Mức ưu tiên:** High
- **Trạng thái:** Bản nháp

**User Story**  
Là một **gateway operator**,  
tôi muốn **đồng bộ gateway với platform**,  
để **cấu hình và trạng thái luôn đồng nhất**.

**Tiêu chí chấp nhận**
- [ ] Gateway có action **Device synchronization**.
- [ ] Người dùng có thể thực thi sync.
- [ ] Hệ thống trả về kết quả sync.

**Luồng tạo mới chi tiết**
1. Người dùng chọn một gateway có sẵn trong danh sách.
2. Người dùng mở **More > Device synchronization**.
3. Hệ thống gửi yêu cầu đồng bộ.
4. Hệ thống trả về thông báo thành công/thất bại.
5. Người dùng xem lại trạng thái sau sync.

---

### Epic 06 — Quản lý Smart Light Controller

### US-LC-02 — Tạo controller theo subtype
- **Mức ưu tiên:** Critical
- **Trạng thái:** Bản nháp

**User Story**  
Là một **quản trị viên chiếu sáng**,  
tôi muốn **tạo Smart Light Controller theo subtype sản phẩm**,  
để **các trường cấu hình theo protocol được ghi nhận đúng**.

**Tiêu chí chấp nhận**
- [ ] Form controller thay đổi theo subtype/product selection.
- [ ] Chỉ hiển thị các trường liên quan subtype đã chọn.
- [ ] Trường bắt buộc theo subtype được kiểm tra trước khi lưu.

**Điều kiện tiên quyết**
- Người dùng có quyền tạo Smart Light Controller.
- Các entity liên quan như light pole, gateway hoặc luminaires tồn tại nếu bắt buộc.

**Luồng tạo mới chi tiết**
1. Người dùng chọn **Smart Light Controller** từ Type sidebar.
2. Người dùng nhấn **Add device**.
3. Hệ thống mở form tạo controller.
4. Người dùng chọn **Product name / subtype**.
5. Hệ thống render các trường riêng theo subtype.
6. Người dùng nhập device name và device number.
7. Người dùng chọn **Gateway** nếu subtype yêu cầu.
8. Người dùng chọn **Light pole** nếu cần.
9. Người dùng mở bộ chọn **Associated luminaires** khi áp dụng.
10. Người dùng chọn project/group/location.
11. Người dùng xem lại Product Information và Asset Info.
12. Người dùng lưu form.
13. Hệ thống kiểm tra các quy tắc theo subtype.
14. Hệ thống tạo controller.

**Quy tắc kiểm tra**
- Trường bắt buộc thay đổi theo subtype.
- Associated luminaire là bắt buộc với subtype điều khiển đèn trực tiếp.
- Gateway chỉ bắt buộc với các subtype hỗ trợ pass-through hay cần gateway.

### US-LC-03 — Gán luminaires cho controller
- **Mức ưu tiên:** High
- **Trạng thái:** Bản nháp

**User Story**  
Là một **quản trị viên chiếu sáng**,  
tôi muốn **gán luminaires cho controller**,  
để **controller điều khiển đúng bộ đèn**.

**Tiêu chí chấp nhận**
- [ ] Form controller có action chọn **Associated luminaires**.
- [ ] Người dùng có thể tìm và chọn luminaires trong selector panel.
- [ ] Kết quả gán hiển thị lại trên form/detail của controller.

**Luồng tạo mới chi tiết**
1. Người dùng mở form tạo/sửa controller.
2. Người dùng nhấn **Associated luminaires**.
3. Hệ thống mở drawer hoặc modal chọn luminaire.
4. Người dùng tìm danh sách luminaire khả dụng.
5. Người dùng chọn một hoặc nhiều luminaire.
6. Người dùng xác nhận lựa chọn.
7. Hệ thống lưu association và quay về form controller.

### US-LC-04 — Thực thi action trên controller
- **Mức ưu tiên:** Medium
- **Trạng thái:** Bản nháp

**User Story**  
Là một **lighting operator**,  
tôi muốn **chạy các action được hỗ trợ của controller**,  
để **vận hành và chẩn đoán controller nhanh hơn**.

**Tiêu chí chấp nhận**
- [ ] Menu ngữ cảnh hiển thị các action phù hợp như Clear, Timing, Local rule enable, Read, Device synchronization, GPS switch khi áp dụng.
- [ ] Action không hỗ trợ sẽ bị ẩn hoặc disable.
- [ ] Hệ thống hiển thị feedback sau khi chạy action.

---

### Epic 07 — Các loại thiết bị khác

### US-POLE-01 — Tạo Lighting Pole
- **Mức ưu tiên:** Medium
- **Trạng thái:** Bản nháp

**User Story**  
Là một **field operator**,  
tôi muốn **tạo bản ghi Lighting Pole**,  
để **các thiết bị được gắn với hạ tầng vật lý ngoài hiện trường**.

**Tiêu chí chấp nhận**
- [ ] Người dùng có thể mở Add device cho Lighting Pole.
- [ ] Form pole hỗ trợ project/group và các trường thiết bị chuẩn.
- [ ] Pole mới xuất hiện trong danh sách Lighting Pole.

**Luồng tạo mới chi tiết**
1. Người dùng chọn **Lighting Pole** trong Type list.
2. Người dùng nhấn **Add device**.
3. Người dùng nhập thông tin định danh pole và project/group.
4. Người dùng lưu form.
5. Hệ thống kiểm tra và tạo pole.

### US-LOOP-01 — Tạo Loop Control
- **Mức ưu tiên:** High
- **Trạng thái:** Bản nháp

**User Story**  
Là một **gateway operator**,  
tôi muốn **tạo bản ghi Loop Control**,  
để **thiết bị loop được cấu hình với thông số kỹ thuật hợp lệ**.

**Tiêu chí chấp nhận**
- [ ] Form loop hỗ trợ gateway, downlink channel, sub-device protocol, project/group và location nếu áp dụng.
- [ ] Hệ thống kiểm tra các ràng buộc kỹ thuật trước khi lưu.

**Luồng tạo mới chi tiết**
1. Người dùng chọn **Loop Control** trong Type list.
2. Người dùng nhấn **Add device**.
3. Hệ thống mở form Loop Control.
4. Người dùng nhập device name, product và device number.
5. Người dùng chọn **Gateway**.
6. Người dùng nhập **Downlink channel**.
7. Người dùng chọn **Sub-device protocol**.
8. Người dùng nhập location/project/group nếu áp dụng.
9. Người dùng lưu form.
10. Hệ thống kiểm tra ràng buộc và tạo bản ghi.

### US-METER-01 — Tạo Smart Electric Meter
- **Mức ưu tiên:** High
- **Trạng thái:** Bản nháp

**User Story**  
Là một **metering operator**,  
tôi muốn **tạo bản ghi Smart Electric Meter**,  
để **dữ liệu đo điện được ghi nhận chính xác**.

**Tiêu chí chấp nhận**
- [ ] Form Smart Electric Meter hỗ trợ associated gateway.
- [ ] Form Smart Electric Meter hỗ trợ meter number và total account number nếu áp dụng.
- [ ] Form Smart Electric Meter hỗ trợ project/group/location.
- [ ] Các trường kỹ thuật được kiểm tra trước khi lưu.

**Luồng tạo mới chi tiết**
1. Người dùng chọn **Smart Electric Meter** trong Type list.
2. Người dùng nhấn **Add device**.
3. Hệ thống mở form Smart Electric Meter.
4. Người dùng nhập thông tin thiết bị và các trường liên quan meter.
5. Người dùng chọn associated gateway.
6. Người dùng nhập project/group/location.
7. Người dùng lưu form.
8. Hệ thống kiểm tra và tạo bản ghi meter.

---

### Epic 08 — Quản lý group & association

### US-GRP-01 — Tạo device group
- **Mức ưu tiên:** High
- **Trạng thái:** Bản nháp

**User Story**  
Là một **quản trị viên vận hành**,  
tôi muốn **tạo group theo product category**,  
để **thiết bị có thể được tổ chức cho các thao tác vận hành**.

**Tiêu chí chấp nhận**
- [ ] Group view hỗ trợ action tạo mới.
- [ ] Có thể nhập các trường riêng theo category.
- [ ] Có hỗ trợ location/frequency khi loại group yêu cầu.

**Luồng tạo mới chi tiết**
1. Người dùng mở `Equipment management > Device configuration > Group`.
2. Người dùng nhấn **Add Group**.
3. Hệ thống mở form tạo group.
4. Người dùng nhập tên group và chọn product category.
5. Người dùng nhập location, frequency hoặc multicast settings nếu áp dụng.
6. Người dùng nhấn **Save** hoặc **Save and associate devices**.
7. Hệ thống kiểm tra trường bắt buộc.
8. Hệ thống tạo group.

### US-GRP-02 — Gán thiết bị vào group
- **Mức ưu tiên:** High
- **Trạng thái:** Bản nháp

**User Story**  
Là một **quản trị viên vận hành**,  
tôi muốn **gán thiết bị vào group**,  
để **các thiết bị có thể được thao tác cùng nhau**.

**Tiêu chí chấp nhận**
- [ ] Flow group có action gán thiết bị.
- [ ] Người dùng có thể chọn một hoặc nhiều thiết bị.
- [ ] Thiết bị sau khi xác nhận sẽ trở thành thành viên của group.

**Luồng tạo mới chi tiết**
1. Người dùng mở group detail hoặc flow save-and-associate.
2. Hệ thống mở bộ chọn thiết bị liên quan.
3. Người dùng tìm thiết bị.
4. Người dùng chọn các thiết bị mục tiêu.
5. Người dùng xác nhận membership.
6. Hệ thống lưu group-device relationships.

### US-GRP-03 — Đồng bộ group hoặc multicast settings
- **Mức ưu tiên:** Medium
- **Trạng thái:** Bản nháp

**User Story**  
Là một **network operator**,  
tôi muốn **đồng bộ cấu hình group xuống thiết bị**,  
để **hành vi multicast hoặc grouped behavior có hiệu lực**.

**Tiêu chí chấp nhận**
- [ ] Hệ thống hỗ trợ đồng bộ sau khi association.
- [ ] Người dùng có thể xem sync results.
- [ ] Người dùng có thể verify hoặc retry khi UI hỗ trợ.
- [ ] Lý do thất bại được hiển thị khi sync lỗi.

---

### Epic 09 — Import / export / recycle bin

### US-BATCH-01 — Import thiết bị hàng loạt
- **Mức ưu tiên:** High
- **Trạng thái:** Bản nháp

**User Story**  
Là một **quản trị viên thiết bị**,  
tôi muốn **import thiết bị theo lô**,  
để **nhiều thiết bị được onboard nhanh hơn**.

**Tiêu chí chấp nhận**
- [ ] Device list có **Batch Import**.
- [ ] Người dùng có thể chọn file import.
- [ ] Hệ thống kiểm tra dữ liệu import.
- [ ] Các record hợp lệ được tạo.
- [ ] Các record không hợp lệ trả về chi tiết lỗi.

**Luồng tạo mới chi tiết**
1. Người dùng mở danh sách thiết bị của một type mục tiêu.
2. Người dùng nhấn **Batch Import**.
3. Hệ thống mở flow import.
4. Người dùng chọn file import.
5. Hệ thống kiểm tra cấu trúc file và nội dung dữ liệu.
6. Hệ thống tạo các bản ghi thiết bị hợp lệ.
7. Hệ thống trả về tổng hợp thành công và lỗi.

---

### Epic 10 — Quản lý rule

### US-RULE-02 — Tạo Platform Rule
- **Mức ưu tiên:** High
- **Trạng thái:** Bản nháp

**User Story**  
Là một **operator**,  
tôi muốn **tạo platform rule theo product category**,  
để **automation trung tâm có thể điều khiển hành vi thiết bị**.

**Tiêu chí chấp nhận**
- [ ] Form rule hỗ trợ name, type, product category, effective date/forever, repeat period, conditions/operations.
- [ ] Người dùng có thể chọn devices to be operated.
- [ ] Rule sau khi lưu xuất hiện trong danh sách.

**Luồng tạo mới chi tiết**
1. Người dùng mở Rule Management.
2. Người dùng nhấn **Add Rule** tại Platform Rules.
3. Hệ thống mở form platform rule.
4. Người dùng nhập metadata của rule.
5. Người dùng thêm một hoặc nhiều trigger conditions.
6. Người dùng thêm một hoặc nhiều execute actions.
7. Người dùng chọn devices to be operated.
8. Người dùng lưu rule.
9. Hệ thống kiểm tra tính đầy đủ của rule.
10. Hệ thống tạo bản ghi rule.

### US-RULE-03 — Tạo Local Rule
- **Mức ưu tiên:** High
- **Trạng thái:** Bản nháp

**User Story**  
Là một **operator**,  
tôi muốn **tạo local rule theo loại thiết bị**,  
để **logic có thể chạy trên thiết bị sau khi đồng bộ**.

**Tiêu chí chấp nhận**
- [ ] Form rule hỗ trợ local rule type và product category.
- [ ] Người dùng có thể định nghĩa trigger conditions và actions.
- [ ] Người dùng có thể chọn target devices.
- [ ] Rule sau khi lưu xuất hiện trong Local Rules list.

**Luồng tạo mới chi tiết**
1. Người dùng mở Local Rules.
2. Người dùng nhấn **Add Local Rule**.
3. Hệ thống mở form local rule.
4. Người dùng nhập metadata của rule.
5. Người dùng thêm trigger conditions như time, sunrise/sunset hoặc sensor threshold.
6. Người dùng thêm execute actions.
7. Người dùng chọn target devices.
8. Người dùng lưu local rule.
9. Hệ thống kiểm tra và tạo rule.

### US-RULE-05 — Tạo Alarm Rule
- **Mức ưu tiên:** High
- **Trạng thái:** Bản nháp

**User Story**  
Là một **operator**,  
tôi muốn **tạo alarm rule cho thiết bị**,  
để **hệ thống cảnh báo cho người dùng khi có bất thường**.

**Tiêu chí chấp nhận**
- [ ] Alarm rule hỗ trợ product/category, effective time, repeat period và trigger conditions.
- [ ] Alarm rule hỗ trợ silence period và hành vi alarm/reminder.
- [ ] Alarm rule hỗ trợ receiving group/notification behavior.

**Luồng tạo mới chi tiết**
1. Người dùng mở Alarm Rules.
2. Người dùng nhấn **Add Rule**.
3. Hệ thống mở form alarm rule.
4. Người dùng nhập metadata cơ bản.
5. Người dùng định nghĩa trigger conditions.
6. Người dùng đặt silence period và hành vi severity.
7. Người dùng gán receiving group và notification behavior.
8. Người dùng lưu rule.
9. Hệ thống kiểm tra và tạo alarm rule.

### US-RULE-06 — Tạo receiving group
- **Mức ưu tiên:** Medium
- **Trạng thái:** Bản nháp

**User Story**  
Là một **operator**,  
tôi muốn **tạo receiving group**,  
để **alert được gửi đúng người nhận**.

**Tiêu chí chấp nhận**
- [ ] Hệ thống cho phép thêm receiving group.
- [ ] Người dùng có thể đặt method/interval/remarks khi hỗ trợ.
- [ ] Group mới có thể chọn trong cấu hình alarm rule.

**Luồng tạo mới chi tiết**
1. Người dùng mở `Rule Management > Other Configurations`.
2. Người dùng chọn khu vực **Receiving Group**.
3. Người dùng nhấn **Add**.
4. Người dùng nhập các trường của receiving group.
5. Người dùng lưu group.
6. Hệ thống kiểm tra và tạo receiving group.

---

### Epic 11 — Dashboard / display information

### US-DASH-01 — Cấu hình Display Information
- **Mức ưu tiên:** Medium
- **Trạng thái:** Bản nháp

**User Story**  
Là một **quản trị viên project**,  
tôi muốn **cấu hình style và modules của dashboard cho project**,  
để **dashboard của project phù hợp nhu cầu giám sát nghiệp vụ**.

**Tiêu chí chấp nhận**
- [ ] Project edit có tab Display Information.
- [ ] Người dùng có thể chọn presentation style và usage scenario.
- [ ] Người dùng có thể bật/tắt modules.
- [ ] Người dùng có thể preview cấu hình.
- [ ] Người dùng có thể save hoặc batch apply nếu UI hỗ trợ.

**Luồng tạo mới chi tiết**
1. Người dùng mở màn chỉnh project.
2. Người dùng vào tab **Display Information**.
3. Người dùng chọn presentation style.
4. Người dùng chọn usage scenario.
5. Người dùng bật/tắt các modules.
6. Người dùng mở cấu hình riêng của module khi cần.
7. Người dùng preview kết quả.
8. Người dùng lưu cấu hình.
9. Hệ thống lưu dashboard settings cho project.

### US-DASH-02 — Cấu hình Lighting schedules today
- **Mức ưu tiên:** Medium
- **Trạng thái:** Bản nháp

**User Story**  
Là một **quản trị viên project**,  
tôi muốn **cấu hình hành vi lịch chiếu sáng**,  
để **điều khiển chiếu sáng hằng ngày được biểu diễn đúng**.

**Tiêu chí chấp nhận**
- [ ] Màn hình schedule hỗ trợ associated sensor.
- [ ] Hỗ trợ on/off thresholds.
- [ ] Hỗ trợ scheduled on/off times.
- [ ] Hỗ trợ sunrise/sunset offset và final time.

**Luồng tạo mới chi tiết**
1. Người dùng mở Display Information.
2. Người dùng mở **Lighting schedules today > Set**.
3. Người dùng chọn sensor hoặc cơ chế lịch.
4. Người dùng nhập threshold hoặc time source.
5. Người dùng đặt sunrise/sunset offset và final time nếu áp dụng.
6. Người dùng lưu cấu hình lịch.

### US-DASH-03 — Cấu hình Electricity Consumption Plan
- **Mức ưu tiên:** Medium
- **Trạng thái:** Bản nháp

**User Story**  
Là một **energy manager**,  
tôi muốn **cấu hình kế hoạch điện năng năm/tháng**,  
để **mức tiêu thụ điện được theo dõi theo mục tiêu**.

**Tiêu chí chấp nhận**
- [ ] Người dùng có thể chọn năm.
- [ ] Người dùng có thể đặt annual planned value và warning ratio.
- [ ] Người dùng có thể cấu hình monthly và daily targets.
- [ ] Người dùng có thể save/reset kế hoạch.

**Luồng tạo mới chi tiết**
1. Người dùng mở Display Information.
2. Người dùng mở **Electricity consumption plan > Set**.
3. Người dùng chọn năm.
4. Người dùng nhập annual plan và warning ratio.
5. Người dùng nhập monthly targets và daily targets nếu cần.
6. Người dùng lưu kế hoạch.
7. Hệ thống lưu giá trị kế hoạch cho reporting và alert logic.

---

## Backlog Story Hỗ trợ

### Xác thực / Truy cập
- Đăng xuất
- Tùy chọn cá nhân

### Quản lý Project & GIS
- Sửa project
- Gỡ thiết bị khỏi project

### Cấu hình Thiết bị
- Tìm kiếm và lọc thiết bị
- Cấu hình cột hiển thị
- Sửa thiết bị

### Gateway / Controller Ops
- Đồng bộ gateway
- Đặt screen password
- Cấu hình three-phase electric ratio
- Xóa gateway local rules
- Chạy action trên controller

### Group / Lifecycle
- Đồng bộ group hoặc multicast settings
- Export thiết bị hàng loạt
- Xóa thiết bị có dependency check
- Khôi phục thiết bị từ recycle bin
- Xóa vĩnh viễn thiết bị

### Rules / Analytics
- Xem running rules
- Đồng bộ local rule xuống thiết bị
- Quản lý alarm levels
- Cấu hình update rules
- Thao tác thiết bị từ operation control
- Xem device detail
- Xem thống kê và xu hướng thiết bị

---

## Ghi chú
- Giả định: các story phản ánh hành vi thấy được trong screenshots/manuals và đã được chuẩn hóa sang ngôn ngữ BA.
- Câu hỏi mở: API entities cuối cùng, regex/range validate cuối cùng, notification channels cuối cùng, schema import/export, và cơ chế retry sync chính xác.