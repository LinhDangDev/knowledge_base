# Troubleshooting Guide

## Overview
- Canonical topic: Troubleshooting and incident response reference
- Goal: Cung cấp guide chẩn đoán cấp cao cho các lỗi thường gặp trong auth, devices, rules, dashboard, performance, và GIS/system-log related operational issues.
- Primary users: Ops, QA, support, Dev, PM

## Provenance
### Source summary
```yaml
Document status: Canonical draft
Confidence: Low
Last validated: 2026-04-12
Validated by: Claude Code
Primary source type: kb
Canonical topic: troubleshooting-guide
```

### Primary sources used
| Source | Path | Why it matters |
|---|---|---|
| Existing KB doc | `08-Development-Guide/Troubleshooting Guide.md` | previous issue library |
| Flow doc | `docs/shuncom-iot-screen-flows.md` | expected behavior of core flows |
| BA doc | `docs/shuncom-iot-ba-user-stories.md` | expected business outcomes |
| Analysis doc | `SHUNCOM_RULR_IoT_Platform_Analysis.md` | module interactions and operational behavior |
| Canonical domain docs | cleaned KB docs | updated domain boundaries and constraints |

### Validation gaps
- Đây là guide chẩn đoán vận hành, không phải incident postmortem archive.
- Root causes và fixes cụ thể trong implementation hiện tại chưa được verify bằng logs/source code thực tế của app.

## Scope
### In scope
- Triage patterns cho auth/device/rule/dashboard/performance/GIS-like issues
- Diagnostic approach
- Root-cause framing
- Resolution verification mindset

### Out of scope
- Runbook production environment chi tiết theo hạ tầng cụ thể
- Incident timeline records per real outage
- Source-code specific fixes cho từng bug hiện hành

## Recommended usage
- Dùng tài liệu này như triage guide đầu tiên.
- Đây là **guidance-only troubleshooting reference**, không phải catalog các fix đã được xác minh trên implementation hiện tại.
- Khi có issue thật, nên tạo record riêng trong incident/debug note hoặc tài liệu vận hành phù hợp.
- Không xem mọi fix trong đây là implementation truth nếu chưa xác nhận bằng logs/source code thực tế.

## Traceability
- Related stories: Auth, Device, Rule, Dashboard, Operations stories from `docs/shuncom-iot-ba-user-stories.md`
- Related flows: Flow 1-25 from `docs/shuncom-iot-screen-flows.md` depending on issue domain
- Related modules: Authentication, Device, Rule, Project, Dashboard, GIS, API inventory

## Core triage flow
1. Xác định domain bị ảnh hưởng: auth / device / rule / dashboard / performance / GIS / logs.
2. Xác định scope ảnh hưởng: single device / single user / project / toàn hệ thống.
3. Thu thập evidence: screenshot, error text, logs, last successful state.
4. So sánh với flow mong đợi trong flow docs/domain docs.
5. Kiểm tra permission/scope trước khi kết luận là bug nghiệp vụ.
6. Xác nhận fix bằng một golden path cụ thể.

## Common issue families
### 1. Authentication issues
| Symptom | Likely directions to check |
|---|---|
| Cannot login | credentials, user state, auth service, scope/role resolution |
| Permission denied | role mapping, function permission, management scope |
| Session expired unexpectedly | token/session model, timeout, clock/timezone issues |

### 2. Device issues
| Symptom | Likely directions to check |
|---|---|
| Device offline | power/network/gateway/communication |
| Controller not controlling lamp | missing fixture association, physical connection, wrong subtype config |
| Gateway not syncing | gateway status, sub-device relation, protocol mismatch, timeout |
| Meter/controller data missing | communication protocol, association, telemetry freshness |

### 3. Rule issues
| Symptom | Likely directions to check |
|---|---|
| Platform rule not firing | timezone, trigger config, target scope, conflicting rule assumptions |
| Local rule not working | sync status, device capability, local storage/firmware support |
| Alarm not generated | threshold/event config, silent period, recipient config |
| Alarm spam | offline threshold too short, silent period too weak |

### 4. Dashboard and GIS issues
| Symptom | Likely directions to check |
|---|---|
| Dashboard empty/stale | scope, API failure, missing data source, realtime delay |
| Map not showing devices | missing coordinates, wrong project context, GIS setup incomplete |
| Device detail incomplete | missing associations / missing historical data / API errors |
| Energy stats look wrong | project display composition, data source mapping, time filter |

### 5. Performance issues
| Symptom | Likely directions to check |
|---|---|
| Slow page load | large dataset, API latency, query/filter volume |
| Browser lag on maps | clustering/viewport loading/many markers |
| High server load | analytics aggregation, bulk operations, realtime volume |

## Diagnostic principles
### Always verify expected behavior first
- So sánh với flow tương ứng trong `docs/shuncom-iot-screen-flows.md`.
- Kiểm tra doc canonical liên quan để biết constraints nghiệp vụ.

### Distinguish 3 classes of problem
1. **Config issue** — setup chưa đúng
2. **Data/state issue** — thiếu association, scope, coordinates, sync result
3. **Implementation issue** — app behavior lệch khỏi expected flow

### High-value checks
- User enabled/disabled state
- Management scope
- Project assignment
- Group association
- Coordinates presence
- Local rule sync status
- Device online/offline state
- Silent period / effective time settings

## Verification after fix
- Golden path hoạt động lại.
- Không phát sinh scope leak hoặc permission regression.
- Log/audit behavior hợp lý.
- Nếu issue liên quan schedule/rules, kiểm tra timezone assumptions.
- Nếu issue liên quan GIS, kiểm tra project context + coordinates.

## Escalation guidance
### Escalate to implementation/code review when
- Config đã đúng nhưng behavior vẫn sai.
- Nhiều project/users/devices cùng bị lỗi.
- Có dấu hiệu contract mismatch giữa docs và app behavior.
- Có data corruption, missing audit trail, hoặc delete/binding inconsistency.

### Evidence to collect before escalation
- steps to reproduce
- affected scope
- screenshot/error text
- last known good behavior
- related story/flow/module

## Related docs
- [02-Authentication System](../02-System-Architecture/02-Authentication%20System.md)
- [03-Device Management Hub](../03-Device-Management/03-Device%20Management%20Hub.md)
- [04-Rule Engine System](../04-Rule-Management/04-Rule%20Engine%20System.md)
- [06-Dashboard Interface](../06-Project-Management/06-Dashboard%20Interface.md)

## Open questions
- Cần thêm runbooks môi trường thật nếu sau này có source về infra/logging/deploy.
- Root-cause/fix recipes cụ thể nên được backfill từ incident thực tế thay vì chỉ giữ ở mức generic guide.
