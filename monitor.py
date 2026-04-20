#system health monitor -- main script

import psutil
import logging
import schedule
import time
from datetime import datetime
import config
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

#logging setup
logging.basicConfig(filename = config.LOG_FILE,
                    level = logging.INFO,
                    format = "%(asctime)s - %(levelname)s - %(message)s")

#sending alerts
def send_alert(subject, message):
    if not config.ALERT_ENABLED:
        return
    try:
        msg = MIMEMultipart()
        msg['From'] = config.ALERT_EMAIL_SENDER
        msg['To'] = config.ALERT_EMAIL_RECEIVER
        msg['Subject'] = subject

        msg.attach(MIMEText(message, "plain"))

        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(config.ALERT_EMAIL_SENDER, config.ALERT_EMAIL_PASSWORD)
        server.send_message(msg)
        server.quit()

        print(f"Alert email sent: {subject}")
        logging.info(f"Alert email sent: {subject}")

    except Exception as e:
        print(f"Failed to send email: {e}")
        logging.error(f"Failed to send email: {e}")

        
def check_cpu():
    cpu_usage = psutil.cpu_percent(interval = 1 )
    if cpu_usage > config.CPU_THRESHOLD:
        logging.warning(f"HIGH CPU ALERT: {cpu_usage}% (Threshold:{config.CPU_THRESHOLD}%)")
        print(f"HIGH CPU: {cpu_usage}%")
        send_alert("HIGH CPU ALERT",
                   f"CPU usage is at {cpu_usage}% which exceeds threshold of {config.CPU_THRESHOLD}%")
    else:
        logging.info(f"CPU OK: {cpu_usage}%")
        print(f"CPU OK: {cpu_usage}%")
    return cpu_usage
        
def check_memory():
    memory = psutil.virtual_memory()
    memory_usage = memory.percent
    if memory_usage > config.MEMORY_THRESHOLD:
        logging.warning(f"HIGH MEMORY ALERT: {memory_usage}% (Threshhold:{config.MEMORY_THRESHOLD}%)")
        print(f"HIGH MEMORY: {memory_usage}%")
        send_alert(
            "HIGH MEMORY ALERT",
            f"MEMORY usage is at {memory_usage}% which exceeds threshold of {config.MEMORY_THRESHOLD}%"
        )
    else:
        logging.info(f"Memory OK: {memory_usage}%")
        print(f"Memory OK: {memory_usage}%")
    return memory_usage

def check_disk():
    disk = psutil.disk_usage('/')
    disk_usage = disk.percent
    if disk_usage > config.DISK_THRESHOLD:
        logging.warning(f"HIGH DISK ALERT: {disk_usage}% (Threshold: {config.DISK_THRESHOLD}%)")
        print(f"HIGH DISK: {disk_usage}%")
        send_alert(
            "HIGH DISK USAGE ALERT",
            f"DISK usage is at {disk_usage}% which exceeds threshold of {config.DISK_THRESHOLD}%"
        )
    else:
        logging.info(f"DISK OK: {disk_usage}%")
        print(f"Disk OK: {disk_usage}%")
    return disk_usage

def run_health_check():
    print(f"\n--- HEALTH CHECK : {datetime.now().strftime('%Y-%m-%d %H:%M:%S')} ---")
    check_cpu()
    check_memory()
    check_disk()
    print("--- CHECK COMPLETE ---\n")


#Run immediately on start
run_health_check()

#Then run every CHECK_INTERVAL seconds
schedule.every(config.CHECK_INTERVAL).seconds.do(run_health_check)
print(f"Monitor running... checking every {config.CHECK_INTERVAL} seconds. Press Ctrl+C to stop.")

while True:
    schedule.run_pending()
    time.sleep(1)
