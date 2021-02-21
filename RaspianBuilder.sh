#!/bin/sh 


dd if=$1 of=$2  bs=4096 status=progress 

ROOT=$2"2"
BOOT=$2"1"

/usr/bin/mount $ROOT /mnt
/usr/bin/mount $BOOT /mnt/boot 

/usr/bin/touch /mnt/boot/ssh 
/usr/bin/sync

/usr/bin/umount /mnt/boot
/usr/bin/umount /mnt

echo "done!" 
