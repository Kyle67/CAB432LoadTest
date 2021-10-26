from flask import Flask

# Import os
import os

blenderRender = Flask(__name__)

@blenderRender.route("/")
def hello():
    os.system("sudo blender -b test.blend -x 1 -o //render -a");
    return "Blender World!"

if __name__ == "__main__":
    blenderRender.run()
