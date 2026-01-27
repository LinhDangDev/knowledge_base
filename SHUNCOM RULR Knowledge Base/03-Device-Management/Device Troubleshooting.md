---
title: Device Troubleshooting Guide
tags: [troubleshooting, devices, support, operations]
created: 2025-01-23
updated: 2025-01-23
status: final
---

# 🔧 Device Troubleshooting Guide

> Detailed troubleshooting procedures for all device types in SHUNCOM RULR

---

## 📋 Quick Diagnosis Matrix

| Symptom | Likely Cause | First Check | Reference |
|---------|--------------|-------------|-----------|
| Device offline | Network/power | Physical connection | [[#Offline Issues]] |
| No control response | Association missing | Fixture linked? | [[#Control Issues]] |
| Wrong readings | Configuration | Transformer ratio | [[#Data Issues]] |
| Sync failed | Gateway issue | Gateway online? | [[#Sync Issues]] |
| Commands delayed | Network congestion | Signal strength | [[#Performance Issues]] |

---

## 🚨 Offline Issues

### Gateway Offline

**Symptoms:**
- Gateway shows "Offline" status
- All sub-devices show offline
- No data updates

**Diagnostic Steps:**

```yaml
Step 1 - Physical Check:
  Action: Verify gateway hardware
  Check:
    - Power LED on?
    - Network LED active?
    - Error LEDs?
  
Step 2 - Network Check:
  Action: Verify network connectivity
  Check:
    - Ethernet cable connected?
    - IP address assigned?
    - Can ping gateway from network?
    - Firewall blocking ports?
    
Step 3 - Platform Check:
  Action: Verify platform configuration
  Check:
    - Correct MAC address in platform?
    - Gateway enabled?
    - Associated project correct?
```

**Solutions:**

| Cause | Solution |
|-------|----------|
| Power failure | Check power supply, circuit breaker |
| Network cable | Replace ethernet cable |
| IP conflict | Assign static IP or fix DHCP |
| Firewall | Open required ports (MQTT: 8883, HTTP: 443) |
| Configuration | Verify MAC address, re-add if needed |

**Verification:**
- Gateway status changes to "Online"
- Sub-devices begin reporting
- Real-time data updates

---

### Light Controller Offline (Zigbee)

**Symptoms:**
- Individual controller offline
- Gateway is online
- Other Zigbee devices working

**Diagnostic Steps:**

```yaml
Step 1 - Distance Check:
  - Is device within Zigbee range of gateway?
  - Are there obstacles blocking signal?
  - Any new sources of interference?

Step 2 - Power Check:
  - Device powered on?
  - Wiring intact?
  
Step 3 - Network Check:
  - Device address correct?
  - Device in Zigbee network?
  - Try re-joining network
```

**Solutions:**

| Cause | Solution |
|-------|----------|
| Out of range | Add Zigbee repeater or move gateway |
| Interference | Change Zigbee channel, remove interference source |
| Power issue | Check wiring, replace device if faulty |
| Network issue | Reset device, re-join network |

---

### Light Controller Offline (NB-IoT/CAT.1)

**Symptoms:**
- Cellular controller offline
- No gateway dependency
- Signal strength unknown

**Diagnostic Steps:**

```yaml
Step 1 - SIM Check:
  - SIM card inserted correctly?
  - SIM activated and has data?
  - Account not suspended?
  
Step 2 - Signal Check:
  - Location has cellular coverage?
  - Antenna connected?
  - Signal strength adequate?
  
Step 3 - Configuration Check:
  - APN settings correct?
  - Device registered to platform?
  - IMEI matches configuration?
```

**Solutions:**

| Cause | Solution |
|-------|----------|
| SIM issue | Check SIM, contact carrier |
| No coverage | Relocate device, use external antenna |
| Wrong APN | Update APN settings |
| Registration | Re-register device on platform |

---

### Light Controller Offline (LoRa)

**Symptoms:**
- LoRa controller offline
- Join attempts failing
- No uplink messages

**OTAA Troubleshooting:**

```yaml
Check Parameters:
  DEVEUI: Must be unique, match device
  APPEUI: Must match LoRa server application
  APPKEY: Must match exactly (case-sensitive)
  
Common Issues:
  - Key mismatch (most common)
  - Device already activated with different keys
  - Frequency band mismatch
  - Gateway not receiving join requests
```

**ABP Troubleshooting:**

```yaml
Check Parameters:
  DEVADDR: Must be unique in network
  APPSKEY: Must match server
  NWKSKEY: Must match server
  
Common Issues:
  - Frame counter desync (reset device or server)
  - Key entry errors
  - Session expired
```

**Solutions:**

| Issue | OTAA Solution | ABP Solution |
|-------|---------------|--------------|
| Key mismatch | Regenerate keys, update both sides | Re-enter keys carefully |
| Frame counter | N/A | Reset counter on server |
| Already joined | Delete and re-add device | Reset device |
| No gateway | Check LoRa gateway status | Same |

---

## 🎮 Control Issues

### Lamp Not Responding to Commands

**Symptoms:**
- Device online
- Commands sent successfully
- Lamp doesn't change state

**Critical Check: Fixture Association**

```yaml
MOST COMMON CAUSE: Missing fixture association

Verification:
  1. Go to Device Configuration
  2. Find the light controller
  3. Check "Associated Luminaire" field
  
If Empty:
  - Lamp is UNCONTROLLABLE
  - Platform shows warning
  - Control buttons may be disabled
  
Fix:
  1. Create lighting fixture if not exists
  2. Edit light controller
  3. Select fixture in association field
  4. Save
  5. Retry control command
```

**Other Causes:**

| Cause | Symptom | Solution |
|-------|---------|----------|
| Wiring issue | Physical disconnect | Check wiring |
| Lamp burned out | No light despite status | Replace lamp |
| Driver failure | Lamp malfunction | Replace driver |
| Wrong command | Unexpected behavior | Verify command parameters |

---

### Dimming Not Working

**Symptoms:**
- On/off works
- Dimming has no effect
- Brightness always 100% or 0%

**Diagnostic Steps:**

```yaml
1. Device Capability:
   - Does device support dimming?
   - Check product specifications
   
2. Lamp Compatibility:
   - Is lamp dimmable?
   - LED driver supports dimming?
   
3. Configuration:
   - Dimming range configured correctly?
   - Minimum brightness set too high?
   
4. Protocol:
   - Dimming command format correct?
   - Controller firmware supports dimming?
```

**Solutions:**

| Cause | Solution |
|-------|----------|
| Non-dimmable lamp | Replace with dimmable lamp |
| Non-dimmable driver | Replace LED driver |
| Configuration | Adjust dimming range (0-100%) |
| Firmware | Update controller firmware |

---

### Group Control Not Working

**Symptoms:**
- Individual control works
- Group commands fail
- Only some devices respond

**For Regular Groups:**
```yaml
Check:
  - All devices in group?
  - All devices online?
  - Permissions for group?
  
Fix:
  - Verify group membership
  - Bring offline devices online
  - Check user permissions
```

**For Zigbee Multicast:**
```yaml
Check:
  - Multicast group number assigned?
  - All devices synced?
  - Sync status successful?
  
Fix:
  - Verify group number (1-255)
  - Re-sync failed devices
  - Check Zigbee network health
```

**For LoRa Multicast:**
```yaml
Check:
  - Group number valid? (1, 2, or 3)
  - Frequency band correct?
  - Devices in receive window?
  
Fix:
  - Use valid group numbers
  - Align frequency settings
  - Time multicast appropriately
```

---

## 📊 Data Issues

### Incorrect Power Readings

**Symptoms:**
- Voltage/current/power values seem wrong
- Values too high or too low
- Negative readings

**Diagnostic Steps:**

```yaml
1. Transformer Ratio:
   - Using current transformers?
   - Ratio configured in platform?
   
2. Phase Configuration:
   - Single-phase or three-phase?
   - Correct phase selected?
   
3. Physical Measurement:
   - Compare with handheld meter
   - Check CT installation
```

**Solutions:**

| Issue | Solution |
|-------|----------|
| Missing CT ratio | Configure transformer ratio in device settings |
| Wrong phase | Select correct phase configuration |
| CT backwards | Reverse CT orientation |
| Calibration | Factory calibration may be needed |

---

### Missing Metrics Data

**Symptoms:**
- Device online
- Some metrics missing
- Gaps in historical data

**Causes & Solutions:**

| Cause | Solution |
|-------|----------|
| Collection disabled | Enable metric collection in settings |
| Network gaps | Check connectivity, review offline periods |
| Storage issue | Check database, retention policy |
| Wrong device type | Verify product supports these metrics |

---

### Stale Data / Not Updating

**Symptoms:**
- Data doesn't refresh
- Same values for long time
- "Last updated" is old

**Solutions:**

```yaml
1. Force Read:
   - Use "Read Data" operation
   - Check if new data appears
   
2. Check Collection Interval:
   - Default: Every minute
   - Can be configured per device type
   
3. Communication Check:
   - Gateway communication working?
   - Device responding to queries?
   
4. Browser Issue:
   - Hard refresh page (Ctrl+F5)
   - Check WebSocket connection
```

---

## 🔄 Sync Issues

### Gateway Sync Failed

**Symptoms:**
- "Sync" operation fails
- Sub-devices not appearing
- Configuration not applied

**Diagnostic Steps:**

```yaml
1. Gateway Status:
   - Gateway online?
   - Last communication time?
   
2. Network Quality:
   - Latency acceptable?
   - Packet loss?
   
3. Payload Size:
   - Too many devices?
   - Try smaller batches
   
4. Gateway Resources:
   - Memory available?
   - Storage space?
```

**Solutions:**

| Issue | Solution |
|-------|----------|
| Gateway offline | Resolve connectivity first |
| Timeout | Retry sync, try smaller batches |
| Memory full | Clear old data, restart gateway |
| Version mismatch | Update gateway firmware |

---

### Local Rule Sync Failed

**Symptoms:**
- Local rule created
- Sync to gateway fails
- Rule not executing offline

**Solutions:**

```yaml
1. Gateway Compatibility:
   - Gateway supports local rules?
   - Firmware version adequate?
   
2. Rule Complexity:
   - Rule too complex for gateway?
   - Simplify if needed
   
3. Storage:
   - Gateway rule storage full?
   - Clear old rules
   
4. Retry:
   - Network issue?
   - Retry sync operation
```

---

## ⚡ Performance Issues

### Slow Command Response

**Symptoms:**
- Commands take long to execute
- Visible delay in control
- Timeouts on operations

**Diagnostic Matrix:**

| Protocol | Normal Latency | Slow If > |
|----------|----------------|-----------|
| Zigbee | < 500ms | 2 seconds |
| LoRa | 1-5 seconds | 30 seconds |
| NB-IoT | < 2 seconds | 10 seconds |
| CAT.1 | < 1 second | 5 seconds |

**Solutions:**

| Cause | Solution |
|-------|----------|
| Network congestion | Reduce traffic, check bandwidth |
| Gateway overloaded | Distribute devices across gateways |
| Poor signal | Improve antenna, reduce distance |
| Platform load | Check server resources |

---

### High Device Offline Rate

**Symptoms:**
- Many devices frequently offline
- Random offline patterns
- Brief offline periods

**Investigation:**

```yaml
Pattern Analysis:
  - All at once? → Network/gateway issue
  - Same time daily? → Scheduled interference
  - Random? → Power quality or signal issues
  
Environmental Factors:
  - New construction nearby?
  - New equipment installed?
  - Weather related?
```

**Solutions:**

| Pattern | Likely Cause | Solution |
|---------|--------------|----------|
| All devices | Gateway/network | Fix gateway or network |
| Cluster of devices | Local interference | Investigate that area |
| Random single | Individual device | Check specific device |
| Time-based | External factor | Identify and mitigate |

---

## 📱 Protocol-Specific Guides

### Zigbee Protocol Guide

```yaml
Network Parameters:
  Channel: 11-26 (check for interference)
  PAN ID: Unique per network
  Device Limit: ~65,000 per network
  Practical Limit: ~500 per gateway

Best Practices:
  - Use mesh topology (devices relay)
  - Avoid Wi-Fi channel overlap (1, 6, 11)
  - Place gateway centrally
  - Use powered devices as repeaters
```

### LoRa Protocol Guide

```yaml
Network Parameters:
  Frequency: Region-specific (AS923, EU868, US915)
  Spreading Factor: SF7-SF12 (trade range vs speed)
  Bandwidth: 125kHz typical
  
OTAA vs ABP:
  OTAA: More secure, recommended
  ABP: Simpler, requires careful counter management
  
Best Practices:
  - Prefer OTAA for security
  - Reset frame counters carefully
  - Use appropriate SF for distance
  - Account for duty cycle limits
```

### NB-IoT/CAT.1 Guide

```yaml
Connectivity:
  - Requires active SIM
  - APN configuration critical
  - May need to configure bands
  
Troubleshooting SIM:
  - Verify SIM not locked
  - Check data plan active
  - Confirm APN settings
  - Test SIM in another device
```

---

## 🔗 Related Documentation

- **[[03-Device Management Hub]]**: Device configuration
- **[[Device Types Reference]]**: Device specifications
- **[[Troubleshooting Guide]]**: General troubleshooting
- **[[Glossary]]**: Technical terms
