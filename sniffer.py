from scapy.all import sniff, IP
from datetime import datetime


def process_packet(packet):
    """
    Extract useful information from packet
    """

    packet_info = {
        "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "source_ip": "N/A",
        "destination_ip": "N/A",
        "protocol": "Unknown",
        "length": len(packet),
        "payload": ""
    }

    if packet.haslayer(IP):

        packet_info["source_ip"] = packet[IP].src
        packet_info["destination_ip"] = packet[IP].dst

        protocol_number = packet[IP].proto

        protocol_map = {
            1: "ICMP",
            6: "TCP",
            17: "UDP"
        }

        packet_info["protocol"] = protocol_map.get(
            protocol_number,
            str(protocol_number)
        )

    try:
        packet_info["payload"] = bytes(packet.payload).hex()[:100]
    except:
        packet_info["payload"] = "No Payload"

    return packet_info


def start_sniffing(packet_count=20):

    print("\n===== BASIC NETWORK SNIFFER =====")
    print(f"Capturing {packet_count} packets...\n")

    captured_packets = sniff(
        count=packet_count,
        store=True
    )

    results = []

    for packet in captured_packets:
        results.append(process_packet(packet))

    return results
