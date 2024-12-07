# gunicorn_config.py

# Sunucuya yönelik temel ayarlar
bind = '0.0.0.0:5000'  # Uygulama hangi IP ve port üzerinden çalışacak
workers = 1  # Sadece 1 worker kullanılacak
threads = 2  # Eğer işlem başına birden fazla thread kullanmak isterseniz, burada ayar yapılabilir
worker_class = 'sync'  # Basit bir worker sınıfı, eğer başka bir iş yükü türü kullanacaksanız (async vs. gevent vs.) değiştirebilirsiniz
timeout = 120  # Zaman aşımı süresi (istek işleme süresi) 120 saniye
loglevel = 'info'  # Log seviyesini ayarlayın
accesslog = '-'  # Erişim loglarını konsola yazdır
errorlog = '-'  # Hata loglarını konsola yazdır
