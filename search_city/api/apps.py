from django.apps import AppConfig
import os
import mmap

class ApiConfig(AppConfig):
	name = 'api'
	verbose_name = "Search City Api"
	def ready(self):
		# pass
		global city_list
		global city_file
		# try:
		# 	# Read txt file from location
		# 	BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
		# 	print BASE_DIR
		# 	# city_list
		# 	with open(BASE_DIR+"/city_names.txt") as city_names_file:
		# 		city = city_names_file.readlines()
		# 	# # you may also want to remove whitespace characters like `\n` at the end of each line
		# 	city_list = [x.strip() for x in city]
		# 	# print 'city_list'
		# 	# print city_list
		# except Exception, e:
		# 	print("Error: " + str(e))
		try:
			# Read txt file from location
			BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
			print BASE_DIR
			# city_list
			with open(BASE_DIR+"/city_names.txt") as city_names_file:
				city_file = mmap.mmap(city_names_file.fileno(), 0, prot=mmap.PROT_READ)
				print(city_file.readline())
				# city_file.close()
			# # you may also want to remove whitespace characters like `\n` at the end of each line
			
			# print 'city_list'
			# print city_list
		except Exception, e:
			print("Error: " + str(e))

		
