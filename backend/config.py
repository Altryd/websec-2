class Config(object):
    DEBUG = False
    TESTING = False
    SQLALCHEMY_DATABASE_URI = "mysql+pymysql://root:password@localhost/mil2?charset=utf8mb4"


class ProductionConfig(Config):
    pass


class DevelopmentConfig(Config):
    DEBUG = True
    SECRET_KEY = 'websec2_secret'
    SECURITY_PASSWORD_SALT = "websec2_secret_password"
    MAX_CONTENT_LENGTH = 16 * 1000 * 1000

    # UPLOAD_PHOTOS_RELATIVE = '/uploads'
    ALLOWED_EXTENSIONS = {'jpg', 'jpeg', 'png'}


class TestingConfig(Config):
    TESTING = True


JWT_SECRET_KEY = "jwt_secret"
