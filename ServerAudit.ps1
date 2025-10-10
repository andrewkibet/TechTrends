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
