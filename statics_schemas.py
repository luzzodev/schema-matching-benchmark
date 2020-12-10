import json
import os
import math

from commons_data import *


####Count headers number, rows number, average % of not null value x column


def countValidValuesAvgPct(rows):

	rows_number = len(rows)
	schema_headers = rows[0].split(";")
	headers_number = len(schema_headers)

	schema_rows = [line.split(";") for line in rows]

	avgValid = 0

	for x in range(1, headers_number):

		counterValid = 0

		for y in range(1, rows_number):
			if not schema_rows[y][x] in ["", "\n"]:
				counterValid +=1

		avgValid += (counterValid/(rows_number-1)*100)

	avgValid = avgValid / (headers_number-1)

	return math.floor(avgValid)




def main():

	categories = os.listdir(SCHEMAS_DICT)

	statistic_row = {}
	statistic_header = {}
	statistic_avg_not_null = {}

	for category in categories:

		statistic_row[category] = {}
		statistic_header[category] = {}
		statistic_avg_not_null[category] = {}

		files_in_category = os.listdir(f"{SCHEMAS_DICT}{category}")

		print(f"Analizing Category {category}")
		for schema_name in files_in_category:

			with open(f"{SCHEMAS_DICT}{category}/{schema_name}", "r", encoding=DEFAULT_ENCODING) as schemaFile:

				schema_rows = schemaFile.readlines()
				schema_headers = schema_rows[0].split(";")

				##Adding result

				rows_number = len(schema_rows) -1
				headers_number = len(schema_headers) - 1

				if not rows_number in statistic_row[category].keys():
					statistic_row[category][rows_number] = 0

				if not headers_number in statistic_header[category].keys():
					statistic_header[category][headers_number] = 0

				statistic_row[category][rows_number] += 1
				statistic_header[category][headers_number] += 1


				####Valid Pct
				avgValidPct = countValidValuesAvgPct(schema_rows)

				if not avgValidPct in statistic_avg_not_null[category].keys():
					statistic_avg_not_null[category][avgValidPct] = 0

				statistic_avg_not_null[category][avgValidPct] += 1

		####Writing csv file foreach category and stat

		if not os.path.exists(f"{STATS_DICT}{category}"):
			os.mkdir(f"{STATS_DICT}{category}")

		with open(f"{STATS_DICT}{category}/row_stats.csv", "w") as stats_row_file:
			orderedKey = sorted(statistic_row[category].keys())
			stats_row_file.write(f"key,value\n")
			for key in orderedKey:
				stats_row_file.write(f"{key},{statistic_row[category][key]}\n")

		with open(f"{STATS_DICT}{category}/header_stats.csv", "w") as stats_header_file:
			orderedKey = sorted(statistic_header[category].keys())
			stats_header_file.write(f"key,value\n")
			for key in orderedKey:
				stats_header_file.write(f"{key},{statistic_header[category][key]}\n")

		with open(f"{STATS_DICT}{category}/valid_value_stats.csv", "w") as stats_valid_file:
			orderedKey = sorted(statistic_avg_not_null[category].keys())
			stats_valid_file.write(f"key,value\n")
			for key in orderedKey:
				stats_valid_file.write(f"{key},{statistic_avg_not_null[category][key]}\n")




		
main()