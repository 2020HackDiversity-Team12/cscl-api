from os import getenv

# ###########################
#  APP CONFIGURATION        #
# ###########################


class Config:
    pass


class ProdConfig(Config):
    DEBUG = False
    MONGODB_DB = getenv('PROD_MONGODB_DB', 'cscl_db')
    MONGODB_HOST = getenv('PROD_MONGODB_HOST', '3.20.216.39')
    MONGODB_PORT = int(getenv('PROD_MONGODB_PORT', 27017))


class DevConfig(Config):
    DEBUG = True
    MONGODB_DB = getenv('DEV_MONGODB_DB', 'cscl_test')
    MONGODB_HOST = getenv('DEV_MONGODB_HOST', '3.20.216.39')
    MONGODB_PORT = int(getenv('DEV_MONGODB_PORT', 27017))
