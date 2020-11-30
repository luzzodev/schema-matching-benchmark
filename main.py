import subprocess
import os
from commons_data import *
import sys

def AnalyzeMatch(f1, f2):
	result = subprocess.run(['java', '-jar', 'C:\\Users\ludovico\Desktop\\tesi\\benchmark\dumas\DumasOnFiles.jar', f1, f2], stdout=subprocess.PIPE).stdout.decode('latin1')
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
			return True
		return True
	except:
		print(f"Dumas Error {f1} --- {f2}")
		return False




fileCategoryList = os.listdir(SCHEMAS_DICT)

for category in fileCategoryList:
	schemaDir = f"{SCHEMAS_DICT}{category}/"
	fileSchemaCategoruList = os.listdir(schemaDir)
	for file1 in fileSchemaCategoruList:
		for file2 in fileSchemaCategoruList:
			if not file1 == file2:
				AnalyzeMatch(schemaDir + file1, schemaDir + file2)
					
