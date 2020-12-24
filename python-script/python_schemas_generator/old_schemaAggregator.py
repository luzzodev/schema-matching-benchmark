import os
import json
from schemaLogger import SchemaLogger
from common_utilities import *
from commons_data import *

from schema_builder import SchemaBuilder, Schema


###Dict Organizzation
### dict[category][source]
### dict[category][source][schema&data]
### dict[category][source][schema_headers]
class SchemaAggragator:

	def __init__(self, input_folder=SCHEMAS_DIRTY_DICT):
		self.input_folder = input_folder
		self.schemas_counter = 0
		self.schemas_dict = {}
		self.record_distribution = {}
		self.logger = SchemaLogger()


	####All this function is deprecated cause the process is now segmented
	#def startAggregation(self):

	#	for category in os.listdir(self.input_folder):
	#		self.__aggregateSourceSchema(category)
		
	#	print(f"Category Founded: {len(self.schemas_dict.keys())}")
		
	#	for eachCategory, categoryEntries in self.schemas_dict.items():
	#		print(f"Category: {eachCategory} --> Sources: {len(categoryEntries.keys())}")
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


		####OLD function searchSchema
			#schema_size = len(unkw_schema.keys())
			#schema_family_name = "".join(sorted(unkw_schema.keys(), key= lambda k : k.lower()))

			#if not schema_size in self.schemas_dict.keys():
			#	self.schemas_dict[schema_size] = {}

			#if not schema_family_name in self.schemas_dict[schema_size].keys():
			#	self.schemas_dict[schema_size][schema_family_name] = []
			#	self.schemas_counter += 1

			#self.schemas_dict[schema_size][schema_family_name].append(unkw_schema)


	def startAggregation(self):

		for category in os.listdir(self.input_folder):				
			for source in os.listdir(self.input_folder+category):
				self.__aggregateSourceSchema(category, source)


	def __aggregateSourceSchema(self, category, source):

		with open(f"{self.input_folder}{category}/{source}", "r", encoding=DEFAULTDEFAULT_ENCODING) as jsonDirtySchemaFile:
			jsonDirtySchema = json.load(jsonDirtySchemaFile)

		###Dropping Schemas With Low Record

		record_number = len(jsonDirtySchema['schema_header'])		
		if len(record_number) < MIN_ROW_X_SCHEMA + 1:
			self.logger.Log(self.__class__.__name__, f"Dropped Schema {source} For Category {category} - Founded: ({len(record_number) -1})")
			return 


		### Remove Duplicate header with set and order Result
		schema_headers = sorted(set(jsonDirtySchema['schema_header']))

		sourceSchema = SchemaBuilder(schema_headers, data).BuildSchema()
		sourceSchema.changeHeader("/n", EMPTY_LABEL_PLACEHOLDER)
		sourceSchema.changeHeader("", EMPTY_LABEL_PLACEHOLDER)


	

			

	def __alignSchemaLabels(self, listOfLabels):

		tempSet = set(listOfLabels)
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
					if label == key:
						row.append(value)
						founded = True
						break
				if not founded:
					row.append("")
			rows.append(row)
		rows.insert(0, labels)
		return rows

	def __columnFilter(self, schema, schemaName):

		tempSchemaDict = {}
		finalSchemaDict = {}
		finalSchema = []

		schemaLines = len(schema)

		####Mapping MultiDimArray to Dict to Filter columns

		for line_n in range(0, schemaLines):
			if line_n == 0:
				for label_n in range(0, len(schema[line_n])):
					tempSchemaDict[schema[line_n][label_n]] = []

				if not len(tempSchemaDict.keys()) == len(schema[line_n]):
					print("Schema label mismatch")
			else:
				for col_n in range(0, len(schema[line_n])):
					if not len(schema[line_n]) == len(schema[0]):
						print(f"Schema label mismatch {line_n} {schemaName}")
					tempSchemaDict[schema[0][col_n]].append(schema[line_n][col_n])

		####Once Dict is created Just iterate over it to check len and filter out bad result

		labelOrd = sorted(tempSchemaDict.keys())

		for label in labelOrd:
			totalColumnValue = len(tempSchemaDict[label])
			validColumnValue = totalColumnValue - tempSchemaDict[label].count("")

			minValidValueRequired = (totalColumnValue/100) * MIN_VALUES_X_COL_PCT

			#print(f"{schemaName} - {label}  ---> {validColumnValue} of {minValidValueRequired}")

			if validColumnValue >= minValidValueRequired:
				finalSchemaDict[label] = tempSchemaDict[label]
			else:
				self.logger.Log(self.__class__.__name__, f" - [Schema: {schemaName}] Dropping Column {label} ({validColumnValue} of {minValidValueRequired})")


		####Finally rewrite dict to Multidimensional array

		finalSchema.append(sorted(finalSchemaDict.keys()))

		###Here will be fixed empty label with placeholder

		for label_n in range(0, len(finalSchema[0])):
			if finalSchema[0][label_n] == "" or finalSchema[0][label_n] == "\n":
				finalSchema[0][label_n] = EMPTY_LABEL_PLACEHOLDER

		##################################################


		finalSchema[0].insert(0, "KeyCol")
		for row in range(1, schemaLines):
			finalSchema.append([])
			for label in labelOrd:
				try:
					finalSchema[row].append(finalSchemaDict[label][row])
				except:
					continue

			if len(finalSchema[row]) >= 1:
				finalSchema[row].insert(0, str(row))



		return finalSchema


	
	def writeSchemas(self):

		for category, sources in self.schemas_dict.items():

			if not os.path.exists(SCHEMAS_DICT+category):
				os.mkdir(SCHEMAS_DICT+category)

			if DEBUG_MODE:
				counter_sources = 0
				print(f"# Start to generate schemas on category {category}" )


			for source, schema in  sources.items():

				if DEBUG_MODE:
					counter_sources += 1
					progressBar(counter_sources, len(sources.keys()), f"Schema sources {source} {counter_sources} of {len(sources.keys())}")

				
				
				schemaLabels = self.__alignSchemaLabels(schema["schema_header"])
				schemaLines = self.__buildSchema(schemaLabels, schema["schemas"])

				schemaLines = self.__columnFilter(schemaLines, source)

				###Filtering Schemas with low record
				if len(schemaLines) < MIN_ROW_X_SCHEMA + 1:
					self.logger.Log(self.__class__.__name__, f"Dropped Schema {source} For Category {category} - Founded: ({len(schemaLines) -1})")
					continue

				with open(SCHEMAS_DICT+category + f"/{source}.csv", "w", encoding=DEFAULT_ENCODING) as testFile:
					

					for row_n in range(0, len(schemaLines)):
						try:
							rowLine = ";".join(schemaLines[row_n])
							nextrowLine = ";".join(schemaLines[row_n + 1])
							if len(rowLine) >= 1 and len(nextrowLine) >= 1:
								testFile.write(rowLine + "\n")
							else:
								testFile.write(rowLine)
						except:
							rowLine = ";".join(schemaLines[row_n])
							testFile.write(rowLine)

			self.logger.Flush()
			return



cc = SchemaAggragator()
cc.startAggregation()
cc.writeSchemas()