

from scapy.all import ARP, Ether, srp
import re
import os

# Define the target IP address
target_ip = "10.0.0.1"

# Craft the ARP request
arp = ARP(pdst=target_ip)

# Create Ethernet frame
ether = Ether(dst="ff:ff:ff:ff:ff:ff")

# Combine the Ethernet frame and ARP request
packet = ether/arp

# Send the packet and capture the response
result = srp(packet, timeout=10, verbose=0)[0]

# Extract and save MAC addresses to mac.txt
with open("mac.txt", "w") as f:
    for sent, received in result:
        mac_address = received[ARP].hwsrc
        # Validate MAC address format
        if re.match(r'^([0-9A-Fa-f]{2}[:-]){5}([0-9A-Fa-f]{2})$', mac_address):
            f.write(f"{mac_address}\n")

print("MAC addresses captured and saved to mac.txt")


