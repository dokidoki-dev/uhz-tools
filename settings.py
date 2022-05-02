
class Config:
    download_mode = 2  # 1 使用非流式下载  2 使用流式下载


class Development(Config):
    ENV = 'development'
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = "mysql+pymysql://root:shen123456@127.0.0.1:3306/msg?charset=utf8mb4"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_ECHO = True
    SQLALCHEMY_RECORD_QUERIES = True


class Production(Config):
    ENV = 'production'
    DEBUG = False
    SQLALCHEMY_DATABASE_URI = "mysql+pymysql://root:123456@10.0.0.0:3306/msg?charset=utf8mb4"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_ECHO = False
    SQLALCHEMY_RECORD_QUERIES = False
