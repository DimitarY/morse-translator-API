from zipfile import ZipFile
from flask_restful import Resource, reqparse
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
        archiveName = "languages.zip"
        returnName = "languages.zip"
        path = "archives/"

        try:
            if os.path.getmtime("JSON") <= os.path.getmtime(archiveName):
                return send_file(path + archiveName, attachment_filename=returnName, as_attachment=True)
        except FileNotFoundError:
            return send_file(shutil.make_archive(path + archiveName[:-4], "zip", "JSON"), attachment_filename=returnName, as_attachment=True)

    def post(self):
        archiveName = "requiredLanguages.zip"
        returnName = "languages.zip"
        path = "archives/"

        parser = reqparse.RequestParser()
        parser.add_argument('languages', type=str,
                            action="append", location="json", required=True)
        args = parser.parse_args()

        with ZipFile(path + archiveName, "w") as zipObj:
            os.chdir("JSON")
            zipObj.write("Numbers.json")
            zipObj.write("Symbols.json")
            for x in args["languages"]:
                if (os.path.exists(x + ".json")):
                    zipObj.write(x + ".json")
            os.chdir("..")

        return send_file(path + archiveName, attachment_filename=returnName, as_attachment=True)
