from ext import db


class User(db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    user = db.Column(db.String(20), nullable=False, unique=True, comment="用户名,唯一不可重复")
    msg = db.Column(db.String(255), nullable=True, comment="需要传递的消息")
    file_name = db.Column(db.String(255), nullable=True, comment="上传的文件名称")
    file_show_name = db.Column(db.String(255), nullable=True, comment="文件页面展示名字")
    create_time = db.Column(db.DateTime, nullable=False, comment="创建时间")
    update_time = db.Column(db.DateTime, nullable=True, comment="更新时间")

    def __str__(self):
        return self.msg
