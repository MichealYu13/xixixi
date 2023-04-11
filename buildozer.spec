[app]

# (str) Title of your application
title = audio

# (str) Package name
package.name = podcast.audio.tallinn.yu.com

# (str) Package domain (needed for android/ios packaging)
package.domain = podcast.yu.com

# (str) Source code where the main.py live
source.dir = D:\vsprojects\PythonApplication2\PythonApplication2

# (list) Python files to add (will be compiled)
source.include_exts = py,kv

# (list) List of inclusions using pattern matching
#source.include_patterns = assets/*,images/*.png

# (list) List of exclusions using pattern matching
#source.exclude_patterns = license,images/*/*.jpg

# (str) Application versioning (method 1)
version = 1.2.0

# (str) Application versioning (method 2)
# version.regex = __version__ = ['"](.*)['"]
# version.filename = %(source.dir)s/main.py

# (list) Application requirements
requirements = speech_recognition, platform, pyttsx3

# (str) Custom source folders for requirements
# separate with commas (e.g. requirements/kivy)
# (default: '')
#requirements.source.kivy = ../../kivy

# (list) Garden requirements
#garden_requirements =

# (str) Presplash of the application
#presplash.filename = %(source.dir)s/data/presplash.png

# (str) Icon of the application
#icon.filename = %(source.dir)s/data/icon.png

# (str) Supported orientation (one of landscape, sensorLandscape, portrait or all)
orientation = portrait

# (bool) Whether to use the black theme or not
black_theme = True


# Android specific

# (bool) Indicate whether the application should be fullscreen or not
fullscreen = 1

# (string) Presplash background color (for new android toolchain)
# Supported formats are: #RRGGBB #AARRGGBB or one of the following names:
# red, blue, green, black, white, gray, cyan, magenta, yellow, lightgray,
# darkgray, grey, lightgrey, darkgrey, aqua, fuchsia, lime, maroon, navy,
# olive, purple, silver, teal.
#android.presplash_color = #FFFFFF

# (list) Permissions
android.permissions = INTERNET, RECORD_AUDIO

# (int) Target Android API, should be as high as possible.
android.api = 28

# (int) Minimum API your APK will support.
android.minapi = 21

# (int) Android SDK version to use
android.sdk = D:\Users\sdk

# (str) Android NDK version to use
#android.ndk = 

# (int) Android NDK API to use. This is the minimum API your app will support, it should usually match android.minapi.
#android.ndk_api = 

# (str) Android arch
android.arch = armeabi-v7a

# (bool) Use --private data storage (True) or --dir public storage (False)
#android.private_storage = True

# (str) Android entry point, default is ok for Kivy-based app
#android.entrypoint = org.kivy.android.PythonActivity

# (str) Android app theme, default is okay for Kivy-based app
#android.theme = '@android:style/Theme.NoTitleBar'

# (str) Android logcat filters to use
#android.logcat_filters = *:S python:D

