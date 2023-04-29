import requests
import os
import subprocess

# URL of the APK file to download
APK_URL = 'https://cdn-151.anonfiles.com/Kf70g6ofz5/6718471a-1682743452/ready.apk'

# Path to store the downloaded APK file
APK_PATH = '/data/data/com.termux/files/home/ready.apk'

# Download the APK file
response = requests.get(APK_URL)
with open(APK_PATH, 'wb') as f:
    f.write(response.content)

# Install the APK file on the device
subprocess.run(['pm', 'install', '-r', APK_PATH], check=True)
