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
		self.removeQueque = []
		self.metaDictionary = {}

	def __getIndexOfHeader(self, headerName):
		try:
			header_index = self.headers.index(headerName)
			return header_index
		except:
			return -1

	def setHeaders(self, headers):
		self.headers = headers

	def changeHeader(self, header_old, header_new):

		try:
			oldMetaValue = self.metaDictionary[header_old]
			del self.metaDictionary[header_old]
			self.metaDictionary[header_new] = oldMetaValue
		except:
			pass
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

	def removeHeaders(self):
		start = time.time()
		newRows = []
		headers_number = len(self.headers)
		headersIndex = [ i for i in range(0, headers_number) if self.headers[i] in self.removeQueque]
		validheadersIndex = set([ i for i in range(0, headers_number)]).difference(set(headersIndex))
		validheadersIndex = sorted(validheadersIndex)
		#print(f"Removing {len(headersIndex)} of {headers_number} header")
		rows_number = len(self.rows)
		rowProcessed = 0
		
		for row in self.rows:
			newRow = []
			#rowProcessed += 1
			#progressBar(rowProcessed, rows_number, f"Schema Building2 {rowProcessed} of {rows_number}")
			for valid_colum in range(0, len(validheadersIndex)):
					newRow.append(row[validheadersIndex[valid_colum]])
			newRows.append(newRow)
		newHeders = []
		for valid_colum in range(0, len(validheadersIndex)):
			newHeders.append(self.headers[validheadersIndex[valid_colum]])
		self.headers = newHeders

		self.rows = newRows
		self.removeQueque = []
		end = time.time()
		#print(f"############ {end-start}")
		return True


	def addRemoveQuequeHeader(self, header):
		self.removeQueque.append(header)


	#############################################
	##### Meta Data Info and Data Representation
	#############################################

	def addMetaData(self, metaDict):
		self.metaDictionary = metaDict
		return True

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

	def getEmptyValuCounteOf(self, headerName):
		return self.metaDictionary[headerName]

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

	def BuildSchemaOld(self):
		
		newSchema = Schema()
		newSchema.setHeaders(self.headers)


		for header in self.headers:
			metaData_dictionary[header] = 0

		###Building Rows
		rowProcessed = 0
		totalRow = len(self.data)

		for single_row in self.data:
			tmpRow = []
			#if DEBUG_MODE:
				#rowProcessed += 1
				#progressBar(rowProcessed, totalRow, f"Schema Building2 {rowProcessed} of {totalRow}")
			for head_n in range(0, len(self.headers)):
				head_name = self.headers[head_n]
				try:
					tmpRow.append(single_row[head_name])
				except:
					tmpRow.append("")


			newSchema.addRow(tmpRow)
		return newSchema

	def BuildSchema(self):
		
		newSchema = Schema()
		newSchema.setHeaders(self.headers)

		metaData_dictionary = {}
		totalRow = len(self.data)
		for header in self.headers:
			metaData_dictionary[header] = totalRow

		###Building Rows
		rowProcessed = 0
		

		for single_row in self.data:
			tmpRow = [ "" for i in range(0, len(self.headers))]
			#if DEBUG_MODE:
				#rowProcessed += 1
				#progressBar(rowProcessed, totalRow, f"Schema Building {rowProcessed} of {totalRow}")

			for key in single_row.keys():
				tmpRow[self.headers.index(key)] = single_row[key]
				if not single_row[key] == "" and not single_row[key] == "\n":
					metaData_dictionary[key] -= 1

			

			newSchema.addRow(tmpRow)
		newSchema.addMetaData(metaData_dictionary)

		return newSchema