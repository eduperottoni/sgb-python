from app import app
from flask import render_template
from flask import request, flash, redirect

def aux_auth():  
  user = request.form.get('user')
  password = request.form.get('password')
  if user=='Eduardo' and password=='1234@':
    return (f'Olá, {user}! Sua senha é {password}')
  else:
    flash('Dados inválidos')
    return redirect('/login')