'''Utility functions to determine operating system and send alerts'''

import subprocess
import platform
import logging

log = logging.getLogger(__name__)


def is_guix():
    '''Checks if this is a guix system'''
    try:
        result = subprocess.run(
            ["guix", "--version"], stdout=subprocess.DEVNULL
        )
        if result.returncode == 0:
            return True
    except:
        pass
    return False


def os_info():
    '''Get operating system information'''
    if is_guix():
        return "guix"
    else:
        os_name = platform.system()
        os_version = platform.release()
        return f"{os_name} {os_version}"


def send_alert(username, title, body, expire_after_ms):
    '''Send alert to specific user'''
    # log.debug("=> Sending alert '{}' to user {} ...".format(title, username))
    try:
        if is_guix():
            subprocess.run(
                [
                    "sudo", "-u", username, "DISPLAY=:0", 
                    f"/home/{username}/.guix-profile/bin/notify-send",
                    "-u", "normal", "-t", str(expire_after_ms), "-c", "network",
                    title, body
                ],
                check=True
            )
        else:
            subprocess.run(
                [
                    "sudo", "-u", username, "DISPLAY=:0",
                    "notify-send",
                    "-u", "normal", "-t", str(expire_after_ms), "-c", "network",
                    title, body
                ],
                check=True
            )
    except Exception as err:
        log.error(err)
