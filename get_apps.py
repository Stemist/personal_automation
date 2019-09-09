#!/usr/bin/env python

import wget
import os

print("----- Get Basic Apps -----")
print("By Christian Pearson, 2019")
print("Let's automate the downloading of basic applications for a new computer setup!")

# Get and display user's current directory.
current_dir = os.getcwd()
print("\n Current working directory is ", current_dir)

# Define the urls to download.
urls = {'Firefox': 'https://cdn.stubdownloader.services.mozilla.com/builds/firefox-stub/en-CA/win/474345d1b16d44aa0c2d3a59f2407a387253177aac1a252c8244fd5dd686e56f/Firefox%20Installer.exe',
        'chrome': 'https://dl.google.com/tag/s/appguid%3D%7B8A69D345-D564-463C-AFF1-A69D9E530F96%7D%26iid%3D%7B415B938C-26AA-A227-522B-75CCBD0F8145%7D%26lang%3Den%26browser%3D4%26usagestats%3D1%26appname%3DGoogle%2520Chrome%26needsadmin%3Dprefers%26ap%3Dx64-stable-statsdef_1%26installdataindex%3Dempty/update2/installers/ChromeSetup.exe',
        'seven_zip': 'https://www.7-zip.org/a/7z1902-x64.exe',
        'vlc': 'https://get.videolan.org/vlc/3.0.8/win64/vlc-3.0.8-win64.exe',
        'itunes': 'https://www.apple.com/itunes/download/win64',
        'adobe_reader': 'http://ardownload.adobe.com/pub/adobe/reader/win/AcrobatDC/1901220036/AcroRdrDC1901220036_en_US.exe'
        }

# Download the files.
for download_name in urls:
    try:
        filename = current_dir + '/' + download_name + '.exe' 
        print("\n File will be downloaded as ", filename)

        print("\n Fetching ", download_name, " from ", urls[download_name])
        wget.download(urls[download_name], filename)

    except Exception:
        print("ERROR: Could not fetch ", download_name)
        print("Check url is still valid.")

print("*** Done ***")