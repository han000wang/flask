import os

DEBUG=True

SECRET_KEY=os.urandom(24)

SQLALCHEMY_DATABASE_URI="mysql+pymysql://root:fengyun666@127.0.0.1:3306/test"

SQLALCHEMY_TRACK_MODIFICATIONS=False
