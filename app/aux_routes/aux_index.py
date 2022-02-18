from app import app
from flask import render_template
from flask import request, flash, redirect

def aux_index():
  nome = "Eduardo"
  dados = {'profissao':'Professora','canal':'Alba Lopes'}
  return render_template('index.html', nome=nome, dados=dados)
