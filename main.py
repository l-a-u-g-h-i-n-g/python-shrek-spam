import time
import requests
POST_URL = "put POST url here" 
#thanks to liamhendricks for posting the raw TXT of the script
SCRIPT_URL = "https://gist.github.com/liamhendricks/5f8342659ff341b9dc4f328bca7be7da/raw/3c16a753975f73853aafa424d98f1500230785ef/shrek.txt"
HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36",
}
response = requests.get(SCRIPT_URL)
if response.status_code == 200:
    bee_movie_script = response.text.strip()  # Remove any leading/trailing spaces
    print("Script downloaded successfully!")
else:
    print("Failed to download script. Exiting...")
    exit()
chunks = [bee_movie_script[i:i+256] for i in range(0, len(bee_movie_script), 256)]

session = requests.Session()

for chunk in chunks:
    data = {"note": chunk}
    response = session.post(POST_URL, data=data, headers=HEADERS)

    if response.status_code == 200:
        print(f"Posted: {chunk[:30]}...")
    else:
	print(f"Failed with status code {response.status_code}")
        break
    time.sleep(0.5)

