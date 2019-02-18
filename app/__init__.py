from flask import Flask
from flask_mail import Mail

app = Flask(__name__)
app.config['SECRET_KEY'] = 'SomeRandomPassphrase'
app.config['MAIL_SERVER'] = 'smtp.mailtrap.io'
app.config['MAIL_PORT'] = '465' 
app.config['MAIL_USERNAME'] = '7e18d9493f0bd9'
app.config['MAIL_PASSWORD'] = '4c22fdf3acfda2'

mail = Mail(app)
from app import views