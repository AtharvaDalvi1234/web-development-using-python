from flask import Flask, redirect, url_for,flash
from flask_sqlalchemy import SQLAlchemy
from os import path
from flask import Flask,render_template,request
from flask_login import login_user, current_user,LoginManager

from werkzeug.security import generate_password_hash, check_password_hash
from .models import User,DB_NAME,db




app=Flask(__name__)
# mail=Mail(app)

# app.config["MAIL_SERVER"]='smtp.gmail.com'
# app.config["MAIL_PORT"]=465
# app.config["MAIL_USERNAME"]='digifx.123@gmail.com'
# app.config['MAIL_PASSWORD']='qjgwphqinoajlufv'                    #you have to give your password of gmail account
# app.config['MAIL_USE_TLS']=False
# app.config['MAIL_USE_SSL']=True
# mail=Mail(app)
# otp=randint(000000,999999)

db = SQLAlchemy()
DB_NAME = "database.db"


def create_app():
   
    app.config['SECRET_KEY'] = 'avra"hta!@#-hs"ay!@#-hsen"giv!@#'
    app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_NAME}'
    db.init_app(app)

    from .views import views
    from .auth import auth

    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/')

    from .models import User

    create_database(app)

    login_manager = LoginManager()
    login_manager.login_view = 'auth.login'
    login_manager.init_app(app)

    @login_manager.user_loader
    def load_user(id):
        return User.query.get(int(id))

    return app

def create_database(app):
    if not path.exists('website/' + DB_NAME):
        db.create_all(app=app)
        print('Created Database!')



# @app.route('/verify',methods=["POST"])
# def verify():
#     email=request.form['email']
#     msg=Message(subject='OTP',sender='digifx.123@gmail.com',recipients=[email])
#     msg.body=str(otp)
#     mail.send(msg)
#     return render_template('verify.html', user=current_user)

# @app.route('/validate',methods=['POST'])
# def validate():
    
#     user_otp=request.form['otp']
#     if otp==int(user_otp):
        
        

      



        

        
       
        
        

#         return redirect(url_for('views.home'))
#     return "<h3>Please Try Again</h3>"



