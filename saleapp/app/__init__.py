from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from urllib.parse import quote
from flask_login import LoginManager
import cloudinary

app = Flask(__name__)
app.secret_key = "HJJGUSJKVNKVNHHF"
app.config["SQLALCHEMY_DATABASE_URI"] = "mysql+pymysql://root:%s@localhost/saledb?charset=utf8mb4" % quote('123456789')
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = True
app.config['PAGE_SIZE'] = 8
db = SQLAlchemy(app)
login = LoginManager(app)
# Configuration
cloudinary.config(
    cloud_name="dvtjeqdfz",
    api_key="263135124563271",
    api_secret="SQnGRxuMOymbOi4Ru7ro9gQSi5U",  # Click 'View API Keys' above to copy your API secret
    secure=True
)
