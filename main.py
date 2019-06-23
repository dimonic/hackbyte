from flask import Flask, render_template
from readCam import takePicture
import potato_detection
import shutil
import os

segment_dir = 'segmented'

app = Flask(__name__)

@app.route('/')
def kickstart():
   return render_template('start.html')

@app.route('/capture')
def get_ses():
    currentfile =  takePicture()
    shutil.rmtree(segment_dir, ignore_errors)
    os.mkdir(segment_dir)
    hb_potato_detection(currentfile)
    images = os.listdir(segment_dir)
    return render_template("multi_result.html", image_list = images)


if __name__ == '__main__':
    
    app.run(debug=True)
