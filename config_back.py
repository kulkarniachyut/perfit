# -*- config:utf-8 -*-



project_name = "Perfit"


# base config class; extend it to your needs.
class Config(object):
    # use DEBUG mode?
    DEBUG = True

    # use TESTING mode?
    TESTING = False

    # DATABASE CONFIGURATION
    KEY = 'Even a broken clock is right twice a day'
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:perfitfall2016@perfitmysql.cf0kcn2storx.us-west-1.rds.amazonaws.com/perfit'
    SQLALCHEMY_COMMIT_ON_TEARDOWN = True
    MYSQL_PORT = 3306
    MYSQL_DATABASE_USER = 'root'
    MYSQL_DATABASE_PASSWORD = 'perfitfall2016' #'perfitfall2016'
    MYSQL_DATABASE_DB = 'perfit'
    MYSQL_DATABASE_HOST = 'perfitmysql.cf0kcn2storx.us-west-1.rds.amazonaws.com'
    AWS_ACCESS_KEY = 'AKIAJNWJQ6SZKGMG4JMA'
    AWS_SECRET_KEY = '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'
    S3_BUCKET_NAME = 'perfit-user-images'
    RECAPTCHA_URL = 'https://www.google.com/recaptcha/api/siteverify'
    RECAPTCHA_SECRET_KEY = '6LfSLgwUAAAAACPNFUXKhBongpdzJNi_2oMGLSqY'
    GOOGLE_OAUTH_URL = 'https://www.googleapis.com/oauth2/v3/tokeninfo?id_token='

    
# config class for development environment
class Dev(Config):
    DEBUG = True  # we want debug level output
    MAIL_DEBUG = True
    SQLALCHEMY_ECHO = True  # we want to see sqlalchemy output
    SQLALCHEMY_DATABASE_URI = "sqlite:////var/tmp/%s_dev.sqlite" % project_name


# config class used during tests
class Test(Config):
    TESTING = True
    WTF_CSRF_ENABLED = False
    SQLALCHEMY_ECHO = False
    SQLALCHEMY_DATABASE_URI = "sqlite:////tmp/%s_test.sqlite" % project_name
