# SHUNCOM IoT — Non-Functional Requirements (NFR)

## 1. Mục đích
Tài liệu này mô tả các yêu cầu phi chức năng cấp cao cho SHUNCOM IoT, làm nền cho thiết kế giải pháp và kiểm thử chất lượng hệ thống.

## 2. Hiệu năng
- Hệ thống nên phản hồi nhanh cho các thao tác CRUD và điều hướng danh sách thông thường.
- Device list, project tree, group views, và rule lists phải hỗ trợ dữ liệu ở quy mô vận hành thực tế.
- Các thao tác batch như import/export/sync nên có phản hồi trạng thái rõ ràng.
- Các màn phân tích/chart nên có chiến lược tải dữ liệu theo thời gian lọc.

## 3. Khả năng mở rộng
- Hệ thống phải hỗ trợ tăng số lượng user, thiết bị, project, group, và rules theo thời gian.
- Thiết kế nên tách rõ các module để giảm coupling khi mở rộng.
- Các flow đồng bộ thiết bị nên tách khỏi request-response đồng bộ nếu xử lý kéo dài.

## 4. Bảo mật
- Chỉ user hợp lệ mới được truy cập hệ thống.
- Tất cả dữ liệu phải chịu sự kiểm soát của role và management scope.
- Các action nhạy cảm như delete, permanent delete, sync, rule management phải có permission phù hợp.
- Hệ thống nên có audit/log cho các thao tác nghiệp vụ quan trọng.

## 5. Độ tin cậy
- Hệ thống nên xử lý lỗi validation rõ ràng.
- Các thao tác đồng bộ thiết bị cần hiển thị trạng thái thành công/thất bại.
- Với các thao tác có rủi ro dữ liệu, hệ thống cần cơ chế kiểm tra dependency hoặc confirm.

## 6. Khả năng sử dụng
- UI cần nhất quán giữa các type/device forms.
- Các form tạo mới nên hiển thị trường động theo type/subtype để tránh nhập sai.
- Các selector như project/group/luminaires nên hỗ trợ search khi dữ liệu lớn.

## 7. Khả năng quan sát và audit
- Nên có log cho login, CRUD, rule changes, sync operations, delete/restore actions.
- Kết quả sync nên lưu đủ để operator có thể retry hoặc đối soát.

## 8. Khả năng bảo trì
- Tài liệu BA/flow/module mapping cần được duy trì đồng bộ với thay đổi sản phẩm.
- Thiết kế nên cho phép thêm loại thiết bị mới mà không phải viết lại toàn bộ flow.

## 9. Tính nhất quán dữ liệu
- Xóa thiết bị phải đi kèm dependency check.
- Association giữa device/project/group/rules phải đảm bảo không tạo trạng thái mồ côi ngoài ý muốn.
- Đồng bộ local rule hoặc multicast phải có cơ chế phản hồi kết quả.

## 10. Tài liệu liên quan
- [BRD Overview](./shuncom-iot-brd-overview.md)
- [Business Requirements Document](./shuncom-iot-business-requirements-document.md)
- [Software Requirements Specification](./shuncom-iot-software-requirements-specification.md)

## 11. Ghi chú
- NFR trong tài liệu này là mức định hướng. Các chỉ số đo cụ thể như latency, throughput, concurrency, retention, và SLA cần được chốt thêm với stakeholder và team kỹ thuật.