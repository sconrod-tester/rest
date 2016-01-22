
from itty import *
import subprocess, time, os, json
from circuitous import Circle

@get('/')
def welcome(request):
    return 'Howdy!'

@get('/now')
def get_time(request):
    return time.ctime()

@get('/free')
def get_free_space(request):
    resp = subprocess.check_output('df', shell=True)
    return Response(resp, content_type='text/plain')

@get('/files')
def get_notes_directory(request):
    files = os.listdir('notes')
    resp = json.dumps(files, indent=2)
    return Response(resp, content_type='application/json')    

@get('/upper/(?P<word>[a-z]+)')     # curl http://localhost:8080/upper/hello
def uppercase_service(request, word):
    return word.upper()

@get('/power')                      # curl http://localhost:8080/power?x=2&y=5
def compute_power_service(request):
    query = request.GET
    x = int(query.get('x', '0'))
    y = int(query.get('y', '0'))
    result = x ** y
    resp = json.dumps(result, indent=2)
    return Response(resp, content_type='application/json')     

@get('/area')                      # curl http://localhost:8080/area?radius=11.1
def circle_area(request):
    query = request.GET
    radius = float(query.get('radius', '0'))
    area = Circle(radius).area()
    resp = json.dumps(area)
    return Response(resp, content_type='application/json')     

@get('/perimeter')                      # curl http://localhost:8080/perimeter?radius=11.1
def circle_perimeter(request):
    query = request.GET
    radius = float(query.get('radius', '0'))
    area = Circle(radius).perimeter()
    resp = json.dumps(area)
    return Response(resp, content_type='application/json') 

@get('/ang_to_grade')                      # curl http://localhost:8080/ang_to_grade?angle=5
def to_grade(request):
    query = request.GET
    angle = float(query.get('angle', '0'))
    area = Circle.angle_to_grade(angle)
    resp = json.dumps(area)
    return Response(resp, content_type='application/json') 


if __name__ == '__main__':
    run_itty(host='')




