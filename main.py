from sniffer import start_sniffing
from logger import save_packets


def main():

    packets = start_sniffing(20)

    save_packets(packets)

    print("\nCapture completed.")


if __name__ == "__main__":
    main()
    

from analyzer import load_data, generate_report

df = load_data()

if df is not None:
    report = generate_report(df)

    with open("reports/analysis_report.txt", "w") as f:
        f.write(report)