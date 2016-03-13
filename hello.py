
def hello(request, start_response):
    status = '200 OK'
    headers_response = [('Content-Type', 'text/plain')]

    # body = 'Hello world'
    #
    # start_response(status, headers_response)
    #
    # return [body]

    queryString = request['QUERY_STRING']

    queryIdx = queryString.find('?')
    queryIdx += 1;

    resp = []
    if queryIdx < len(queryString):
        resp = queryString[queryIdx:].split('&')

    body = ''
    for curArg in resp:
        body += curArg
        body += '\n'


    start_response(status, headers_response)
    return [body]
 

   #
    #
    # def test(val):
    #     argList = []
    #
    #     idx = val.find('?')
    #     idx += 1
    #
    #     reqString = ''
    #     if len(val) > idx:
    #         reqString = val[idx:]
    #
    #
    #     respString = reqString.split('&')
    #
    #     for argVal in respString:
    #         print(argVal)
    #
    #
    #
    # req = '/?a=1&a=2&b=3'
    #
    # test(req)
    #
    #
    # setVal = [('Content-type', 'text/plain')]
    #
    # print(setVal)
