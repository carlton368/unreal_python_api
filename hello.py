import os.path

import unreal
import uuid


def say_hi():
    unreal.log("Hi! I am a new hello script!")


print("I just got imported!")

random_name = str(uuid.uuid4())
path = os.path.join(r"Z:\tech art channel\PyAutomationCourse\Content\Python", random_name)

with open(path, "w") as f:
    pass

print(f"Created {random_name}")

