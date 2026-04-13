# Testing Scenarios

## Overview
- Canonical topic: QA scenario inventory
- Goal: Cung cấp bộ test scenarios nghiệp vụ cấp cao cho SHUNCOM RULR, bám theo flows/stories/domain docs. Đây là test inventory/reference, không phải test automation spec cuối cùng.
- Primary users: QA, BA, PM, Dev

## Provenance
### Source summary
```yaml
Document status: Canonical draft
Confidence: Medium
Last validated: 2026-04-12
Validated by: Claude Code
Primary source type: flow-doc
Canonical topic: testing-scenarios
```

### Primary sources used
| Source | Path | Why it matters |
|---|---|---|
| Flow doc | `docs/shuncom-iot-screen-flows.md` | main user flows to validate |
| BA doc | `docs/shuncom-iot-ba-user-stories.md` | user intent and acceptance direction |
| Traceability map | `docs/shuncom-iot-story-flow-screen-module-mapping.md` | module/story/flow coverage |
| Existing KB doc | `08-Development-Guide/Testing Scenarios.md` | prior scenario library |
| Canonical domain docs | supporting KB canonical docs | latest cleaned domain framing |

### Validation gaps
- Đây chưa phải test-case set đã verify với implementation source code hoặc automated tests.
- Coverage percentages và performance targets cũ là guideline, không phải measured reality của codebase hiện tại.

## Scope
### In scope
- Business and system-level test scenarios
- Cross-module QA coverage
- Golden path + edge-case inventory
- Pointers cho permission/scope/error/realtime behavior cần test

### Out of scope
- Playwright/Vitest/Jest test scripts cụ thể
- CI/CD test implementation details
- Measured coverage metrics hiện tại của repo

## Recommended usage
- Dùng tài liệu này để lập test plan và review coverage theo flow/module.
- Đây là **guidance-only QA inventory**, không phải release contract hay proof rằng hệ thống hiện tại đã đáp ứng các behavior bên dưới.
- Nếu cần test automation spec cuối cùng, phải derive từ implementation thực tế.
- Mỗi scenario nên trace được về story/flow/module.

## Coverage map
### Authentication and access
- Login success / invalid credentials / disabled user / permission denial / scope denial

### Project and GIS
- Create project / associate device / GIS placement / display information / schedule / ECP

### Device domain
- Create device by type / associations / controller-fixture / batch import / delete/recycle / command execution

### Rule domain
- Platform rule / local rule / sync result / alarm rule / receiving group / silent period / retry behavior

### Operations and dashboard
- Dashboard load / GIS view / device detail / statistics / alarm handling / system log view

## Scenario design principles
- Cover main scenario trước, rồi mới edge/failure cases.
- Luôn test permission + scope với feature quan trọng.
- Với feature có sync/realtime, phải test delayed/failure/retry path.
- Với analytics/dashboard, phải test context filtering theo project/group/device.

## Scenario groups
### 1. Authentication and user management
| ID | Scenario | Why it matters |
|---|---|---|
| `TC-AUTH-01` | Login với credentials hợp lệ | entrypoint chính |
| `TC-AUTH-02` | Login sai password | auth failure handling |
| `TC-AUTH-03` | User disabled | access-state enforcement |
| `TC-AUTH-04` | Permission denied | RBAC enforcement |
| `TC-AUTH-05` | Scope denied | management-scope enforcement |

### 2. Device lifecycle
| ID | Scenario | Why it matters |
|---|---|---|
| `TC-DEV-01` | Add device by type | onboarding baseline |
| `TC-DEV-02` | Controller with fixture association | lighting control dependency |
| `TC-DEV-03` | Controller without required association | validation/business warning |
| `TC-DEV-04` | Batch import | high-volume onboarding |
| `TC-DEV-05` | Delete/recycle with bindings | integrity protection |
| `TC-DEV-06` | Control offline device | operational edge case |

### 3. Project, GIS, display configuration
| ID | Scenario | Why it matters |
|---|---|---|
| `TC-PRJ-01` | Create project | scope root |
| `TC-PRJ-02` | Associate devices to project | visibility/dashboard dependency |
| `TC-GIS-01` | Place device on map | location flow |
| `TC-GIS-02` | Batch path distribution | map bulk behavior |
| `TC-DASHCFG-01` | Configure display information | project dashboard behavior |
| `TC-SCH-01` | Configure lighting schedule | schedule dependency |
| `TC-ECP-01` | Configure Electricity Consumption Plan (ECP) | energy target logic |

### 4. Rule engine
| ID | Scenario | Why it matters |
|---|---|---|
| `TC-RULE-01` | Create platform rule | central automation |
| `TC-RULE-02` | Create local rule | device-side automation |
| `TC-RULE-03` | Local rule sync success/failure | sync visibility |
| `TC-ALARM-01` | Create alarm rule | monitoring baseline |
| `TC-ALARM-02` | Offline alarm behavior | ops critical path |
| `TC-ALARM-03` | Silent period / auto-handle | spam prevention logic |

### 5. Dashboard and operations
| ID | Scenario | Why it matters |
|---|---|---|
| `TC-DASH-01` | Dashboard loads project stats | top-level ops experience |
| `TC-DASH-02` | GIS map shows device context | location visibility |
| `TC-DASH-03` | Device detail loads sections | ops workflow |
| `TC-DASH-04` | Statistical analysis filters work | analytics validity |
| `TC-OPS-01` | Alarm processing flow | maintenance workflow |
| `TC-LOG-01` | System log filtering | traceability/audit ops |

## Edge-case checklist
- Missing coordinates
- Wrong project scope
- Device offline during command/sync
- Rule conflict / unsupported trigger combination
- Empty dashboard data
- Unassigned project visibility
- Batch import partial failure
- Late or missing realtime updates

## Security and reliability checklist
- Verify invalid credentials are rejected
- Verify scope leakage does not occur
- Verify unauthorized command execution is blocked
- Verify delete with active bindings is blocked or warned
- Verify alarm spam is limited by silent period or similar controls if supported
- Verify audit log is generated for sensitive actions

## Performance posture
Các con số coverage/load/latency từ tài liệu cũ nên xem là QA target ideas, không phải benchmark hiện tại đã verify. Nếu cần performance contract thật, nên chuyển sang tài liệu benchmark/performance đã được đo từ implementation.

## Related docs
- [02-Authentication System](../02-System-Architecture/02-Authentication%20System.md)
- [03-Device Management Hub](../03-Device-Management/03-Device%20Management%20Hub.md)
- [04-Rule Engine System](../04-Rule-Management/04-Rule%20Engine%20System.md)
- [05-Project Management](../05-User-Management/05-Project%20Management.md)
- [06-Dashboard Interface](../06-Project-Management/06-Dashboard%20Interface.md)

## Open questions
- Which scenarios already have automated coverage in the actual codebase is not yet verified.
- Performance/load thresholds cần implementation-based measurement nếu dùng cho release criteria.
