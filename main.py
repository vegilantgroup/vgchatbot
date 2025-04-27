import os
import json
import random


if os.name == "nt":
    os.system("cls")
elif os.name == "posix":
    os.system("clear")

def banner():
    return """                                                                            
              @@@@@@@                            @@@@@                              
               @@++@@@                          @@++@                               
                @@+++@@                        @@+++@@@@@@@@@@@@@                   
                 @@+++@@                      @@++++++++++++++++@@@                 
                  @@+++@@                    @@+@@@@@@@@@@@@@@@+++@                 
                   @@#++@@                  @@+@@             @@@@@                 
                    @@@++@@                @@+@@               @ #                  
                      @@++@@              @@+@@                                     
                       @@++@@            @@+@@                                      
                        @@++@@          @@+@@      @@@@@@@@@@@@@@@@                 
                         @@++@@        @@+@@       @@@@@@@@@@@@+++@                 
                          @@++@@      @@+@@                   @+++@                 
                           @@++@@    @@+@@                    @++=@                 
                            @@++@@  @@+@@                     @+++@                 
                             @@++@@@@++@                      @+++@                 
                              @@+++++++@@@@@@@@@@@@@@@@@@@@@@@@+++@                 
                               @@++++++++++++++++++++=++++++++++@@@                 
                                @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@    

                                                        Coded by VegilantGroup                                                                             
"""

veri_dosyası = "chatbot_veri.json"

# Eğitim verisini yükleme fonksiyonu
def veriyi_yükle():
    try:
        with open(veri_dosyası, "r") as dosya:
            return json.load(dosya)
    except FileNotFoundError:
        return {}

def veriyi_kaydet(veri):
    with open(veri_dosyası, "w") as dosya:
        json.dump(veri, dosya, indent=4)

# soru eşleştirme vs. basit bir doğal dil işleme fonksiyonu
def en_iyi_eşleşme(kullanıcı_girişi, chatbot_verisi):
    benzerlik_puanları = {}
    
    # Kullanıcı inputunu küçük harfe çevirip anahtar kelimelere ayırıyoruz
    kullanıcı_girişi = kullanıcı_girişi.lower().split()

    for soru, cevaplar in chatbot_verisi.items():
        # json'daki soruyu anahtar kelimelere ayırıyoruz
        soru_anahtar_kelimeler = soru.lower().split()
        # Ortak anahtar kelimeleri buluyoruz (benzerleri alıyoruz)
        ortak_anahtar_kelimeler = set(kullanıcı_girişi) & set(soru_anahtar_kelimeler)
        
        benzerlik_puanları[soru] = len(ortak_anahtar_kelimeler)

    # En yüksek ortak anahtar kelime sayısına sahip soruyu alıyoruz
    en_iyi_soru = max(benzerlik_puanları, key=benzerlik_puanları.get)
    return en_iyi_soru, random.choice(chatbot_verisi[en_iyi_soru])

def chatbot_eğit():
    print("Chatbot'u eğitmek için bir soru ve cevap girin (çıkmak için 'exit' yazın):")
    chatbot_verisi = veriyi_yükle()

    while True:
        soru = input("Soru: ")
        if soru.lower() == "exit":
            break
        
        # Eğer soru zaten var ise, cevap ekleme işlemi yapıcaz
        if soru in chatbot_verisi:
            cevap = input(f"Bu soruya eklemek istediğiniz cevabı girin ({len(chatbot_verisi[soru])} mevcut cevap): ")
            chatbot_verisi[soru].append(cevap)
        else:
            cevap = input("Cevap: ")
            chatbot_verisi[soru] = [cevap]

        veriyi_kaydet(chatbot_verisi)
        print(f"Soru-Cevap başarıyla eklendi! ({soru}: {cevap})\n")

def chatbot_ile_sohbet_et():
    chatbot_verisi = veriyi_yükle()

    print("\nChatbot ile sohbet etmeye başlayın (çıkmak için 'exit' yazın):")
    while True:
        kullanıcı_girişi = input("Siz: ")
        if kullanıcı_girişi.lower() == "exit":
            break
        
        # Benzerlik hesaplama ve en iyi cevabı almayı burada yapıyoruz
        en_iyi_soru, cevap = en_iyi_eşleşme(kullanıcı_girişi, chatbot_verisi)
        print(f"Chatbot: {cevap}")

def ana():
    print(banner())
    print("VGChatbot - 1.0")
    while True:
        print("\n1. Chatbot ile sohbet et")
        print("2. Chatbot'u eğit")
        print("3. Çıkış")
        seçim = input("Seçiminizi yapın: ")

        if seçim == "1":
            chatbot_ile_sohbet_et()
        elif seçim == "2":
            chatbot_eğit()
        elif seçim == "3":
            print("Çıkılıyor...")
            break
        else:
            print("Geçersiz seçenek, tekrar deneyin.")

if __name__ == "__main__":
    ana()
