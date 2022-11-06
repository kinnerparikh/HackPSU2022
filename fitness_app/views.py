from flask import render_template, Response, request
import cv2
from fitness_app import app
from fitness_app import gamer
from fitness_app import posture as po
from fitness_app import PoseModule as pm
from fitness_app import plank as pl
from fitness_app import squat as sq
#from fitness_app.PoseModule import cap as pm_cap
#from fitness_app.gamer import cap as gamer_cap
'''
camera = cv2.VideoCapture(0)

def gen_frames():  
    while True:
        success, frame = camera.read()  # read the camera frame
        if not success:
            break
        else:
            ret, buffer = cv2.imencode('.jpg', frame)
            frame = buffer.tobytes()
            yield (b'--frame\r\n'
                   b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')



@app.route('/')
def index():
	return render_template('index.html')
'''


feed = pm.main()
@app.route('/video_feed')
def video_feed():
    global feed
    return Response(feed, mimetype='multipart/x-mixed-replace; boundary=frame')

@app.route("/", methods=['GET', 'POST'])
def index():
    global feed
    if request.method == 'POST':
        if request.form.get('submit_btn') == 'off':
            if pm.cap is not None and pm.cap.isOpened():
                pm.cap.release()
                cv2.destroyAllWindows()
            elif gamer.cap is not None and gamer.cap.isOpened():
                gamer.cap.release()
                cv2.destroyAllWindows()
            feed=None
        elif  request.form.get('submit_btn') == 'Push Up':
            feed= gamer.main()
        elif  request.form.get('submit_btn') == 'Pose Module':
            feed= pm.main()
        elif  request.form.get('submit_btn') == 'Plank':
            feed= pl.main()
        elif  request.form.get('submit_btn') == 'Squat':
            feed= sq.main()
        elif  request.form.get('submit_btn') == 'Posture':
            feed= po.main()
        else:
            pass # unknown
    elif request.method == 'GET':
        return render_template('index.html')
    
    return render_template("index.html")


