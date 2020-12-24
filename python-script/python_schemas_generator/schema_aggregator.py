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


	def startAggregation(self):

		for category in os.listdir(self.input_folder):
			#if not category == "Computers_and_Accessories":
				#continue
			counter_aggregation = 0
			for source in os.listdir(self.input_folder+category):

				if DEBUG_MODE:
					counter_aggregation += 1
					progressBar(counter_aggregation, len(os.listdir(self.input_folder+category)), f"Schema sources {source} {counter_aggregation} of {len(os.listdir(self.input_folder+category))}")

				self.__aggregateSourceSchema(category, source)
		self.logger.Flush()
				


	def __aggregateSourceSchema(self, category, source):

		with open(f"{self.input_folder}{category}/{source}", "r", encoding=DEFAULT_ENCODING) as jsonDirtySchemaFile:
			jsonDirtySchema = json.load(jsonDirtySchemaFile)

		###Dropping Schemas With Low Record

		record_number = len(jsonDirtySchema['schemas'])		
		if record_number < MIN_ROW_X_SCHEMA:
			self.logger.Log(self.__class__.__name__, f"Dropped Schema {source} For Category {category} - Founded: ({record_number})")
			return 


		### Remove Duplicate header with set and order Result
		schema_headers = sorted(set(jsonDirtySchema['schema_header']))

		sourceSchema = SchemaBuilder(schema_headers, jsonDirtySchema['schemas']).BuildSchema()
		sourceSchema.changeHeader("\n", EMPTY_LABEL_PLACEHOLDER)
		sourceSchema.changeHeader("", EMPTY_LABEL_PLACEHOLDER)

		###Removing Column With Low Value %

		totalColumnValue = sourceSchema.getRowsNumber()
		minValidValueRequired = (totalColumnValue/100) * MIN_VALUES_X_COL_PCT
		headers = list(sourceSchema.getHeaders())

		header_counter = 0
		header_total = len(headers)

		for header in headers:
			#Old With no metadata usage
			#validColumnValue = totalColumnValue - sourceSchema.countEmptyValueOf(header)

			#if DEBUG_MODE:
				#header_counter += 1
				#progressBar(header_counter, header_total, f"Schema Building1 {header_counter} of {header_total}")

			validColumnValue = totalColumnValue - sourceSchema.getEmptyValuCounteOf(header)
			if not validColumnValue >= minValidValueRequired:
				sourceSchema.addRemoveQuequeHeader(header)
				self.logger.Log(self.__class__.__name__, f"{category} - [Schema: {source}] Dropping Column {header} ({validColumnValue} of {minValidValueRequired})")
		sourceSchema.removeHeaders()
			

		###Once all process of filtering is ended if schema is still valid header >= 1 then write with keyPos

		if len(sourceSchema.getHeaders()) > 0:
			self.__writeSchema(category, source, sourceSchema)
	

			
	def __writeSchema(self, category, source, sourceSchema):

		if not os.path.exists(SCHEMAS_DICT+category):
			os.mkdir(SCHEMAS_DICT+category)

		with open(SCHEMAS_DICT+category + f"/{source}.csv", "w", encoding=DEFAULT_ENCODING) as testFile:
			testFile.write(sourceSchema.getDoumasHeadersStr())
			testFile.write(sourceSchema.getDoumasRowsStr())



	


cc = SchemaAggragator()
cc.startAggregation()
