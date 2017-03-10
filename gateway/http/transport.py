import os

try:
    import requests
except ImportError:
    requests = None

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

def new_http_client(*args, **kwargs):
    """
    Get available HTTP Package from local system
    Implemented packages - (requests)
    """
    if requests is not None:
        implementation = RequestsTransport
    else:
        raise RuntimeError("Cant send request via HTTP. In your system, (Requests) package not found.")

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

    def request(self, http_method=HTTP_POST, http_url=None, request_data=None):
        raise NotImplementedError(
            'HTTPClient subclasses must implement `request`')


class RequestsTransport(HttpTransport):
    def __init__(self, timeout=60, **kwargs):
        super(RequestsTransport, self).__init__(**kwargs)
        self.timeout = timeout
        self.__session = requests.Session()

    def request(self, http_method=HTTP_POST, http_url=None, request_data=None):
        """
        Make HTTP request

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
        if self.verify_ssl:
            kwargs['verify'] = os.path.join(os.path.dirname(__file__), 'data/ca-certificates.crt')
        else:
            kwargs['verify'] = False

        if self.proxy:
            kwargs['proxies'] = self.proxy

        try:
            request_result = self.__session.request(
                method=http_method,
                url=http_url,
                json=request_data,
                timeout=self.timeout, **kwargs
            )
        except:
            raise

        return request_result.content, request_result.status_code, request_result.headers
