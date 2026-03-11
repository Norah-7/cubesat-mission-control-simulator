 System Architecture

This project models a simplified CubeSat telemetry pipeline similar to those used in small satellite missions.

The system is divided into three main components:

1. Telemetry Generation
   - The CubeSat simulator produces telemetry parameters such as altitude, battery level, temperature, signal strength, and orientation.

2. Telemetry Packet Protocol
   - Telemetry is formatted into structured packets following a simple satellite-style protocol:

SAT:NORAH-SAT TIME:32 PASS:IN_RANGE LINK:OK TEMP:22.5C BAT:84% STATUS:NOMINAL


3. Mission Control Console
- Telemetry packets are parsed and visualized in a mission control display that highlights satellite health, communication events, and system alerts.

This architecture mirrors the basic workflow of a real satellite ground station:

Satellite Sensors → Telemetry Packet → Ground Station Parser → Mission Control Interface