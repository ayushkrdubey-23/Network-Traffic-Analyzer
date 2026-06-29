from sniffer import start_sniffing

packets = start_sniffing(5)

print("\nCaptured Packets:\n")

for packet in packets:
    print(packet)
    