#!/bin/sh
DEV=/dev/nda1
logger "Setting up zfs for poudriere"
if [ -e $DEV ]; then
	zpool create poudriere $DEV
	zfs create -o mountpoint=/usr/local/poudriere poudriere/poudriere
	zfs create poudriere/distfiles
	zfs create -o mountpoint=/usr/obj poudriere/obj
else
	logger "missing ssd $DEV"
fi
