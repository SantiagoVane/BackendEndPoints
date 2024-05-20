import os

class Config:
    SQLALCHEMY_DATABASE_URI = 'mysql://root:password@localhost/vapor'
    SQLALCHEMY_TRACK_MODIFICATIONS = False