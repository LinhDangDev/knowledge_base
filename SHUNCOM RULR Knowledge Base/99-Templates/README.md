# Templates Index

Đây là landing page chính cho bộ template chuẩn của SHUNCOM RULR knowledge base.

## Dùng template nào khi nào
### Governance
- [Documentation Standards](Documentation%20Standards.md) — quy chuẩn chung, canonical strategy, section order, review checklist
- [Source Provenance Template](Source%20Provenance%20Template.md) — block nguồn kiểm chứng cho mọi canonical doc

### Structure templates
- [High-Level Module Template](High-Level%20Module%20Template.md) — cho tài liệu module/domain như Device, Rule, Dashboard, GIS, Auth, System Log
- [System Flow Template](System%20Flow%20Template.md) — cho create flow, sync flow, scheduling flow, alarm flow, GIS flow
- [API Constraints Template](API%20Constraints%20Template.md) — cho ràng buộc API/channel đã xác thực
- [System Log and Audit Template](System%20Log%20and%20Audit%20Template.md) — cho event catalog, retention, masking, filtering, audit scope

### Legacy/domain templates đã đồng bộ lại
- [Feature Document Template](Feature%20Document%20Template.md)
- [Device Configuration Template](Device%20Configuration%20Template.md)
- [Rule Configuration Template](Rule%20Configuration%20Template.md)
- [Troubleshooting Template](Troubleshooting%20Template.md)

## Workflow ngắn
1. Chọn canonical topic và kiểm tra chưa có doc canonical trùng.
2. Chọn template phù hợp.
3. Copy block provenance từ [Source Provenance Template](Source%20Provenance%20Template.md).
4. Điền traceability: story, flow, screen, module.
5. Chỉ tạo markdown links cho link thật; placeholder giữ dạng text/code.
6. Ghi open questions nếu còn assumption.

## Nguồn nên đọc trước khi viết doc mới
- `manual-images/`
- `SHUNCOM_RULR_IoT_Platform_Analysis.md`
- `docs/shuncom-iot-screen-flows.md`
- `docs/shuncom-iot-ba-user-stories.md`
- `docs/shuncom-iot-story-flow-screen-module-mapping.md`

## Related navigation
- [Knowledge Base README](../README.md)
- [Map of Content (MOC)](../Map%20of%20Content%20%28MOC%29.md)
