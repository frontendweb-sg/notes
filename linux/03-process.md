# Managing process

**`Managing startup process:`**

`Systemd` Initialization System

Most modern `Linux` distributions use `systemd` as their initialization system. `systemd` is responsible for `starting` up and `managing` services.

```sh
# list all services
systemctl list-units --type=service --all

# enable service at startup
sudo systemctl enable service_anme

# disable service at startup
sudo systemctl disable service_anme

# start service mannually
sudo systemctl start service_name

# stop servie mannually
sudo systemctl stop service_name

# restart service
sudo systemctl restart service_name

# check status of service
sudo systemctl status service_name
```

**Creating Custom Startup Services:**

To create a custom service that runs at startup, you need to create a service unit file in `/etc/systemd/system/` directory

`Example:`

```sh
# create directory [my_custom_service]
sudo nano /etc/systemd/system/my_custom_service.service

# define the service configuration
[Unit]
Description=My Custom Service
After=network.target

[Service]
ExecStart=/path/to/your/script.sh
Restart=always
User=your_username
Group=your_groupname

[Install]
WantedBy=multi-user.target

# reload systemd, enable and start the service
sudo systemctl daemon-reload
sudo systemctl enable my_custom_service
sudo systemctl start my_custom_service

# check status of service
sudo systemctl status my_custom_service
```

<br/>

**`Managing Shutdown Processes:`**

```sh
# shutdown the system immideatly
sudo systemctl poweroff

# reboot the system
sudo systemctl reboot

# halt the system (stop all process but doesn't power off)
sudo systemctl halt

# schedule shutdown
sudo shutdown +30 # this will schedule shutdown 30 minutes from now

# schedule exact time
sudo shutdown 10:00

# cancel scedule shutdown
sudo shutdown -c
```

**Customizing Startup and Shutdown Scripts:**

You can create scripts that run at `startup` and `shutdown` by placing them in the appropriate directories.

`use:` /etc/rc.local (Make sure it’s executable)

```sh
sudo nano /etc/rc.local

# add your command to the file
```

**`Edit cron jobs:`**

```sh
# edit root crontab
sudo crontab -e

# run at shutdown (using custom script to handle shutdown)
@reboot /path/to/your/monitor_shutdown_script.sh


# ancrontab format
cat /etc/anacrontab
```

<br />

**`Summary of Additional Advanced Tasks:`**

```sh
# system target
systemctl get-default
systemctl set-default
systemctl isolate

# crub customization (/etc/default/grub)
sudo update-grub
```
