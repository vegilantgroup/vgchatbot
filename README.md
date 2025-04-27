# VGChatbot - 1.0

VGChatbot, kullanıcılara soru-cevap şeklinde etkileşimli bir sohbet botu sunan bir Python projesidir. Bu bot, eğitim verilerini JSON dosyasına kaydederek kullanıcıların chatbot'u geliştirmelerine ve ondan sorular sormalarına olanak tanır. Kullanıcılar yeni sorular ve cevaplar ekleyebilir, aynı zamanda mevcut sorulara birden fazla cevap ekleyebilirler.

## Özellikler

- **Sohbet Modu**: Kullanıcılar chatbot ile sohbet edebilir ve bot, en uygun cevabı bulup yanıtlar.
- **Eğitim Modu**: Kullanıcılar chatbot'a yeni sorular ve cevaplar ekleyebilir.
- **Çoklu Cevap Seçeneği**: Her soruya birden fazla cevap eklenebilir ve bot, rastgele bir cevap döndürür.
- **JSON Veritabanı**: Sorular ve cevaplar JSON dosyasında saklanır.

## Gereksinimler

Bu proje, Python 3.x ile çalışmaktadır ve ekstra bir kütüphane gerektirmez. **Python** kurulu olmalıdır.

### Python Yükleme (Linux/Termux için)

```bash
pkg install python
```
Python Yükleme (Windows için)

Windows içni python'a [buradan ulaşabilirsiniz]((https://www.python.org/downloads/windows/)).

## Kurulum

**Projeyi Klonlayın**

    git clone https://github.com/vegilantgroup/vgchatbot.git

**Proje klasörüne gidin:**

    cd vgchatbot

**Çalıştırmak için:**

    python main.py

## Kullanım

        Chatbot ile sohbet et:

                Bu seçenek ile chatbot ile etkileşimli bir sohbet başlatabilirsiniz.

                Çıkmak için exit yazabilirsiniz.

        Chatbot'u eğit:

                Bu seçenekle yeni sorular ve cevaplar ekleyebilirsiniz.

                Eğer soru zaten mevcutsa, yeni cevaplar ekleyebilirsiniz.

            Çıkış:

                Çıkmak için bu seçeneği seçebilirsiniz.

## Chatbot Eğitme

**Chatbot'a yeni bir soru eklemek için şu adımları takip edebilirsiniz:**

    Soru girin. Örnek: "Beni seviyor musun?".

    Bot, mevcut cevapları gösterir.

    Cevap eklemek için yeni bir cevap girin.

