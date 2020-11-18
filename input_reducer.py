import os
import sys
import json
import time
import math
from commons_data import *
from common_utilities import *

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

			self.__makeSegments(self.n_segment -1, (self.n_segment -1)* segment_size, self.lines_count )



	def __makeSegments(self, segment_number, segment_start, segment_end):

		if DEBUG_MODE:
			print(f">> Building Segment #{segment_number} ({segment_end-segment_start} lines)" )
			counter = 0

		with open(self.output_dict + f"segment_{segment_number}", "w", encoding=DEFAULT_ENCODING) as segmentFile:
			for line in self.lines[segment_start:segment_end]:
				if DEBUG_MODE:
					counter += 1
					progressBar(counter, segment_end - segment_start, f"Segment {segment_number} {counter} of {segment_end - segment_start}")

				segmentFile.write(line)

		if DEBUG_MODE:
			print(f">>Segment #{segment_number} Completed" )







main = InputSegmentator()
main.startSegmentation()



