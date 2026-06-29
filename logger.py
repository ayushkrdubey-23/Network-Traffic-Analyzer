import csv
import os


CSV_FILE = "data/packet_logs.csv"


def initialize_csv():

    if not os.path.exists(CSV_FILE):

        with open(CSV_FILE, "w", newline="", encoding="utf-8") as file:

            writer = csv.writer(file)

            writer.writerow([
                "timestamp",
                "source_ip",
                "destination_ip",
                "protocol",
                "length",
                "payload"
            ])


def save_packets(packet_list):

    initialize_csv()

    with open(CSV_FILE, "a", newline="", encoding="utf-8") as file:

        writer = csv.writer(file)

        for packet in packet_list:

            writer.writerow([
                packet["timestamp"],
                packet["source_ip"],
                packet["destination_ip"],
                packet["protocol"],
                packet["length"],
                packet["payload"]
            ])

    print(f"\n{len(packet_list)} packets saved successfully.")