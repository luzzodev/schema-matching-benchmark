import os
import sys
import json
import time
import math
from commons_data import *

#Due the huge size of input we consider to skip pandas usage 
#Input Segmentation approach





class InputSegmentator:

	def __init__(self, input_file=BIG_FILE_JSON, output_segments_dict=DIRTY_SEGMENTS_DICT, n_segment=N_OF_SEGMENT):
		self.input_file = input_file
		self.output_dict = output_segments_dict
		self.n_segment = n_segment

	def startSegmentation(self):

		with open(self.input_file, "r", encoding=DEFAULT_ENCODING) as fileStream:
			
			if DEBUG_MODE:
				print(f"Stream of {self.input_file} opened" )

			self.lines = fileStream.readlines()
			self.lines_count = len(self.lines)
			segment_size = math.floor(self.lines_count/ self.n_segment)

			if DEBUG_MODE:
				print(f">> Lines Loaded {self.lines_count}" )

			for n_seg in range(0, self.n_segment -1 ):				
				self.__makeSegments(n_seg, n_seg* segment_size, (n_seg+1)* segment_size )

			self__.makeSegments(self.n_segment -1, (self.n_segment -1)* segment_size, self.lines_count )



	def __makeSegments(self, segment_number, segment_start, segment_end):

		if DEBUG_MODE:
			print(f">> Building Segment #{segment_number} ({segment_end-segment_start} lines)" )

		with open(self.output_dict + f"segment_{segment_number}", "w", encoding=DEFAULT_ENCODING) as segmentFile:
			for line in self.lines[segment_start:segment_end]:
				segmentFile.write(line)

		if DEBUG_MODE:
			print(f">>Segment #{segment_number} Completed" )



class SegmentsCleaner:
	
	def __init__(self, input_dir=DIRTY_SEGMENTS_DICT, output_dir=CLEAN_SEGMENTS_DICT):

		self.dirty_segments_dir= input_dir
		self.clean_segments_dir= output_dir

		self.object_counter=0
		self.object_valid_counter=0


	def clearSegments(self):
		
		for dirty_segment in os.listdir(self.dirty_segments_dir):
			self.__clearSegment(dirty_segment)

		if DEBUG_MODE:
			print(f"All Segments Clean. Valid {self.object_valid_counter} of {self.object_counter}" )

	def __clearSegment(self, segment_name):

		local_object_counter = 0
		local_object_valid_counter = 0
		local_valid_object_list = []

		if DEBUG_MODE:
			print(f"Starting Cleaning {segment_name} segment" )

		with open(self.dirty_segments_dir+segment_name, "r", encoding=DEFAULT_ENCODING) as dirty_segment:

			dirty_segment_lines = dirty_segment.readlines()
			local_object_counter = len(dirty_segment_lines)
			self.object_counter += local_object_counter

			dirty_segment_json = json.loads("["+",".join(dirty_segment_lines)+"]")

			###Cleaning Phase

			for dirty_object in dirty_segment_json:
				if dirty_object["keyValuePairs"]:

					local_valid_object_list.append(dirty_object["keyValuePairs"])
					local_object_valid_counter += 1

			self.object_valid_counter += local_object_valid_counter

			if DEBUG_MODE:
				print(f"Starting {segment_name} segment cleaned. Valid {local_object_valid_counter} of {local_object_counter}" )

			###Saving CleanedSegment
			with open(self.clean_segments_dir+segment_name, "w", encoding="utf8") as segment_clean:
				segment_clean.write(json.dumps(local_valid_object_list, indent=-1))



main = InputSegmentator()
main.startSegmentation()

sCleaner = SegmentsCleaner()
sCleaner.clearSegments()

