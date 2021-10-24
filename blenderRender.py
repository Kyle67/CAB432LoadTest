from flask import Flask

# Import os
import os

blenderRender = Flask(__name__)

@blenderRender.route("/")
def hello():
    os.system("blender -b test.blend");
    return "Blender World!"

if __name__ == "__main__":
    blenderRender.run()
