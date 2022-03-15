import requests


def downloadPlace(placeID, auth):

    header = {
        "cookie": '.ROBLOSECURITY=' + auth
    }

    result = requests.get(
        'https://assetdelivery.roblox.com/v1/place/?ID=' + placeID, headers=header)

    switch = {
        409: "User is not authorized to access Asset.",
        404: "Asset not found."
    }

    if result.status_code == 200:
        print("Downloading place: " + placeID)
        return result.text
    else:
        if result.status_code in switch:
            print(switch[result.status_code])
        else:
            print("Error: " + result.status_code)


def uploadPlace(fileContent, placeID, auth, versionType = "Published"):
    header = {
        "cookie": '.ROBLOSECURITY=' + auth
    }

    result = requests.post("https://apis.roblox.com/universes/v1/" + getUniverseID(placeID) + "/places/" + placeID + "/versions?versionType="+ versionType, headers=header, data=fileContent)

    switch = {
        400: "Invalid request / Invalid file content.",
        401: "API key not valid for operation, user does not have authorization.",
        403: "Publish not allowed on place.",
        404: "Place or universe does not exist.",
        409: "Place not part of the universe.",
        500: "Server internal error./ unknown error."
    }

    if result.status_code == 200:
        print("Uploading place: " + placeID)
    else:
        if result.status_code in switch:
            print(switch[result.status_code])
        else:
            print("Error: " + result.status_code)



def getUniverseID(placeID):
    result = requests.get("https://api.roblox.com/universes/get-universe-containing-place?placeid=" + placeID)
    if result.status_code == 200:
        return result.json()["UniverseId"]
    else:
        return False
