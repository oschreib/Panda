#The package of the files list
import os
from flask import Flask

app = Flask(__name__)

#Service get counts
@app.route('/')

def get_counts():
    with open("/home/vagrant/images-app/counts.txt", "r") as f:
      count = f.read()
      return str(count)
