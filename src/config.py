from os import getenv

# ###########################
#  APP CONFIGURATION        #
# ###########################


class Config:
    pass


class ProdConfig(Config):
    DEBUG = False
    MONGODB_DB = getenv('PROD_MONGODB_DB')
    MONGODB_HOST = getenv('PROD_MONGODB_HOST')
    MONGODB_PORT = int(getenv('PROD_MONGODB_PORT'))


class DevConfig(Config):
    DEBUG = True
    MONGODB_DB = getenv('DEV_MONGODB_DB')
    MONGODB_HOST = getenv('DEV_MONGODB_HOST')
    MONGODB_PORT = int(getenv('DEV_MONGODB_PORT'))
