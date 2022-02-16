import os

class Config:
  SECRET_KEY = 'Moringa School'
  UPLOADED_PHOTOS_DEST ='app/static/photos'



class ProdConfig(Config):
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL').replace("://", "ql://", 1)



class DevConfig(Config):
    # DEBUG = True
    pass

config_options = {
'development':DevConfig,
'production':ProdConfig
}