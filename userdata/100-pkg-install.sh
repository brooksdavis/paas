#!/bin/sh
# XXX: install llvm11 or similar to speed 
PACKAGES="awscli git poudriere"
env ASSUME_ALWAYS_YES=yes pkg install ${PACKAGES}
