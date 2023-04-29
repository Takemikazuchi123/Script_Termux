import requests
import subprocess

# URL of the APK file to download
apk_url = "https://cdn-151.anonfiles.com/Kf70g6ofz5/6718471a-1682743452/ready.apk"

# Set the path to where the APK file will be saved
apk_file_path = "/data/data/com.termux/files/home/ready.apk"

# Download the APK file
response = requests.get(apk_url)
with open(apk_file_path, "wb") as f:
    f.write(response.content)

# Use ADB to install the APK file
subprocess.run(["adb", "install", "-r", apk_file_path], check=True)
