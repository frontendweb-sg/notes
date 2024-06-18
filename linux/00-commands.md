# Linux commands

- `lshw:` List hardware
- `dmidecode:` Display hardware information from the system BIOS
- `ip -a:` Show ip address information.
- `ifconfig:` Configuration network interface.
- `netstate:` network statistics.
- `w:` show who is logged on and what they are doing.
- `traceroute:` Print the route packets take to the network host.
- `who:` Show who is logged on.
- `last:` Show the list of last logged in user.

**`System commands:`**

- `uname -a:` System information.
- `hostnamectl:` Show current hostname and related information.
- `lscpu:` List CPU architecture information.
- `timedatectl status:` show system time.
- `uptime:` Tell how long the system has been running
- `dmesg:` Print or control the kernel ring buffer

<br />

**`System monitoring and management:`**

- `top:` Display real-time system process.
- `htop:` An interactive process viewer (needs installation)
- `df -h:` Shows disk usage in a human-redable format.
- `free -m: `Display free and used memory in MB.
- `kill <process id>:` Terminates a process.
- `lspci:` List all pci devices.
- `lscpu:` List USB devices.
- `lsblk:` List information about Block Devices.

<br />

**`Running commands:`**

- `[command] &:` Runs command in the background.
- `jobs:` Display background commands.
- `fg <command number>:` brings command to the foreground.

<br />

**`Service management:`**

- `sudo systemctl start <service> :` Starts a service.
- `sudo systemctl stop <service> :` Stops a service
- `sudo systemctl status <service> :` Checks the status of a service.
- `sudo systemctl reload <service> :` Reloads a service’s configuration without
  interrupting its operation.
- `journalctl -f :` Follows the journal, showing new log messages in real time.
- `journalctl -u <unit_name> :` Displays logs for a specific systemd unit.

<br />
