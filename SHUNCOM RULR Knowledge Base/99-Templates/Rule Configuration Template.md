# 📋 Rule Configuration Template

> Template for documenting automation rules in SHUNCOM RULR IoT Platform

{% hint style="info" %}
**Platform:** SHUNCOM RULR IoT Platform v1.1 | **Last Updated:** January 2025
{% endhint %}


---

## 📝 Template Instructions

**How to use this template:**
1. Copy this template to a new file
2. Replace `{{placeholders}}` with actual values
3. Select appropriate rule type section
4. Remove sections not applicable
5. Add test results after validation

---

## 📋 Rule Overview

### Basic Information
```yaml
Rule Name: {{rule_name}}
Rule Type: {{rule_type}}  # platform, local, alarm
Description: {{rule_description}}
Priority: {{priority_level}}  # 1-10, lower = higher priority
Status: {{status}}  # enabled, disabled
Created By: {{creator_name}}
Created Date: {{creation_date}}
```

---

## ⏰ Trigger Configuration

### Time-based Trigger
```yaml
Trigger Type: time
Schedule:
  Type: {{schedule_type}}  # once, daily, weekly, monthly, custom
  
  # For daily/weekly/monthly:
  Execution Time: {{time_HH:MM}}
  Days: {{days_list}}  # Mon, Tue, Wed, etc.
  
  # For custom:
  Cron Expression: {{cron_expression}}
  
Date Range:
  Start Date: {{start_date}}
  End Date: {{end_date}}  # Optional
  
Timezone: {{timezone}}
```

### Astronomical Trigger
```yaml
Trigger Type: astronomical
Event: {{event_type}}  # sunrise, sunset
Offset: {{offset_minutes}} minutes  # +30, -15, etc.
Location:
  Latitude: {{latitude}}
  Longitude: {{longitude}}
```

### Event-based Trigger
```yaml
Trigger Type: event
Event Source: {{event_source}}  # device, alarm, system
Event Type: {{event_type}}
Event Conditions:
  - Field: {{field_name}}
    Operator: {{operator}}  # equals, greater_than, less_than, contains
    Value: {{value}}
```

### Condition-based Trigger
```yaml
Trigger Type: condition
Conditions:
  - Source: {{source_type}}  # device_metric, environment, time
    Metric: {{metric_name}}
    Operator: {{operator}}
    Value: {{threshold_value}}
    Duration: {{duration_seconds}}  # How long condition must be true
    
Condition Logic: {{logic}}  # and, or
```

---

## 🎯 Target Selection

### Device Targets
```yaml
Target Type: devices
Selection Method: {{method}}  # specific, group, project, all

# For specific devices:
Device IDs:
  - {{device_id_1}}
  - {{device_id_2}}

# For groups:
Group IDs:
  - {{group_id_1}}

# For projects:
Project IDs:
  - {{project_id_1}}

Device Filters:
  Type: {{device_type}}  # Optional filter
  Status: {{device_status}}  # Optional filter
```

---

## ⚡ Action Configuration

### Power Control Action
```yaml
Action Type: power
Operation: {{operation}}  # on, off, toggle
Apply To: {{target_reference}}
```

### Dimming Action
```yaml
Action Type: dim
Brightness: {{brightness_percent}}%
Transition Time: {{transition_seconds}}s  # Optional
Apply To: {{target_reference}}
```

### Multi-Action Sequence
```yaml
Actions:
  - Order: 1
    Type: {{action_type_1}}
    Parameters:
      {{param_1}}: {{value_1}}
    Delay After: {{delay_seconds}}s
    
  - Order: 2
    Type: {{action_type_2}}
    Parameters:
      {{param_2}}: {{value_2}}
```

### Notification Action (for alarm rules)
```yaml
Action Type: notification
Channels:
  - Type: email
    Recipients:
      - {{email_1}}
      - {{email_2}}
    Template: {{template_name}}
    
  - Type: sms
    Recipients:
      - {{phone_1}}
    Template: {{template_name}}
    
  - Type: webhook
    URL: {{webhook_url}}
    Method: POST
    Headers:
      Authorization: {{auth_header}}
```

---

## 🚨 Alarm Configuration (for Alarm Rules)

```yaml
Alarm Settings:
  Severity: {{severity}}  # critical, major, minor, warning, info
  Title Template: {{alarm_title}}
  Message Template: {{alarm_message}}
  
Auto-Recovery:
  Enabled: {{true/false}}
  Recovery Condition: {{recovery_condition}}
  
Notification Delay:
  Initial: {{initial_delay_minutes}} minutes
  Repeat: {{repeat_interval_minutes}} minutes
  Max Notifications: {{max_count}}
```

---

## 🔄 Local Rule Settings (for Local Rules)

```yaml
Local Rule Settings:
  Target Gateway: {{gateway_name}}
  Execution Mode: local  # Executes on gateway, not platform
  
Sync Status:
  Last Synced: {{sync_timestamp}}
  Sync Status: {{status}}  # synced, pending, failed
  
Offline Behavior:
  Execute When Platform Offline: Yes
  Log Execution Locally: Yes
```

---

## 📊 Execution History

| Date | Time | Trigger | Status | Devices Affected | Notes |
|------|------|---------|--------|------------------|-------|
| {{date}} | {{time}} | {{trigger}} | {{status}} | {{count}} | {{notes}} |

---

## ✅ Validation Checklist

### Pre-deployment
- [ ] Rule logic reviewed
- [ ] Target devices verified
- [ ] Trigger timing confirmed
- [ ] Actions tested individually
- [ ] No conflicting rules identified
- [ ] Rollback plan documented

### Post-deployment
- [ ] First execution monitored
- [ ] Expected devices affected
- [ ] Execution time acceptable
- [ ] No unexpected side effects
- [ ] Logging working correctly

---

## 🧪 Test Results

### Test Execution
```yaml
Test Date: {{test_date}}
Test Type: {{manual/automated}}
Tester: {{tester_name}}

Test Scenario:
  Trigger Condition: {{how_triggered}}
  Expected Result: {{expected_outcome}}
  Actual Result: {{actual_outcome}}
  
Test Status: {{pass/fail}}
Notes: {{test_notes}}
```

---

## 📝 Notes & Considerations

```
{{Additional notes about this rule}}
{{Dependencies on other rules or systems}}
{{Known limitations}}
{{Maintenance schedule}}
```

---

## 🔗 Related Documentation

- **[04-Rule Engine System](../04-Rule-Management/04-Rule%20Engine%20System.md)**: Rule system overview
- **[Rule Configuration Patterns](../04-Rule-Management/Rule%20Configuration%20Patterns.md)**: Common rule patterns
- **[Testing Scenarios](../08-Development-Guide/Testing%20Scenarios.md)**: Rule testing procedures
- **[Troubleshooting Guide](../08-Development-Guide/Troubleshooting%20Guide.md)**: Rule execution issues
