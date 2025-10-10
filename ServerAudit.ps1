# Get system information
systeminfo

# Show firewall status
netsh advfirewall show allprofiles

# Check Windows Defender antivirus status
Get-MpComputerStatus

# List installed updates
wmic qfe list brief /format:table

# List running services
Get-Service | Where-Object {$_.Status -eq "Running"}

List scheduled tasks
Get-ScheduledTask

# Get current audit policy
auditpol /get /category:*

# Enable auditing for all categories
auditpol /set /category:* /success:enable /failure:enable