import requests
import os

def download_default_background():
    if not os.path.exists("background.jpg"):
        try:
            url = "https://images.unsplash.com/photo-1517248135467-4c7edcad34c4?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D&auto=format&fit=crop&w=2070&q=80"
            response = requests.get(url)
            with open("background.jpg", "wb") as f:
                f.write(response.content)
            print("Downloaded default background image")
        except Exception as e:
            print(f"Couldn't download background image: {e}")

if __name__ == "__main__":
    download_default_background() 