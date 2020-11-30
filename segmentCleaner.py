import os
import sys
import json
import time
import math
from commons_data import *
from common_utilities import *
from site_source_cleaner import SiteSourceCleaner


class SegmentsCleaner:
	
	def __init__(self, input_dir=DIRTY_SEGMENTS_DICT, output_dir=CLEAN_SEGMENTS_DICT):

		self.dirty_segments_dir = input_dir
		self.clean_segments_dir = output_dir

		self.site_sources = SiteSourceCleaner()

		self.object_counter = 0
		self.object_valid_counter = 0


	def clearSegments(self):

		##First Site Mapping is required

		#self.site_sources.makeMapping()
		#self.site_sources.makeJsonFIle()
		self.site_sources.loadJsonMappedSite()
		self.site_sources_map = self.site_sources.getMappedID()
		
		for dirty_segment in os.listdir(self.dirty_segments_dir):
			self.__clearSegment(dirty_segment)

		if DEBUG_MODE:
			print(f"All Segments Clean. Valid {self.object_valid_counter} of {self.object_counter}" )

	def __clearSegment(self, segment_name):

		local_object_counter = 0
		local_object_valid_counter = 0
		local_valid_object_list = []
		counter_processed = 0

		if DEBUG_MODE:
			print(f"Starting Cleaning {segment_name} segment" )

		with open(self.dirty_segments_dir+segment_name, "r", encoding=DEFAULT_ENCODING) as dirty_segment:

			dirty_segment_lines = dirty_segment.readlines()
			local_object_counter = len(dirty_segment_lines)
			self.object_counter += local_object_counter

			dirty_segment_json = json.loads("["+",".join(dirty_segment_lines)+"]")
			segment_n_objects = len(dirty_segment_json)

			###Cleaning Phase
			for dirty_object in dirty_segment_json:

				if DEBUG_MODE:
					counter_processed += 1
					progressBar(counter_processed, segment_n_objects, f"Cleaning {segment_name} {counter_processed} of {segment_n_objects}")

				if dirty_object["keyValuePairs"] and dirty_object["category"]:
					

					try:
						schema_source = self.site_sources_map["" + str(dirty_object["id"])]
						local_valid_object_list.append({"id" : dirty_object["id"], "schema_source" : schema_source, "category" : dirty_object["category"], "schema" : dirty_object["keyValuePairs"]})
						local_object_valid_counter += 1
					except:
						continue

			self.object_valid_counter += local_object_valid_counter

			if DEBUG_MODE:
				print(f"# {segment_name} segment cleaned. Valid {local_object_valid_counter} of {local_object_counter}" )

			###Saving CleanedSegment
			with open(self.clean_segments_dir+segment_name, "w", encoding="utf8") as segment_clean:
				segment_clean.write(json.dumps(sorted(local_valid_object_list, key=lambda obj : len(obj.keys())), indent=-1))


sCleaner = SegmentsCleaner()
sCleaner.clearSegments()