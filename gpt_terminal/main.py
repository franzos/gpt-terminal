'''GPT Terminal main loop'''

import time
import os
import sys
import getpass
import logging
from .command import Command
from .gpt import ask_gpt
from .log import *

log = logging.getLogger(__name__)


def main():
    '''Main loop'''
    commands = []

    username = getpass.getuser()
    filename = f'/home/{username}/.gpt_terminal.log'

    openai_api_key = os.environ.get('OPENAI_API_KEY')
    if openai_api_key is None or openai_api_key == '':
        log.error('OPENAI_API_KEY is not set')
        sys.exit(1)

    with open(filename, 'w', encoding='utf-8'):
        pass

    with open(filename, 'r', encoding='utf-8') as log_file:
        status = 0 # 0 = input, 1 = output
        usr_input = ''
        output = ''

        while True:
            line = log_file.readline()

            if not line:
                time.sleep(1)
                log.debug('Waiting for more input...')
                continue

            if status == 0:
                if '?2004l' in line:
                    log.debug('Input finished')
                    status = 1

                    if 'gpt-help' in usr_input:
                        ask_gpt(commands[len(commands) - 1], username)

                else:
                    usr_input += line.strip()

            if status == 1:
                if '?2004h' in line:
                    log.debug('Output finished')
                    status = 0

                    command = Command(usr_input, output)
                    command.clean()
                    command.print()
                    commands.append(command)

                    usr_input = ''
                    output = ''
                else:
                    output += line


if __name__ == '__main__':
    main()
