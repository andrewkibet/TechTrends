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

sudo lsof -i :8000                                                                                                                              1 ⨯
COMMAND     PID USER   FD   TYPE DEVICE SIZE/OFF NODE NAME
docker-pr 15375 root    4u  IPv4 101066      0t0  TCP *:8000 (LISTEN)
docker-pr 15383 root    4u  IPv6 101477      0t0  TCP *:8000 (LISTEN)
                                                                                                                                                        
┌──(rootKALI)-[~/splunk-setup]
└─# sudo kill -9 15375
                                                                                                                                                        
┌──(rootKALI)-[~/splunk-setup]
└─# sudo kill -9 15383

Now, docker and splunk work together and they is a file that is of much importance: docker-compose.yml

version: "3"
services:
  web:
    image: nginx
    ports:
      - "8080:80"
  db:
    image: mysql
    environment:
      MYSQL_ROOT_PASSWORD: example




OFFSET=$(expr 512 \* 2048)  
mkdir -p /mnt/linux_image  
losetup -o ${OFFSET} /dev/loop0 ./linux_lab_final_acme_corp.img  
mount -t auto /dev/loop0 /mnt/linux_image 


find / -name "linux_lab_final_acme_corp.img" 2>/dev/null # Used to llocate the image

#Hardening Process of Windows system

#STIG & SCAP Resources
 #SCAP (Security Content Automation Protocol)
#SCAP is a standard used to automate vulnerability checks and security compliance using tools. SCAP content includes:

#Machine-readable checks (e.g., XML files)

#redefined rules (like password settings, firewall configs)

#So instead of manually checking if a system is compliant, SCAP tools automatically scan it using these rules.



# mounting images

mount -t auto /dev/loop0 /mnt/linux_image
## View All AD Groups

Get-ADGroup -Filter * | Select Name, DistinguishedName | Format-Table

