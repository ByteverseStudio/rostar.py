import sys

import api
import executor

if sys.version_info[0] < 3:
    print("Python 3 or a more recent version is required.")
    sys.exit(1)


def downloadPlace():
    file = sys.argv[1]
    placeID = sys.argv[2]
    auth = sys.argv[3]

    result = api.downloadPlace(placeID, auth)

    open(file, "w").write(result)

def uploadPlace():
    file = sys.argv[1]
    placeID = sys.argv[2]
    auth = sys.argv[3]
    versionType = sys.argv[4] | "Published"

    api.uploadPlace(open(file).read(), placeID, auth, versionType)




switch = {
    "download": lambda : downloadPlace(),
    "upload": lambda : uploadPlace(),
    "exportWorkspace": lambda : exportWorkspace(),
}
