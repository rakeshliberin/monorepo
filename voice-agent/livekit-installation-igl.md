# Livekit Installation

## Server Details

- IP: `172.16.20.91`
- Username: `root`
- Password: `root123`

## Connect to the server

```bash
ssh root@172.16.20.91
```

## Pre-Setup Steps

Check docker deomon is running or not

```bash
sudo systemctl status docker
```

If not running, start it

```bash
sudo systemctl start docker
```

Stop all the running containers (if not needed)

```bash
docker stop $(docker ps -q)
```

## Installation Steps

Go to the home directory

```bash
cd ~
```

Go to the livekit directory

```bash
cd livekit
```

Pull the latest livekit generator image

```bash
docker pull livekit/generate
```

Run the livekit generator container

```bash
docker run --rm -it -v$PWD:/output livekit/generate
```

## Useful Commands

Kill a process running on a port

```bash
fuser -k PORT/tcp
```
