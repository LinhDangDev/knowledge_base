# 📋 Device Configuration Template

> Template for documenting device configuration requirements and specifications

{% hint style="info" %}
**Platform:** SHUNCOM RULR IoT Platform v1.1 | **Last Updated:** January 2025
{% endhint %}


---

## 📝 Template Instructions

**How to use this template:**
1. Copy this template to a new file
2. Replace `{{placeholders}}` with actual values
3. Remove sections not applicable to your device type
4. Add additional sections as needed

---

## 🔧 Device Information

### Basic Details
```yaml
Device Name: {{device_name}}
Device Type: {{device_type}}  # gateway, light_controller, fixture, pole, distribution, loop, meter
Product Name: {{product_name}}
Manufacturer: {{manufacturer}}
Model Number: {{model_number}}
```

### Identification
```yaml
Device Number: {{device_number}}  # MAC, IMEI, or unique identifier
Serial Number: {{serial_number}}
Firmware Version: {{firmware_version}}
Hardware Version: {{hardware_version}}
```

---

## 🔗 Associations

### Parent Associations
```yaml
Associated Gateway: {{gateway_name}}  # Required for sub-devices
Associated Project: {{project_name}}
Associated Group: {{group_name}}
```

### Child/Related Associations
```yaml
Associated Fixture: {{fixture_name}}  # For light controllers
Sub-devices: 
  - {{sub_device_1}}
  - {{sub_device_2}}
```

---

## 📍 Location Information

```yaml
Coordinates:
  Latitude: {{latitude}}
  Longitude: {{longitude}}
Altitude: {{altitude_meters}}m
Address: {{physical_address}}
Installation Location: {{location_description}}
```

---

## ⚙️ Protocol Configuration

### For Zigbee Devices
```yaml
Zigbee Configuration:
  Network Address: {{zigbee_address}}
  Channel: {{zigbee_channel}}
  PAN ID: {{pan_id}}
```

### For LoRa Devices (OTAA)
```yaml
LoRa OTAA Configuration:
  DEVEUI: {{dev_eui}}
  APPEUI: {{app_eui}}
  APPKEY: {{app_key}}
  DEV_PROFILE: {{dev_profile}}
```

### For LoRa Devices (ABP)
```yaml
LoRa ABP Configuration:
  DEVEUI: {{dev_eui}}
  DEVADDR: {{dev_addr}}
  APPSKEY: {{apps_key}}
  NWKSKEY: {{nwks_key}}
```

### For NB-IoT/CAT.1 Devices
```yaml
Cellular Configuration:
  IMEI: {{imei}}
  IMSI: {{imsi}}
  Connected Base Station: {{base_station}}
```

---

## 📊 Monitoring Parameters

### Electrical Parameters
```yaml
Monitored Values:
  - Voltage: Yes/No
  - Current: Yes/No
  - Active Power: Yes/No
  - Power Factor: Yes/No
  - Active Energy: Yes/No
  - Frequency: Yes/No
  
Three-Phase Monitoring:
  Enabled: Yes/No
  Current Transformer Ratio: {{ratio}}
```

### Environmental Parameters
```yaml
Monitored Values:
  - Temperature: Yes/No
  - Humidity: Yes/No
  - Illuminance: Yes/No
  - Color Temperature: Yes/No
```

---

## 🎛️ Control Capabilities

```yaml
Supported Operations:
  - Power On/Off: Yes/No
  - Dimming: Yes/No
  - Color Temperature Adjustment: Yes/No
  - Scheduling: Yes/No
  - Local Rules: Yes/No

Dimming Range:
  Minimum: {{min_brightness}}%
  Maximum: {{max_brightness}}%
  Step: {{brightness_step}}%
```

---

## 🔐 Security Configuration

```yaml
Screen Password: {{6_digit_password}}  # For gateways
Communication Encryption: {{encryption_type}}
Authentication Method: {{auth_method}}
```

---

## 📝 Notes & Special Considerations

```
{{Additional notes about this device configuration}}
{{Special installation requirements}}
{{Known issues or limitations}}
```

---

## ✅ Configuration Checklist

- [ ] Basic device information filled
- [ ] Associations configured
- [ ] Location coordinates set
- [ ] Protocol configuration complete
- [ ] Monitoring parameters verified
- [ ] Control capabilities tested
- [ ] Device synced with platform
- [ ] Appears correctly in device list
- [ ] Control operations working

---

## 🔗 Related Documentation

- **[03-Device Management Hub](../03-Device-Management/03-Device%20Management%20Hub.md)**: Device management guide
- **[Device Types Reference](../Device%20Types%20Reference.md)**: Device type specifications
- **[Troubleshooting Guide](../08-Development-Guide/Troubleshooting%20Guide.md)**: Common issues and solutions
