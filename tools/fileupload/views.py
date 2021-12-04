import json
import uuid
from datetime import datetime
import os
from flask import Blueprint, request, Response

from ext import db
from tools.message.models import User

file = Blueprint("file", __name__)

upload_path = os.path.abspath('.' + "/static/files/upload")


@file.route("/upload", methods=["POST"])
def upload():
    data = {
        "object": None,
        "msg": "添加成功",
        "code": 200,
    }
    file_obj = request.files.get("file", None)
    user_id = request.form.get("user", None)
    if file_obj is None or not user_id:
        data["msg"] = "文件内容不能为空"
        data["code"] = 9999
        return Response(json.dumps(data), content_type="application/json")
    file_id = "".join(str(uuid.uuid1()).split("-"))
    file_name = file_id + "." + file_obj.filename.split(".")[1]
    print(upload_path)
    user = User()
    user_name = User.query.filter(User.user == user_id).first()
    if user_name is None:
        user.user = user_id
        user.create_time = datetime.strftime(datetime.now(), '%Y-%m-%d %H:%M:%S')
        file_obj.save(upload_path + "/" + file_name)
        user.file_name = file_name
        db.session.add(user)
        db.session.commit()
        data["msg"] = "上传成功"
        data["code"] = 200
        return Response(json.dumps(data), content_type="application/json")
    else:
        # 处理旧文件覆盖删除问题
        m = user_name.file_name
        print(m)
        user_name.update_time = datetime.strftime(datetime.now(), '%Y-%m-%d %H:%M:%S')
        user_name.file_name = file_name
        db.session.commit()
        file_obj.save(upload_path + "/" + file_name)
        data["msg"] = "上传成功"
        data["code"] = 200
        return Response(json.dumps(data), content_type="application/json")
