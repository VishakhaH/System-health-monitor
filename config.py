#System Health Monitor - Configuration File

#Threshhold - if usage goes above these numbers, alern will trigger
CPU_THRESHOLD = 2 #percentage
MEMORY_THRESHOLD = 80 #percentage
DISK_THRESHOLD = 85 #percentage

#How often to check system health (in seconds)
CHECK_INTERVAL = 30

#Log file location
LOG_FILE = "logs/system_health.log"

#Alert settings
ALERT_ENABLED = True #setting to True after adding email address
ALERT_EMAIL_SENDER = "vishakhahanumante@gmail.com"
ALERT_EMAIL_RECEIVER = "vishakhahanumante@gmail.com"
ALERT_EMAIL_PASSWORD = "uofc rqgu ikdh lltu"
