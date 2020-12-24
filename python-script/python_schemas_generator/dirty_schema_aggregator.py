import os
import json
from schemaLogger import SchemaLogger
from common_utilities import *
from commons_data import *


###Dict Organizzation
### dict[category][source]
### dict[category][source][schema&data]
### dict[category][source][schema_headers]

###### InputType Array of Dict

###### unkw_schema Format ########

############# Dict item ############## 

## simple key Value --> id, schema_source, category
## composite Key Value -->  schema->dict

######################################



class DirtySchemaAggragator:

	def __init__(self, input_folder=CLEAN_SEGMENTS_DICT):
		self.input_folder = input_folder
		self.schemas_counter = 0
		self.schemas_dict = {}
		self.logger = SchemaLogger()

	def startAggregation(self):

		for segment in os.listdir(self.input_folder):
			self.__searchSchema(segment)
		
		print(f"Category Founded: {len(self.schemas_dict.keys())}")
		
		for eachCategory, categoryEntries in self.schemas_dict.items():
			print(f"Category: {eachCategory} --> Sources: {len(categoryEntries.keys())}")

		self.__writeSchemas()

	def __normalizeKeyValue(self, itm):

		tmpDict = {}

		for key, value in itm.items():
			
			nkey= key.lower().replace(";", "")
			nvalue = value.lower().replace(";", "")
			tmpDict[nkey] = nvalue

		return tmpDict

	def __searchSchema(self, segmentName):

		with open(self.input_folder+segmentName, "r", encoding=DEFAULT_ENCODING) as c_segment:
			jsonArrayData = json.load(c_segment)
		
		for unkw_schema in jsonArrayData:

			###Building Category In Dictionary
			if not unkw_schema['category'] in self.schemas_dict.keys():
				self.schemas_dict[unkw_schema['category']] = {}

			###Building Sources-Category In Dictionary
			if not unkw_schema['schema_source'] in self.schemas_dict[unkw_schema['category']].keys():
				self.schemas_dict[unkw_schema['category']][unkw_schema['schema_source']] = { "schemas" : [], "schema_header" : []}

			###Populating Dictionary with schema. Each Schema is divided by source and category

			unkw_schema_norm = self.__normalizeKeyValue(unkw_schema["schema"])

			self.schemas_dict[unkw_schema['category']][unkw_schema['schema_source']]["schemas"].append(unkw_schema_norm)
			self.schemas_dict[unkw_schema['category']][unkw_schema['schema_source']]["schema_header"] += unkw_schema_norm.keys()


		print(f"Schema Matched in {segmentName}")

	def __writeSchemas(self):

		if not os.path.exists(SCHEMAS_DIRTY_DICT):
			os.mkdir(SCHEMAS_DIRTY_DICT)

		####Save each Schema as json

		for category, value in self.schemas_dict.items():

			if DEBUG_MODE:
				print(f"Building schemas In Category: {category}")
				counter_progression = 0
				total_counter = len( value.keys())

			if not os.path.exists(SCHEMAS_DIRTY_DICT+category):
				os.mkdir(SCHEMAS_DIRTY_DICT+category)



			for source, data in value.items():
				with open(f"{SCHEMAS_DIRTY_DICT}{category}/{source}.json", "w", encoding=DEFAULT_ENCODING) as jsonCatSchemaFile:
					jsonCatSchemaFile.write(json.dumps(data, indent=4))

				if DEBUG_MODE:
					counter_progression += 1
					progressBar(counter_progression, total_counter, f"Building Source {source} {counter_progression} of {total_counter}")


DirtySchemaAggragator().startAggregation()