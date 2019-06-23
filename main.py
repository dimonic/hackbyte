from flask import Flask, render_template
from readCam import takePicture

app = Flask(__name__)

@app.route('/')
def kickstart():
   return render_template('start.html')

@app.route('/capture')
def get_ses():
	currentfile =  takePicture()
	return render_template("result.html", user_image = currentfile)


if __name__ == '__main__':
    
    app.run(debug=True)