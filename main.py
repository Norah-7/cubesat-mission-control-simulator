import random
import time


class CubeSat:
    def __init__(self, name):
        self.name = name
        self.altitude = 410.0  # km
        self.battery = 100     # percent
        self.temperature = 20  # Celsius
        self.signal_strength = "Strong"
        self.orientation = "Stable"

    def update_telemetry(self):
        # Simulate changes in telemetry values
        self.altitude += random.uniform(-1.5, 1.5)
        self.battery -= random.uniform(0.5, 2.0)
        self.temperature += random.uniform(-2.0, 2.0)

        # Keep values in realistic bounds
        self.altitude = max(380, min(450, self.altitude))
        self.battery = max(0, min(100, self.battery))
        self.temperature = max(-20, min(50, self.temperature))

        # Signal strength based on battery and randomness
        signal_options = ["Weak", "Moderate", "Strong"]
        self.signal_strength = random.choice(signal_options)

        # Orientation occasionally becomes unstable
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


def main():
    satellite = CubeSat("NORAH-SAT")

    print("Starting CubeSat Telemetry Simulation...\n")

    for cycle in range(10):
        print(f"Telemetry Cycle #{cycle + 1}")
        satellite.update_telemetry()
        satellite.display_telemetry()
        time.sleep(1.5)

    print("\nSimulation complete.")


if __name__ == "__main__":
    main()