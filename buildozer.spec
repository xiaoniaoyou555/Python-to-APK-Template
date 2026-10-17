[app]
#标题允许中文标题语言不限
标题=记账
package.name = packagename

#发布模式不能用 org.test'org.test
domain=org.簿记
#工作目录工作目录
source.dir = .
#需要打包的文件类型文件类型要打包
source.include_exts = py,png,jpg,kv,atlas
#打包 image limage liveyodo youse Pack youp you you you you you big you big
#source.include_patterns = image/*
version = 0.0.1
#依赖库，你需要最后两个是包装
requirements = python3,kivy,libiconv,libffi
#icon.filename = icon.png
#presplash.filename = presplash.png
#fullscreen = 0
#定向=肖像
#主程序 Main，我能说什么呢
entrypoint = main.py

这些不要改不要换这些
android.accept_sdk_license = True
android.allow_api_min = 21
android.api = 33
android.minapi = 21
android.ndk = 25b
exclude_patterns = **/test/*, **/tests/*
android.gradle_download = https://services.gradle.org/distributions/gradle-7.6.4-all.zip
android.gradle_plugin = 7.4.2
android.sdk = 33
android.ndk_api = 21
p4a.gradle_dependencies = gradle:7.6.4
p4a.bootstrap = sdl2
p4a.gradle_options = -Dorg.gradle.java.home=/usr/lib/jvm/java-17-openjdk-amd64
p4a.gradle_options = -Dorg.gradle.java.home=/usr/lib/jvm/java-17-openjdk-amd64
#android.keystore_keypass = android#强制构建 APK是AAB，它为什么要构建. AAB而不是. APK？

#以下为 release，请问release mode需要以下几点

#android. keystore_keypass=android#强制构建 you apaab，you you you。AAB而不是
#以下为发布，您的发布模式

#android.keystore_alias = DomainName.PackageName
log_level = 2
#签名配置签名配置
#android.aab = False
#签名配置签名配置

[buildozer]
log_level = 2
warn_on_root = 1
