import uuid
import logging
from flask import Flask, render_template, request, session

from flask_session import Session
from flask_session_captcha import FlaskSessionCaptcha


app = Flask(__name__)

#databse config




#cpatcha configuration
app.config["SECRET_KEY"] = str(uuid.uuid4())
app.config['CAPTCHA_ENABLE']= True

#captcha length
app.config['CAPTCHA_LENGTH']=5
app.config['CAPTCHA_WIDTH']=160
app.config['CAPTCHA_HEIGHT']=70

app.config['SESSION_TYPE'] = 'FILESYSTEM'
app.config['SESSION_COOKIE_NAME'] = 'hotboi'

#enable sever session
Session(app)

#initialize flask session captcha
captcha = FlaskSessionCaptcha(app)


@app.route('/', methods=['POST','GET'])
def index() :
    if request.method == 'POST':
        if captcha.validate():
            return "success"
        else :
            return "fail"
    
    return render_template('form.html')


if __name__ == "__main__":
    app.debug = True
    logging.getLogger().setLevel("DEBUG")
    app.run()

