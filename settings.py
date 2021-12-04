
class Config:
    download_mode = 2  # 1 使用非流式下载  2 使用流式下载


class Development(Config):
    ENV = 'development'
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = "mysql+pymysql://root:shenyongfu@127.0.0.1:3306/msg?charset=utf8mb4"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_ECHO = True
    SQLALCHEMY_RECORD_QUERIES = True


class Production(Config):
    ENV = 'production'
    DEBUG = False
    SQLALCHEMY_DATABASE_URI = "mysql+pymysql://root:liebao123@10.43.1.7:3306/msg?charset=utf8mb4"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_ECHO = False
    SQLALCHEMY_RECORD_QUERIES = False
