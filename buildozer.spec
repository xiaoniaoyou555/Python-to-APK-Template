[app]
#标题允许中文标题语言不限
title = 记账
package.name = bookkeeping
package.domain = org.bookkeeping

#工作目录
source.dir = .
#需要打包的文件类型
source.include_exts = py,png,jpg,kv,atlas

version = 0.0.1
#依赖库
requirements = python3,kivy

#icon.filename = icon.png
#presplash.filename = presplash.png
#fullscreen = 0
#定向=肖像

android.accept_sdk_license = True
android.api = 33
android.minapi = 21
android.ndk = 25b
exclude_patterns = **/test/*, **/tests/*
android.gradle_download = https://services.gradle.org/distributions/gradle-7.6.4-all.zip
android.gradle_plugin = 7.4.2
android.sdk = 33
android.ndk_api = 21
p4a.bootstrap = sdl2
p4a.gradle_options = -Dorg.gradle.java.home=/usr/lib/jvm/java-17-openjdk-amd64

log_level = 2
#android.aab = False

[buildozer]
log_level = 2
warn_on_root = 1
