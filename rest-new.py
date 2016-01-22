
from itty import *
import subprocess, time, os, json
from get_n import *

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

    query = request.GET
    n = float(query.get('n', '0'))
    fibo = Fibo(n).fibo()
    resp = json.dumps(fibo)
    return Response(resp, content_type='application/json')     

@get('/fibo_num')                      # curl http://localhost:8080/fibo_num?n=11.1
def fibo_num(request):
    query = request.GET
    n = float(query.get('n', '0'))
    fibo = fibo(n)
    resp = json.dumps(fibo)
    return Response(resp, content_type='application/json') 

if __name__ == '__main__':
    run_itty(host='')




