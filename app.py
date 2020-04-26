import numpy as np 
from flask import Flask,request,render_template
import wikipedia
from bs4 import BeautifulSoup
import re
import datetime
import csv
import matplotlib.pyplot as plt
import pandas as pd
from vikiprocess import show

app = Flask(__name__)

@app.route('/')
def dynamic_page():
	return vikiprocess.show()
	
if __name__ == '__main__':
	app.run(debug=True)
