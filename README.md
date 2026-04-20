# System Health Monitor 🖥️

A production-grade system monitoring tool built in Python that continuously 
tracks CPU, memory and disk usage, logs results with timestamps, and sends 
automated email alerts when thresholds are breached.

## Why I Built This

During my time at Thales Avionics, I monitored fleet health and system 
performance manually every day. This project automates that exact workflow — 
continuously watching system metrics, logging results and alerting when 
something needs attention. Same concept, built from scratch in Python.

## How It Works
System Metrics (CPU, Memory, Disk)
->
Python script collects metrics every 60 seconds
->
Checks against configurable thresholds
->
Logs results to timestamped log file
->
Sends email alert if threshold is breache

## Features

- Real time CPU, memory and disk monitoring
- Configurable thresholds via config.py
- Automatic timestamped logging to file
- Email alerts via Gmail SMTP when limits exceeded
- Runs continuously on a schedule — no manual intervention needed

## Technologies Used

- Python 3.14
- psutil — system metrics collection
- schedule — automated interval execution
- smtplib — email alert delivery
- logging — audit trail generation

## How To Run

1. Clone the repository
git clone https://github.com/yourusername/system-health-monitor.git
cd system-health-monitor

2. Install dependencies
pip3 install -r requirements.txt

3. Configure settings
Edit config.py to set your thresholds and email credentials

4. Run the monitor
python3 monitor.py

## Configuration

Edit config.py to customize —

| Setting | Default | Description |
|---|---|---|
| CPU_THRESHOLD | 80% | Alert if CPU exceeds this |
| MEMORY_THRESHOLD | 80% | Alert if memory exceeds this |
| DISK_THRESHOLD | 85% | Alert if disk exceeds this |
| CHECK_INTERVAL | 60 | Seconds between each check |
| ALERT_ENABLED | True | Enable or disable email alerts |

## Sample Output

--- Health Check: 2026-04-20 19:47:32 ---
✅ CPU OK: 5.4%
✅ Memory OK: 55.4%
✅ Disk OK: 3.6%
--- Check Complete ---

## Future Improvements

- Add network bandwidth monitoring
- Build a dashboard to visualize metrics
- Add Slack or SMS alerts
- Deploy on AWS EC2 to monitor cloud instances
- Add Docker support for containerized deployment

## Author

Vishakha Hanumante
LinkedIn: https://www.linkedin.com/in/vishakhahanumante/
