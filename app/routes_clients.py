from app import app
from flask import render_template, request, flash, redirect

from classes.db import db
from classes.book import supergenres, subgenres

@app.route('/profile')
def profile():
  if db.get_logged():
    usertype = db.get_usertype()
    user = db.get_user()
    return render_template('profile.html', user=user, usertype=usertype)
  else:
    return redirect('/')

@app.route('/return')
def to_return():
  if db.get_logged():
    usertype = db.get_usertype()
    user = db.get_user()
    
    return render_template('rent.html', user=user, usertype=usertype)
  else:
    return redirect('/')