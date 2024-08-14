from lib.imports import *

class Login:
    USERNAME = '//*[@id="app__container"]//input[@id="username"]'
    PASSWORD = '//*[@id="app__container"]//input[@id="password"]'
    SIGN_BTN = '//*[@id="app__container"]//div[@class="login__form_action_container "]/button[contains(normalize-space(), "Sign in")]'
class Code:
    Search_Bar = '//*[@placeholder="Search"]'
    Post_fil = '//button[contains(normalize-space(), "Posts")]'
    Sort_By = '//button[contains(normalize-space(), "Sort by")]'
    Latest_post = '//*[@class="display-flex"][contains(normalize-space(), "Latest")]'
    Latest_post_btn = '(//button[contains(normalize-space(), "Show results")])[1]'
    Date_posted = '//button[contains(normalize-space(), "Date posted")]'
    past_24_hours = '//*[@class="display-flex"][contains(normalize-space(), "Past 24 hours")]'
    past_24_hours_btn = '(//button[contains(normalize-space(), "Show results")])[2]'
    first_post_cmnt = '(//*[@id="fie-impression-container"])[1]//button[contains(normalize-space(), "Comment")]'
    cmnt_box = '(//*[@id="fie-impression-container"])[1]//*[@data-placeholder="Add a comment…"]'
    post_btn = '(//button[contains(normalize-space(), "Post")])[2]'
    security_check = '//h1[contains(normalize-space(), "Let’s do a quick security check")]'
    email_code_check = '//h1[contains(normalize-space(), "Let’s do a quick verification")]'
    security_code = '//h1[contains(normalize-space(), "Enter the code you see on your authenticator app")]'
    security_code_input = '(//*[contains(normalize-space(), "Enter the code you see on your authenticator app")]//*[@name="pin"])[1]'
    security_code_input_em = '(//*[contains(normalize-space(), "The login attempt seems suspicious. To finish signing in please enter the verification code we sent to your email address.")]//*[@name="pin"])[1]'
    main_feed = '//*[@aria-label="Main Feed"]'
    security_code_submit_btn = '(//button[contains(normalize-space(), "Submit")])[1]'

class Captcha:
    funcaptcha_iframe = '//iframe[@id="captcha-internal"]'
    # funcaptcha_iframe = '//*[@role="main"]//*[@id="captcha-challenge"]//*[@name="captchaSiteKey"]'
    # funcaptcha_iframe = '//*[@id="FunCaptcha"]/iframe'