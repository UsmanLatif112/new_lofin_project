import requests
import json
class Mlx_data:
    tokenn = "eyJhbGciOiJIUzUxMiJ9.eyJicGRzLmJ1Y2tldCI6Im1seC1icGRzLXByb2QtZXUtMSIsImVtYWlsIjoiaHVnb0BhaXJicmlja3Byb3BlcnRpZXMuY29tIiwiaXNBdXRvbWF0aW9uIjpmYWxzZSwibWFjaGluZUlEIjoiIiwicHJvZHVjdElEIjoibHQiLCJzaGFyZElEIjoiY2JlMTM4MDAtYmJhZi00YzhmLTgwYjMtMTk3Zjg5NjM5NGYyIiwidGVuYW50SUQiOiJtbHgiLCJ1c2VySUQiOiIxZjA3M2M1Yi1lNTRiLTQ0NjctYTI4ZS0xMDU1MWIyZGVhZDciLCJ2ZXJpZmllZCI6dHJ1ZSwid29ya3NwYWNlSUQiOiJhYzk0ZWE4OS00NWQ2LTQzZmYtODU1Yi05M2I3OWY0MGM5NjEiLCJ3b3Jrc3BhY2VSb2xlIjoib3duZXIiLCJqdGkiOiIxNTEzOTBlOS00YThlLTQxZWItYWRiOC03NmMyNDc4MTYyMTEiLCJzdWIiOiJNTFgiLCJpc3MiOiIxZjA3M2M1Yi1lNTRiLTQ0NjctYTI4ZS0xMDU1MWIyZGVhZDciLCJpYXQiOjE3MjI0NTM0ODQsImV4cCI6MTcyMjQ1NzA4NH0.37zJzHWC0aZMKRyXgMiQs7a1hCc_hl_8JAXQFRG5BzdBWgvhRrqIi0kZj5RUAAdFof50_kc9MaXccCRC0BZy4w"
    folder_id = "725851d5-eac0-498b-9781-e1b358c69ff1"
    
    def get_access_token(self):
        req_url = "https://api.multilogin.com/user/signin"
        
        headers_list = {
            "Accept": "*/*",
            "User-Agent": "Thunder Client (https://www.thunderclient.com)",
            "Content-Type": "application/json"
        }
        
        payload = json.dumps({
            "email": "hugo@airbrickproperties.com",
            "password": "d11be2c5acb7c67a95bd940287b40368"
        })
        
        response = requests.post(req_url, data=payload, headers=headers_list)
        
        if response.status_code == 200:
            return response.json()['data'].get('token', 'No token found')
        else:
            return f"Error: {response.status_code}, {response.text}"
    

class Login_Credentials:
    user_name = "latifusman107@gmail.com"
    pass_word = "Usman@112"
    









 
    
    

# csv_file_path = "Keywords.csv"

# with open(csv_file_path, "r") as file:
#     reader = csv.reader(file)
#     next(reader)
#     for row in reader:
        # accptance_modalll = HomePage(driver)
        # accptance_modalll.wait(Google.accptance_modal)   
                               
        # modall = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, Google.accptance_modal)))
        
# import pdb;
# pdb.set_trace()