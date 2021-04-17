from rest_framework.decorators import api_view
# from rest_framework.request import Request
from rest_framework.response import Response
# Create your views here.

@api_view()
def userAPI(request):
	context = [
	{'name' : 'sumit', 'language' : 'python'},
	{'name' : 'umesh', 'language' : 'c++'}
	]
	
	return Response(context)