import pandas as pd

CSV_FILE = "data/packet_logs.csv"


def load_data():

    try:

        df = pd.read_csv(CSV_FILE)

        if len(df) == 0:
            return None

        df["length"] = pd.to_numeric(
            df["length"],
            errors="coerce"
        )

        df = df.dropna()

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