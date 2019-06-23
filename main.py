from flask import Flask, render_template
from readCam import takePicture
from potato_detection import hb_detect_potatoes
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
    shutil.rmtree(segment_dir, ignore_errors=True)
    os.mkdir(segment_dir)
    hb_detect_potatoes('./static/'+currentfile)
    good = 1
    bad = 0
    # for potato in os.listdir(segment_dir):
    #     if (classifier(potato)):
    #         ++good
    #     else:
    #         ++bad
    render_template("result.html", quantity = good + bad, quality = good / (good+bad), user_image = currentfile)
    time.sleep(60)

if __name__ == '__main__':
    
    app.run(debug=True)
