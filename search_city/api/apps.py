from django.apps import AppConfig
import os
import mmap

class ApiConfig(AppConfig):
	name = 'api'
	verbose_name = "Search City Api"
	def ready(self):
		global city_file
		try:
			# Read txt file from location
			BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

			# open file and keep in memory map
			with open(BASE_DIR+"/city_names.txt") as city_names_file:
				city_file = mmap.mmap(city_names_file.fileno(), 0, prot=mmap.PROT_READ)
		except Exception, e:
			print("Error: " + str(e))

		
