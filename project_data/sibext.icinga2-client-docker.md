# icinga2

This repository contains the source for the [icinga2](https://www.icinga.org/icinga2/) [docker](https://www.docker.com) image.

It is only the **client side**. When used inside a priviledged container, you'll be able to monitor the whole machine with this image.

For the **master node** consult [@jjethwa's docker image](https://github.com/jjethwa/icinga2/).

# Why the fuck would I need an icinga2-client-node in a docker-container?

Well, actually. That's a good question. But let me answer it with a question: Have you ever used synology-products and their shell?

- **No:** You had been lucky.
- **Yes:** You know the evidence.

Well, to paraphrase it:

- It's impossible to build icinga2 on a Synology NAS with 1G of RAM. It may be. But if so, it's at least a PITA.
- I disliked the monitoring of my NAS via the SNMP plugin, as the service had been flapping constantly, because Synology reported every time, when it had not been connected to the update site. Which results in a flapping service. This is just impractical.
- Hacking a docker client-image was straight forward, as I contributed much things to @jjethwa's image.
  - **Now my Synology Box just feels like another good Linux-Box.** And I can produce for every HDD/FS/RAID/... a single icinga2-service.
  - docker is squeezable.

## Usage

Recommended execution is via `docker-compose`. There is too much stuff which has to be configured outside the container to run it via plain `docker run` but of course, it would be possible.

    wget https://raw.githubusercontent.com/bebehei/icinga2-client-docker/master/docker-compose.yml
    #add your ticket-salt information
    $EDITOR docker-compose.yml
    docker-compose up

## Environment variables Reference

| Environmental Variable | Default Value          | Description |
| ---------------------- | ---------------------- | ----------- |
| `ICINGA2_TICKET_SALT`  | *undefined*            | **required:** Container will stop without ticket-salt to process certificate request. |
| `ICINGA2_MASTER_HOST`  | mon                    | The hostname of icinga2
| `ICINGA2_MASTER_FQDN`  | *$ICINGA2_MASTER_HOST* | If your icinga2 master certs' FQDN does not match the hostname, define this in addition. If you set `ICINGA2_MASTER_HOST` correctly, you should not worry about this. |
| `ICINGA2_MASTER_PORT`  | 5665                   | Default port on the icinga2 master. |
| `ICINGA2_CLIENT_FQDN`  | *$(hostname --fqdn)*   | To request a certificate from your master, your requesting FQDN has to match the FQDN chained to your given ticket salt. If your hostname does not match the FQDN, defined this variable and set the value to the corresponding value of the master. |
## Volume Reference

All these folders are configured and able to get mounted as volume. The bottom ones are not quite neccessary.

| Volume | ro/rw | Description & Usage |
| ------ | ----- | ------------------- |
| /etc/icinga2 | rw | Icinga2 configuration folder |
| /var/lib/icinga2 | rw | Icinga2 Data |
| /var/log/icinga2 | rw | logfolder for icinga2 (not neccessary) |
| /var/log/supervisor | rw | logfolder for supervisord (not neccessary) |
| /var/spool/icinga2 | rw | spool-folder for icinga2 (not neccessary) |
| /var/cache/icinga2 | rw | cache-folder for icinga2 (not neccessary) |
