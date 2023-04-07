'''OpenAI integration to query GPT-3 for suggestions'''

import logging
import openai
from .utils import send_alert, os_info
from .command import Command

log = logging.getLogger(__name__)


def ask_gpt(command: Command, username: str):
    '''Send command and output to GPT and get a suggestion'''
    log.debug('DEBUG: Asking GPT for help')
    log.debug(command.command)
    log.debug(command.output)
    send_alert(username, 'Suggestions', 'Checking with ChatGPT ...', 3000)

    completion = openai.ChatCompletion.create(model="gpt-3.5-turbo", messages=[
        {
            "role": "system",
            "content": f'''You are a system engineer helping a user troubleshoot a problem.
The user has run a command {os_info()} and you want to help them understand the output.
You can provide the user with a suggestion of what to do next.'''
        },
        {
            "role": "user", "content": f'''I ran the command:
{command.command}

and got the following output:
{command.output}
'''
        }
    ])
    log.debug(completion)
    suggestion = completion.choices[0].message.content
    log.debug(suggestion)
    send_alert(username, 'Suggestions', suggestion, 20000)
