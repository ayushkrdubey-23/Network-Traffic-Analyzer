import streamlit as st
import pandas as pd
import plotly.express as px
from streamlit_autorefresh import st_autorefresh

from analyzer import (
    load_data,
    traffic_summary,
    detect_suspicious_packets,
    generate_report
)

# ==========================
# PAGE CONFIGURATION
# ==========================

st.set_page_config(
    page_title="Cyber Network Traffic Monitor",
    page_icon="**",
    layout="wide"
)

# Auto refresh every 5 seconds
st_autorefresh(interval=5000, key="refresh")

# ==========================
# HEADER
# ==========================

st.title("Cyber Network Traffic Analyzer")
st.markdown(
    "### Real-Time Packet Capture, Traffic Analysis & Threat Detection Dashboard"
)

# ==========================
# LOAD DATA
# ==========================

df = load_data()

if df is None:
    st.warning("No packet data found.")
    st.info("Run main.py first to capture packets.")
    st.stop()

# ==========================
# SIDEBAR FILTERS
# ==========================

st.sidebar.title("Filters")

protocol_options = ["ALL"] + sorted(df["protocol"].unique().tolist())

selected_protocol = st.sidebar.selectbox(
    "Protocol",
    protocol_options
)

search_ip = st.sidebar.text_input(
    "Search Source IP"
)

filtered_df = df.copy()

if selected_protocol != "ALL":
    filtered_df = filtered_df[
        filtered_df["protocol"] == selected_protocol
    ]

if search_ip:
    filtered_df = filtered_df[
        filtered_df["source_ip"].astype(str).str.contains(
            search_ip,
            case=False,
            na=False
        )
    ]

if filtered_df.empty:
    st.warning("No packets match the selected filters.")
    st.stop()

# ==========================
# ANALYTICS
# ==========================

summary = traffic_summary(filtered_df)

col1, col2, col3 = st.columns(3)

col1.metric(
    "Total Packets",
    summary["total_packets"]
)

col2.metric(
    "Avg Packet Size",
    f'{summary["average_packet_size"]} Bytes'
)

col3.metric(
    "Largest Packet",
    f'{summary["largest_packet"]} Bytes'
)

st.divider()

# ==========================
# PROTOCOL DISTRIBUTION
# ==========================

st.subheader("Protocol Distribution")

protocol_df = pd.DataFrame(
    list(summary["protocols"].items()),
    columns=["Protocol", "Count"]
)

if not protocol_df.empty:

    fig = px.bar(
        protocol_df,
        x="Protocol",
        y="Count",
        text="Count",
        color="Protocol"
    )

    fig.update_layout(
        height=420,
        xaxis_title="Protocol",
        yaxis_title="Packets"
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )

st.divider()

# ==========================
# TOP IPS
# ==========================

col4, col5 = st.columns(2)

with col4:

    st.subheader("Top Source IPs")

    source_df = pd.DataFrame(
        list(summary["top_sources"].items()),
        columns=["Source IP", "Packets"]
    )

    st.dataframe(
        source_df,
        use_container_width=True
    )

with col5:

    st.subheader("Top Destination IPs")

    destination_df = pd.DataFrame(
        list(summary["top_destinations"].items()),
        columns=["Destination IP", "Packets"]
    )

    st.dataframe(
        destination_df,
        use_container_width=True
    )

st.divider()

# ==========================
# THREAT DETECTION
# ==========================

st.subheader("Threat Detection")

suspicious = detect_suspicious_packets(filtered_df)

if suspicious.empty:

    st.success("No suspicious packets detected.")

else:

    st.error(
        f"{len(suspicious)} Suspicious Packet(s) Detected"
    )

    st.dataframe(
        suspicious,
        use_container_width=True
    )

st.divider()

# ==========================
# PACKET TABLE
# ==========================

st.subheader("Live Captured Packets")

st.dataframe(
    filtered_df,
    use_container_width=True,
    hide_index=True
)

# ==========================
# DOWNLOAD BUTTONS
# ==========================

st.download_button(
    label="Download Packet Logs (CSV)",
    data=filtered_df.to_csv(index=False),
    file_name="packet_logs.csv",
    mime="text/csv"
)

report = generate_report(filtered_df)

st.download_button(
    label="Download Analysis Report",
    data=report,
    file_name="analysis_report.txt",
    mime="text/plain"
)

st.success("Dashboard Updated Successfully")