# CubeSat Telemetry & Mission Control Simulator

A Python-based multi-satellite mission control simulator that models CubeSat telemetry transmission, health monitoring, orbit pass events, and communication warnings.

## Features
- Multi-satellite monitoring
- Live telemetry updates
- Mission clock
- Orbit pass detection
- Communication warning simulation
- Telemetry logging to file

## Satellites Simulated
- NORAH-SAT
- KAUST-SAT
- ORBIT-1

## Telemetry Parameters
- Altitude
- Battery level
- Temperature
- Signal strength
- Orientation stability
- System health status

## Example Events
- Orbit pass detected
- Ground station link connected
- Communication signal dropout
- Warning alerts for abnormal conditions

## Files
- `main.py` — main simulation program
- `telemetry_log.txt` — generated telemetry log file

## Purpose
This project was built to simulate a basic satellite mission control environment and demonstrate system monitoring, telemetry handling, and event-based mission operations in Python.