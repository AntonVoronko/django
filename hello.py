def app(environ, start_response):
    start_response('200 OK', [('Content-Type', 'text/plain')])
    body = '\n'.join(environ['QUERY_STRING'].split('&'))
    return iter([body])