from dataclasses import dataclass
from typing import Union
import unreal

SLOW_TASK: Union[None, unreal.ScopedSlowTask] = None


@dataclass
class ProgressBarState:
    steps: int = 0
    current_step: int = 0


PROGRESS_BAR_STATE = ProgressBarState()


@unreal.uclass()
class ProgressBarTechArtCorner(unreal.Object):
    @unreal.ufunction(ret=bool, params=[int, str], meta=dict(Category="TechArtCorner"))
    def progress_bar_start(self, steps, label):
        """
        http://localhost:30010/remote/object/call
        {
        "objectPath": "/Engine/PythonTypes.Default__RemoteControlDemo",
        "functionName": "return_params",
        "parameters": {
            "integer": 4,
            "steps": "It's alive!"
            }
        }
        """
        global SLOW_TASK
        if SLOW_TASK:
            return False

        SLOW_TASK = unreal.ScopedSlowTask(steps, label)
        global PROGRESS_BAR_STATE
        PROGRESS_BAR_STATE.steps = steps

        SLOW_TASK.__enter__()
        SLOW_TASK.make_dialog()

        return True

    @unreal.ufunction(ret=bool, meta=dict(Category="TechArtCorner"))
    def progress_bar_increment(self):
        """
        http://localhost:30010/remote/object/call
        {
        "objectPath" : "/Engine/PythonTypes.Default__ProgressBarTechArtCorner",
        "functionName" : "progress_bar_increment"
        }
        """
        global SLOW_TASK
        if not SLOW_TASK:
            return False

        global PROGRESS_BAR_STATE
        if PROGRESS_BAR_STATE.current_step <= PROGRESS_BAR_STATE.steps:
            PROGRESS_BAR_STATE.current_step += 1
            SLOW_TASK.enter_progress_frame(1)
            return True

        return False

    @unreal.ufunction(ret=bool, meta=dict(Category="TechArtCorner"))
    def progress_bar_finish(self):
        """
        http://localhost:30010/remote/object/call
        {
        "objectPath" : "/Engine/PythonTypes.Default__ProgressBarTechArtCorner",
        "functionName" : "progress_bar_finish"
        }
        """
        global SLOW_TASK
        if not SLOW_TASK:
            return False

        SLOW_TASK.__exit__()
        SLOW_TASK = None

        global PROGRESS_BAR_STATE
        PROGRESS_BAR_STATE = ProgressBarState()
