echo "Please read source code and execute appropriate commands manually"

# System File Checker (Only on OS drive)
# sfc /scannow

# OS Image Repair (Only on OS drive)
# dism.exe /online /cleanup-image /restorehealth

# Fix App Store Apps
# Get-AppXPackage | Foreach {Add-AppxPackage -DisableDevelopmentMode -Register "$($_.InstallLocation)\AppXManifest.xml"}

# Check Disk
# chkdsk C: /x /f /r