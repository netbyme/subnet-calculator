# subnet-calculator

A Python tool that calculates all subnet information from an IP address and prefix length. Built to reinforce CCNA subnetting knowledge and automate manual calculations.

## What it does

- Calculates network address, broadcast, first and last host
- Shows subnet mask, prefix length and IP class
- Splits a network into smaller subnets automatically
- Interactive mode — enter any IP/prefix and get instant results
- Handles Class A, B, and C networks

## Why this matters

Subnetting is the foundation of every CCNA exam and every real network design. This tool automates the calculations that engineers do manually — and helped me deeply understand how subnetting works from the inside out.

## How to run

```bash
python3 subnet_calc.py
```

## Output example
=== Subnet Calculator ===
IP Address    : 192.168.1.0
Prefix        : /24
Subnet Mask   : 255.255.255.0
Network       : 192.168.1.0
Broadcast     : 192.168.1.255
First Host    : 192.168.1.1
Last Host     : 192.168.1.254
Total Hosts   : 256
Usable Hosts  : 254
IP Class      : Class C