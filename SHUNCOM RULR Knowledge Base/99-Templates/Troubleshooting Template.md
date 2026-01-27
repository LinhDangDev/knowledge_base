# 📋 Troubleshooting Template

> Template for documenting and resolving common issues in SHUNCOM RULR IoT Platform

**Tags**: #template #troubleshooting #support #documentation  
**Created**: {{date}}  
**Last Updated**: {{date}}

---

## 📝 Template Instructions

**How to use this template:**
1. Copy this template to document a new issue
2. Fill in all observable symptoms
3. Follow diagnostic steps systematically
4. Document the solution for future reference
5. Update knowledge base with findings

---

## 🚨 Issue Summary

### Basic Information
```yaml
Issue ID: {{issue_id}}  # e.g., TSB-001
Issue Title: {{brief_descriptive_title}}
Category: {{category}}  # device, network, rule, user, system
Severity: {{severity}}  # Critical, High, Medium, Low
Status: {{status}}  # New, Investigating, Resolved, Closed
Reported By: {{reporter}}
Reported Date: {{date}}
Environment: {{production/staging/development}}
```

### Problem Statement
```
{{Clear description of what is happening vs what should happen}}
```

---

## 🔍 Symptoms Observed

### Primary Symptoms
- [ ] {{symptom_1}}
- [ ] {{symptom_2}}
- [ ] {{symptom_3}}

### Error Messages
```
{{Exact error message or code displayed}}
```

### Screenshots/Logs
```
{{Paste relevant log entries}}
{{Link to screenshots}}
```

### Frequency & Pattern
```yaml
Occurrence: {{always/intermittent/specific_conditions}}
First Observed: {{datetime}}
Last Observed: {{datetime}}
Frequency: {{every_time/X_times_per_day/random}}
Affected Scope: {{all_users/specific_users/specific_devices}}
```

---

## 🔬 Diagnostic Steps

### Step 1: Verify the Issue
```yaml
Action: {{what_to_check_first}}
Expected Result: {{what_you_should_see}}
Actual Result: {{what_you_observed}}
Conclusion: {{issue_confirmed/not_confirmed}}
```

### Step 2: Gather Information
```yaml
Checklist:
  - [ ] Check device online status
  - [ ] Review recent changes
  - [ ] Check system logs
  - [ ] Verify network connectivity
  - [ ] Check resource utilization
  - [ ] Review error logs

Collected Data:
  Device Status: {{status}}
  Last Successful Operation: {{datetime}}
  Error Log Entries: {{count}}
  Network Status: {{status}}
  System Load: {{cpu/memory/disk}}
```

### Step 3: Isolate the Problem
```yaml
Questions to Answer:
  - Is this affecting one device or multiple?
  - Is this affecting one user or multiple?
  - Did this work before? When did it stop?
  - What changed recently?
  
Isolation Results:
  Scope: {{single/multiple/all}}
  Component: {{frontend/backend/device/network}}
  Timing: {{always/specific_times/after_specific_action}}
```

### Step 4: Identify Root Cause
```yaml
Possible Causes:
  1. {{possible_cause_1}}
     - Evidence for: {{supporting_evidence}}
     - Evidence against: {{contradicting_evidence}}
     
  2. {{possible_cause_2}}
     - Evidence for: {{supporting_evidence}}
     - Evidence against: {{contradicting_evidence}}

Root Cause Identified: {{confirmed_root_cause}}
Confidence Level: {{high/medium/low}}
```

---

## ✅ Solution

### Immediate Fix
```yaml
Action: {{specific_steps_to_fix}}
Expected Outcome: {{what_should_happen}}
Verification: {{how_to_confirm_fix_worked}}
```

### Step-by-Step Resolution
1. {{step_1_action}}
   - Command/Action: `{{command_or_ui_action}}`
   - Expected Result: {{result}}
   
2. {{step_2_action}}
   - Command/Action: `{{command_or_ui_action}}`
   - Expected Result: {{result}}
   
3. {{step_3_action}}
   - Command/Action: `{{command_or_ui_action}}`
   - Expected Result: {{result}}

### Verification Steps
- [ ] {{verification_1}}
- [ ] {{verification_2}}
- [ ] {{verification_3}}

---

## 🛡️ Prevention

### Root Cause Prevention
```yaml
Prevention Measure: {{what_to_do_to_prevent_recurrence}}
Implementation: {{how_to_implement}}
Owner: {{who_is_responsible}}
Target Date: {{when_to_implement}}
```

### Monitoring/Alerting
```yaml
Alert to Add: {{alert_description}}
Trigger Condition: {{when_to_alert}}
Notification: {{who_to_notify}}
```

### Documentation Updates
- [ ] Update [[{{relevant_documentation}}]]
- [ ] Add to known issues list
- [ ] Update FAQ

---

## 📊 Impact Analysis

### Affected Components
```yaml
Components:
  - {{component_1}}: {{impact_description}}
  - {{component_2}}: {{impact_description}}
```

### Affected Users
```yaml
User Impact:
  Users Affected: {{number_or_percentage}}
  User Types: {{admin/operator/viewer}}
  Duration: {{how_long_affected}}
```

### Business Impact
```yaml
Business Impact:
  Severity: {{critical/high/medium/low}}
  Operations Affected: {{list_of_affected_operations}}
  Data Loss: {{yes/no}} - {{details_if_yes}}
  Revenue Impact: {{if_applicable}}
```

---

## 📝 Resolution Notes

### What Worked
```
{{Description of successful resolution approach}}
```

### What Didn't Work
```
{{Approaches tried that didn't resolve the issue - helpful for future reference}}
```

### Lessons Learned
```
{{Key takeaways from this troubleshooting experience}}
```

---

## 📚 Related Issues

### Similar Issues
- **[[{{related_issue_1}}]]**: {{brief_description}}
- **[[{{related_issue_2}}]]**: {{brief_description}}

### Related Documentation
- **[[{{related_doc_1}}]]**: {{why_relevant}}
- **[[{{related_doc_2}}]]**: {{why_relevant}}

---

## 📋 Timeline

| DateTime | Action | Result | By |
|----------|--------|--------|-----|
| {{datetime}} | Issue reported | - | {{reporter}} |
| {{datetime}} | Investigation started | {{initial_findings}} | {{investigator}} |
| {{datetime}} | Root cause identified | {{cause}} | {{investigator}} |
| {{datetime}} | Fix applied | {{outcome}} | {{resolver}} |
| {{datetime}} | Verification complete | {{verified_working}} | {{verifier}} |
| {{datetime}} | Issue closed | - | {{closer}} |

---

## ✅ Resolution Checklist

- [ ] Issue reproduced and understood
- [ ] Root cause identified
- [ ] Fix implemented
- [ ] Fix verified
- [ ] Affected users notified
- [ ] Documentation updated
- [ ] Prevention measures identified
- [ ] Issue closed

---

## 🏷️ Tags for Categorization

```yaml
Issue Type: {{bug/configuration/user_error/external}}
Component: {{device/rule/user/dashboard/api}}
Device Type: {{gateway/controller/fixture/meter}}  # if applicable
Urgency: {{immediate/soon/later}}
Resolution Type: {{code_fix/config_change/user_training/workaround}}
```
