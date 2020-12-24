import os
from datetime import datetime
from commons_data import *

class SchemaLogger:

	class __SchemaLoggerSingleton:
		def __init__(self, logDir):
			self.logdir = logDir
			self.logLine = []

			dt_string = datetime.now().strftime("%d-%m-%Y-%H-%M-%S")
			self.fileName = f"{dt_string}.txt"

		def Log(self, modName, logline):
			dt_string = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
			self.logLine.append(f"[{modName}][{dt_string}] - {logline}")

			if len(self.logLine) > 200:
				self.Save()

		def Save(self):
			with open(self.logdir + self.fileName, "a+", encoding=DEFAULT_ENCODING) as logFile:
				for singleLog in self.logLine:
					logFile.write(f"{singleLog}\n")
			self.logLine = []

	instance = None

	def __init__(self, logDir=LOG_DICT):
		if not SchemaLogger.instance:
			SchemaLogger.instance = SchemaLogger.__SchemaLoggerSingleton(logDir)

	def Log(self, modName, logline):
		self.instance.Log(modName, logline)

	def Flush(self):
		self.instance.Save()

		


