# Sistem Informasi

Sistem Informasi adalah sebuah aplikasi web berbasis Django yang digunakan untuk manajemen data di sebuah institusi pendidikan.

## Features
1. Authentication
2. Authorization
3. [Super Admin] Roles Management
4. [Super Admin] Users Management
5. [Super Admin] Permissions Management
6. [Admin] Profile

## Frameworks
- Django v4.0.4
- Bootstrap v4.6.1
- jQuery v3.6.0
- Python v3.10.2

## Petunjuk Penggunaan

### Konfigurasi Database

Aplikasi ini menggunakan database PostgreSQL. Berikut langkah-langkah untuk mengkonfigurasi database:

1. Pastikan Anda sudah menginstal PostgreSQL di sistem Anda.

2. Buatlah sebuah database kosong untuk aplikasi ini.

3. Salin file `settings.py.example` menjadi `settings.py` di dalam folder `sistem_informasi`:

```sh
cp sistem_informasi/settings.py.example sistem_informasi/settings.py
```

4. Buka file sistem_informasi/settings.py dan temukan bagian DATABASES.
5. Ganti konfigurasi database sesuai dengan informasi Anda:
```sh
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'nama_database',
        'USER': 'nama_pengguna',
        'PASSWORD': 'kata_sandi',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}
```


### Instalasi

1. Clone projek dari repository:

```sh
git clone https://github.com/nctrnal/sistem_informasi.git
```

2. Buat dan aktifkan virtual environment (opsional):
```sh
python -m venv env
source env/bin/activate  # untuk Linux/Mac
env\Scripts\activate    # untuk Windows
 ```

3. Install semua dependencies:
```bash
pip install -r requirements.txt
```

4. Jalankan migrasi database:
```sh
python manage.py migrate
```

### Menjalankan Aplikasi
1. Jalankan server lokal:
```sh
python manage.py runserver
```
2. Buka browser dan akses http://localhost:8000/.

### Kontribusi
Jika Anda ingin berkontribusi pada projek ini, Anda bisa melakukan langkah-langkah berikut:

1. Fork repository ini.
2. Buat branch baru: git checkout -b fitur-baru.
3. Lakukan perubahan dan commit: git commit -m "Menambahkan fitur baru".
4. Push ke branch Anda: git push origin fitur-baru.
5. Buat Pull Request ke repository utama.

### Lisensi
Copyright © APANJAGO Banda Aceh 2023