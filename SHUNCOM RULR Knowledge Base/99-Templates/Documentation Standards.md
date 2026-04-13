# Documentation Standards

## Mục tiêu
Bộ chuẩn này định nghĩa cách viết, kiểm chứng, và duy trì tài liệu cho SHUNCOM RULR IoT Platform knowledge base.

## Nguyên tắc chuẩn
- Viết **VN-first**, giữ nguyên thuật ngữ kỹ thuật tiếng Anh khi cần.
- Dùng **markdown links** làm chuẩn chính.
- Mỗi chủ đề chỉ có **1 canonical document**.
- Mọi nhận định quan trọng phải có **nguồn kiểm chứng**.
- Tài liệu phải đủ cho BA, PM, QA, Dev, và Ops dùng chung.

## Thứ tự nguồn ưu tiên
1. Manual PDF gốc hoặc bản trích xuất đáng tin cậy
2. `manual-images/` screenshots
3. `SHUNCOM_RULR_IoT_Platform_Analysis.md`
4. `docs/shuncom-iot-screen-flows.md`
5. `docs/shuncom-iot-ba-user-stories.md`
6. `docs/shuncom-iot-story-flow-screen-module-mapping.md`
7. Knowledge base markdown hiện có

## Bắt buộc cho mọi canonical doc
### 1. Provenance
Mỗi tài liệu chuẩn phải có:
- nguồn chính đã dùng
- loại bằng chứng: screenshot / flow / BA doc / analysis / KB
- confidence: High / Medium / Low
- ngày kiểm chứng gần nhất
- open validation items

### 2. Traceability
Nếu là tài liệu nghiệp vụ hoặc hệ thống, phải map được tới một hoặc nhiều mục sau:
- Story ID
- Flow ID
- Screen / Context
- Module / Domain
- API / Constraint ID nếu có

### 3. Open questions
Nếu còn giả định hoặc chưa xác nhận, phải ghi rõ ở cuối tài liệu. Không được ngầm xem là đã xác thực.

## Canonical doc types
### Overview doc
Dùng cho: overview hệ thống, capability map, scope, kiến trúc cấp cao.

Bắt buộc có:
- Overview
- Scope
- Actors / Modules
- Constraints cấp cao
- Related docs
- Provenance
- Open questions

### Module doc
Dùng cho: Project, Device, Rule, Dashboard, GIS, Auth, Operations, System Log.

Bắt buộc có:
- Module overview
- Business responsibilities
- Actors
- Main screens / contexts
- Related stories and flows
- Business constraints
- Data / API touchpoints
- Logging / audit implications
- Provenance
- Open questions

### Flow doc
Dùng cho: create flows, sync flows, scheduling flows, alarm handling, GIS distribution.

Bắt buộc có:
- Trigger
- Preconditions
- Main flow
- Alternate flows
- Failure flows
- Validations
- Result states
- APIs / logs touched
- Provenance
- Open questions

### API constraints doc
Dùng để mô tả **ràng buộc đã xác nhận**, không bịa endpoint behavior chưa kiểm chứng.

Bắt buộc có:
- Endpoint / Channel
- Purpose
- Auth / Scope
- Request fields
- Validation rules
- Business constraints
- Side effects
- Error model
- Logging / realtime implications
- Provenance
- Confidence

### Troubleshooting doc
Bắt buộc có:
- symptom
- affected scope
- evidence
- diagnostic steps
- root cause hypothesis
- confirmed fix
- verification
- prevention
- related docs

## Canonical topic map
- System overview -> `01-Overview/01-System Overview.md`
- Authentication and access -> `02-System-Architecture/02-Authentication System.md`
- Device domain -> `03-Device-Management/03-Device Management Hub.md`
- Rule domain -> `04-Rule-Management/04-Rule Engine System.md`
- Project domain -> `05-User-Management/05-Project Management.md`
- Dashboard domain -> `06-Project-Management/06-Dashboard Interface.md`
- API reference -> `02-System-Architecture/API Endpoints Map.md`
- Data schema -> `02-System-Architecture/Database Schema.md`

## Section order standard
Khuyến nghị thứ tự section cho doc canonical:
1. Title
2. Overview
3. Provenance
4. Scope / Responsibility
5. Traceability
6. Main content
7. Constraints / Edge cases
8. Related docs
9. Open questions

## Link standard
- Dùng markdown links tương đối: `[Tên tài liệu](../path/file.md)`
- Tránh dùng `[[wikilinks]]` trong canonical docs mới.
- Nếu tài liệu cũ còn wikilinks, thay dần khi có chỉnh sửa.

## Diagram standard
- Ưu tiên markdown thường, bảng, checklist.
- Mermaid chỉ dùng khi nội dung vẫn hiểu được nếu GitBook/Honkit không render đúng.
- Không để diagram là nguồn duy nhất chứa thông tin quan trọng.

## Update workflow
1. Xác định canonical doc cần sửa
2. Đọc lại nguồn kiểm chứng
3. Cập nhật Provenance
4. Cập nhật nội dung
5. Kiểm tra links và traceability
6. Ghi open questions nếu còn giả định

## Review checklist
- [ ] Có provenance
- [ ] Có confidence level
- [ ] Có traceability phù hợp
- [ ] Chỉ dùng markdown links cho links thật; placeholder phải để dạng text/code, không tạo link gãy
- [ ] Không trùng canonical topic
- [ ] Có open questions nếu cần
- [ ] Nội dung bám nguồn kiểm chứng
