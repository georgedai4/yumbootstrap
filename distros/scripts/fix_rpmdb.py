#!/usr/bin/python3

import os,sys
import time
import logging
sys.path.insert(0, '/root/project/yumbootstrap/lib')
import yumbootstrap.yum
import yumbootstrap.log

#-----------------------------------------------------------------------------

logger = logging.getLogger()
logger.addHandler(yumbootstrap.log.ProgressHandler())
if os.environ['VERBOSE'] == 'true':
  logger.setLevel(logging.INFO)

#-----------------------------------------------------------------------------

yum = yumbootstrap.yum.Yum(chroot = os.environ['TARGET'])

# to prevent yumbootstrap.yum.Yum from running Python in chroot $TARGET
# one may specify `expected_rpmdb_dir' manually:
#   yum.fix_rpmdb(expected_rpmdb_dir = '/var/lib/rpm')
# if /usr/bin/db_load or /bin/rpm have a different name, this also could be
# provided:
#   yum.fix_rpmdb(db_load = '/usr/bin/db_load')
#   yum.fix_rpmdb(rpm = '/bin/rpm')
yum.fix_rpmdb()

#-----------------------------------------------------------------------------
# vim:ft=python
