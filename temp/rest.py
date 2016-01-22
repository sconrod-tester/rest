from itty import *
import subprocess, time, os, json
from cache import *
from fibo import *
from itty import *
import subprocess, time, os, json

@get('/')
def welcome(request):
    return 'Welcome!'

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

@get('fibo')	# curl http://localhost:8080/fibo?x=2&y=5
def fibo(request):
	return fibo.i	
	

if __name__ == '__main__':

    run_itty(host='')





@get('/')
def welcome(request):
    return 'Welcome!'

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

if __name__ == '__main__':
    run_itty(host='')




