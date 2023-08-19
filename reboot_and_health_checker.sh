#!/bin/bash

LA_THRESHOLD=$1

la=$(awk '{print $1}' /proc/loadavg)

if (( $(echo "$la > $LA_THRESHOLD" | bc -l) )); then
  echo "stop: high load average!! > $la"
  echo $(cat /proc/loadavg)
  echo "rebooting..."
  sleep 10
  reboot
fi
