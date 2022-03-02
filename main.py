import math
from math import *

def sayi_al(min=0, max=10000): # Girilen sayıların hata kontrolü
    sayi = int(input("giriniz: "))
    while sayi < min or sayi > max:
        sayi = int(input("Yanlış değer girdiniz! Lütfen tekrar giriniz: "))
    return sayi

def oyuncu_al(oyuncu_liste,LNo,oyuncu_liste2): # Oyuncuların bilgilerinin alınması ve listeye geçirilmesi
    oyuncu_liste[1] = LNo
    ad_soyad_gecici = input("Lütfen ad ve soyadınızı giriniz: ")
    ad_soyad = ""
    for harf in ad_soyad_gecici:
        if harf == "i":
            ad_soyad += "İ"
        else:
            ad_soyad += harf.upper()

    oyuncu_liste[2] = ad_soyad
    print("Lütfen ELO'nuzu ",end="")
    elo = int(input("giriniz:"))
    if elo ==0:
        oyuncu_liste[3] = elo
    else:
        while elo < 1000:
            if elo == 0:
                oyuncu_liste[3] = elo
                break
            else:
                elo = int(input("Yanlış değer girdiniz! Lütfen tekrar giriniz: "))
        oyuncu_liste[3] = elo
    print("Lütfen UKD'nizi ",end="")
    ukd = int(input("giriniz:"))
    if ukd ==0:
        oyuncu_liste[4] = ukd
    else:
        while ukd < 1000:
            if ukd == 0:
                oyuncu_liste[4] = ukd
                break
            else:
                ukd = int(input("Yanlış değer girdiniz! Lütfen tekrar giriniz: "))
        oyuncu_liste[4] = ukd
    oyuncu_liste2.append(oyuncu_liste)
    return oyuncu_liste2

def buyukten_kucuge(oyuncu_liste2): # Listenin önceliklere göre sort işlemlerinin yapılması

    oyuncu_liste2.sort(key=lambda oyuncu_liste2: oyuncu_liste2[1])
    oyuncu_liste2.sort(key=lambda oyuncu_liste2: oyuncu_liste2[2])
    oyuncu_liste2.sort(key=lambda oyuncu_liste2: oyuncu_liste2[4], reverse=True)
    oyuncu_liste2.sort(key=lambda oyuncu_liste2: oyuncu_liste2[3], reverse=True)
    for i in range(len(oyuncu_liste2)): # Başlangıç sıra numaralarının, liste önceliklere göre sort edildikten sonra atanması !
        oyuncu_liste2[i][0] = i+1
        oyuncu_liste2[i][5] = 0 # herkese default 0 puan
        oyuncu_liste2[i][6] = ""
    return oyuncu_liste2

def rakip_bul(oyuncu_liste2, temp_beyaz_liste, temp_siyah_liste):
    durum = True # Döngünün kırılma koşulu
    durum2 = True # if içine hiç girmeme durumu
    i=1
    oyuncu_liste2.sort(key=lambda oyuncu_liste2: oyuncu_liste2[5], reverse=True)
    while ((i < len(oyuncu_liste2) and durum == True)):
        if (len(oyuncu_liste2) == 1):
            if (len(temp_beyaz_liste) <= len(temp_siyah_liste)):
                temp_beyaz_liste.append(oyuncu_liste2[0])
            else:
                temp_siyah_liste.append(oyuncu_liste2[0])

        elif (oyuncu_liste2[0][5] == oyuncu_liste2[i][5]):
            temp_beyaz_liste.append(oyuncu_liste2[0])
            temp_siyah_liste.append(oyuncu_liste2[i])
            durum = False
            oyuncu_liste2.remove(oyuncu_liste2[i])
            oyuncu_liste2.remove(oyuncu_liste2[0])

            durum2 = False# if'e girmedi --> ilk değeri ekle

        i+=1

    if(durum2):
        if (len(temp_beyaz_liste) <= len(temp_siyah_liste)):
            temp_beyaz_liste.append(oyuncu_liste2[0])
            oyuncu_liste2.remove(oyuncu_liste2[0])
        else:
            temp_siyah_liste.append(oyuncu_liste2[0])
            oyuncu_liste2.remove(oyuncu_liste2[0])


    return temp_beyaz_liste ,temp_siyah_liste

def rakip_ara(beyaz_liste, siyah_liste,oyuncu_liste2):
    temp_beyaz_liste1 = []
    temp_siyah_liste1 = []

    if(len(oyuncu_liste2) == 0):
        for i in range(len(beyaz_liste)):
            oyuncu_liste2.append(beyaz_liste[i])
        for j in range(len(siyah_liste)):
            oyuncu_liste2.append(siyah_liste[j])



    while(len(oyuncu_liste2) != 0):
        beyaz_liste, siyah_liste = rakip_bul(oyuncu_liste2, temp_beyaz_liste1, temp_siyah_liste1)

    return beyaz_liste, siyah_liste

def listeyi_birlestir(beyaz_liste,siyah_liste,oyuncu_liste2):
    for i in range(len(oyuncu_liste2)):
        for j in range(len(beyaz_liste)):
            if (beyaz_liste[j][0] == oyuncu_liste2[i][0]):
                oyuncu_liste2[i] = beyaz_liste[j]

    for k in range(len(oyuncu_liste2)):
        for t in range(len(siyah_liste)):
            if (siyah_liste[t][0] == oyuncu_liste2[k][0]):
                oyuncu_liste2[k] = siyah_liste[t]



    return oyuncu_liste2


def listeyi_yazdir(liste):
    for i in range(len(liste)):
        print(format(liste[i][0],">4"),end=" ")
        print(format(liste[i][1], ">6"), end=" ")
        print(format(liste[i][2], ">19"), end=" ")
        print(format(liste[i][3], ">6"), end=" ")
        print(format(liste[i][4], ">5"))


def eslestirme_olustur(baslangic_renk,beyaz_liste,siyah_liste,oyuncu_liste2):
    for i in range(len(oyuncu_liste2)):
        if oyuncu_liste2[i][0] % 2 == 1 and (baslangic_renk == "b" or baslangic_renk == "B"):
            oyuncu_liste2[i][6] = baslangic_renk
            beyaz_liste.append(oyuncu_liste2[i].copy())
        elif oyuncu_liste2[i][0] % 2 == 1 and (baslangic_renk == "s" or baslangic_renk == "S"):
            oyuncu_liste2[i][6] = baslangic_renk
            siyah_liste.append(oyuncu_liste2[i].copy())
        elif oyuncu_liste2[i][0] % 2 == 0 and (baslangic_renk == "b" or baslangic_renk == "B"):
            oyuncu_liste2[i][6] = baslangic_renk
            siyah_liste.append(oyuncu_liste2[i].copy())
        elif oyuncu_liste2[i][0] % 2 == 0 and (baslangic_renk == "s" or baslangic_renk == "S"):
            oyuncu_liste2[i][6] = baslangic_renk
            beyaz_liste.append(oyuncu_liste2[i].copy())
    return beyaz_liste,siyah_liste

def main():
    print("Lütfen lisans numaranızı ", end="")
    LNo = sayi_al()
    Lno_kontrol = []
    Lno_kontrol.append(LNo)
    oyuncu_liste2 = []
    oyuncu_say_kontrol=0
    while LNo > 0 :
        oyuncu_liste = [[0] for _ in range(7)]
        oyuncu_liste2=oyuncu_al(oyuncu_liste,LNo,oyuncu_liste2)
        oyuncu_say_kontrol+=1
        print("Lütfen lisans numaranızı giriniz: ", end="")
        LNo = int(input())
        for element in Lno_kontrol:
            while(element == LNo):
                LNo = int(input("Zaten olan bir lisans numarası girdiniz! Lütfen tekrar giriniz: "))
        Lno_kontrol.append(LNo)

    buyukten_kucuge(oyuncu_liste2)
    print()
    print("BSNo    LNo        Ad-Soyad        ELO   UKD\n"
          "----  -----    ----------------   ----  ----")
    listeyi_yazdir(oyuncu_liste2)
    print()

    baslangic_renk = input("Lütfen ilk oyuncunun başlangıç rengini giriniz(beyaz:b/siyah:s) :")
    while baslangic_renk not in ["b","B","s","S"]:
        baslangic_renk = input("Yanlış renk! Lütfen tekrar giriniz: ")

    tur_say = int(input("Lütfen tur sayısını giriniz: "))
    while (oyuncu_say_kontrol-1) < tur_say or ceil(math.log(oyuncu_say_kontrol,2)) > tur_say :
        tur_say = int(input("Yanlış tur sayısı! Lütfen tekrar giriniz: "))
    beyaz_liste = []
    siyah_liste = []
    beyaz_liste,siyah_liste = eslestirme_olustur(baslangic_renk,beyaz_liste,siyah_liste,oyuncu_liste2)

    oynanan_tur_say = 1

    for_tur_say = tur_say
    print()
    while (tur_say > 0):
        MNo = 1
        print("            Beyazlar                  Siyahlar\n")
        print("MNo    BSNo    LNo   Puan   -   Puan     LNo  BSNo\n"
              "---    ----  -----   ----       ----   -----  ----")
        if oyuncu_say_kontrol % 2 == 0:
            esit = int(oyuncu_say_kontrol/2)
            for i in range(esit):
                print(format(MNo, ">3"), end= "")
                print(format(beyaz_liste[i][0], ">8"), end=" ")
                print(format(beyaz_liste[i][1], ">6"), end=" ")
                print(format(beyaz_liste[i][5], ">6"),end=" ")
                print(format(siyah_liste[i][5], ">10"), end=" ")
                print(format(siyah_liste[i][1], ">7"), end=" ")
                print(format(siyah_liste[i][0], ">5"))
                MNo+=1
        else:
            esit = int(oyuncu_say_kontrol/2)
            for i in range(esit):
                print(format(MNo, ">3"), end="")
                print(format(beyaz_liste[i][0], ">8"), end=" ")
                print(format(beyaz_liste[i][1], ">6"), end=" ")
                print(format(beyaz_liste[i][5], ">6"), end=" ")
                print(format(siyah_liste[i][5], ">10"), end=" ")
                print(format(siyah_liste[i][1], ">7"), end=" ")
                print(format(siyah_liste[i][0], ">5"))
                MNo += 1
            # Burada masa no her döngüde 1 artırılıyor dolayısıyla, bye geçen oyuncu son masaya oturmuş gibi kabul edebiliriz.
            # O yüzden ekstra bir değişken kullanmak yerine MNo'yu tercih ettim. Masa numarası indeksi --> [MNo - 1]

            if baslangic_renk in ["b", "B"]:
                print(format(MNo, ">3"), end="")
                print(format(beyaz_liste[MNo-1][0], ">8"), end=" ")
                print(format(beyaz_liste[MNo-1][1], ">6"), end=" ")
                print(format(beyaz_liste[MNo-1][5], ">6"), end=" ")
                print(format("BYE", ">10"))
                beyaz_liste[MNo-1][5] += 1

            else:
                index = len(siyah_liste) - 1
                print(format(MNo, ">3"), end="")
                print(format(siyah_liste[index][0], ">8"), end=" ")
                print(format(siyah_liste[index][1], ">6"), end=" ")
                print(format(siyah_liste[index][5], ">6"), end=" ")
                print(format("BYE", ">10"))
                siyah_liste[index][5] += 1


        oynanan_masa_no = 1
        for i in range(for_tur_say-1):
            print("\n", oynanan_tur_say, ". turda oynanan", oynanan_masa_no,
                  ". masa numarasındaki maçın sonucunu giriniz(0-5): ")
            durum = int(input())
            while durum not in [0, 1, 2, 3, 4, 5]:
                durum = int(input("Yanlış girdiniz! Lütfen tekrar maçın sonucunu giriniz:"))
            oynanan_masa_no += 1
            if durum == 0:
                beyaz_liste[i][5] += 1 / 2
                siyah_liste[i][5] += 1 / 2
            elif durum == 1:
                beyaz_liste[i][5] += 1
            elif durum == 2:
                siyah_liste[i][5] += 1
            elif durum == 3:
                beyaz_liste[i][5] += 1
            elif durum == 4:
                siyah_liste[i][5] += 1
            # elif durum == 5:
                # draw.

        oyuncu_liste2 = listeyi_birlestir(beyaz_liste, siyah_liste, oyuncu_liste2)
        beyaz_liste, siyah_liste = rakip_ara(beyaz_liste, siyah_liste, oyuncu_liste2)
        listeyi_yazdir(oyuncu_liste2)
        oynanan_tur_say += 1
        tur_say -= 1



main()
