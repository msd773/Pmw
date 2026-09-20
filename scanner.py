# Pmw - Protection & Monitoring Web
# By msd773 | Yemen

import requests

print("Pmw Scanner by msd773 - Yemen")

url = input("ادخل رابط الموقع: ")
if not url.startswith("http"):
    url = "https://" + url

try:
    r = requests.get(url, timeout=5)
    print(f"الموقع: {url}")
    print(f"كود الحالة: {r.status_code}")
    
    if "X-Frame-Options" in r.headers:
        print("محمي من Clickjacking")
    else:
        print("غير محمي!")

    print("تم الفحص بواسطة msd773")

except:
    print("الموقع غير متاح")
