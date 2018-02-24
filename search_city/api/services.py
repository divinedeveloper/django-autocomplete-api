from api.apps import city_file
import re

class SearchService():
	def __init__(self):
		return

	def search_city_by_name(self, search_query):
		"""
		This method searches for city within city list
		if atleast one record is present, return city name
		else returns empty list
		"""
		# try:
			# importer_exporter_code_details = ImporterExporterCodeDetails.objects.get(importer_exporter_code= importer_exporter_code)
		# print "length of city file"
		# print len(city_file)
		# for eachCity in city_file:
		# 	if search_query in eachCity:
		# 		result.append(eachCity)
		result = []

		# mo = re.compile(search_query, re.IGNORECASE).search(city_file)
		# print "mo"
		# print mo.groups()

		mystring = """Zuerich (Kreis 4) / Aussersihl
		Mar''ina Horka 
		Marseille 09
		Hats'avan
		`Ain el Hadjel
		Sant Pere, Santa Caterina i La Ribera
		St. Pauli
		"""
		# mo = re.compile(search_query, re.IGNORECASE, re.MULTILINE).findall(city_file)
		# regex_string = r'%s.*+$' % search_query
		# regex_string = r'%s+' % search_query
		# regex_string = r'(^$)+$' % search_query
		# regex_string = r'\S.*%s.*\S' % search_query #this works as expected but fails for `( ) .
		# regex_string = r'\S.*\%s.*\S' % search_query #this works as expected but fails for ar, 09, `
		regex_string = r'\S.*\W*%s.*\S' % search_query #this works for ar ` but fails for 09

		print regex_string
		mo = re.compile(regex_string, re.IGNORECASE).findall(mystring)
		print "mo"
		print mo
		# if mo:
		# 	result.append(mo.group(search_query))	

		return mo
		# except ImporterExporterCodeDetails.DoesNotExist:
		# 	raise CustomApiException(utils.IEC_NOT_FOUND_IN_DB, status.HTTP_404_NOT_FOUND)