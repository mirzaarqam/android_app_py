[app]
title = Test_AND_APP
package.name = com.example.Test_AND_APP
source.dir = .
# Add this line
osx.python_version = 3
android.arch = armeabi-v7a
android.sdk = C:/Users/arqam.mirza/AppData/Local/Android/Sdk

source.include_exts = py,png,jpg,kv,atlas

version = 1.0  # Or your desired version number
# Or use version.regex to extract version from your code:
# version.regex = __version__ = ['"](.*)['"]

[buildozer]
log_level = 2
warn_on_root = 1
