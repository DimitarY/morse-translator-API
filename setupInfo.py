from flask import send_file
from flask_restful import Resource
from msilib import OpenDatabase

import json
import os

file = "Setup/Morse Translator.msi"
dataLocation = "Setup/data.json"


# def updateData():
#     data = {"filename": file[6::], "version": getMsiVersion()}
#     with open(dataLocation, "w") as f:
#         json.dump(data, f, indent=2)


# def getMsiVersion():
#     db = OpenDatabase(file, 0)
#     view = db.OpenView(
#         "SELECT Value FROM Property WHERE Property='ProductVersion'")
#     view.Execute(None)
#     result = view.Fetch()
#     return result.GetString(1)

# updateData()

class SetupVersion(Resource):
    global dataLocation

    def get(self):
        with open(dataLocation, 'r') as f:
            data = json.load(f)

        return data["version"], 200


class DownloadSetup(Resource):
    global file, dataLocation

    def get(self):
        with open(dataLocation, 'r') as f:
            data = json.load(f)

        return send_file(file, attachment_filename=data["filename"], as_attachment=True)
