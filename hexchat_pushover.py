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
import requests

__module_name__ = 'pushbullet'
__module_version__ = '0.1'
__module_description__ = 'Sends an alert message when queried or named'


PUSHBULLET_ACCESS_TOKEN=''

headers = {
    'Access-Token': PUSHBULLET_ACCESS_TOKEN,
    'Content-Type': 'application/json',
}

def send_pushover_message(channel,message):
    json_data = {
    'body': message,
    'title': channel,
    'type': 'note',}
    response = requests.post('https://api.pushbullet.com/v2/pushes', headers=headers, json=json_data)


def callback_channel(word, wordeol, userdata, **kwargs):
    channel = hexchat.get_info('channel')
    if channel == word[0]:
        channel = 'Private'
    message = '%s: %s' % (word[0], word[1])
    send_pushover_message(channel,message)


# Hooks for different events
hexchat.hook_print("Channel Action Hilight", callback_channel)
hexchat.hook_print("Channel Msg Hilight", callback_channel)
hexchat.hook_print("Private Action to Dialog", callback_channel)
hexchat.hook_print("Private Message to Dialog", callback_channel)

# Notify plugin is loaded
hexchat.prnt('Pushbullet alert plugin loaded')
