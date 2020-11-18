import os
import sys
import json
from commons_data import *
from common_utilities import *
from urllib.parse import urlparse


class SiteSourceCleaner:

	def __init__(self, input_file=BIG_FILE_SOURCE_SITE):
		self.inpt_file = input_file
		self.output_file= BIG_FILE_SOURCE_SITE_DIRTY_JSON
		self.dictionary_site = {}

		if DEBUG_MODE:
			print("Init SiteSourceCleaner")

	def makeJsonFIle(self):
		with open(self.output_file, "w") as cleanedJson:
			cleanedJson.write(json.dumps(self.dictionary_site, indent=1))

	def getMappedID(self):
		return self.dictionary_site

	def loadJsonMappedSite(self):
		with open(self.output_file, "r") as cleanedJson:
			self.dictionary_site = json.load(cleanedJson)

			if DEBUG_MODE:
				print(f"Record founded: {len(self.dictionary_site.keys())} ")
				print("################################################")

				progressBar(len(self.dictionary_site.keys()), len(self.dictionary_site.keys()), f"{len(self.dictionary_site.keys())} of {len(self.dictionary_site.keys())}")

	def makeMapping(self):
		
		with open(self.inpt_file, "r", encoding=DEFAULT_ENCODING) as csvFile:
			
			lines = csvFile.readlines()
			lines_number = len(lines)
			lines_worked = 0
			counter_removed = 0

			if DEBUG_MODE:
				print(f"Record founded: {lines_number} ")
				print("################################################")

			for lineData in lines[1:]:
				lines_worked +=1
				if DEBUG_MODE:
					progressBar(lines_worked, lines_number, f"{lines_worked} of {lines_number}")

				objID, urlSite = self.__cleanString(lineData)

				if not urlSite in self.dictionary_site.keys():
					self.dictionary_site[urlSite] = []
				self.dictionary_site[urlSite].append(objID)

		if DEBUG_MODE:
			print(f"Sources Founded : {len(self.dictionary_site.keys())}")
			print("Cleaning low record Schemas")


		###Filtering out All Sources with 3 or less record
		###Make Dictionary Inverse Values As Key and Key As Value 
		###More space Exepencive  but needed for search optimization in SegmentCleaner
		tempdict = {}
		for key, value in self.dictionary_site.items():
			if len(value) > 3:
				for single_id in value:
					tempdict[single_id] = key
			else:
				counter_removed +=1

		if DEBUG_MODE:
			print(f"Site Removed : {counter_removed}")

		self.dictionary_site = tempdict

		

	def __cleanString(self, string):
		tokenLine = string.split(",")
		return tokenLine[0], urlparse(tokenLine[1]).netloc

