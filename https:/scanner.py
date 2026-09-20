# Pmw Tool by msd773 - Yemen
import requests
url = input("ادخل رابط الموقع: ")
if not url.startswith("http"):
    url = "https://" + url
try:
    r = requests.get(url, timeout=5)
    print(f"\n[+] الموقع: {url} - الحالة: {r.status_code}")
    print("[✔] محمي" if "X-Frame-Options" in r.headers else "[✘] غير محمي")
except:
    print("[-] الموقع غير متاح")
