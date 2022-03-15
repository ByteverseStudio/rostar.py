local informationFile = json.fromString(remodel.readFile("RostarData.json"))

local game = remodel.readPlaceFile(informationFile.placeFilePath)

local Workspace = game.Workspace

remodel.createDirAll("workspace")

remodel.writeModelFile(Workspace, "workspace/Workspace.rbxm")