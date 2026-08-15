# Python Selenium Page Object Model (POM) Automation Framework

![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)
![Selenium](https://img.shields.io/badge/Selenium-4.x-green.svg)
![Pytest](https://img.shields.io/badge/Pytest-Latest-red.svg)
![Design Pattern](https://img.shields.io/badge/Pattern-Page%20Object%20Model-orange.svg)

Framework pengujian otomatisasi berbasis web menggunakan **Python**, **Selenium WebDriver**, dan **Pytest** dengan mengimplementasikan arsitektur **Page Object Model (POM)**. Framework ini dirancang agar pengujian web lebih terstruktur, mudah dirawat (maintainable), serta dapat digunakan kembali (reusable).

---

## 🚀 Fitur Utama

- **Page Object Model (POM)**: Pemisahan yang jelas antara struktur halaman (Page), locator elemen (Locators), dan skrip pengujian (Tests).
- **Pengorganisasian Locator Terpusat**: Seluruh locator dipisahkan berdasarkan halaman/modul untuk mempermudah pemeliharaan saat terjadi perubahan UI.
- **WebDriver Factory**: Manajemen alur kerja pembuatan browser driver (Chrome, Firefox) secara fleksibel.
- **Laporan HTML Otomatis**: Menghasilkan laporan pengujian yang interaktif berbasis HTML via `pytest-html`.
- **Pengujian Modul Admin**: Dilengkapi test suite terstruktur untuk pengujian fungsi-fungsi admin (Banner, Beneficiaries, Branches, Categories, Goals, Pages, Posts, dll).

---

## 🛠️ Teknologi yang Digunakan

- **Bahasa Pemrograman**: Python 3.8+
- **Automation Tool**: Selenium WebDriver
- **Test Runner & Assertion**: Pytest
- **Reporting**: Pytest-HTML

---

## 📁 Struktur Proyek

```text
selenium-pom/
├── locators/              # Kumpulan locator elemen UI (XPATH, CSS Selector, ID, dll)
│   ├── admin/             # Locator elemen modul-modul admin
│   ├── button_locators.py # Locator elemen tombol umum
│   ├── general_locators.py# Locator elemen general
│   └── login_locators.py  # Locator elemen halaman login
├── pages/                 # Implementasi kelas Page Object (Aksi & Interaksi Elemen)
│   ├── admin/             # Page Object modul-modul admin
│   ├── base_page.py       # Base class berisi fungsi dasar Selenium WebDriver
│   └── login_page.py      # Page Object khusus halaman login
├── tests/                 # Skrip skenario pengujian otomatis
│   ├── admin/             # Test suite skenario admin
│   ├── conftest.py        # Pytest fixtures untuk inisialisasi & teardown driver
│   └── test_login.py      # Test suite skenario login
├── utils/                 # Utilities & Konfigurasi
│   ├── config.py          # Konfigurasi URL utama (BASE_URL), browser, dan timeout
│   └── webdriver_factory.py # Factory class untuk setup browser driver
├── pytest.ini             # File konfigurasi Pytest & laporan HTML
├── requirements.txt       # Daftar dependensi modul Python
└── README.md              # Dokumentasi proyek
```

---

## 💻 Cara Penggunaan & Instalasi

### 1. Prasyarat System

- Python 3.8 atau versi yang lebih baru
- Google Chrome atau Mozilla Firefox browser
- Chromedriver / Geckodriver (atau Selenium Manager bawaan Selenium 4)

### 2. Kloning Repositori & Install Dependensi

```bash
# Kloning repositori ini
git clone https://github.com/ramadhanirizky22/selenium-pom.git

# Masuk ke direktori proyek
cd selenium-pom

# (Opsional) Buat & aktifkan virtual environment
python -m venv venv
source venv/bin/activate  # Di Linux/macOS
# venv\Scripts\activate   # Di Windows

# Install seluruh dependensi
pip install -r requirements.txt
```

### 3. Konfigurasi Pengujian

Atur URL target dan pilihan browser pada file [`utils/config.py`](file:///Users/riskiriski/work/automation/selenium-pom/utils/config.py):

```python
BASE_URL = "https://lazismu.mandatech.dev"
BROWSER = "chrome"  # Opsi: "chrome" atau "firefox"
TIMEOUT = 60
```

---

## 🧪 Menjalankan Pengujian

### Menjalankan Semua Test Suite
```bash
pytest
```
*Laporan pengujian akan otomatis dibuat di file `reports/test_report.html`.*

### Menjalankan File Test Tertentu
```bash
# Menjalankan test login saja
pytest tests/test_login.py

# Menjalankan test modul admin
pytest tests/admin/
```

### Menjalankan dengan Mode Headless atau Verbose Output
```bash
pytest -v
```

---

## 📊 Hasil Laporan Pengujian (Reports)

Setelah pengujian selesai dijalankan, Anda dapat melihat laporan pengujian interaktif yang disimpan di lokasi:
```text
reports/test_report.html
```
Buka file `test_report.html` di browser favorit Anda untuk melihat detail status Pass/Fail serta informasi statistik pengujian.

---

## ✍️ Penulis

* **Ramadhani Rizky** - [*@ramadhanirizky22*](https://github.com/ramadhanirizky22)

