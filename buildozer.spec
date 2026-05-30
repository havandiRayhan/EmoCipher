# buildozer.spec
# File konfigurasi untuk export app ke Android menggunakan Buildozer
# Letakkan file ini di folder yang sama dengan main.py

[app]

# ─── Identitas App ───
title = Emoji Cipher
package.name = emojichipher
package.domain = com.myapp

# File utama
source.dir = .
source.include_exts = py,png,jpg,kv,atlas,ttf

# Versi app
version = 1.0

# File yang dijalankan pertama kali
entrypoint = main.py

# ─── Dependensi ───
requirements = python3,kivy

# ─── Orientasi layar ───
# portrait = hanya vertikal, landscape = hanya horizontal
orientation = portrait

# ─── Ikon & splash screen ───
# Uncomment baris di bawah jika kamu punya file ikon sendiri:
# icon.filename = %(source.dir)s/icon.png
# presplash.filename = %(source.dir)s/splash.png

# ─── Izin Android ───
# Tambahkan izin yang dibutuhkan app kamu di sini
android.permissions = INTERNET

# ─── Target Android ───
android.minapi = 21
android.sdk = 33
android.ndk = 25b
android.archs = arm64-v8a, armeabi-v7a

# ─── iOS (opsional, perlu Mac) ───
# ios.kivy_ios_url = https://github.com/kivy/kivy-ios
# ios.kivy_ios_branch = master

[buildozer]

# Level log: 0 = error saja, 1 = info, 2 = debug
log_level = 2

# Apakah otomatis install dependensi yang kurang?
warn_on_root = 1
