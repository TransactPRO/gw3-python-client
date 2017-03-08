import os

try:
    import requests
except ImportError:
    requests = None


def new_http_client(*args, **kwargs):
    """
    Get available HTTP Package from local system
    Implemented packages - (requests)
    """
    if requests is not None:
        implementation = RequestsTransport
    else:
        raise RuntimeError("Cant send request via HTTP. In your system, (Pycurl) or (Requests) package not found.")

    return implementation(*args, **kwargs)


class HttpTransport(object):
    def __init__(self, verify_ssl=True, proxy=None, timeout=60):
        if verify_ssl is bool:
            self.__verify_ssl = verify_ssl
        else:
            self.__verify_ssl = True

        if proxy and type(proxy) is str:
            proxy = {"http": proxy, "https": proxy}
        self.__proxy = proxy.copy()

        if timeout is not None:
            self.__timeout = timeout
        pass

    # TODO Add response method for different Package

    def request(self, url, request_data=None):
        raise NotImplementedError(
            'HTTPClient subclasses must implement `request`')


class RequestsTransport(HttpTransport):
    def __init__(self, timeout=60, **kwargs):
        """
        Transporting HTTP request via Requests package

        Args:
            timeout (int): Timeout value
        """
        super(RequestsTransport, self).__init__(**kwargs)
        self.__timeout = timeout
        self.__session = requests.Session()
        pass

    def request(self, url, request_data=None):
        if request_data is None:
            request_data = {}

        kwargs = {}
        if self.__verify_ssl:
            kwargs['verify'] = os.path.join(os.path.dirname(__file__), 'data/ca-certificates.crt')
        else:
            kwargs['verify'] = False

        try:
            response = self.__session.request(url, json=request_data, timeout=self.__timeout, **kwargs)
        except:
            raise

        return response
