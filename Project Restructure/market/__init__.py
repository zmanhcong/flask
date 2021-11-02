from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///market.db'
db = SQLAlchemy(app)
#app.config is config key name and create market.db::: SQLALCHEMY_DATABASE_URI: is key name

from market import routes   #use this stament for connect with routes.