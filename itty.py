from itty import *
import subprocess, time, os, json
from func_get_n import n

@get('/')
def welcome(request):
    return 'Howdy!'

@get('/now')
def get_time(request):
    return time.ctime()

@get('/power')                      # curl http://localhost:8080/power?x=2&y=5
def compute_power_service(request):
    query = request.GET
    x = int(query.get('x', '0'))
    y = int(query.get('y', '0'))
    result = x ** y
    resp = json.dumps(result, indent=2)
    return Response(resp, content_type='application/json')     

