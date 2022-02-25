from flask import Flask

app = Flask(__name__)
app.config['SECRET_KEY'] = "fer_edu"


from app import routes
from app import utils