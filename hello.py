def app(env: dict, start_response: callable(object)) -> tuple[str]:
    status = '200 OK'
    headers = [('Content-Type', 'text/plain')]

    params = env.get('QUERY_STRING', False)
    if params is False:
        status = '401 No params'
        params = 'ERROR! There is no params.'

    body = params.lstrip('/?').split('&')
    print(body)
    start_response(status, headers)
    return tuple(*body)
