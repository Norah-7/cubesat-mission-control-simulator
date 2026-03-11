import random
import time


def generate_demo_packet():
    mission_time = random.randint(1, 120)
    in_range = (mission_time % 13) < 8

    if not in_range:
        link = "LOST"
        status = "COMMS_LOSS"
    elif mission_time % 17 in [6, 7]:
        link = "DROPOUT"
        status = "SIGNAL_DROP"
    else:
        link = "OK"
        status = "NOMINAL"

    temperature = round(random.uniform(15.0, 25.0), 1)
    battery = random.randint(10, 100)

    if battery < 20 and status == "NOMINAL":
        status = "LOW_BAT"

    pass_state = "IN_RANGE" if in_range else "OUT_OF_RANGE"

    packet = (
        f"SAT:NORAH-SAT "
        f"TIME:{mission_time} "
        f"PASS:{pass_state} "
        f"LINK:{link} "
        f"TEMP:{temperature}C "
        f"BAT:{battery}% "
        f"STATUS:{status}"
    )

    return packet


def parse_packet(packet):
    data = {}

    parts = packet.split()

    for part in parts:
        if ":" in part:
            key, value = part.split(":", 1)
            data[key] = value

    return data


def display_mission_control(data):
    print("\n" + "=" * 55)
    print("              CUBESAT MISSION CONTROL")
    print("=" * 55)
    print(f"Satellite Name   : {data.get('SAT', 'UNKNOWN')}")
    print(f"Mission Time     : {data.get('TIME', 'N/A')} s")
    print(f"Orbit Pass       : {data.get('PASS', 'N/A')}")
    print(f"Link Status      : {data.get('LINK', 'N/A')}")
    print(f"Temperature      : {data.get('TEMP', 'N/A')}")
    print(f"Battery          : {data.get('BAT', 'N/A')}")
    print(f"System Status    : {data.get('STATUS', 'N/A')}")

    print("\nAlerts:")
    status = data.get("STATUS", "N/A")
    link = data.get("LINK", "N/A")

    if status == "LOW_BAT":
        print("- Low Battery Warning")
    elif status == "SIGNAL_DROP":
        print("- Communication Dropout Detected")
    elif status == "COMMS_LOSS":
        print("- Satellite Out of Range / Link Lost")
    elif link == "DROPOUT":
        print("- Link Instability Detected")
    else:
        print("- None")

    print("=" * 55)


def main():
    print("Starting CubeSat Packet Parser Simulation...\n")

    for cycle in range(10):
        packet = generate_demo_packet()

        print(f"\nRAW PACKET #{cycle + 1}")
        print(packet)

        parsed_data = parse_packet(packet)
        display_mission_control(parsed_data)

        time.sleep(1.5)

    print("\nSimulation complete.")


if __name__ == "__main__":
    main()