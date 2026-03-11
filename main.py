import random
import time


class CubeSat:
    def __init__(self, name):
        self.name = name
        self.altitude = 410.0
        self.battery = 100
        self.temperature = 20
        self.signal_strength = "Strong"
        self.orientation = "Stable"

    def update_telemetry(self):
        self.altitude += random.uniform(-1.5, 1.5)
        self.battery -= random.uniform(0.5, 2.0)
        self.temperature += random.uniform(-2.0, 2.0)

        self.altitude = max(380.0, min(450.0, self.altitude))
        self.battery = max(0.0, min(100.0, self.battery))
        self.temperature = max(-20.0, min(50.0, self.temperature))

        signal_options = ["Weak", "Moderate", "Strong"]
        self.signal_strength = random.choice(signal_options)

        self.orientation = "Unstable" if random.random() < 0.15 else "Stable"

    def get_status(self):
        warnings = []

        if self.battery < 20:
            warnings.append("Low Battery")
        if self.temperature > 35:
            warnings.append("High Temperature")
        if self.temperature < -5:
            warnings.append("Low Temperature")
        if self.signal_strength == "Weak":
            warnings.append("Weak Signal")
        if self.orientation == "Unstable":
            warnings.append("Orientation Issue")

        if warnings:
            return "WARNING", warnings
        return "NOMINAL", []

    def display_telemetry(self):
        status, warnings = self.get_status()

        print("\n" + "=" * 45)
        print("        CUBESAT MISSION CONTROL")
        print("=" * 45)
        print(f"Satellite Name   : {self.name}")
        print(f"Altitude         : {self.altitude:.2f} km")
        print(f"Battery          : {self.battery:.1f}%")
        print(f"Temperature      : {self.temperature:.1f} °C")
        print(f"Signal Strength  : {self.signal_strength}")
        print(f"Orientation      : {self.orientation}")
        print(f"System Status    : {status}")

        if warnings:
            print("\nAlerts:")
            for warning in warnings:
                print(f"- {warning}")
        else:
            print("\nAlerts: None")
        print("=" * 45)

    def log_telemetry(self, mission_time):
        with open("telemetry_log.txt", "a") as f:
            f.write(
                f"{mission_time} | Altitude: {self.altitude:.2f} km | "
                f"Battery: {self.battery:.1f}% | Temp: {self.temperature:.1f} C | "
                f"Signal: {self.signal_strength}\n"
            )


def main():
    satellite = CubeSat("NORAH-SAT")

    print("Starting CubeSat Telemetry Simulation...\n")

    mission_seconds = 0

    for cycle in range(10):
        mission_seconds += 5
        minutes = mission_seconds // 60
        seconds = mission_seconds % 60

        print(f"\nMISSION TIME: {minutes:02d}:{seconds:02d}")
        print(f"TELEMETRY CYCLE #{cycle + 1}")

        if cycle in [0, 4, 7]:
            print("\n=== ORBIT PASS DETECTED ===")
            print("Ground Station Link : CONNECTED")
            print("Downlink Status     : ACTIVE")
            print("Receiving telemetry...")

        if cycle == 6:
            print("\n⚠ COMMUNICATION WARNING")
            print("Signal dropout detected")
            print("Attempting reconnection...")

        satellite.update_telemetry()
        satellite.display_telemetry()

        mission_time = f"{minutes:02d}:{seconds:02d}"
        satellite.log_telemetry(mission_time)

        time.sleep(1.5)

    print("\nSimulation complete.")


if __name__ == "__main__":
    main()