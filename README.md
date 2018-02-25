# django-autocomplete-api
Autocomplete Rest api to search cities by names

  1) A django application which serves a autocomplete JSON REST API

  2) Import the list of city names from file city_names.txt (Download here: https://goo.gl/ziBFRG)

  3) Application should be provided with an initial list of city names from the above downloaded file which is loaded once during application startup in search_city/api/apps.py 

  4) The API should accept one or more characters of input as 'q' parameter for the API '/search-city/' and return with autocomplete suggestions for matched city names (maximum 50 results)

  5) Do not store the city names in database. Just store them in application memory. File is stored in memory using mmap module.

  6) The API URL is optimized for time and speed by searching regex on mmap file.

  7) Create a free acount, deploy and host your django project on www.heroku.com 

  Live demo on heroku
  https://pure-earth-30986.herokuapp.com/api/v1/search-city/?q=Mumbai
