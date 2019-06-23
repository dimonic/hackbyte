from flask import Flask, render_template
from readCam import takePicture
import potato_detection
import shutil
import os
import time

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
    good = 0
    bad = 0
    for potato in os.listdir(segment_dir):
        if (classifier(potato)):
            ++good
        else
            ++bad
    render_template("result.html", quantity = good + bad, quality = good / (good+bad), user_image = currentfile)
    time.sleep(60)

if __name__ == '__main__':
    
    app.run(debug=True)
