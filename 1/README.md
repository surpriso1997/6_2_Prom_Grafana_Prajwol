# Insatallation of prometheus:

These were the steps followed:

- Downloading the prometheus source code with wget:

```bash
wget https://github.com/prometheus/prometheus/releases/download/v2.31.1/prometheus-2.31.1.linux-amd64.tar.gz

```

![prometheus download](https://github.com/surpriso1997/6_2_Prom_Grafana_Prajwol/blob/main/1/screenshots/downlaoding-prommetheus-from-github-releaes-source.png)

- extract the downlaoded file with tar

```bash
tar xvf prometheus-2.31.1.linux-amd64.tar.gz

```

![extract](https://github.com/surpriso1997/6_2_Prom_Grafana_Prajwol/blob/main/1/screenshots/extract-prom.png)

- Created `/etc/prometheus` dir and moved `prometheus.yml` and `console_libraries` to `/etc/prometheus` dir. Moved `promtool` to `/usr/local/bin/`

![moved files ](https://github.com/surpriso1997/6_2_Prom_Grafana_Prajwol/blob/main/1/screenshots/copied-prometheus-files-to-differnet-config-locations.png)

- Listing prometheus and promtool version

```bash
prometheus --version
promtool --version
```

![lsting prometheus versions](https://github.com/surpriso1997/6_2_Prom_Grafana_Prajwol/blob/main/1/screenshots/prometheus-and-promtool-version.png)

- creating `prometheus` user and user group:

```bash
sudo groupadd --system prometheus

sudo useradd -s /sbin/nologin --system -g prometheus prometheus

```

- Give permisssion of `/etc/prometheus`, `/var/lib/prometheus` dirs to `prometheus` user

```bash
sudo chown -R prometheus:prometheus /etc/prometheus/ /var/lib/prometheus
sudo chmod -R 755 /etc/prometheus/ /var/lib/prometheus
```

- Creating a `prometheus.service` file in `/etc/systemd/system/` so that we can use `systemctl` to
  control the prometheus service

![prometheus sevice file](https://github.com/surpriso1997/6_2_Prom_Grafana_Prajwol/blob/main/3/screenshots/prometheus.service-file.png)

- Relaoded and the systemctl daemon to add prometheus and enabled and started the prometheus service:

```bash
sudo systemctl daemon-reload
sudo systemctl enable prometheus
sudo systemctl restart prometheus
sudo systemctl status prometheus
```

![promethus service runnign](https://github.com/surpriso1997/6_2_Prom_Grafana_Prajwol/blob/main/1/screenshots/prometheus-running-in.png)

- To generate a bcrypt hashed password the follwing python script was created:

```python

 import getpass
 import bcrypt


 password= getpass.getpass("password: ")

 hashed_pass= bcrypt.hashpw(password.encode("utf-8"), bcrypt.gensalt())

 print(hashed_password.decode())

```

![generated password](https://github.com/surpriso1997/6_2_Prom_Grafana_Prajwol/blob/main/1/screenshots/gen-password.png)

- created new web.yml file and added the password created into it as:

```yml
basic_auth_users:
  admin: generated_password
```

- prometheus running in browser on port 9090:

![browser](https://github.com/surpriso1997/6_2_Prom_Grafana_Prajwol/blob/main/1/screenshots/prometheus-running-in-browser.png)
