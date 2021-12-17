import json
import uuid
from datetime import datetime
import os
from flask import Blueprint, request, Response, send_from_directory, render_template

import settings
from ext import db
from tools.message.models import User

file = Blueprint("file", __name__)

upload_path = os.path.abspath('.' + "/static/files/upload/")


@file.route("/upload", methods=["POST"])
def upload():
    data = {
        "object": None,
        "msg": "添加成功",
        "code": 200,
    }
    file_obj = request.files.get("file", None)
    user_id = request.form.get("user", None)
    if file_obj is None:
        data["msg"] = "文件内容不能为空"
        data["code"] = 9999
        return Response(json.dumps(data), content_type="application/json")
    if not user_id:
        data["msg"] = "用户名不能为空"
        data["code"] = 9999
        return Response(json.dumps(data), content_type="application/json")
    file_id = "".join(str(uuid.uuid1()).split("-"))
    file_name = file_id + "." + file_obj.filename.split(".")[-1]
    user = User()
    user_name = User.query.filter(User.user == user_id).first()
    if user_name is None:
        user.user = user_id
        user.create_time = datetime.strftime(datetime.now(), '%Y-%m-%d %H:%M:%S')
        file_obj.save(upload_path + "\\" + file_name)
        user.file_name = file_name
        db.session.add(user)
        db.session.commit()
        data["msg"] = "上传成功"
        data["code"] = 200
        return Response(json.dumps(data), content_type="application/json")
    else:
        # 处理旧文件覆盖删除问题
        if user_name.file_name:
            try:
                if os.path.exists(upload_path + "\\" + user_name.file_name):
                    os.remove(upload_path + "\\" + user_name.file_name)
            except Exception as e:
                print(e)
            else:
                pass
        user_name.update_time = datetime.strftime(datetime.now(), '%Y-%m-%d %H:%M:%S')
        user_name.file_name = file_name
        db.session.commit()
        file_obj.save(upload_path + "\\" + file_name)
        data["msg"] = "上传成功"
        data["code"] = 200
        return Response(json.dumps(data), content_type="application/json")


@file.route("/downloads/<string:user>", methods=["GET"])
def downloads(user):
    li = User.query.filter(User.user == user).first()
    if not li or not li.file_name:
        return render_template("404.html")
    if settings.Config.download_mode == 1:
        return send_from_directory(upload_path, filename=li.file_name, as_attachment=True)
    elif settings.Config.download_mode == 2:
        # 使用流式下载
        def send_file():
            with open(upload_path + "\\" + li.file_name, 'rb') as targetfile:
                while 1:
                    data = targetfile.read(2 * 1024 * 1024)  # 每次读取2MB (可用限速)
                    if not data:
                        break
                    yield data
        response = Response(send_file(), content_type='application/octet-stream')
        response.headers["Content-disposition"] = 'attachment; filename={}'.format(li.file_name)
        return response
    return "未知异常"

