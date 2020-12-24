import os
from commons_data import *


directoryFileToCheck = "C:/Users/ludovico/Desktop/tesi/benchmark/common_corpus/schemas/Computers_and_Accessories/"


fileList = os.listdir(directoryFileToCheck)

for fileName in fileList:
	with open(directoryFileToCheck+fileName, "r", encoding=DEFAULT_ENCODING) as file:
		print(f"Anlizyng File : {fileName}")
		fileLines = file.readlines()
		lineNumber = len(fileLines)

		labelNumber = len(fileLines[0].split(";"))

		for singleLineNumber in range(0, lineNumber):
			fieldNumberFounded  = len(fileLines[singleLineNumber].split(";"))
			if not labelNumber ==  fieldNumberFounded:
				print(f"Mismatch Field On Line {singleLineNumber} ->> Expeted: {labelNumber} Founded {fieldNumberFounded}")

		print("################################################")