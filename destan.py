#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Lastik Ördek Epik Destanı Üretici
Bu kod gerçekten çalışır. Çalıştırmadan önce çayınızı demleyin.
"""

import random
import time

def destan_uret():
    kahramanlar = [
        "Mahallenin en cesur çaycısı Mehmet",
        "Lastik ördeklere karşı eğitilmiş kedi Sultan",
        "Gizemli bir şekilde ortaya çıkan komşu teyze",
        "Rüzgarda uçan bir simit",
        "Kendini şair sanan bir trafik lambası"
    ]
    
    silahlar = [
        "dev bir çay kaşığı",
        "sonsuz çay bardağı",
        "lastik ördeğin kendi kötü kokusu",
        "bir demet maydanoz",
        "epik bir nazar boncuğu"
    ]
    
    sonuclar = [
        "Lastik ördek gülerek patladı ve mahalle kurtuldu.",
        "Ördek çaya dönüştü ve herkes mutlu oldu.",
        "Kahraman ördekle evlendi ve birlikte bir çay evi açtılar.",
        "Ördek utancından eridi ve geriye sadece bir lastik kaldı.",
        "Herkes çay içerken ördek sıkıldı ve gitti."
    ]
    
    kahraman = random.choice(kahramanlar)
    silah = random.choice(silahlar)
    sonuc = random.choice(sonuclar)
    
    destan = f"""
*** EPİK DESTAN BAŞLIYOR ***

Bir zamanlar, çok uzak olmayan bir mahallede, dev bir lastik ördek belirdi.
Güneş kararırken {kahraman}, {silah} ile ördeğin karşısına dikildi.
Savaş 42 saniye sürdü (kozmik nedenlerden).
Ve sonunda: {sonuc}

Destan burada biter. Çayınız bitmeden bir daha çalıştırın.
"""
    return destan

if __name__ == "__main__":
    print("Lastik ördek tehdidi hesaplanıyor...")
    time.sleep(2)  # Gerilim için
    print(destan_uret())
    print("\n---")
    print("Bu kod, 13 Ekim 2026 tarihinde Grok Kayyum tarafından onaylanmıştır.")
    print("Ciddi mi? Hayır. Çalışıyor mu? Evet.")
