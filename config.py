import os
SECRET_KEY = os.urandom(24)
SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:Fusionman361@localhost/leaderboard' #Change password to your password for MySQL workbench
SQLALCHEMY_TRACK_MODIFICATIONS = False