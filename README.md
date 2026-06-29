# 🌐 Network Traffic Analyzer
> **A Python-based Network Traffic Analyzer that captures, analyzes, and visualizes network packets through an interactive Streamlit dashboard.**
# 📌 Project Overview

The **Network Traffic Analyzer** is a cybersecurity project developed using **Python** to monitor and analyze network packets in real time. The application captures packets using **Scapy**, stores them in CSV format, performs protocol analysis, detects suspicious traffic based on predefined rules, and visualizes all collected information through an interactive **Streamlit Dashboard**.

This project was completed as part of the **CodeAlpha Cyber Security Internship**.

---

# 🎯 Objectives

- Capture live network packets
- Analyze packet information
- Identify network protocols
- Display packet statistics
- Detect suspicious packets
- Visualize traffic using charts
- Export packet logs and reports

---

# 🚀 Features

✅ Live Packet Capture

✅ Packet Analysis

✅ Source & Destination IP Detection

✅ TCP / UDP / ICMP Protocol Identification

✅ Payload Preview

✅ CSV Packet Logging

✅ Interactive Streamlit Dashboard

✅ Protocol Distribution Charts

✅ Top Source IP Analysis

✅ Top Destination IP Analysis

✅ Average Packet Size

✅ Largest Packet Detection

✅ Packet Filtering

✅ Suspicious Packet Detection

✅ Download Packet Logs

✅ Generate Network Analysis Report

---

# 🛠️ Technologies Used

- Python
- Scapy
- Streamlit
- Pandas
- Plotly
- CSV
- Streamlit Auto Refresh

---

# 📂 Project Structure

```
Network-Traffic-Analyzer/
│
├── assets/
│
├── data/
│   └── packet_logs.csv
│
├── reports/
│   └── analysis_report.txt
│
├── analyzer.py
├── dashboard.py
├── logger.py
├── main.py
├── sniffer.py
├── test_analyzer.py
├── test_sniffer.py
├── requirements.txt
├── README.md
```

---

# ⚙️ Installation

## Clone Repository

```bash
git clone https://github.com/your-username/Network-Traffic-Analyzer.git
```

```bash
cd Network-Traffic-Analyzer
```

---

## Install Dependencies

```bash
pip install -r requirements.txt
```

---

# ▶️ Running the Project

## Capture Network Packets

```bash
python main.py
```

---

## Launch Dashboard

```bash
streamlit run dashboard.py
```

---

# 📊 Dashboard Includes

- Network Overview
- Total Packets
- Average Packet Size
- Largest Packet
- Protocol Distribution
- Top Source IPs
- Top Destination IPs
- Packet Table
- Threat Detection
- CSV Download
- Analysis Report Download

---

# 🚨 Basic Threat Detection

The application performs simple anomaly detection by identifying unusually large packets and highlighting them as potentially suspicious traffic.

---

# 📄 Generated Files

After execution, the following files are automatically generated:

- packet_logs.csv
- analysis_report.txt

---

# 📚 Learning Outcomes

Through this project, I gained practical experience in:

- Network Packet Sniffing
- Network Protocol Analysis
- Cybersecurity Fundamentals
- Python Programming
- Data Analysis
- Dashboard Development
- Data Visualization
- Traffic Monitoring
- Report Generation
- Streamlit Application Development

---

# 🎓 Internship Information

**Internship:** Cyber Security Internship

**Organization:** CodeAlpha

**Project Title:** Basic Network Sniffer

**Duration:** Internship Project

This project was successfully developed as a part of the practical tasks assigned during the **CodeAlpha Cyber Security Internship**, demonstrating real-world implementation of packet capturing, network traffic analysis, and visualization using Python.

---

# 👨‍💻 Author

**Ayush Kumar Dubey**

Python Developer | Cyber Security Enthusiast

GitHub: https://github.com/ayushkrdubey-23

LinkedIn: www.linkedin.com/in/ayushkrdubey23

---

# ⭐ If you found this project useful, consider giving it a Star!
