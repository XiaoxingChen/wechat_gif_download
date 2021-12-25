import itchat, time
from itchat.content import *
import re
import os
import shutil

img_counter = 0

def checkImageType(filename):
    with open(filename, 'rb') as f:
        s = f.read()
        if s[0:4] == b'\xff\xd8\xff\xe0':
            return 'jpg'
        if s[0:3] == b'GIF':
            return 'gif'
        if s[0:4] == b'\x89PNG':
            return 'png'
        return 'txt'

@itchat.msg_register(INCOME_MSG)
def text_reply(msg):
    pattern = 'cdnurl = "(.*?)"'

    if msg.MsgType == 47:
        # print("msg.Content: {}".format(msg.Content))
        url = re.search(pattern, msg.Content).groups()[0]
        # url = url.replace("&amp;", "&")
        cache_name = ''
        if "stodownload" in url:
            cache_name = 'stodownload'
            url = url.replace("&amp;", "%26")
            url = url.replace("?", "%3F")
            print(url)
            return
        else:
            cache_name = 'index.html'
            print(url)
        os.system('wget {}'.format(url))

        img_type = checkImageType(cache_name)
        target_filename = str(img_counter) + '.' + img_type
        shutil.move(cache_name, os.path.join('pics', target_filename))

if not os.path.isdir('pics'):
    os.mkdir('pics')
itchat.auto_login(True, enableCmdQR=False)
itchat.run()

