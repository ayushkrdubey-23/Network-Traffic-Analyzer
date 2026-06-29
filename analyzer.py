import pandas as pd


CSV_FILE = "data/packet_logs.csv"


def load_data():

    try:
        df = pd.read_csv(CSV_FILE)

        if df.empty:
            return None

        return df

    except Exception as e:
        print(f"Error loading data: {e}")
        return None


def total_packets(df):

    return len(df)


def protocol_distribution(df):

    return df["protocol"].value_counts().to_dict()


def top_source_ips(df, limit=5):

    return (
        df["source_ip"]
        .value_counts()
        .head(limit)
        .to_dict()
    )


def top_destination_ips(df, limit=5):

    return (
        df["destination_ip"]
        .value_counts()
        .head(limit)
        .to_dict()
    )


def average_packet_size(df):

    return round(df["length"].mean(), 2)


def largest_packet(df):

    return int(df["length"].max())


def traffic_summary(df):

    return {
        "total_packets": total_packets(df),
        "average_packet_size": average_packet_size(df),
        "largest_packet": largest_packet(df),
        "protocols": protocol_distribution(df),
        "top_sources": top_source_ips(df),
        "top_destinations": top_destination_ips(df)
    }


def detect_suspicious_packets(df):

    suspicious = df[df["length"] > 1000]

    return suspicious


def generate_report(df):

    summary = traffic_summary(df)

    report = f"""
==============================
NETWORK TRAFFIC ANALYSIS REPORT
==============================

Total Packets : {summary['total_packets']}

Average Packet Size : {summary['average_packet_size']} Bytes

Largest Packet : {summary['largest_packet']} Bytes

Protocol Distribution:
{summary['protocols']}

Top Source IPs:
{summary['top_sources']}

Top Destination IPs:
{summary['top_destinations']}

Potential Suspicious Packets:
{len(detect_suspicious_packets(df))}
"""

    return report