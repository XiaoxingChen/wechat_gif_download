import itchat, time
from itchat.content import *
import re
import os
import shutil

@itchat.msg_register(INCOME_MSG)
def text_reply(msg):
    pattern = 'cdnurl = "(.*?)"'
    # msg.Content
    # print("msg.Content: {}".format(msg.Content))
    if msg.MsgType == 47:
        url = re.search(pattern, msg.Content).groups()[0]
        url = url.replace("&amp;", "&")
        if "&amp;" in url:
            url = url.replace("&amp;", "&")
            print(url)
        else:
            print(url)
            os.system('wget {}'.format(url))
            target_filename = url.split('/')[-2] + '.gif'
            shutil.move('index.html', os.path.join('pics', target_filename))

if not os.path.isdir('pics'):
    os.mkdir('pics')
itchat.auto_login(True, enableCmdQR=False)
itchat.run()

