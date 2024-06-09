import os

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'super_secret_key'
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or 'mysql+pymysql://root:meet%40123@localhost/my_bizDB'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
