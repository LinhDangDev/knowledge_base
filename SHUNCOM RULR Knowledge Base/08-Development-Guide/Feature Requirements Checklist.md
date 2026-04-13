# Feature Requirements Checklist

## Overview
Checklist này dùng để cross-check phạm vi tính năng chính của SHUNCOM RULR sau khi chuẩn hóa lại role model, device taxonomy, rules, dashboard, GIS, và docs structure.

## Phase 1 — Authentication and user management
### Standard roles
- [ ] Manufacturer role documented as global all-area/all-permission role
- [ ] Project Admin documented as full control in managed project scope
- [ ] Project Member documented as delegated/configurable by Project Admin
- [ ] Legacy role names removed from canonical docs

### User and scope management
- [ ] User creation flow updated
- [ ] Project-member permission delegation documented
- [ ] Management scope model aligned with project-centric access
- [ ] Auth and security docs aligned to new role model

## Phase 2 — Device support alignment
### Current supported device set
- [ ] Gateway
- [ ] Industrial Controller
- [ ] Smart Light Controller
- [ ] Power Distribution Control (PDC)
- [ ] Weather Sensor
- [ ] Environmental Sensor
- [ ] Smart Electric Meter
- [ ] Lighting Pole
- [ ] Lighting Fixture
- [ ] Loop Control
- [ ] Smart Water Meter
- [ ] Leakage Monitoring
- [ ] Indoor Light Controller
- [ ] Scene Panel
- [ ] Accessory Device

### Device documentation alignment
- [ ] No remaining “7 device categories” wording in canonical docs
- [ ] Device quick reference updated
- [ ] Device schema analysis updated
- [ ] Device config template updated
- [ ] Rules/docs/examples reflect expanded target set where relevant

## Phase 3 — Project, GIS, dashboard
- [ ] Project scope behavior aligned with Project Admin / Project Member model
- [ ] GIS setup guidance aligned with canonical project docs
- [ ] Dashboard docs align with current project/device scope model
- [ ] Lighting schedule and ECP docs remain consistent with current project behavior

## Phase 4 — Rule management
- [ ] Platform rule docs aligned to current device taxonomy
- [ ] Local rule docs aligned to current device taxonomy
- [ ] Alarm docs aligned to current device taxonomy
- [ ] Rule target examples no longer assume old limited device set only

## Phase 5 — Docs layer cleanup
### Canonical vs supporting vs mirror
- [ ] Canonical docs identified clearly
- [ ] Mirror docs removed where duplicated content is already merged
- [ ] Supporting docs no longer compete with canonical docs

### One-part-one-file cleanup
- [ ] Useful content from short `/docs` files merged into stronger docs
- [ ] Short duplicate summary files deleted after merge
- [ ] Navigation updated after deletions
- [ ] No dead links remain to removed files

## Final review checklist
- [ ] Role model consistent across KB and `/docs`
- [ ] Device taxonomy consistent across KB and `/docs`
- [ ] `Accessory Device` spelling normalized
- [ ] Canonical API/schema docs remain the only real source of truth for those topics
- [ ] Supporting/mirror docs clearly marked or removed
- [ ] README / MOC / SUMMARY reflect final structure
