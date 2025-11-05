# Clear-Host

echo "Username: ........ $($env:USERNAME)"
echo "Computer name: ... $($env:COMPUTERNAME)"
echo "OS: .............. $($env:OS)"

echo ""
echo "==================== DRIVES ===================="
echo "Home drive: ...... $($env:HOMEDRIVE)"
./get-hdd-usage.ps1

echo ""
echo "==================== SETTINGS ===================="
echo "Culture: ......... $(($Host).CurrentCulture.Name)"
echo "UI culture: ...... $(($Host).CurrentUICulture.Name)"

echo ""
echo "==================== CPU ===================="
echo "#processors: ..... $($env:NUMBER_OF_PROCESSORS)"
echo "CPU arch.: ....... $($env:PROCESSOR_ARCHITECTURE)"
echo "CPU id: .......... $($env:PROCESSOR_IDENTIFIER)"
echo "CPU temp.: ....... $(./get-cpu-temperature.ps1)"

echo ""
echo "==================== Path ===================="
$env:Path -split ";"
