import os
import sys
import json

from commons_data import *


###Dict Organizzation
### dict[category][source]
### dict[category][source][schema&data]
### dict[category][source][schema_headers]
class SchemaAggragator:

	def __init__(self, input_folder=CLEAN_SEGMENTS_DICT):
		self.input_folder = input_folder
		self.schemas_counter = 0
		self.schemas_dict = {}
		self.record_distribution = {}

	def startAggregation(self):

		for segment in os.listdir(self.input_folder):
			self.__searchSchema(segment)
		
		print(f"Category Founded: {len(self.schemas_dict.keys())}")
		
		for eachCategory, categoryEntries in self.schemas_dict.items():
			print(f"Category: {eachCategory} --> Sources: {len(categoryEntries.keys())}")
		#test_counter2=0
		#test_glob = 0
		#for nKeys in self.schemas_dict.keys():
		#	testCounter = 0
		#	for schemaName in self.schemas_dict[nKeys]:
		#		if len(self.schemas_dict[nKeys][schemaName]) >= 4:
		#			testCounter +=1
		#			test_counter2 += 1

		#			if not len(self.schemas_dict[nKeys][schemaName]) in self.record_distribution.keys():
		#				self.record_distribution[len(self.schemas_dict[nKeys][schemaName])] = 0
		#			self.record_distribution[len(self.schemas_dict[nKeys][schemaName])] +=1
		#			test_glob += 1

		#	print(f"#Columns: {nKeys}  ->> #Schema: {len(self.schemas_dict[nKeys])} --> > 1 Record: {testCounter}")

		#print(f"Schemas Founded {self.schemas_counter}")
		#print(f"Schemas Founded with more the 3 records {test_counter2}")
		#print(f"Record Distribution:")

		#for cp in sorted(self.record_distribution.items(), key= lambda kv : kv[1], reverse=True):
		#	print(f"{cp} --> {((cp[1]/test_glob)*100):9.4f} %")

	def __alignSchemaLabels(self, listOfLabels):

		tempSet = set([label.lower() for label in listOfLabels])
		sortedLabels = sorted(list(tempSet))
		return sortedLabels

	def __buildSchema(self, labels, data):
		rows = []

		for eachRow in data:
			####Need To Align RowData With Labels
			row = []
			for label in labels:
				founded = False
				for key, value in eachRow.items():
					if label == key.lower():
						row.append(value)
						founded = True
						break
				if not founded:
					row.append("")
			rows.append(row)
		rows.insert(0, labels)
		return rows

	def writeSchemas(self):

		for category, sources in self.schemas_dict.items():

			if not os.path.exists(SCHEMAS_DICT+category):
				os.mkdir(SCHEMAS_DICT+category)

			for source, schema in  sources.items():
				schemaLabels = self.__alignSchemaLabels(schema["schema_header"])
				schemaLines = self.__buildSchema(schemaLabels, schema["schemas"])

				with open(SCHEMAS_DICT+category + f"/{source}.csv", "w", encoding=DEFAULT_ENCODING) as testFile:
					
					for row in schemaLines:
						rowLine = ";".join(row)
						testFile.write(rowLine + "\n")
			return

	def __searchSchema(self, segmentName):

		with open(self.input_folder+segmentName, "r", encoding=DEFAULT_ENCODING) as c_segment:
			jsonArrayData = json.load(c_segment)
		
		for unkw_schema in jsonArrayData:

			if not unkw_schema['category'] in self.schemas_dict.keys():
				self.schemas_dict[unkw_schema['category']] = {}

			if not unkw_schema['schema_source'] in self.schemas_dict[unkw_schema['category']].keys():
				self.schemas_dict[unkw_schema['category']][unkw_schema['schema_source']] = { "schemas" : [], "schema_header" : []}

			self.schemas_dict[unkw_schema['category']][unkw_schema['schema_source']]["schemas"].append(unkw_schema["schema"])
			self.schemas_dict[unkw_schema['category']][unkw_schema['schema_source']]["schema_header"] += unkw_schema["schema"].keys()


			schema_size = len(unkw_schema.keys())
			schema_family_name = "".join(sorted(unkw_schema.keys(), key= lambda k : k.lower()))

			if not schema_size in self.schemas_dict.keys():
				self.schemas_dict[schema_size] = {}

			if not schema_family_name in self.schemas_dict[schema_size].keys():
				self.schemas_dict[schema_size][schema_family_name] = []
				self.schemas_counter += 1

			self.schemas_dict[schema_size][schema_family_name].append(unkw_schema)

		print(f"Schema Matched in {segmentName}")



cc = SchemaAggragator()
cc.startAggregation()
cc.writeSchemas()