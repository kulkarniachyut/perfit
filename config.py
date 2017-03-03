# config.py

class Config(object):
    """
    Common configurations
    """

    # Put any configurations here that are common across all environments

class DevelopmentConfig(Config):
    """
    Development configurations
    """

    DEBUG = True
    SQLALCHEMY_ECHO = True

class ProductionConfig(Config):
    """
    Production configurations
    """

    DEBUG = False

class TestConfig(Config):

    TESTING = True
    WTF_CSRF_ENABLED = False
    SQLALCHEMY_ECHO = False
    # SQLALCHEMY_DATABASE_URI = "sqlite:////tmp/%s_test.sqlite" % project_name


app_config = {
    'development': DevelopmentConfig,
    'production': ProductionConfig,
    'testing' : TestConfig
}
