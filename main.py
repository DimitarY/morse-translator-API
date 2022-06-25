from flask import Flask
from flask_restful import Api

from JSON import Languages, Files
from setupInfo import SetupVersion, DownloadSetup

from updateSetupInfo import updateSetupData

app = Flask("Morse")
api = Api(app)

api.add_resource(Languages, "/get/json-languages")
api.add_resource(Files, "/download/json_files")
api.add_resource(SetupVersion, "/get/setup-version")
api.add_resource(DownloadSetup, "/download/Morse_Translator")

if __name__ == '__main__':
    updateSetupData()
    app.run(debug=True)  # run our Flask app
