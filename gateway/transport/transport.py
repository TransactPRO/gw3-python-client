# The MIT License
#
# Copyright (c) 2017 Transact Pro.
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
# THE SOFTWARE.

from urllib.parse import (
    urlparse
)

try:
    import requests
except ImportError:
    requests = None

try:
    import pycurl
except ImportError:
    pycurl = None


# HTTP Methods const
# HTTP defines a set of request methods to indicate the desired action to be performed for a given resource.
# Although they can also be nouns, these requests methods are sometimes referred as HTTP verbs.
# Each of them implements a different semantic,
# but some common features are shared by a group of them:
# e.g. a request method can be safe, idempotent, or cacheable.
HTTP_POST = 'POST'
HTTP_HEAD = 'HEAD'
HTTP_GET = 'GET'
HTTP_PUT = 'PUT'
HTTP_DELETE = 'DELETE'
HTTP_CONNECT = 'CONNECT'
HTTP_OPTIONS = 'OPTIONS'
HTTP_TRACE = 'TRACE'
HTTP_PATCH = 'PATCH'


def new_http_client(cli_name='requests', *args, **kwargs):
    """
    Get available HTTP Package from local system
    Implemented packages - (requests)
    """
    if cli_name == 'requests':
        if requests is not None:
            implementation = RequestsTransport
        else:
            raise RuntimeError("Cant send request via HTTP. In your system, (Requests) package not found.")
    elif cli_name == 'pycurl':
        if pycurl is not None:
            implementation = PyCurlTransport
        else:
            raise RuntimeError("Cant send request via HTTP. In your system, (pycurl) package not found.")
    else:
        raise RuntimeError("Unknown implementation of http transport package given: " + cli_name)

    return implementation(*args, **kwargs)


class HttpTransport(object):
    def __init__(self, verify_ssl=True, proxy=None, timeout=60):
        if verify_ssl is bool:
            self.verify_ssl = verify_ssl
        else:
            self.verify_ssl = True

        if proxy:
            if type(proxy) is str:
                proxy = {"http": proxy, "https": proxy}

        self.proxy = proxy.copy() if proxy else None

        if timeout is not None:
            self.timeout = timeout
        pass

    def request(self, http_method=HTTP_POST, http_url=None, authorization_header=None, request_data=None):
        raise NotImplementedError(
            'HTTPClient subclasses must implement `request`')


class RequestsTransport(HttpTransport):
    def __init__(self, timeout=60, **kwargs):
        super(RequestsTransport, self).__init__(**kwargs)
        self.timeout = timeout
        self.__session = requests.Session()

    def request(self, http_method=HTTP_POST, http_url=None, authorization_header=None, request_data=None):
        """
        Make HTTP request via requests

        Returns:
            tuple: HTTP content, HTTP status code, HTTP headers

        Examples:
        (
            b'{"acquirer-details":{"eci-sli":275,"result-code":"000","status-description":' b'"Approved",
            "status-text":"Approved","terminal-mid":"3988920","transaction-id'
            b'":"ae:ece2a6585fcceae79294e2fe151fa71e"},"error":[],"gw":{"gateway-transacti'
            b'on-id":"0aca6fed-fff2-47d6-9da3-093e8f8e83ef","status-code":7,"status-text":' b'"SUCCESS"}}',

            200,

            {'Server': 'nginx/1.11.8', 'Content-Length': '315', 'Date': 'Thu, 09 Mar 2017 09:08:36 GMT', 'Content-Type':
            'application/json; charset=utf-8', 'X-Sessionid': '98SxgNljZ2i6tRyvLPIEDMUqBV1T5pQmnuf', 'X-Duration':
            '0.565', 'Connection': 'keep-alive', 'X-Version': 'v3.0'}
        )
        """
        if request_data is None:
            request_data = {}

        kwargs = {}
        if not self.verify_ssl:
            kwargs['verify'] = False

        if self.proxy:
            kwargs['proxies'] = self.proxy

        headers = None
        if authorization_header is not None:
            headers = {'Authorization': authorization_header}
        if http_method != HTTP_GET:
            headers['Content-Type'] = 'application/json'

        try:
            request_result = self.__session.request(
                method=http_method,
                url=http_url,
                headers=headers,
                json=request_data if http_method != HTTP_GET else None,
                timeout=self.timeout, **kwargs
            )
        except:
            raise

        return request_result.content, request_result.status_code, request_result.headers


class PyCurlTransport(HttpTransport):
    def __init__(self, timeout=60, **kwargs):
        super(PyCurlTransport, self).__init__(**kwargs)
        self.timeout = timeout
        if self.proxy:
            proxy = self.proxy
            for scheme in proxy:
                proxy[scheme] = urlparse(proxy[scheme])

    def request(self, http_method=HTTP_POST, http_url=None, authorization_header=None, request_data=None):
        """
        Make HTTP request via pycurl

        Returns:
            tuple: HTTP content, HTTP status code, HTTP headers

        Examples:
        (
             b'{"acquirer-details":{"eci-sli":336,"result-code":"000","status-description":'
             b'"Approved","status-text":"Approved","terminal-mid":"3988920","transaction-id'
             b'":"ae:d4dec6cb9cc353c2dfad10773455f0ef"},"error":{},"gw":{"gateway-transacti'
             b'on-id":"ffb366a8-2281-4aae-8296-e7ffbf404d02","status-code":7,"status-text":'
             b'"SUCCESS"}}',

             200,

             b'HTTP/1.1 200 OK\r\nServer: nginx/1.11.8\r\nDate: Wed, 22 Mar 2017 10:09:19 G'
             b'MT\r\nContent-Type: application/json; charset=utf-8\r\nContent-Length: 3'
             b'15\r\nConnection: keep-alive\r\nX-Duration: 1.065\r\nX-Sessionid: FdKIUXap'
             b'Sg5zoq8ZORD7uhAPTYEVn6Lxs3lkMyi1\r\nX-Version: v3.0\r\n\r\n'
         )
        """
        import json
        import io

        headers = []
        if authorization_header is not None:
            headers.append('Authorization:' + authorization_header)
        if http_method != HTTP_GET:
            headers.append('Content-Type: application/json')

        # Setup curl options
        c = pycurl.Curl()
        c.setopt(c.URL, http_url)
        c.setopt(pycurl.CUSTOMREQUEST, http_method)
        c.setopt(pycurl.HTTPHEADER, headers)
        c.setopt(pycurl.FAILONERROR, True)
        c.setopt(pycurl.FOLLOWLOCATION, True)
        c.setopt(pycurl.TIMEOUT, self.timeout)
        if http_method != HTTP_GET:
            c.setopt(pycurl.POSTFIELDS, json.dumps(request_data))

        header_buffer = io.BytesIO()
        body_buffer = io.BytesIO()
        c.setopt(c.HEADERFUNCTION, header_buffer.write)
        c.setopt(pycurl.WRITEFUNCTION, body_buffer.write)

        # Execute request via curl
        c.perform()

        # Parse response
        status_code = c.getinfo(pycurl.RESPONSE_CODE)
        headers = header_buffer.getvalue()
        content = body_buffer.getvalue()
        if content == "" or content is None:
            content = c.errstr()

        header_buffer.close()
        body_buffer.close()
        c.close()

        return content, status_code, headers
