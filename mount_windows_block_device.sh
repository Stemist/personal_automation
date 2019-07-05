#!/bin/bash

# Mount Windows block device automatically.
# Written by Christian Pearson - July 2019

# Print block devices.
echo "Block devices detected: "
block_device_output= 'lsblk'
echo $block_device_output

echo "Which Windows block device to mount? (E.g. sda1)"
read block_device

# Prepare block device for mount.
echo "ntfsfix /dev/$block_device"
ntfsfix /dev/$block_device

echo "mkdir /mnt/$block_device"
mkdir /mnt/$block_device

# Mount partition with assumption of unclean filesystem.
echo "mount -o remove_hiberfile /dev/$block_device"
mount -o remove_hiberfile /dev/$block_device /mnt/$block_device

echo "-----------------------------------------------------------"
lsblk
