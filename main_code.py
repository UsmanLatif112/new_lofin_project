import os
import requests
from lib.start_profile import *
from lib.resources import Login,Code,Captcha
from lib.function import *
from lib.data import *
WEB_APP_URL = 'http://13.48.229.102:5000'
# from twocaptcha import TwoCaptcha
"""=================================================="""

# solver = TwoCaptcha('c102b4fcaed58016e9fc39489ae89415')
"""=================================================="""
def increment_number_in_file(file_path='profile_count.txt'):
    # Check if the file exists
    if os.path.exists(file_path):
        # Read the current number from the file
        with open(file_path, 'r') as file:
            try:
                number = int(file.read().strip())
            except ValueError:
                print("The file does not contain a valid integer.")
                return
        # Increment the number by one
        number += 1
    else:
        # If the file does not exist, initialize the number to 0
        number = 1
    
    # Write the number back to the file
    with open(file_path, 'w') as file:
        file.write(str(number))
    return number

def main_code(username, password,session_id):
    
    try:
        driver,profile_iD= start_profile(
            profile_name=f"#{increment_number_in_file()} {username}",
            notes_str=f"Email:{username};Password:{password}"
        )
    except Exception as e:
        print(e)
        time.sleep(3)
        driver,profile_iD= start_profile(
            profile_name=f"#{increment_number_in_file()} {username}",
            notes_str=f"Email:{username};Password:{password}"
        )
        
    driver.maximize_window()
    prgroess_obj ={
        "is_2f_required":False,
        "login_pass_status":False,
        "login_fail_status":False,
        "is_security_check_found":False
    }
    driver.get("https://www.linkedin.com/login")
    print(f"MLX profile id is {profile_iD}")
    time.sleep(2)
    try:
        Sign_btnn = HomePage(driver)
        Sign_btnn.wait_ten(Login.SIGN_BTN)
        time.sleep(2)
        if Sign_btnn:
            print("sign in btton")
            try:
                Username = HomePage(driver)
                Username.click_btn(Login.USERNAME)  
                time.sleep(.5)
                Username = HomePage(driver)
                Username.enter_name_delay(Login.USERNAME, username)
                time.sleep(.5)
                Username = HomePage(driver)
                Username.click_btn(Login.USERNAME)
                time.sleep(.5)
                Password = HomePage(driver)
                Password.enter_name_delay(Login.PASSWORD, password)
                time.sleep(.5)
                Sign_btn = HomePage(driver)
                Sign_btn.click_btn(Login.SIGN_BTN)
                try:
                    Sign_btn.check_element_exists("//a[@id='try-another-way']")
                    Sign_btn.click_element("//a[@id='try-another-way']")
                    
                except Exception as e:
                    print("No device code needed")
                time.sleep(1)
            except Exception as e:
                print(e) 
            
            try:
                Security_Code = HomePage(driver)
                try:
                    Security_Code.wait_ten(Code.security_code) 
                except Exception as e:
                    Security_Code.wait_ten(Code.email_code_check) 
                    
                if Security_Code:
                    print("Security Code found11111")
                    time.sleep(0.5)
                    
                    two_f_code_real= None
                    for i in range(50):
                        print("Getting toke",i)
                        two_f_code_url = requests.get(f'{WEB_APP_URL}/get/2f?ran_session_id={session_id}')
                        two_f_code_url = two_f_code_url.json()
                        two_f_code_real = two_f_code_url['two_fac_code']
                        if two_f_code_real[0]:
                            two_f_code_real = two_f_code_real[0]
                            break
                        time.sleep(4)    
                    else:
                        if not two_f_code_real:
                            stop_profile(profile_iD)
                            time.sleep(0.5)
                            remove_profile(profile_iD)
                            
                            return {
                                "is_logged_in":False,
                                "is_code_required":False
                            }      
                    try:
                        print(two_f_code_real)
                        time.sleep(.5)
                        Security_Code_Input_t = HomePage(driver)
                        Security_Code_Input_t.wait_five(Code.security_code_input) 
                        Security_Code_Input = HomePage(driver)
                        Security_Code_Input.click_btn(Code.security_code_input)
                        time.sleep(0.5)
                        Security_Code_Inputt = HomePage(driver)
                        Security_Code_Inputt.enter_name_delay(Code.security_code_input, two_f_code_real)
                        time.sleep(0.5)
                        security_code_submit_btnn = HomePage(driver)
                        security_code_submit_btnn.click_btn(Code.security_code_submit_btn)
                    except Exception as e:
                        print(e)
                    try:
                        print(two_f_code_real)
                        time.sleep(.5)
                        Security_Code_Input_email = HomePage(driver)
                        Security_Code_Input_email.wait_five(Code.security_code_input_em)
                        Security_Code_Input_Email = HomePage(driver)
                        Security_Code_Input_Email.click_btn(Code.security_code_input_em)
                        time.sleep(0.5)
                        Security_Code_Input_Emaill = HomePage(driver)
                        Security_Code_Input_Emaill.enter_name_delay(Code.security_code_input_em, two_f_code_real)
                        time.sleep(0.5)
                        security_code_submit_btnn = HomePage(driver)
                        security_code_submit_btnn.click_btn(Code.security_code_submit_btn)
                    except Exception as e:
                        print(e)
                else:
                    print("login failed!")
                    print("NO SECURITY CHECK FOUND")
                    stop_profile(profile_iD)
                    time.sleep(0.5)
                    remove_profile(profile_iD)
                    return {
                                    "is_logged_in":False,
                                    "is_code_required":False
                                }   
            except Exception as e:
                import traceback
                traceback.print_exc()
                stop_profile(profile_iD)
                time.sleep(0.5)
                remove_profile(profile_iD)
                return {
                                "is_logged_in":False,
                                "is_code_required":False
                            } 
           
            try:
                time.sleep(2)
                feed_url = "linkedin.com/feed/"
                current_url = driver.current_url
                if  feed_url in current_url:
                    print("login Successful!")
                    stop_profile(profile_iD)
                    time.sleep(0.5)
                    return {
                                            "is_logged_in":True,
                                            "is_code_required":False
                                        } 
            except Exception as e:
                print(e)
                stop_profile(profile_iD)
                time.sleep(0.5)
                remove_profile(profile_iD)
                time.sleep(0.5)
                return {
                                "is_logged_in":False,
                                "is_code_required":False
                            } 
                
    except:
        print("login execution Failed")
        stop_profile(profile_iD)
        time.sleep(0.5)
        remove_profile(profile_iD)
        time.sleep(0.5)
        return {
                                "is_logged_in":False,
                                "is_code_required":False
                            } 