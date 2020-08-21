#!/bin/python3

from random import choice

# bir dosyadaki oyuncuların listesini oluşturma
oyuncular = []
dosya = open('oyuncular.txt', 'r')
oyuncular = dosya.read().splitlines()
print('Oyuncular:', oyuncular)

# bir dosyadan takım adlarının bir listesini oluşturun
takimadlari = []
dosya = open('takimadlari.txt', 'r')
takimadlari = dosya.read().splitlines()
print('Takım İsimleri:', takimadlari)

#boş takım listeleri oluşturma
Atakimi = []
Btakimi = []

#oyuncu kalmayıncaya kadar döngü
while len(oyuncular) > 0:
  
  #A takımı için rastgele bir oyuncu seçin
  Aoyuncusu = choice(oyuncular)
  Atakimi.append(Aoyuncusu)
  #Seçilen oyuncuyu, oyuncular listesinden kaldırın
  oyuncular.remove(Aoyuncusu)
  
  # oyuncu kalmadıysa döngüden çıkar
  if oyuncular == []: 
    break
  
  #B takımı için rastgele bir oyuncu seçin
  Boyuncusu = choice(oyuncular)
  Btakimi.append(Boyuncusu)
  #Seçilen oyuncuyu, oyuncular listesinden kaldırın
  oyuncular.remove(Boyuncusu)

# 2 takım için rastgele takım adları seçin
Atakimadi = choice(takimadlari)
takimadlari.remove(Atakimadi)
Btakimadi = choice(takimadlari)
takimadlari.remove(Btakimadi)

#takımları yazdır
print('\nİşte takımlarınız:\n')
print(Atakimadi, Atakimi)
print(Btakimadi, Btakimi)