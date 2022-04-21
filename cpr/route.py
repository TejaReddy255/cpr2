from flask import  flash, redirect, render_template, url_for
from cpr import app,db,bcrypt
from cpr.form import RegistrationFrom,LoginFrom,RecruterLoginFrom,RecruterRegistrationFrom
from cpr.models import User,Ruser
from flask_login import login_user,current_user, logout_user
@app.route('/')
def home():
    return render_template('index.html')
@app.route('/register',methods=['GET','POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for("getStarted"))
    form= RegistrationFrom()
    if form.validate_on_submit():
        hashed_password=bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        user=User(username=form.username.data,email=form.email.data,password=hashed_password)
        db.session.add(user)
        db.session.commit()
        return redirect(url_for('login'))
    return render_template('register.html',form=form) 
@app.route('/login',methods=["GET","POST"])
def login():
    if current_user.is_authenticated:
        return redirect(url_for("getStarted"))    
    form= LoginFrom()
    if form.validate_on_submit():
        user=User.query.filter_by(email=form.email.data).first()
        if user and  bcrypt.check_password_hash(user.password,form.password.data):
            login_user(user)
            return redirect(url_for('getStarted'))
        else:
            flash('Login Unsuccessful. Please check email and password', 'danger')    
        
    return render_template('login.html',form=form) 

@app.route('/about-us')
def aboutUs():
    return render_template('aboutUs.html')

@app.route('/get-started')
def getStarted():
    print(current_user.is_authenticated)    

    return render_template('getStarted.html')
@app.route('/output')
def output():
    return render_template('output.html') 
@app.route('/Logout')
def logout():
    if not current_user.is_authenticated:
        return redirect(url_for("home"))
    logout_user()
    return redirect(url_for('home'))
@app.route('/rregister',methods=['GET','POST'])
def rregister():
    if current_user.is_authenticated:
        return redirect(url_for("getStarted"))
    form=RecruterRegistrationFrom()
    if form.validate_on_submit():
        hashed_password=bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        user=Ruser(companyname=form.companyname.data,username=form.username.data,email=form.email.data,password=hashed_password)
        db.session.add(user)
        db.session.commit()
        return redirect(url_for('rlogin'))
    return render_template('rregister.html',form=form)
@app.route('/rlogin',methods=["GET","POST"])
def rlogin():
    if current_user.is_authenticated:
        return redirect(url_for("getStarted"))    
    form=RecruterLoginFrom()
    if form.validate_on_submit():
        user=Ruser.query.filter_by(email=form.email.data).first()
        if user and  bcrypt.check_password_hash(user.password,form.password.data):
            login_user(user)
            return redirect(url_for('getStarted'))
        else:
            flash('Login Unsuccessful. Please check email and password', 'danger')    
        
    return render_template('rlogin.html',form=form) 

