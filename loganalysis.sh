#!/bin/bashI 

#I have been reading about log analysis in linux systems. On Linux systems, 
#log files accumulate data from applications and system processes. They monitor 
#various conditions of application, state changes, information, and errors. Growing log files 
#can consume storage space and then be difficult to manage and review. Automated log rotation is
# used to solve this storage issue.

docker start splunk

cd /etc/cron.daily #Logrotate is controlled by the cron system. Cron is a Linux service that allows you to run commands or scripts at 
#pecific times or intervals—unattended. By default, your Linux system likely has a cron job set up to run logrotate daily. 
#his cron job is usually located in a file /etc/cron.daily/logrotate.
cat logrotate
cat /etc/logrotate.conf
cat /etc/crontab
sudo lsof -i :8000 # This checks whats running on port 8000