from api.apps import city_file
import re

class SearchService():
	def __init__(self):
		return

	def search_city_by_name(self, search_query):
		"""
		This method searches for city within city file string
		if atleast one record is present, return list of city names
		else returns empty list.
		"""

		# multiline and case insensitive mode
		# escape meta characters if any in search_query
		regex_string = r'(?mi).*%s.*' % re.escape(search_query)

		# find all matches of the regex string in city_file and limit results to 50
		result = re.findall(regex_string, city_file)[:50]	
		return result
