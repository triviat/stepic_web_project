def app(env, start_response):
    status = '200 OK'
    headers = [('Content-Type', 'text/plain')]

    params = env.get('QUERY_STRING', False)
    if params is False:
        status = '401 No params'
        params = 'ERROR! There is no params.'

    body = params.lstrip('/?').split('&')

    start_response(status, headers)
    return body
