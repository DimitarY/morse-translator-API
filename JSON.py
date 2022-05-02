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

        return {"languages": languages}, 200
