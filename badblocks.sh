#!/bin/bash

# Test harddrives for bad block sectors.
# Written by Christian Pearson - July 2019

echo "Block devices detected: "
block_device_output= 'lsblk'
echo $block_device_output

echo "Which block device to badblocks?"
read block_device

badblocks_command="badblocks -sv /dev/$block_device"
echo $badblocks_command
$badblocks_command 
