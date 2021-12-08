# Installing grafana and creating dashboard:

These are the steps followed:

- Installing dependencies:

```bash
sudo apt-get install -y apt-transport-https
sudo apt-get install -y software-properties-common wget

```

![install dependencies](https://github.com/surpriso1997/6_2_Prom_Grafana_Prajwol/blob/main/3/screenshots/install-https-.png)

![image](https://github.com/surpriso1997/6_2_Prom_Grafana_Prajwol/blob/main/3/screenshots/install-dependencies.png)

- Adding grafana siging key and apt repository:

```bash
wget -q -O - https://packages.grafana.com/gpg.key | sudo apt-key add -
echo "deb https://packages.grafana.com/oss/deb stable main" | sudo tee -a /etc/apt/sources.list.d/grafana.list
```

![addking key and repo](https://github.com/surpriso1997/6_2_Prom_Grafana_Prajwol/blob/main/3/screenshots/adding-grafana-key-and-repository.png)

- Installing grafana:

```bash
sudo apt-get update
sudo apt-get install grafana

```

![intall grafana](https://github.com/surpriso1997/6_2_Prom_Grafana_Prajwol/blob/main/3/screenshots/install-grafana.png)

- Starting grafana server:

```bash
sudo systemctl start grafana-server
sudo systemctl status grafana-server

```

![garafna service runnign](https://github.com/surpriso1997/6_2_Prom_Grafana_Prajwol/blob/main/3/screenshots/grafana-service-running.png)

- Running grafana in browser. Default username and password admin were used to login.

![running in browser](https://github.com/surpriso1997/6_2_Prom_Grafana_Prajwol/blob/main/3/screenshots/grafana-running-browser.png)

![login with default pass and dashboard](https://github.com/surpriso1997/6_2_Prom_Grafana_Prajwol/blob/main/3/screenshots/logged-in-with-default-username-passsword.png)

- Adding prometheus as data source:

  ![adding as data source ](https://github.com/surpriso1997/6_2_Prom_Grafana_Prajwol/blob/main/3/screenshots/adding-prometheus-data-srouce.png)

  ![prometheus data source wrking](https://github.com/surpriso1997/6_2_Prom_Grafana_Prajwol/blob/main/3/screenshots/data-source-working.png)

- Adding/importing `Node Exporter Full` dashboard into grafana with it's UID:

  ![importing](https://github.com/surpriso1997/6_2_Prom_Grafana_Prajwol/blob/main/3/screenshots/importing-node-exporter-full.png)

- Showing prometheus monitoring data in grafa dashbaord:
  ![grafana dashboard](https://github.com/surpriso1997/6_2_Prom_Grafana_Prajwol/blob/main/3/screenshots/grafana-dashboard.png)
