#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
from flask import Flask
app = Flask(__name__)
app.debug = True

import sys

print(sys.maxunicode)
print(os.system('ls -l'))

import tensorflow as tf
import numpy as np
import pandas as pd

@app.route('/')
def index():
    print(os.system('cd /tmp && du -hd 1'))
    print(os.system('ls -larth /tmp'))
    x = tf.ones(5) * 2
    with tf.Session():
        y = x.eval()
    print(pd.__version__)
    return "Hello, world!" + str(y), 200

# We only need this for local development.
if __name__ == '__main__':
    app.run()
