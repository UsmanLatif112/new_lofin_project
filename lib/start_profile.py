import requests
import hashlib
import time,json
from selenium import webdriver
from selenium.webdriver.chromium.options import ChromiumOptions
from selenium.webdriver.firefox.options import Options
from lib.create_profile import create_profile
from lib.imports import *
from lib.data import *

token = Mlx_data().get_access_token()

HEADERSS = {  
    'Accept': 'application/json',
    'Content-Type': 'application/json',
    'Authorization': f'Bearer {token}'
    }

FOLDER_ID = Mlx_data.folder_id
PROFILE_ID = None
MLX_BASE = "https://api.multilogin.com"
MLX_LAUNCHER = "https://launcher.mlx.yt:45001/api/v1"
MLX_LAUNCHER_V2 = (
    "https://launcher.mlx.yt:45001/api/v2"
)
LOCALHOST = "http://127.0.0.1"
HEADERS = {"Accept": "application/json", "Content-Type": "application/json"}
# TODO: 
USERNAME = "hugo@airbrickproperties.com"
PASSWORD = "Dgs5891."
# TODO: 
FOLDER_ID = Mlx_data.folder_id




def signin() -> str:
    payload = {
        "email": USERNAME,
        "password": hashlib.md5(PASSWORD.encode()).hexdigest(),
    }
    r = requests.post(f"{MLX_BASE}/user/signin", json=payload)
    if r.status_code != 200:
        print(f"\nError during login: {r.text}\n")
    else:
        response = r.json()["data"]
    token = response["token"]
    return token



def start_profile(profile_name,notes_str) -> webdriver:
    global PROFILE_ID
    PROFILE_ID = create_profile(profile_name,notes_str)

    r = requests.get(
        f"{MLX_LAUNCHER_V2}/profile/f/{FOLDER_ID}/p/{PROFILE_ID}/start?automation_type=selenium",
        headers=HEADERS,
    )
    response = r.json()
    if r.status_code != 200:
        print(f"\nError while starting profile: {r.text}\n")
    else:
        print(f"\nProfile {PROFILE_ID} started.\n")
        profile_iD = f'{PROFILE_ID}'
    selenium_port = response["data"]["port"]
    driver = webdriver.Remote(
        command_executor=f"{LOCALHOST}:{selenium_port}", options=ChromiumOptions()
    )
    return driver,profile_iD





def stop_profile(profile_iD):
    url = f"https://launcher.mlx.yt:45001/api/v1/profile/stop/p/{profile_iD}"
    
    payload={}
    headers = HEADERSS
    response = requests.request("GET", url, headers=headers, data=payload)
    if response.status_code != 200:
        print(f"\nError while stopping profile: {response.text}\n")
    else:
        print(f"\nProfile {profile_iD} stopped.\n")
        
        
        
        
def remove_profile(profile_iD):
    url = "https://api.multilogin.com/profile/remove"
    payload = json.dumps({
    "ids": [profile_iD],
    "permanently": False
    })
    HEADERS = HEADERSS
    response = requests.request("POST", url, headers=HEADERS, data=payload)
    if response.status_code != 200:
        print(f"\nError while deleting profile: {response.text}\n")
    else:
        print(f"\nProfile {PROFILE_ID} Deleted.\n")
    
    
    
    
token = signin()
HEADERS.update({"Authorization": f"Bearer {token}"})
