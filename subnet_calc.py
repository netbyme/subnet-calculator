# subnet-calculator
# Takes an IP address and prefix length
# Calculates all subnet information automatically
# Built to reinforce CCNA subnetting knowledge

import ipaddress

def calculate_subnet(ip_with_prefix):
    # create network object
    network = ipaddress.IPv4Network(ip_with_prefix, strict=False)
    
    # calculate all values
    print(f"\n=== Subnet Calculator ===\n")
    print(f"IP Address    : {ip_with_prefix.split('/')[0]}")
    print(f"Prefix        : /{network.prefixlen}")
    print(f"Subnet Mask   : {network.netmask}")
    print(f"Network       : {network.network_address}")
    print(f"Broadcast     : {network.broadcast_address}")
    print(f"First Host    : {network.network_address + 1}")
    print(f"Last Host     : {network.broadcast_address - 1}")
    print(f"Total Hosts   : {network.num_addresses}")
    print(f"Usable Hosts  : {network.num_addresses - 2}")
    print(f"IP Class      : {get_ip_class(str(network.network_address))}")

def get_ip_class(ip):
    first = int(ip.split(".")[0])
    if 1 <= first <= 126:
        return "Class A"
    elif 128 <= first <= 191:
        return "Class B"
    elif 192 <= first <= 223:
        return "Class C"
    else:
        return "Other"

# test with different subnets
subnets = ["192.168.1.0/24", "10.0.0.0/8", "172.16.0.0/16", "192.168.1.0/26"]

for subnet in subnets:
    calculate_subnet(subnet)
    print()