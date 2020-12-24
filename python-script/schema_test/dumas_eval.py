import subprocess
import os
import sys
import json

resultJSonDict = {}


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

	def getHeaderIndex(self, header):
		try:
			return self.headers.index(header)
		except:
			print(repr(header))
			print(repr(self.headers))
			sys.exit()

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

def AnalyzeMatch(category, fp1, fp2, f1, f2):
	print("Comparing:", fp1, fp2)
	result = subprocess.run(['java', '-jar', 'C:\\Users\ludovico\Desktop\\tesi\\benchmark\dumas\DumasOnFiles.jar', fp1, fp2], stdout=subprocess.PIPE).stdout.decode('latin1')
	#print(result)
	result = result.split("\n")
	resultData = False

	lines = []
	for line in result:
		#if line.startswith("score"):
			#print(line)

		if line.startswith("Schema"):
			resultData = True

		if line.startswith(">>>>>DUMAS"):
			resultData = False

		if resultData:
			lines.append(line)
	try:
		possibleResult = lines[1].split(";")
		if len(possibleResult[0]) > 1:
			print(f1, f2, f"Match --> {possibleResult[0]}")
			AddToResult(category, f1, f2, possibleResult[0])
			return True
		return True
	except:
		print(f"Dumas Error {f1} --- {f2}")
		print("eee")
		print(lines[1].split(";")[0])
		print(lines[1].split(";"))
		return False

	


def AddToResult(category, f1, f2, result):

	if not category in resultJSonDict.keys():
		resultJSonDict[category] = {}

	firstKey, secondKey = min(f1,f2), max(f1,f2)
	currentkeydict = f"{firstKey};{secondKey}"

	if not currentkeydict in resultJSonDict[category].keys():
		resultJSonDict[category][currentkeydict] = []

	resultString = result.encode("latin1").decode("utf-8")
	resultString = resultString.replace("} {", "};{").replace("{", "").replace("}", "")[:-1]
	matchList = resultString.split(";")


	for singleMatch in matchList:
		srcHeaders, dstHeaders = singleMatch.split("->")
		srcHeaders = srcHeaders.split(",")
		dstHeaders = dstHeaders.split(",")
		for singleSrcHead in srcHeaders:
			for singleDstHead in dstHeaders:
				resultJSonDict[category][currentkeydict].append( {f1 : (singleSrcHead, 0), f2: (singleDstHead, 0)})

	#if f1 == "organic-store.eu.json.csv" or f2 == "organic-store.eu.json.csv":
	#	print(result)
	#	print(f1,f2)
	#	print(firstKey, secondKey)
	#	print(resultJSonDict[category][currentkeydict])
	#	sys.exit()


def AdjustResultHeaderIndex():

	for category in resultJSonDict.keys():

		filepairList = resultJSonDict[category]

		for eachpair in filepairList:
			f1, f2 = eachpair.split(";")
			s1build = SchemaBuilder(f"dataset/{category}/{f1}")
			s2build = SchemaBuilder(f"dataset/{category}/{f2}")
			print(f"{category}/{f1}", f"{category}/{f2}")
			for itemdic in resultJSonDict[category][eachpair]:
				itemdic[f1] = (itemdic[f1][0], str(s1build.getHeaderIndex(itemdic[f1][0])))
				itemdic[f2] = (itemdic[f2][0], str(s2build.getHeaderIndex(itemdic[f2][0])))


def Main():
	fileCategoryList = os.listdir("./dataset/")

	for category in fileCategoryList:
		schemaDir = f"dataset/{category}/"
		fileSchemaCategoryList = os.listdir(schemaDir)
		filesNumber = len(fileSchemaCategoryList)
		for index_f1 in range(0, filesNumber):
			for index_f2 in range(index_f1+1, filesNumber):
				if not ((fileSchemaCategoryList[index_f1] == "2fwww.leasetrader.com.json.csv" and fileSchemaCategoryList[index_f2] == "adachevy.com.json.csv") or (fileSchemaCategoryList[index_f1] == "2fwww.leasetrader.com.json.csv" and fileSchemaCategoryList[index_f2] == "huntersvilleford.com.json.csv")):
					AnalyzeMatch(category, schemaDir + fileSchemaCategoryList[index_f1], schemaDir + fileSchemaCategoryList[index_f2], fileSchemaCategoryList[index_f1], fileSchemaCategoryList[index_f2])
					
			
		

	AdjustResultHeaderIndex()
	with open("dumas_match_result.json", "w", encoding="utf-8") as resultJsonFile:
		json.dump(resultJSonDict, resultJsonFile, indent=4)

Main()
					
