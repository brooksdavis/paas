#!/bin/sh
#poudriere jail -c -j cheribsd-head -m git -v dev
# if extracting from archive:
#  if aws s3 ls s3://brooks-test/poudriere/jails/freebsd-head.tar.zstd > /dev/null 2>&1; then
#    aws s3 cp s3://brooks-test/poudriere/jails/freebsd-head.tar.zstd - | poudriere jail -c -j freebsd-head -m tar=/dev/stdin -v 13.0-CURRENT
#  else
poudriere jail -c -j freebsd-head -m git -v freebsd-head
# if archiving:
#  tar cf - -C /usr/local/poudriere/jails/freebsd-head/ . | zstd | aws s3 cp - s3://brooks-test/poudriere/jails/freebsd-head.tar.zstd
# 
poudriere ports -c -p ports
poudriere ports -c -p cheri-ports-overlay -U https://github.com/CTSRD-CHERI/cheri-ports-overlay.git -m git -B main
