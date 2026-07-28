[app]
title = OTG Clicker
package.name = otgclicker
package.domain = org.test
source.dir = .
source.include_exts = py,png,jpg,kv,atlas
version = 0.1

# 核心套件
requirements = python3,kivy

orientation = portrait
fullscreen = 0

# 相容性最穩定的 Android SDK & NDK 設定
android.permissions = INTERNET, USB_PERMISSION
android.api = 31
android.minapi = 21
android.ndk = 23b
android.accept_sdk_license = True
android.archs = arm64-v8a

[buildozer]
log_level = 2
warn_on_root = 1
