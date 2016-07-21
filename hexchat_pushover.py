# The MIT License (MIT)
#
# Copyright (c) 2016 Oliver Gutiérrez
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

import hexchat
import subprocess

__module_name__ = 'pushover'
__module_version__ = '0.1'
__module_description__ = 'Sends an alert message when queried or named'


PUSHOVER_APP_TOKEN=''
PUSHOVER_USER_TOKEN=''

CURL_COMMAND = [
  'curl',
  '-s',
  '--form-string', '"token=%s"' % PUSHOVER_APP_TOKEN,
  '--form-string', '"user=%s"' % PUSHOVER_USER_TOKEN,
  '--form-string', '"message=%s"',
  'https://api.pushover.net/1/messages.json'
]


def send_pushover_message(message):
    subprocess.Popen(
        ' '.join(CURL_COMMAND) % message,
        shell=True
    )


def callback_channel(word, wordeol, userdata, **kwargs):
    channel = hexchat.get_info('channel')
    if channel == word[0]:
        channel = 'Private'
    message = '%s - %s: %s' % (channel, word[0], word[1])
    send_pushover_message(message)


# Hooks for different events
hexchat.hook_print("Channel Action Hilight", callback_channel)
hexchat.hook_print("Channel Msg Hilight", callback_channel)
hexchat.hook_print("Private Action to Dialog", callback_channel)
hexchat.hook_print("Private Message to Dialog", callback_channel)

# Notify plugin is loaded
hexchat.prnt('Pushover alert plugin loaded')
