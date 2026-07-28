[app]
title = OTG Clicker
package.name = otgclicker
package.domain = org.test
source.dir = .
source.include_exts = py,png,jpg,kv,atlas
version = 0.1

# 必備核心庫
requirements = python3,kivy,pyserial

orientation = portrait
fullscreen = 0

android.permissions = INTERNET, USB_PERMISSION
android.api = 33
android.minapi = 21
android.ndk = 25b
android.accept_sdk_license = True
android.archs = arm64-v8a

[buildozer]
log_level = 2
warn_on_root = 1
