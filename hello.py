def app(env, start_response):
    status = '200 OK'
    headers = [('Content-Type', 'text/plain'),]

    params = env['QUERY_STRING']
    body = '\n'.join(params.lstrip('/?').split('&'))

    start_response(status, headers)
    return [bytes(body, 'ascii')]
