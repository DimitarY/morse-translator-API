from flask import send_file
from flask_restful import Resource

import json

file = "Setup/Morse Translator.msi"
dataLocation = "Setup/data.json"

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
