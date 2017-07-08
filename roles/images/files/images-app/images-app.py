#The package of the files list
import os
import random

#The package of the api server
from flask import Flask
from flask import send_file

app = Flask(__name__)
count_int = 0
images_path='/home/vagrant/images-app/resources/'
images = os.listdir(images_path)

#Service get random image
@app.route('/')

def url_request():
    counter(1)
    return send_file(images_path + rnd())

def rnd():
    random_image = random.choice(images)
    return random_image

def counter(add_count):
    with open("/home/vagrant/images-app/counts.txt", "r+") as f:
        count = f.read()
        count_int = [ int(x) for x in count.split() ]
        count_int = sum(count_int)
        int(count_int)
        count_int +=add_count
        count_str = str(count_int)
        count = f.write
        f.seek(0)
        f.truncate()
        f.write(count_str)
    return str(count_int)
