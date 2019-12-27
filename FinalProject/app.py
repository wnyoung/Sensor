from flask import Flask, render_template
import sys
import datetime
import RPi.GPIO as GPIO
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QIcon
import alarm
import oledTest

name = ''
num = 0

class Before(QWidget):
	def __init__(self):
		super().__init__()
		#self.initUI()
		self.getText()
		self.getInteger()
		
	def initUI(self):
		self.setWindowTitle("title")
		self.getText()
		self.getInteger()
		
	def getText(self):
		global name
		text, okPressed = QInputDialog.getText(self, "Get Integer", "Plant name: ", QLineEdit.Normal, "")
		if okPressed and text != '':
			print(text)
			name = text
			
	def getInteger(self):
		global num
		i, okPressed = QInputDialog.getInt(self, "Get integer", "Water rate: ", 28, 0, 100, 1)
		if okPressed:
			print(i)
			num = i
			alarm.func(i)
			oledTest.oled()
			
			
app = Flask(__name__)

@app.route('/')

def index():
	templateData = {
		'name': name,
		'cycle': num
	}
	return render_template('index.html', **templateData) 

if __name__ == "__main__":
	before = QApplication(sys.argv)
	print("11")
	ex = Before()
	print("22")
	app.run(host = '0.0.0.0', port = 80, debug = True)
	sys.exit(before.exec_())
