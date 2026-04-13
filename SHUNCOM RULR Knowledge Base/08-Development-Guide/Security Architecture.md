# Security Architecture

## Overview
- Canonical topic: Security architecture guidance
- Goal: Mô tả security layers, auth/authz posture, audit expectations, và nguyên tắc bảo vệ dữ liệu/thiết bị theo model hiện tại của SHUNCOM RULR.
- Primary users: Dev, architect, QA, PM, security reviewer

## Provenance
### Source summary
```yaml
Document status: Canonical draft
Confidence: Low
Last validated: 2026-04-12
Validated by: Claude Code
Primary source type: kb
Canonical topic: security-architecture
```

### Primary sources used
| Source | Path | Why it matters |
|---|---|---|
| Existing KB doc | `08-Development-Guide/Security Architecture.md` | previous security architecture draft |
| Existing KB doc | `02-System-Architecture/02-Authentication System.md` | auth/access model |
| Existing KB doc | `05-User-Management/Permission Matrices.md` | role/scope model |
| Existing KB doc | `05-User-Management/Role Design Patterns.md` | delegated-permission semantics |
| Analysis doc | `SHUNCOM_RULR_IoT_Platform_Analysis.md` | system architecture context |

### Validation gaps
- Phần lớn nội dung cụ thể về JWT, bcrypt, Redis, KMS, WAF, DDoS, secure boot, v.v. trong version cũ là security design guidance, chưa được verify từ source/deploy hiện tại.
- Vì vậy tài liệu này nên được hiểu là **guidance-only security architecture reference**, không phải implementation contract.

## Scope
### In scope
- Security layer model
- Auth/authz principles
- Data/device security guidance
- Audit and incident-response posture

### Out of scope
- Verified implementation inventory của production
- Exact infrastructure controls đang chạy thật
- Pen-test results / real incident reports

## Guidance posture
- Tài liệu này mô tả **security expectations và recommended architecture**.
- Không nên coi từng control ở đây là đã được implementation đầy đủ nếu chưa kiểm chứng từ source/deploy/config thật.
- Role model bảo mật chuẩn hiện tại gồm: Manufacturer, Project Admin, Project Member.

## Security layers
- Network security
- Application security
- Data security
- Device security
- Audit and incident response

## Authentication and authorization posture
### Authentication
- Hệ thống cần xác thực user trước khi vào các module chính.
- User disabled phải bị chặn login.
- Session/token controls nên được thiết kế an toàn, nhưng chi tiết implementation cần verify riêng.

### Authorization
- Manufacturer: full access toàn hệ thống.
- Project Admin: full access trong managed project scope.
- Project Member: delegated permissions trong project scope.
- Access decision phải luôn kết hợp role + scope.

## Data security guidance
- Dữ liệu nhạy cảm nên có chiến lược bảo vệ phù hợp.
- Audit-sensitive actions cần được log.
- Export/report access cần bám permission boundaries.
- PII/token/secret material không nên xuất hiện trong logs thô.

## Device security guidance
- Device communication nên có authentication/integrity controls phù hợp protocol.
- Các action nhạy cảm như sync/config/control nên có traceability.
- Firmware/device-side controls trong version cũ là architecture suggestions, chưa verified.

## Network and API security guidance
- Protected endpoints cần auth.
- Input validation, rate limiting, và secure headers là các control hợp lý nên có.
- Nhưng exact settings/thresholds/framework choices trong tài liệu cũ không nên xem là production fact nếu chưa verify.

## Audit and compliance posture
- Login, role change, scope change, device control, rule config, project config, export actions đều nên có audit trail.
- Security-sensitive changes by Manufacturer and Project Admin cần dễ truy vết.
- Compliance references trong tài liệu cũ nên hiểu là guidance framework, không phải chứng nhận hiện tại.

## Incident-response posture
- Cần phân loại incident theo severity.
- Cần flow phát hiện, containment, recovery, review.
- Nhưng đây là architectural guidance; runbook cụ thể cần tài liệu riêng khi có infra/source thật.

## Related docs
- [02-Authentication System](../02-System-Architecture/02-Authentication%20System.md)
- [Permission Matrices](../05-User-Management/Permission%20Matrices.md)
- [Role Design Patterns](../05-User-Management/Role%20Design%20Patterns.md)
- [Troubleshooting Guide](Troubleshooting%20Guide.md)
- [Testing Scenarios](Testing%20Scenarios.md)

## Open questions
- Những control nào đang thực sự được triển khai trong code/deploy hiện tại cần verification riêng.
- Nếu cần security contract kỹ thuật chi tiết, nên tách một verified implementation doc sau khi đọc source/deploy configs.
