'''Logging'''

import logging
from logging.handlers import SysLogHandler
from platform import system

opsys = system()


log = logging.getLogger('gpt_terminal')
formatter = logging.Formatter(
    '%(asctime)s - %(name)s - %(levelname)s: %(message)s', "%Y-%m-%d %H:%M:%S"
)
formatter_cli = logging.Formatter('%(levelname)s: %(message)s')

log.setLevel(logging.DEBUG)

if opsys == 'Linux':
    sh = SysLogHandler()
    sh.setLevel(logging.WARNING)
    sh.setFormatter(formatter)
    log.addHandler(sh)

ch = logging.StreamHandler()
ch.setLevel(logging.INFO)
ch.setFormatter(formatter_cli)
log.addHandler(ch)
