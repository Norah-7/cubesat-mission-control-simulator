import random
import time


class CubeSat:
    def __init__(self, name):
        self.name = name
        self.altitude = 410.0
        self.battery = 100.0
        self.temperature = 20.0
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

    def display_summary(self):
        print(
            f"{self.name:<12} | Battery: {self.battery:5.1f}% | "
            f"Signal: {self.signal_strength:<8} | Status: {self.get_status()[0]}"
        )

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
        with open("telemetry_log.txt", "a", encoding="utf-8") as f:
            f.write(
                f"{mission_time} | {self.name} | "
                f"Altitude: {self.altitude:.2f} km | "
                f"Battery: {self.battery:.1f}% | "
                f"Temp: {self.temperature:.1f} C | "
                f"Signal: {self.signal_strength} | "
                f"Orientation: {self.orientation} | "
                f"Status: {self.get_status()[0]}\n"
            )


def main():
    satellites = [
        CubeSat("NORAH-SAT"),
        CubeSat("KAUST-SAT"),
        CubeSat("ORBIT-1")
    ]

    print("Starting Multi-Satellite Telemetry Simulation...\n")

    with open("telemetry_log.txt", "w", encoding="utf-8") as f:
        f.write("=== CUBESAT TELEMETRY LOG ===\n\n")

    mission_seconds = 0

    for cycle in range(10):
        mission_seconds += 5
        minutes = mission_seconds // 60
        seconds = mission_seconds % 60
        mission_time = f"{minutes:02d}:{seconds:02d}"

        print(f"\nMISSION TIME: {mission_time}")
        print(f"TELEMETRY CYCLE #{cycle + 1}")

        print("\n=== ACTIVE SATELLITES ===")
        for sat in satellites:
            sat.display_summary()

        if cycle in [0, 4, 7]:
            print("\n=== ORBIT PASS DETECTED ===")
            print("Ground Station Link : CONNECTED")
            print("Downlink Status     : ACTIVE")
            print("Receiving telemetry...")

        if cycle == 6:
            print("\n⚠ COMMUNICATION WARNING")
            print("Signal dropout detected")
            print("Attempting reconnection...")

        for sat in satellites:
            sat.update_telemetry()
            sat.display_telemetry()
            sat.log_telemetry(mission_time)

        time.sleep(1.5)

    print("\nSimulation complete.")


if __name__ == "__main__":
    main()