from flask_restful import Resource
from flask import send_file

import glob
import shutil
import os


class Languages(Resource):
    def get(self):
        languages = []

        for x in glob.glob("JSON/*.json"):
            if x[5:-5] != "Numbers" and x[5:-5] != "Symbols":
                languages.append(x[5:-5])

        return languages, 200

class Files(Resource):
    def get(self):
        filename = "json.zip"
        path = "archives/"
        
        try:
            if os.path.getmtime("JSON") <= os.path.getmtime(filename):
                return send_file(path + filename, attachment_filename=filename, as_attachment=True)
        except FileNotFoundError:
            return send_file(shutil.make_archive(path + filename[:-4], "zip", "JSON"), attachment_filename=filename, as_attachment=True)
