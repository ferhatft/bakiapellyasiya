# Mahkeme Veri Yönetim Uygulaması

Bu Django tabanlı uygulama, mahkeme verilerinin tutulması ve araştırılmasına yönelik bir platform sağlar.

## Özellikler

- Mahkeme verilerinin güvenli bir şekilde depolanması ve yönetilmesi.
- Kullanıcıların mahkeme dosyalarını aramasına ve filtrelemesine olanak sağlayan gelişmiş filtreleme özelliği.
- Dosya aktarımlarını kolaylaştırmak için Django'nun önde gelen üçüncü taraf uygulamalarından bazılarının kullanılması (örneğin: django-import-export).
- Görsel olarak zengin içerik oluşturmak için Django CKEditor'un entegrasyonu.
- Mahkeme verilerini Excel, CSV veya diğer formatlarda aktarabilme ve içe aktarabilme imkanı.

## Başlarken

1. Projeyi bilgisayarınıza klonlayın.
2. Sanal bir ortam oluşturun ve bağımlılıkları yüklemek için `pip install -r requirements.txt` komutunu çalıştırın.
3. Veritabanını oluşturmak için `python manage.py migrate` komutunu çalıştırın.
4. Sunucuyu başlatmak için `python manage.py runserver` komutunu çalıştırın.
5. Tarayıcınızda `http://localhost:8000` adresine giderek uygulamayı görüntüleyebilirsiniz.

