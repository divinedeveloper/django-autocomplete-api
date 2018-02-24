from django.shortcuts import render
from api.custom_exceptions import CustomApiException
import django_filters
from rest_framework import filters
import json
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from django.http import HttpResponse
from api.services import SearchService 
from rest_framework import status


# Create your views here.
@csrf_exempt
def search_city(request):
	"""
	request contains q param with one or more characters
	returns: list of matched city names limited to 50 results
	"""
	try:
		search_query = request.GET.get('q', '').strip()
		if not search_query:
			raise CustomApiException("Please provide atleast one character to search city by name", status.HTTP_400_BAD_REQUEST)

		search_service = SearchService()
		result = search_service.search_city_by_name(search_query)

		HttpResponse.status_code = status.HTTP_200_OK
		return JsonResponse(result, safe=False)
	except CustomApiException as err:
		HttpResponse.status_code = err.status_code
		return JsonResponse({'status_code': err.status_code, 'message': err.detail})
	except Exception, e:
		HttpResponse.status_code = status.HTTP_500_INTERNAL_SERVER_ERROR
		return JsonResponse({'status_code': status.HTTP_500_INTERNAL_SERVER_ERROR, 'message': str(e)})
