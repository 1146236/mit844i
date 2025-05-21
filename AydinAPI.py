import urllib.request
import json
import csv
from io import StringIO

url = 'https://admin.opendata.az/api/3/action/package_show?id=azerbaycanin-milli-parklari'

try:
    with urllib.request.urlopen(url) as response:
        data = json.loads(response.read().decode())

        if data.get('success'):
            result = data['result']
            print(f"\nTitle: {result.get('title', 'No title')}")
            print(f"Name: {result.get('name', 'No name')}")
            print(f"Notes: {result.get('notes', 'No description')}\n")

            # Find the first CSV resource
            resources = result.get('resources', [])
            csv_url = None
            for res in resources:
                if res.get('format', '').lower() == 'csv':
                    csv_url = res.get('url')
                    break

            if csv_url:
                print("Fetching CSV data...\n")
                with urllib.request.urlopen(csv_url) as csv_response:
                    csv_bytes = csv_response.read()
                    csv_text = csv_bytes.decode('utf-8')  # decode bytes to string

                # Use StringIO to parse the CSV text
                csv_file = StringIO(csv_text)
                reader = csv.reader(csv_file)

                # Print each row
                for row in reader:
                    print(" | ".join(row))
            else:
                print("No CSV resource found.")
        else:
            print("API response was not successful.")

except urllib.error.URLError as error:
    print('Error fetching data:', error)
