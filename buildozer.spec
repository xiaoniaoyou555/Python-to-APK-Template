[app]

标题=记账
name=簿记
package.domain = org.test
source.dir = .
source.include_exts = py,png,jpg,kv,atlas
source.exclude_exts = spec
source.exclude_dirs = tests, bin, venv

版本=0.1

requirements = python3,kivy
权限=INTERNET
android.api = 33
android.ndk = 25b
android.sdk = 24
android.build_tools = 30.0.3
android.accept_sdk_license = True

[buildozer]
log_level = 2
warn_on_root = 0
