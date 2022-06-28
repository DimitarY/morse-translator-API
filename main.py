from flask import Flask
from flask_restful import Api, Resource

from JSON import Languages, Files
from setupInfo import SetupVersion, DownloadSetup

from updateSetupInfo import updateSetupData

app = Flask("Morse")
api = Api(app)


class Main(Resource):
    def head(self):
        return "online", 200

    def get(self):
        return "online", 200


api.add_resource(Main, "/")
api.add_resource(Languages, "/get/json-languages")
api.add_resource(Files, "/download/json_files")
api.add_resource(SetupVersion, "/get/setup-version")
api.add_resource(DownloadSetup, "/download/Morse_Translator")

if __name__ == '__main__':
    updateSetupData()
    app.run(threaded=True, debug=True)  # run our Flask app
