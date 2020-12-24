import os
import sys
import json
from common_utilities import jaccard
from fuzzywuzzy import fuzz
from nltk.util import ngrams

with open("match_result.json", "r", encoding="utf-8") as resultFile:
	fileResult = json.load(resultFile)

with open("dumas_match_result.json", "r", encoding="utf-8") as resultDumasFile:
	fileDumasResult = json.load(resultDumasFile)

HEADERS_THRESHOLD = 0.8
VALUES_THRESHOLD = 0.015
##IF 5 GRAM VALUES_NGRAM_THRESHOLD = 0.025
##IF 4 GRAM VALUES_NGRAM_THRESHOLD = 0.035
##IF 3 GRAM VALUES_NGRAM_THRESHOLD = 0.08
VALUES_NGRAM_THRESHOLD = 0.025

NGRAM_NUMBER = 5

resultJaccardHeader = {}
resultJaccardValues = {}
resultJaccardValuesNGram = {}

resultEcoded = { "All" : []}
resultDumasEcoded = { "All" : []}
resultHeaderEncode = { "All" : [] }
resultValueEncoded = { "All" : [] }
resultValueNgramEncoded = { "All" : [] }


ENABLE_JACCARD_HEADER = True
ENABLE_JACCARD_VALUES = True
ENABLE_JACCARD_VALUES_NGRAM = False
ENABLE_DUMAS = True

ENABLE_PRINT_INFO = True


currentFM = 0
newFM = 0

class SchemaBuilder:

	def __init__(self, filePath):
		self.schema = {}
		self.headers = []

		self.__Build__(filePath)

	def __Build__(self, path):
		with open(path, "r", encoding="utf-8") as schemaFile:
			schemaRows = schemaFile.readlines()
			rowsNumber = len(schemaRows)
			self.headers = schemaRows[0].rstrip("\n").split(";")[1:]
			headersNumber = len(self.headers)
			for header in self.headers:
				self.schema[header] = []

			for x in range(1, rowsNumber):
				row = schemaRows[x].rstrip("\n").split(";")[1:]
				for hx in range(0, headersNumber):
					self.schema[self.headers[hx]].append(row[hx])

	def getHeaders(self):
		return self.headers

	def getValues(self, columName):
		return self.schema[columName]

	def getNgramValues(self, columName):
		ngramValueList = []
		for singleValue in self.schema[columName]:			
			if len(singleValue) < NGRAM_NUMBER:
				ngramValueList.append(singleValue)
			else:
				listofgram = list(ngrams(singleValue, NGRAM_NUMBER))
				ngramValueList += [ "".join(ngram) for ngram in listofgram]
		return ngramValueList



def calculateJaccard():
	
	for category in os.listdir("dataset"):
		
		fileNameList = sorted(os.listdir(f"dataset/{category}"))
		filesNumber = len(fileNameList)
		if ENABLE_PRINT_INFO:
			print(f"Comparing Category: {category}")
		for f1_index in range(0, filesNumber):

			s1build = SchemaBuilder(f"dataset/{category}/{fileNameList[f1_index]}")

			for f2_index in range(f1_index+1, filesNumber):
				s2build = SchemaBuilder(f"dataset/{category}/{fileNameList[f2_index]}")

				if ENABLE_JACCARD_HEADER:
					mtc_result_headers = calculateJaccardHeaders(s1build, s2build)
					addResult(resultJaccardHeader, category, fileNameList[f1_index], fileNameList[f2_index], mtc_result_headers)
				if ENABLE_JACCARD_VALUES:
					mtc_result_values = calculateJaccardOnValues(s1build, s2build)
					addResult(resultJaccardValues, category, fileNameList[f1_index], fileNameList[f2_index], mtc_result_values)
				if ENABLE_JACCARD_VALUES_NGRAM:
					mtc_result_valuesngram = calculateJaccardOnValuesNgram(s1build, s2build)
					addResult(resultJaccardValuesNGram, category, fileNameList[f1_index], fileNameList[f2_index], mtc_result_valuesngram)

def addResult(dict, category, f1, f2, result):
	if not category in dict.keys():
		dict[category] ={}
	if len(result) > 0:
		f1_name = f1
		f2_name = f2
		keyname = f"{f1_name};{f2_name}"

		if not keyname in dict[category].keys():
			dict[category][keyname] = []

		for single_result in result:
			dict[category][keyname].append({ f1_name : single_result[0],  f2_name : single_result[1]})

def calculateJaccardHeaders(schema1, schema2):

	headers1 = schema1.getHeaders()
	headers2 = schema2.getHeaders()
	headers1N = len(headers1)
	headers2N = len(headers2)

	matchResult = []

	for h1i in range(0, headers1N):
		for h2i in range(0, headers2N):
			if jaccard(headers1[h1i], headers2[h2i]) >= HEADERS_THRESHOLD:
				matchResult.append(((headers1[h1i], str(h1i)), (headers2[h2i], str(h2i))))

	return matchResult

def calculateJaccardOnValues(schema1, schema2):
	headers1 = schema1.getHeaders()
	headers2 = schema2.getHeaders()
	headers1N = len(headers1)
	headers2N = len(headers2)


	matchResult = []

	for h1i in range(0, headers1N):
		for h2i in range(0, headers2N):
			values1 = schema1.getValues(headers1[h1i])
			values2 = schema2.getValues(headers2[h2i])
			if jaccard(values1, values2) >= VALUES_THRESHOLD:
				matchResult.append(((headers1[h1i], str(h1i)), (headers2[h2i], str(h2i))))

	return matchResult

def calculateJaccardOnValuesNgram(schema1, schema2):
	headers1 = schema1.getHeaders()
	headers2 = schema2.getHeaders()
	headers1N = len(headers1)
	headers2N = len(headers2)


	matchResult = []

	for h1i in range(0, headers1N):
		for h2i in range(0, headers2N):
			values1 = schema1.getNgramValues(headers1[h1i])
			values2 = schema2.getNgramValues(headers2[h2i])
			scoreResult = jaccard(values1, values2)
			if scoreResult >= VALUES_NGRAM_THRESHOLD:
				matchResult.append(((headers1[h1i], str(h1i)), (headers2[h2i], str(h2i))))
			if scoreResult == -1:
				print(values1)
				print("############")
				print(values2)
				input()

	return matchResult

def EncodeDataToString(category,itemDict):
	sortedNames = sorted(itemDict.keys())
	return f"{category};{sortedNames[0]};{sortedNames[1]};{itemDict[sortedNames[0]][1]};{itemDict[sortedNames[1]][1]}"

def encodeAllResultMatch():

	categories = sorted(fileResult.keys())
	for category in categories:

		resultEcoded[category] = []
		resultDumasEcoded[category] = []
		resultHeaderEncode[category] = []
		resultValueEncoded[category] = []
		resultValueNgramEncoded[category] = []
		try:
			if ENABLE_PRINT_INFO:
				print(f"Encoding: {category}")
			###Encoding ResultMatch
			for mtch_files in fileResult[category].keys():
				for item in fileResult[category][mtch_files]:
					encodeditem = EncodeDataToString(category, item)
					resultEcoded[category].append( encodeditem)
					resultEcoded["All"].append( encodeditem)

			if ENABLE_PRINT_INFO:
				print(f"Encoding: {category}")
			###Encoding ResultMatch
			for mtch_files in fileDumasResult[category].keys():
				for item in fileDumasResult[category][mtch_files]:
					encodeditem = EncodeDataToString(category, item)
					resultDumasEcoded[category].append( encodeditem)
					resultDumasEcoded["All"].append( encodeditem)

			###Encoding Result Header
			if ENABLE_JACCARD_HEADER:
				for mtch_files in resultJaccardHeader[category].keys():
					for item in resultJaccardHeader[category][mtch_files]:
						encodeditem = EncodeDataToString(category, item)
						resultHeaderEncode[category].append( encodeditem)
						resultHeaderEncode["All"].append( encodeditem)


			###Encoding Result Value
			if ENABLE_JACCARD_VALUES:
				for mtch_files in resultJaccardValues[category].keys():
					for item in resultJaccardValues[category][mtch_files]:
						encodeditem = EncodeDataToString(category, item)
						resultValueEncoded[category].append( encodeditem)
						resultValueEncoded["All"].append( encodeditem)

			###Encoding Result Value Ngram
			if ENABLE_JACCARD_VALUES_NGRAM:
				for mtch_files in resultJaccardValuesNGram[category].keys():
					for item in resultJaccardValuesNGram[category][mtch_files]:
						encodeditem = EncodeDataToString(category, item)
						resultValueNgramEncoded[category].append( encodeditem)
						resultValueNgramEncoded["All"].append( encodeditem)
		except:
			print(f"Skipping Econding of {category}")

def calculate_P_R_FM(setGroundTruth, setGenerated):

	set1 = setGroundTruth
	set2 = setGenerated

	tp = set1.intersection(set2)
	fn = set1.difference(set2)
	fp = set2.difference(set1)

	try:
		precision = len(tp)/(len(tp) + len(fp))
	except:
		precision = 0
	try:
		recall = len(tp)/(len(tp) + len(fn))
	except:
		recall = 0
	try:
		f_measure = (2 * precision * recall)/(precision + recall)
	except:
		f_measure = 0

	return precision, recall, f_measure

def evaluate():

	global currentFM, newFM

	encodeAllResultMatch()
	####First Evalute Headers Approach


	categories = sorted(fileResult.keys())
	categories.append("All")
	#categories = ["Automotive"]
	for category in categories:


			setg = set(resultEcoded[category])	
			
			if ENABLE_JACCARD_HEADER:
				seth = set(resultHeaderEncode[category])
				precision_h, recall_h, f_measure_h = calculate_P_R_FM(setg, seth)
				if category =="All":
					newFM = f_measure_h

			if ENABLE_JACCARD_VALUES:
				setv = set(resultValueEncoded[category])
				precision_v, recall_v, f_measure_v = calculate_P_R_FM(setg, setv)
				if category =="All":
					newFM = f_measure_v

			if ENABLE_JACCARD_VALUES_NGRAM:
				setvn = set(resultValueNgramEncoded[category])
				precision_vn, recall_vn, f_measure_vn = calculate_P_R_FM(setg, setvn)
				if category =="All":
					newFM = f_measure_vn

			if ENABLE_DUMAS:
				setdm = set(resultDumasEcoded[category])
				precision_dm, recall_dm, f_measure_dm = calculate_P_R_FM(setg, setdm)
				

			if ENABLE_PRINT_INFO:
				print("------------------------------")
				print(f"Category : {category}")
				print("------------------------------")
				if ENABLE_JACCARD_HEADER:
					print(f"Jaccard ThresHolder: {HEADERS_THRESHOLD}")
					print("Jaccard Header Approach")
					print(f"Precision: {precision_h}")
					print(f"Recall: {recall_h}")
					print(f"F_Measure: {f_measure_h}")
					print("###################")

				if ENABLE_JACCARD_VALUES:
					print(f"Jaccard ThresHolder: {VALUES_THRESHOLD}")
					print("Jaccard Value Approach")
					print(f"Precision: {precision_v}")
					print(f"Recall: {recall_v}")
					print(f"F_Measure: {f_measure_v}")
					print("###################")

				if ENABLE_JACCARD_VALUES_NGRAM:
					print(f"Jaccard ThresHolder: {VALUES_NGRAM_THRESHOLD}")
					print(f"Jaccard Value NGram:{NGRAM_NUMBER} Approach")
					print(f"Precision: {precision_vn}")
					print(f"Recall: {recall_vn}")
					print(f"F_Measure: {f_measure_vn}")
				if ENABLE_DUMAS:
					print(f"Dumas Benchmark")					
					print(f"Precision: {precision_dm}")
					print(f"Recall: {recall_dm}")
					print(f"F_Measure: {f_measure_dm}")

def resetStats():

	global resultJaccardHeader, resultJaccardValues, resultJaccardValuesNGram
	global resultEcoded, resultHeaderEncode, resultValueEncoded, resultValueNgramEncoded

	resultJaccardHeader = {}
	resultJaccardValues = {}
	resultJaccardValuesNGram = {}

	resultEcoded = { "All" : []}
	resultHeaderEncode = { "All" : [] }
	resultValueEncoded = { "All" : [] }
	resultValueNgramEncoded = { "All" : [] }

def findSweetThresHold():
	global ENABLE_JACCARD_HEADER, ENABLE_JACCARD_VALUES, ENABLE_JACCARD_VALUES_NGRAM
	global currentFM, newFM
	global HEADERS_THRESHOLD, VALUES_THRESHOLD, VALUES_NGRAM_THRESHOLD

	ENABLE_JACCARD_HEADER = False
	ENABLE_JACCARD_VALUES = False
	ENABLE_JACCARD_VALUES_NGRAM = True
	counterCycle = 1
	while True:
		
		

		resetStats()
		calculateJaccard()
		evaluate()

		if newFM < currentFM:
			break
		currentFM = newFM

		print(f"Ciclio n:{counterCycle}")
		print(f"Current Threshold: {VALUES_NGRAM_THRESHOLD}")
		print(f"Current FM: {newFM}")
		print("----------------------")
		
		if ENABLE_JACCARD_HEADER:
			HEADERS_THRESHOLD += 0.1
		if ENABLE_JACCARD_VALUES:
			VALUES_THRESHOLD = ((VALUES_THRESHOLD * 1000) + 5) / 1000.0
		if ENABLE_JACCARD_VALUES_NGRAM:
			VALUES_NGRAM_THRESHOLD = ((VALUES_NGRAM_THRESHOLD * 1000) + 5) / 1000.0

		counterCycle += 1
	print(f"SweetThreshold: {((VALUES_NGRAM_THRESHOLD * 1000) - 5) / 1000.0}")
	print(f"FM: {currentFM}")
	

def main():

	#findSweetThresHold()
	calculateJaccard()
	evaluate()
	
	#with open("match_result_headers_jaccard.json", "w", encoding="utf-8") as jsonJaccardHeaderFile:
	#	json.dump(resultJaccardHeader, jsonJaccardHeaderFile, indent=4)
	#with open("match_result_values_jaccard.json", "w", encoding="utf-8") as jsonJaccardValueFile:
	#	json.dump(resultJaccardValues, jsonJaccardValueFile, indent=4)
	



main()