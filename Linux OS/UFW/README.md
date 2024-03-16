<p align="center"><strong>Uncomplicated Firewall</strong></p>

**Notes:**
```
1. UFW is a simple interface for managing iptables firewall rules on Linux systems.
2. UFW provides logging capabilities to track firewall activity, allowing users to monitor connections and detect potential security threats.
```


**How to install ufw:**
```
$sudo apt install ufw
```

**Ways to allow specific ports:**
```
$sudo ufw allow <Port_Number>
$sudo ufw allow from <IP_address_or_range> to any port <Port_Number>
$sudo ufw allow proto tcp to any port <Port_Number>
$sudo ufw allow proto tcp from <IP_address_or_range> to any port <Port_Number>
```

**To view port status:**
```
sudo ufw status numbered
sudo ufw status
```

**To reomve ports allowed:**
```
sudo ufw delete <NumberID>
```