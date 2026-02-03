---
title: Glossary & Terminology
tags: [glossary, terminology, reference, shuncom-rulr]
created: 2025-01-23
updated: 2025-01-23
status: final
---

# 📖 Glossary & Terminology

> Definitions of technical terms and acronyms used in SHUNCOM RULR IoT Platform

{% hint style="info" %}
**Platform:** SHUNCOM RULR IoT Platform v1.1 | **Last Updated:** January 2025
{% endhint %}

---

## A

### ABP (Activation by Personalization)
LoRa device activation method where network credentials are pre-programmed into the device. Requires manual configuration of DEVADDR, APPSKEY, and NWKSKEY. Compare with [[#OTAA]].

### Active Energy
Total electrical energy consumed by a device, measured in kWh (kilowatt-hours).

### Active Power
Real power consumed by a device at any moment, measured in Watts (W).

### Alarm Rule
Rule type that monitors device conditions and generates alerts when thresholds are exceeded. See [04-Rule Engine System](../04-Rule-Management/04-Rule%20Engine%20System.md).

### APPEUI (Application EUI)
8-byte unique identifier for LoRa application. Used in OTAA join process.

### APPKEY (Application Key)
16-byte AES encryption key used in LoRa OTAA activation.

### APPSKEY (Application Session Key)
Session key for encrypting LoRa application payload in ABP mode.

---

## B

### Batch Import
Feature to create multiple devices simultaneously by uploading a template file. Maximum 5,000 devices per operation.

### Brightness Level
Light intensity expressed as percentage (0-100%). Also called "dimming level."

---

## C

### CAT.1 (Category 1)
LTE cellular IoT standard providing medium bandwidth connectivity. Used for light controllers requiring direct cloud communication.

### Circuit
Individual electrical loop controlled by a loop controller or gateway.

### Current Transformer Ratio
Multiplier applied to meter readings when using current transformers for high-amperage monitoring.

---

## D

### DEVADDR (Device Address)
4-byte network address assigned to LoRa device in ABP mode.

### DEVEUI (Device EUI)
8-byte globally unique identifier for LoRa devices.

### DEV_PROFILE (Device Profile)
LoRa device configuration profile defining class (A/B/C), data rates, and regional parameters.

### Dimming
Adjusting light brightness to a specific percentage level.

### Downlink Channel
Communication channel from gateway to sub-device. Options typically 1 or 2.

---

## E

### EUI (Extended Unique Identifier)
Globally unique identifier used in LoRa networking (DEVEUI, APPEUI).

---

## F

### Firmware
Software embedded in IoT devices. Can be updated remotely (OTA).

### Fixture
See [[#Lighting Fixture]].

---

## G

### Gateway
Central communication hub connecting sub-devices (light controllers, meters) to the platform. See [[03-Device Management Hub#Smart Gateway]].

### GIS (Geographic Information System)
Map-based visualization system for displaying device locations and status.

### Group
Collection of devices for bulk operations and organization. Types include regular groups, multicast groups, luminaire groups, and loop groups.

---

## H

### Hardware Multicast Group
Device group where commands are broadcast at the hardware level (Zigbee or LoRa), enabling simultaneous control of many devices.

---

## I

### IMEI (International Mobile Equipment Identity)
Unique identifier for cellular devices (NB-IoT, CAT.1 controllers).

### IMSI (International Mobile Subscriber Identity)
Identifier associated with the SIM card in cellular devices.

---

## J

### JWT (JSON Web Token)
Authentication token format used for API authorization.

---

## L

### Light Controller
Device that controls lighting fixtures. Types include Zigbee, LoRa, NB-IoT, and CAT.1 variants.

### Lighting Fixture
The actual light/lamp device. Must be associated with a light controller for control functionality.

### Lighting Pole
Physical structure (pole) that houses lighting devices. Acts as a container for organizational purposes.

### Local Rule
Automation rule stored and executed on the gateway device, enabling offline operation. See [[04-Rule Engine System#Local Rules]].

### Loop Control
Circuit-level control system managed through gateways. Can be built-in (Device #0) or extended (Device #4-255).

### LoRa (Long Range)
Low-power wide-area network (LPWAN) protocol for IoT devices. Supports OTAA and ABP activation.

### LoRaWAN
Network protocol built on LoRa physical layer, managed by LoRa Alliance.

### Luminaire
Technical term for a complete lighting unit (fixture + lamp + housing).

### Luminaire Group
Special group type for dual-way light controllers managing 2 lamps under 1 controller.

---

## M

### MAC Address
Media Access Control address - unique identifier for network interfaces, commonly used for gateway identification.

### Management Scope
User's authorized access boundary - can be organization-wide, project-specific, or group-specific.

### Meter
See [[#Smart Meter]].

### MFA (Multi-Factor Authentication)
Security feature requiring multiple verification methods (password + code).

### Multicast
One-to-many communication where a single command reaches multiple devices simultaneously.

---

## N

### NB-IoT (Narrowband IoT)
Cellular IoT standard optimized for low-power, wide-area applications. Light controllers with NB-IoT communicate directly with the platform without a gateway.

### NWKSKEY (Network Session Key)
Session key for LoRa network layer encryption in ABP mode.

---

## O

### Offline Status
Device state when not communicating with the platform. Local rules continue executing on gateways.

### Online Status
Device state when actively communicating with the platform.

### Organization
Top-level tenant in multi-tenant deployments. Contains users, projects, and devices.

### OTA (Over-The-Air)
Remote firmware update capability.

### OTAA (Over-The-Air Activation)
LoRa device activation method where credentials are negotiated dynamically. More secure than ABP. Requires DEVEUI, APPEUI, and APPKEY.

---

## P

### PAN ID (Personal Area Network ID)
Network identifier for Zigbee networks.

### Pass-through Device
Light controller that communicates through a gateway (e.g., Zigbee controllers).

### Permission
Granular access right (e.g., devices.read, rules.write).

### Platform Rule
Automation rule executed on the cloud platform. Supports complex logic and scheduling. See [[04-Rule Engine System#Platform Rules]].

### Power Distribution Control
Device type for managing electrical distribution cabinets and circuits.

### Power Factor
Ratio of real power to apparent power (0-1). Higher values indicate more efficient power usage.

### Project
Organizational unit for grouping devices and users. Supports hierarchical structure (parent/child projects).

---

## R

### RBAC (Role-Based Access Control)
Authorization model where permissions are assigned to roles, and roles are assigned to users.

### Real-time
Immediate data transmission and display with minimal latency (<1 second).

### Recycle Bin
Temporary storage for deleted devices. Allows recovery of basic configuration (historical data is lost).

### Role
Named collection of permissions assigned to users (e.g., Admin, Operator, Viewer).

### Rule
Automation definition consisting of triggers, conditions, and actions. See [04-Rule Engine System](../04-Rule-Management/04-Rule%20Engine%20System.md).

---

## S

### Screen Password
6-digit numeric PIN for gateway physical display access.

### Severity
Alarm importance level: Critical, Major, Minor, Warning, Info.

### Smart Gateway
See [[#Gateway]].

### Smart Meter
Device for measuring electrical consumption. Typically connects via gateway using Modbus/DLT645 protocols.

### Sub-device
Any device that communicates through a gateway (light controllers, meters, loop controllers).

### Sync (Synchronization)
Process of updating device configuration between platform and physical device.

---

## T

### Three-Phase
Electrical power system with three alternating currents. Gateways and meters can monitor all three phases.

### Time Zone
Regional time setting affecting all scheduled operations. Critical for rule execution timing.

### Trigger
Event or condition that initiates rule execution (time-based, event-based, or condition-based).

---

## U

### Uplink
Communication from device to platform/gateway.

---

## V

### VietQR
Vietnamese QR code payment standard (if payment integration applies).

---

## W

### WebSocket
Bidirectional communication protocol for real-time data updates.

### Widget
Dashboard component displaying specific data or controls.

---

## Z

### Zigbee
Low-power mesh networking protocol. Light controllers use Zigbee to communicate through gateways. Supports multicast groups 1-255.

---

## 📊 Quick Reference Tables

### Protocol Comparison
| Protocol | Gateway Required | Range | Power | Best For |
|----------|-----------------|-------|-------|----------|
| Zigbee | Yes | Short (10-100m) | Very Low | Dense deployments |
| LoRa | Depends | Long (2-15km) | Low | Wide area coverage |
| NB-IoT | No | Cellular | Medium | Urban areas |
| CAT.1 | No | Cellular | Medium | Higher bandwidth needs |

### Device Hierarchy
```
Organization
└── Project
    └── Device Group
        └── Gateway
            ├── Light Controller → Lighting Fixture
            ├── Loop Controller → Circuits
            └── Smart Meter
```

### Rule Type Comparison
| Type | Execution | Offline Support | Use Case |
|------|-----------|-----------------|----------|
| Platform | Cloud | No | Complex scheduling |
| Local | Gateway | Yes | Real-time response |
| Alarm | Cloud | No | Threshold monitoring |

---

## 🔗 Related Documents

- **[01-System Overview](01-System%20Overview.md)**: System architecture
- **[03-Device Management Hub](../03-Device-Management/03-Device%20Management%20Hub.md)**: Device details
- **[04-Rule Engine System](../04-Rule-Management/04-Rule%20Engine%20System.md)**: Rule configuration
- **[Device Types Reference](../Device%20Types%20Reference.md)**: Device specifications
