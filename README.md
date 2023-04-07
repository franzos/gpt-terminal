# GPT Terminal

GPT Terminal is your AI-assistant on the command line. Whenever a command fails, simply type `gpt-help` to get a suggestion on how to fix it.

This application has been developed on, and tested with bash, but should work on any modern shell.

- Relies on GPT 3.5
- Right now Linux only (due to `notify-send`)
- Should work with any modern shell

![GPT Terminal](./preview.png?raw=true)

## Installation

Install with pip:

```bash
pip3 install gpt-terminal
```

Make sure `notify-send` is available on your system. On Guix, you can install it with:

```bash
guix package -i libnotify
```

Set OpenAI API key (GPT 3.5):

```bash
export OPENAI_API_KEY='sk-...'
```

## Usage

Make sure `gpt-terminal` is running:

You can run GPT Terminal in a seperate terminal window, or as a service with systemd or shepherd.

```bash
gpt-terminal
```

Activate suggestions for current terminal:

```bash
exec &> >(tee -a /home/$(whoami)/.gpt_terminal.log)
```

To restore the original behaviour, open a new terminal or run:

```
exec &> /dev/tty
```

To get help on the last command, simply type:

```bash
echo gpt-help
```

### Alias

You can setup a alias in your `.bashrc`:

```bash
alias gpt-help='echo gpt-help'
```

Then simply type:

```bash
gpt-help
```

## Development

The approach here is fairly simple:

1. Redirect all shell in-, and output to a log file.
2. Have `gpt-terminal` tail the log file.
3. Whenever you type `gpt-help`, `gpt-terminal` will send the last command to ChatGPT
4. Once we got the response, a desktop notification is triggered with `notify-send`

### Setup

```bash
git clone https://github.com/franzos/gpt-terminal; cd gpt-terminal
python3 -m venv venv
source venv/bin/activate
pip3 install .
```

## TODO

This was just thrown together out of curiosity. There is a lot of room for improvement.

- [ ] Tweak desktop notification
- [ ] Improve OS recognition (to provide better suggestions)
- [ ] Support other LLM's (local and API)
- [ ] Store log in `~/.local/share/gpt-terminal/` or `/tmp/...` instead
- [ ] Supply API key via config or command line
- [ ] A more obvious name
- [ ] ...
