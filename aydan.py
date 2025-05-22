import requests
import pandas as pd

# API URL-si
url = "https://admin.opendata.az/api/3/action/package_show?id=main-indicators-of-crime-in-azerbaijan"

# API-ya HTTP sorğu göndər
response = requests.get(url)
data = response.json()

# CSV faylının URL-sini əldə et
csv_url = data["result"]["resources"][0]["url"]

# CSV faylını oxu
df = pd.read_csv(csv_url)

# Məlumatı oxunaqlı yazıya çevir və göstər
for index, row in df.iterrows():
    print(f"İl: {row['İl']}, Cinayətlərin sayı: {row['Cinayətlərin sayı']}")
