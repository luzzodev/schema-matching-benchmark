import os
import sys
import json
import time
import math
from commons_data import *
from common_utilities import *



class Schema:

	def __init__(self):
		self.headers = []
		self.rows = []

	def __getIndexOfHeader(self, headerName):
		try:
			header_index = self.headers.index(headerName)
			return header_index
		except:
			return -1

	def setHeaders(self, headers):
		self.headers = headers

	def changeHeader(self, header_old, header_new):
		for head_n in range(0, len(self.headers)):
			if self.headers[head_n] == header_old:
				self.headers[head_n] = header_new
				return True
		return False
	
	def addRow(self, row):
		self.rows.append(row)

	def removeHeader(self, headerName):
		
		header_index = self.__getIndexOfHeader(headerName)
		if header_index >= 0:
			###First Align Rows
			for row in self.rows:
				row.pop(header_index)

			self.headers.pop(header_index)
			
			return True
		return False


	#############################################
	##### Meta Data Info and Data Representation
	#############################################

	def getHeaders(self):
		return self.headers

	def countEmptyValueOf(self, headerName):
		count = 0
		header_index = self.__getIndexOfHeader(headerName)
		if header_index >= 0:
			for row in self.rows:
				if row[header_index] == "" or row[header_index] == "\n":
					count += 1
		return count

	def getRowsNumber(self):
		return len(self.rows)


	def getDoumasHeadersStr(self):
		return ";".join(["KeyCol"] + self.headers) + "\n"

	def getDoumasRowsStr(self):
		tmpRows = []

		rowIndexKey = 1
		for row_index in range(0, len(self.rows)):
			###Removing Empty Rows
			if self.rows[row_index].count("") + self.rows[row_index].count("\n") == len(self.rows[row_index]):
				continue
			aggregate_row = ";".join(self.rows[row_index])
			aggregate_row = aggregate_row.replace("\n", "")
			row = f"{rowIndexKey};{aggregate_row}"
			rowIndexKey +=1
			tmpRows.append(row)
		return "\n".join(tmpRows)


class SchemaBuilder:

	def __init__(self, headers, data):
		self.headers= headers
		self.data = data

	def BuildSchema(self):
		
		newSchema = Schema()
		newSchema.setHeaders(self.headers)

		###Building Rows

		for single_row in self.data:
			tmpRow = []
			for head_n in range(0, len(self.headers)):
				try:
					tmpRow.append(single_row[self.headers[head_n]])
				except:
					tmpRow.append("")
			newSchema.addRow(tmpRow)

		return newSchema