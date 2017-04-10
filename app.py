#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys

from flask import Flask
import tensorflow as tf

app = Flask(__name__)
app.debug = True

print(sys.maxunicode)

@app.route('/')
def index():
    x = tf.ones(5) * 2
    with tf.Session():
        y = x.eval()
    return "Hello, world!" + str(y), 200

# We only need this for local development.
if __name__ == '__main__':
    app.run()
