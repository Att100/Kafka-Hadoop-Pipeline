#!/bin/bash
rm /etc/apt/sources.list
cp /home/workspace/modifications/sources.list /etc/apt/sources.list

apt-get update && apt-get install -y python3 python3-pip