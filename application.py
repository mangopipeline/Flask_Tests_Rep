'''
Created on Sep 19, 2019

@author: carlos
'''
from flask import Flask
from blue_prints.data_table import data_table_bp

APP = Flask('test_flask_app')
APP.register_blueprint( data_table_bp)

if __name__ == '__main__':
    APP.run(debug=True)