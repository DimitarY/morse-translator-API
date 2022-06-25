from msilib import OpenDatabase

import json

file = "Setup/Morse Translator.msi"
dataLocation = "Setup/data.json"


def getMsiVersion():
    db = OpenDatabase(file, 0)
    view = db.OpenView(
        "SELECT Value FROM Property WHERE Property='ProductVersion'")
    view.Execute(None)
    result = view.Fetch()
    return result.GetString(1)


def updateSetupData():
    data = {"filename": file[6::], "version": getMsiVersion()}
    with open(dataLocation, "w") as f:
        json.dump(data, f, indent=2)

updateSetupData()