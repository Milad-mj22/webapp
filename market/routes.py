from market import app
from flask import render_template , redirect,url_for,flash,get_flashed_messages
from market import forms
from market.models import Item, User
from market.forms import RegisterForm,loginForm
from market import db
from flask_login import login_user,logout_user,login_required
@app.route('/')
@app.route('/home')
def home_page():
    return render_template('home.html')

@app.route('/market')
@login_required
def market_page():
    items = Item.query.all()
    return render_template('market.html', items=items)

@app.route('/register',methods=['GET','POST'])
def register_page():
    form = RegisterForm()
    if form.validate_on_submit():
        user_to_create = User(username=form.username.data,email_address=form.email_address.data,password=form.password1.data)
        db.session.add(user_to_create)
        db.session.commit()
        login_user(user_to_create)
        flash('Account create successfully and log in',category='success')
        return redirect(url_for('market_page'))        
        return redirect(url_for('market_page'))
    if form.errors != {}: 
        for err_msg in form.errors.values():
           flash(f'there is erorr in : {err_msg}',category='danger')

        
    return render_template('register.html', form=form)

@app.route('/login',methods=['GET','POST'])
def login_page():
    form=loginForm()
    if form.validate_on_submit():
        attempted_user = User.query.filter_by(username=form.username.data).first()
        if attempted_user and attempted_user.check_password(attempted_password=form.password.data):
            login_user(attempted_user)
            flash('success you are login',category='success')
            return redirect(url_for('market_page'))
        else:
            flash('username and password are not match',category='danger')

    return render_template('login.html',form=form)

@app.route('/logout')
def logout_page():
    logout_user()
    flash('you have been logout',category='info')
    return redirect(url_for('home_page'))