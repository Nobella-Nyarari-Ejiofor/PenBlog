import os

class Config:
  SECRET_KEY = 'Moringa School'
  SQLALCHEMY_DATABASE_URI='postgresql+psycopg2://moringa:access@localhost/blog'
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