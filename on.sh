#! /bin/bash
Exporting pin: $1. #
echo $1 > /sys/class/gpio/export
echo Setting direction to OUT.
echo out > /sys/class/gpio/gpio$1/direction
echo Setting PIN to HIGH
echo 1 > /sys/class/gpio/gpio$1/value
