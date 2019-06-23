from flask import Flask, render_template
from readCam import takePicture
import potato_detection
import shutil
import os

app = Flask(__name__)

@app.route('/')
def kickstart():
   return render_template('start.html')

@app.route('/capture')
def get_ses():
	currentfile =  takePicture()
	shutil.rmtree('segmented')
	hb_potato_detection(currentfile)
	images = os.listdir('segmented')
	return render_template("multi_result.html", image_list = images)


if __name__ == '__main__':
    
    app.run(debug=True)
