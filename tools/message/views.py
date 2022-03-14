from datetime import datetime

from flask import Blueprint
from flask import request, render_template, Response
import json

from ext import db
from tools.message.models import User

tools = Blueprint("tools", __name__)


@tools.route('/add', methods=["POST"])
def add_msg():
    data = {
        "object": None,
        "msg": "添加成功",
        "code": 200,
    }
    user_name = request.form.get("user", type=str)
    message = request.form.get("message", type=str)
    user_li = User.query.filter(User.user == user_name).first()
    if user_li:
        user_li.user = user_name
        user_li.msg = message
        user_li.update_time = datetime.strftime(datetime.now(), '%Y-%m-%d %H:%M:%S')
        db.session.commit()
        return Response(json.dumps(data), content_type='application/json')
    else:
        user = User()
        user.user = user_name
        user.msg = message
        user.create_time = datetime.strftime(datetime.now(), '%Y-%m-%d %H:%M:%S')
        db.session.add(user)
        db.session.commit()
        return Response(json.dumps(data), content_type='application/json')


@tools.route('/<string:user>', methods=["GET"])
def get_msg(user):
    user_li = User.query.filter(User.user == user).first()
    if user_li is None:
        return render_template("404.html")
    up_time = user_li.upload_time
    if up_time is None:
        up_time = "暂无数据"
    context = {
        "user": user_li.user,
        "msg": user_li.msg,
        "filename": user_li.file_show_name,
        "time": up_time
    }
    if not user_li.msg:
        context["msg"] = "你没有提交内容！"
    if not user_li.file_name:
        context["filename"] = "你没有上传文件！"
    return render_template("copy.html", context=context)


@tools.route("/", methods=["GET"])
def index():
    return render_template("index.html")
