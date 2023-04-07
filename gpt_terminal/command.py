'''Terminal command and output read from log file'''

import logging
from dataclasses import dataclass

log = logging.getLogger(__name__)


@dataclass
class Command:
    '''Command and output'''
    command: str
    output: str

    def print(self):
        '''Print command and output'''
        log.info('#### SUMMARY ####')
        log.info('Command: ' + self.command)
        log.info('Output: ' + self.output)

    def clean(self):
        '''Strip whitespace from command and output'''
        self.command = self.command.strip()
        self.output = self.output.strip()
