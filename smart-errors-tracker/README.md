# Smart Errors Tracker

Smart Errors Tracker, Flask ile geliştirilmiş web tabanlı bir hata takip sistemidir.  
Kullanıcıların sisteme üye olup giriş yapabildiği, hataları kaydedebildiği ve otomatik çözüm önerileri alabildiği bir uygulamadır.

---

##  Özellikler

- Kullanıcı kayıt ve giriş sistemi (Register / Login / Logout)
- Hata ekleme ve silme işlemleri
- Otomatik çözüm önerisi (basit AI mantığı)
- Dashboard üzerinde hata istatistikleri (Kritik / Orta / Düşük)
- Kullanıcıya özel hata görüntüleme
- Modern ve responsive arayüz (Bootstrap 5)

---

##  Kullanılan Teknolojiler

- Python
- Flask
- SQLite
- SQLAlchemy
- Bootstrap 5

---

##  Kurulum Adımları

###  1.Projeyi klonlayın
```bash
git clone https://github.com/KULLANICI_ADINIZ/smart-errors-tracker.git
cd smart-errors-tracker



2. Sanal ortam oluşturun (isteğe bağlı)
python -m venv venv
source venv/bin/activate   # Mac/Linux
venv\Scripts\activate      # Windows

3. Gerekli paketleri yükleyin
pip install flask flask_sqlalchemy werkzeug

4️. Uygulamayı çalıştırın
python app.py


Tarayıcıda açın:
http://127.0.0.1:5050





 Proje Yapısı
smart-errors-tracker/
│
├── app.py
├── models.py
├── README.md
│
├── templates/
│   ├── base.html
│   ├── login.html
│   ├── register.html
│   ├── index.html
│   ├── add.html
│
└── instance/
    └── errors.db


Projenin Amacı

Bu proje, yazılım projelerinde oluşan hataların merkezi bir panel üzerinden takip edilmesini sağlamak amacıyla geliştirilmiştir.
Aynı zamanda kullanıcı bazlı veri yönetimi ve temel düzeyde otomatik çözüm önerisi mantığını içermektedir.

Gelecek Geliştirmeler

REST API desteği
JWT tabanlı kimlik doğrulama
OpenAI entegrasyonu
Grafiksel analiz ekranı
Dark mode
Canlı sunucuya deploy


Geliştirici
Zeynep Manap