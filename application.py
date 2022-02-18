#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Feb  5 21:43:36 2021

@author: govardhan
play file
"""
import os
from flask import Flask, render_template, request, \
    Response, send_file, redirect, url_for
from camera import Camera
from funcs import scan_image,Text_to_speech
app_path = os.path.dirname(os.path.realpath('__file__'))
p = '/'
application = Flask(__name__)
camera = None
def get_camera():
    global camera
    if not camera:
        camera = Camera()

    return camera


@application.route('/')
def root():
    return redirect(url_for('index'))

@application.route('/index/')
def index():
    return render_template('index.html')
def gen(camera):
    while True:
        frame = camera.get_feed()
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')
@application.route('/video_feed/')
def video_feed():
    camera = get_camera()
    return Response(gen(camera),
        mimetype='multipart/x-mixed-replace; boundary=frame')
@application.route('/capture/')
def capture():
    camera = get_camera()
    stamp = camera.capture()
    return redirect(url_for('show_capture', timestamp=stamp))

def stamp_file(timestamp):
    global timestampp
    timestampp = timestamp
    return 'captures/' + timestamp +".jpg"
    
   
@application.route('/capture/image/<timestamp>', methods=['POST', 'GET'])
def show_capture(timestamp):
    path = stamp_file(timestamp)
    print(path)
    if request.method == 'POST':
        print("go")
    
    return render_template('capture.html',
        stamp=timestamp, path=path )


@application.route('/result',methods=['POST','GET'])
def result():
    global fie
    fie = 'static/captures/'+timestampp+'.jpg'
    text = scan_image(fie)
    file_name = Text_to_speech(text,timestampp)
    file_name = p+'audio'+p+file_name
    return render_template('text_file.html',text = text,path = file_name)

if __name__ == '__main__':
    application.debug = True
    application.run()
