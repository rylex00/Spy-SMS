#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import requests
from os import system as s



banner = """
         >SPY - HACKERZ | SMS GÖNDERME ARACI	

         $$$$$$$$$  $$$$$$$$  $$$$#   #$$$$	
	 $$$        $$    $$     $$   $$  	
	 $$$$$$$$   $$$$$$$$       $$$	
	      $$$   $$             $$$		
	$$$$$$$$$   $$             $$$	       >Coder By Rylex

|> İstediginiz telefon adresine hergun 1 defa mesaj atma hakkınız vardır!
|> Mesajınızdaki karakter sayısı sınırlıdır.
|> Tel adresinizi Doğru girmezseniz hata vericektir.
|> Çalıştığını kendinizde deneyebilirsiniz.
"""

print(banner)

sor = input("Tel adresi Örn:+905555555555 >>> ")

mesaj = input("Mesajınız >>> ")

arlk = mesaj[0:70]

print("\n| Mesajınızın Gönderilebilecek kısmı aşagıdaki gibidir.\n"+arlk)

drlm = input("\n| Mesajınız Gönderilsinmi?[y/n] >>> ")

if drlm == "y" or drlm == "Y":
    print("\n"+sor+"\n"+arlk+"\n")
    resp = requests.post('https://textbelt.com/text', {
  'phone': sor,
  'message': arlk,
  'key': '393d3d2b1d7a087a28948c16b8bd1e2d83248a7aQDy8VU00Cf5n5CuRDNsjp0QZZ',
    })
    print(resp.json())

elif drlm == "n" or drlm == "N":
    quit()
else:
    print("\n|Hata yaptınız.")
