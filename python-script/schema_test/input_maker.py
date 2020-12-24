import os
import sys
import json
import shutil

INPUT_RESULT_FILE = "../schema_comparison/match_result.csv"
INPUT_SCHEMAS_FOLDER = "C:/Users/ludovico/Desktop/tesi/benchmark/common_corpus/schemas/"
OUTPUT_SCHEMAS_FOLDER = "dataset/"
OUTPUT_RESULT_FILE = "match_result.json"

resultJSonDict = {}
schemaOutputDict = {}


def BuildDataSet():

	for category in schemaOutputDict.keys():
		if not os.path.exists(f"{OUTPUT_SCHEMAS_FOLDER}{category}"):
			os.mkdir(f"{OUTPUT_SCHEMAS_FOLDER}{category}")
		for fileName in schemaOutputDict[category]:
			shutil.copy2(f"{INPUT_SCHEMAS_FOLDER}{category}/{fileName}", f"{OUTPUT_SCHEMAS_FOLDER}{category}/{fileName}")


def main():
	
	#first Load Result Into Json
	with open(INPUT_RESULT_FILE, "r", encoding="utf-8") as resultFileCSV:
		resultLines = resultFileCSV.readlines()
	
	for resultLine in resultLines:
		singleResult = resultLine.rstrip("\n")
		if len(singleResult) < 1:
			continue
		category, f1, f2, h1, h2, h1i, h2i = [ token.strip() for token in singleResult.split(";")]

		if not category in resultJSonDict.keys():
			resultJSonDict[category] = {}
			schemaOutputDict[category] = []

		if not f1 in schemaOutputDict[category]:
			schemaOutputDict[category].append(f1)

		if not f2 in schemaOutputDict[category]:
			schemaOutputDict[category].append(f2)
		
		firstKey, secondKey = min(f1,f2), max(f1,f2)
		currentkeydict = f"{firstKey};{secondKey}"
		if not currentkeydict in resultJSonDict[category].keys():
			resultJSonDict[category][currentkeydict] = []
		resultJSonDict[category][currentkeydict].append( {f1 : (h1, h1i), f2: (h2, h2i)})

	with open(OUTPUT_RESULT_FILE, "w", encoding="utf-8") as resultFileJSON:
		json.dump(resultJSonDict, resultFileJSON, indent=4)

	BuildDataSet()

main()