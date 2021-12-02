from flask import Blueprint, request

file = Blueprint("file", __name__)

@file.route('/upload', methods=['POST'])
def upload():
    upload = request.file[]



@file.route('/download', methods=['GET'])
def download():

