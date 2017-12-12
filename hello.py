def app(environ, start_response):
    start_response('200 OK', [('Content-Type', 'text/plain')])
    data = [environ['QUERY_STRING'].replace('&', '\n')]    
    return data