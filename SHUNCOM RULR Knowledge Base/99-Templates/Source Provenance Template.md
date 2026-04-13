# Source Provenance Template

## Mục đích
Dùng block này ở đầu mọi canonical doc để chỉ ra tài liệu đang bám vào nguồn nào và độ tin cậy tới đâu.

---

## Provenance

### Source summary
```yaml
Document status: Draft
Confidence: High  # High / Medium / Low
Last validated: YYYY-MM-DD
Validated by: <name>
Primary source type: screenshot  # screenshot / flow-doc / ba-doc / analysis / kb
Canonical topic: <topic-name>
```

### Primary sources used
| Source            | Path                                                   | Why it matters                      |
| ----------------- | ------------------------------------------------------ | ----------------------------------- |
| Manual screenshot | `manual-images/<image-file>`                           | UI field / layout / action evidence |
| Flow doc          | `docs/shuncom-iot-screen-flows.md`                     | flow behavior                       |
| BA doc            | `docs/shuncom-iot-ba-user-stories.md`                  | business goal                       |
| Traceability map  | `docs/shuncom-iot-story-flow-screen-module-mapping.md` | story-flow-screen mapping           |
| Analysis doc      | `SHUNCOM_RULR_IoT_Platform_Analysis.md`                | system-level interpretation         |

### Evidence notes
- [SRC:IMG-<image-file>] xác nhận trường / nút / tab / màn hình
- [SRC:FLOW-<flow-id>] xác nhận luồng
- [SRC:STORY-<story-id>] xác nhận mục tiêu nghiệp vụ
- [SRC:ANALYSIS-<section>] xác nhận tổng hợp kiến trúc hoặc constraint

### Validation gaps
- <gap 1>
- <gap 2>

### Open questions
- <question 1>
- <question 2>
