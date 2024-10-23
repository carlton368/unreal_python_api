import json
import unreal


@unreal.uclass()
class RemoteControlDemo(unreal.Object):
    @unreal.ufunction(ret=bool, meta=dict(Category="TechArtCorner"))
    def ping_unreal(self):
        """
        http://localhost:30010/remote/object/call
        {
        "objectPath" : "/Engine/PythonTypes.Default__RemoteControlDemo",
        "functionName" : "ping_unreal"
        }
        """
        return True

    @unreal.ufunction(ret=str, params=[int, str], meta=dict(Category="TechArtCorner"))
    def return_params(self, integer, string):
        """
        http://localhost:30010/remote/object/call
        {
        "objectPath" : "/Engine/PythonTypes.Default__RemoteControlDemo",
        "functionName" : "return_params",
        "parameters": {
            "integer": 1234,
            "string": "It's alive!"
            }
        }
        """
        return json.dumps({"integer": integer, "string": string})
