import json
import os
import math
from datetime import datetime

from commons_data import *
from common_utilities import jaccard, getHostName, progressBar


def main():

	categories = os.listdir(SCHEMAS_DICT)

	pair_category = {}

	for category in categories:

		pair_category[category] = {}
		

		files_in_category = os.listdir(f"{SCHEMAS_DICT}{category}")

		print(f"Analizing Category {category}")

		files_num = len(files_in_category)
		for file_1_n in range(0, files_num):

			progressBar(file_1_n+1, files_num, f"[{file_1_n+1}/{files_num}] {files_in_category[file_1_n]}")
			#print(f"{SCHEMAS_DICT}{category}/{files_in_category[file_1_n]}")
			with open(f"{SCHEMAS_DICT}{category}/{files_in_category[file_1_n]}", "r", encoding=DEFAULT_ENCODING) as file1:
				rows_file_1 = file1.readlines()
				header1 = rows_file_1[0].split(";")

				hostName1 = getHostName(files_in_category[file_1_n])

				###Building inverse matrix
				invSchema_1 = []

				for h1_n in range(1, len(header1)):
					invSchema_1.append([ rows_file_1[i].rstrip("\n").split(";")[h1_n] for i in range(1, len(rows_file_1))])

			for file_2_n in range(file_1_n + 1, files_num):

				hostName2 = getHostName(files_in_category[file_2_n])

				if hostName1 == hostName2:
					continue

				scoreFounded = False

				with open(f"{SCHEMAS_DICT}{category}/{files_in_category[file_2_n]}", "r", encoding=DEFAULT_ENCODING) as file2:
					rows_file_2 = file2.readlines()

					header2=  rows_file_2[0].split(";")

					###Building inverse matrix
					invSchema_2 = []

					for h2_n in range(1, len(header2)):
						invSchema_2.append([ rows_file_2[i2].rstrip("\n").split(";")[h2_n] for i2 in range(1, len(rows_file_2))])


					for z_index_1 in range(0, len(invSchema_1)):
						for z_index_2 in range(0, len(invSchema_2)):
							jscore = jaccard(invSchema_1[z_index_1], invSchema_2[z_index_2])
							if jscore > JACCARD_MIN_SCORE:
								
								#print(set(invSchema_1[z_index_1]))
								#print(set(invSchema_2[z_index_2]))

								if not hostName1 in pair_category[category].keys():
									pair_category[category][hostName1] = []
								commonValues = set(invSchema_1[z_index_1]).intersection(set(invSchema_2[z_index_2]))
								commonValues.discard("")
								pairObject = {
									#"src_host" : hostName1,
									#"dst_host" : hostName2,
									"src_file" : files_in_category[file_1_n],
									"dst_file" : files_in_category[file_2_n]
									#"src_col_index" : z_index_1 +2,
									#"dst_col_index" : z_index_2 +2,
									#"score" : jscore,
									#"common_value" : list(commonValues)
									}
								pair_category[category][hostName1].append(pairObject)
								#print(category, files_in_category[file_1_n], files_in_category[file_2_n], z_index_1, z_index_2, jscore)

						
		
	dt_string = datetime.now().strftime("%d-%m-%Y-%H-%M-%S")
	fileName = f"{dt_string}.txt"
	with open(f"{JACCARD_MATCH_RESULT_DIR}{fileName}", "w", encoding=DEFAULT_ENCODING) as resultFile:
		json.dump(pair_category, resultFile, indent=4)
							
				



			



		
main()