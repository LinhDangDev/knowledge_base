# Knowledge Base Setup Guide

## Overview
- Purpose: Hướng dẫn dùng và maintain knowledge base SHUNCOM RULR theo trạng thái hiện tại của repo.
- Audience: BA, PM, QA, Dev, Ops, documentation maintainers
- Posture: Guide này mô tả cách dùng cấu trúc KB hiện tại; không giả định Obsidian-only và không giả định có template folder riêng.

## Current documentation model
- VN-first
- Markdown links là chuẩn chính
- 1 chủ đề = 1 canonical doc
- Navigation hub chính là [Map of Content (MOC).md](../Map%20of%20Content%20%28MOC%29.md)
- Supporting docs chỉ tồn tại nếu giúp đọc nhanh hơn mà không tranh canonical source

## Starting points
- [README](../README.md) — điểm vào chính của knowledge base
- [Map of Content (MOC)](../Map%20of%20Content%20%28MOC%29.md) — navigation hub chính
- [01-System Overview](../01-Overview/01-System%20Overview.md) — overview hệ thống
- [Business Requirements Document](../../docs/shuncom-iot-business-requirements-document.md) — business summary
- [Software Requirements Specification](../../docs/shuncom-iot-software-requirements-specification.md) — system requirements

## Folder model
```text
SHUNCOM RULR Knowledge Base/
├── README.md
├── Map of Content (MOC).md
├── 01-Overview/
├── 02-System-Architecture/
├── 03-Device-Management/
├── 04-Rule-Management/
├── 05-User-Management/
├── 06-Project-Management/
├── 07-Dashboard/
└── 08-Development-Guide/
```

## Canonical vs supporting docs
### Canonical docs
- là nguồn chính cho một chủ đề
- được ưu tiên update khi nội dung thay đổi
- không nên có file khác cạnh tranh nội dung cùng chủ đề

### Supporting docs
- dùng để hướng dẫn, quick reference, checklist, best practices
- có thể ngắn gọn hoặc thiên về usage hơn
- không được override canonical topic

## How to add or update a doc
1. Xác định chủ đề đã có canonical doc chưa.
2. Nếu có rồi, cập nhật canonical doc thay vì tạo doc trùng.
3. Nếu cần supporting doc, đảm bảo nó chỉ bổ trợ, không lặp nguyên canonical content.
4. Dùng markdown links cho link thật.
5. Nếu nội dung là docs-derived assumption, phải ghi rõ posture đó trong file.
6. Nếu file ngắn không còn giá trị riêng, merge vào file mạnh hơn rồi xóa.

## Recommended maintenance workflow
### For maintainers
- Bắt đầu từ [Map of Content (MOC)](../Map%20of%20Content%20%28MOC%29.md)
- Sửa trực tiếp canonical doc tương ứng với chủ đề
- Nếu có supporting doc trùng nội dung, merge rồi xóa thay vì giữ link-chain dài

### For domain updates
- Device topic -> [03-Device Management Hub](../03-Device-Management/03-Device%20Management%20Hub.md)
- Rule topic -> [04-Rule Engine System](../04-Rule-Management/04-Rule%20Engine%20System.md)
- Project/GIS topic -> [05-Project Management](../05-User-Management/05-Project%20Management.md), [GIS Setup Guide](../06-Project-Management/GIS%20Setup%20Guide.md)
- Dashboard topic -> [06-Dashboard Interface](../06-Project-Management/06-Dashboard%20Interface.md)
- API topic -> [API Endpoints Map](../02-System-Architecture/API%20Endpoints%20Map.md)

## Tooling notes
- Obsidian vẫn dùng tốt cho local reading.
- GitBook/Honkit cần markdown links ổn định hơn wikilinks.
- Mermaid có thể hữu ích, nhưng không nên là nơi duy nhất chứa thông tin quan trọng.

## What to avoid
- Không tạo duplicate canonical docs.
- Không dùng wikilinks trong doc mới/canonical.
- Không viết contract quá cứng nếu nội dung chỉ là docs-derived working assumption.
- Không giữ file ngắn kiểu râu ria nếu đã merge xong vào file tốt hơn.

## Quick verification checklist
- [ ] Doc nằm đúng folder/domain
- [ ] Nếu là canonical doc: không có file khác cạnh tranh cùng chủ đề
- [ ] Dùng markdown links
- [ ] Không còn placeholder/broken links
- [ ] Có note rõ nếu nội dung chỉ là working assumption

## Related docs
- [Map of Content (MOC)](../Map%20of%20Content%20%28MOC%29.md)
- [README](../README.md)
- [Business Requirements Document](../../docs/shuncom-iot-business-requirements-document.md)
- [Software Requirements Specification](../../docs/shuncom-iot-software-requirements-specification.md)
