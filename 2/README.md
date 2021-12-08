# Insatalling node exporter:

- Downloading node port source from github with wget:
  node_exporter version 1.3.0 has problem execuing the executable file so 1.3.1 version was downloaded later

```bash
wget https://github.com/prometheus/node_exporter/releases/download/v1.3.1/node_exporter-1.3.1.linux-amd64.tar.gz

```

![downlaoding node exporter](https://github.com/surpriso1997/6_2_Prom_Grafana_Prajwol/blob/main/2/screenshots/fetch-node-exporter.png)

- Extract node_exporter with tar

```bash
tar xvfz node_exporter-1.3.1.linux-amd64.tar.gz

```

![extract](https://github.com/surpriso1997/6_2_Prom_Grafana_Prajwol/blob/main/2/screenshots/unzip-node-exporter.png)

- Running the `node_exporter` executable:

![node exporter](https://github.com/surpriso1997/6_2_Prom_Grafana_Prajwol/blob/main/2/screenshots/node-exporter-running.png)

- Edited and updated `prometheus.yml` file located at `/etc/prometheus` and added `node_exporter` job and set ip address:

![node exporter ip](https://github.com/surpriso1997/6_2_Prom_Grafana_Prajwol/blob/main/2/screenshots/added-node-exporter-static-confis.png)

- Restarted prometheus service

- node exporter running in browser:
  ![running in browser](https://github.com/surpriso1997/6_2_Prom_Grafana_Prajwol/blob/main/2/screenshots/node-exporter-running-browser.png)

- Listing targets:

![listing node targets](https://github.com/surpriso1997/6_2_Prom_Grafana_Prajwol/blob/main/2/screenshots/targets%20listing.png)


