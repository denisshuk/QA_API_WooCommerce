import requests
from configuration import ENDPOINT
from baseclasses.response import Response
from enums.list_codes import ListStatusCodes

def test_endpoint(url: str = ENDPOINT, status_code: int = ListStatusCodes.SUCCES.value):
    '''
    This method use for check status endpoint.
    Endpoint and status code passed in arguments.
    Return - is whether the received status code corresponds to the passed one.
    '''
    input_data = requests.get(url)
    response = Response(input_data)
    print(input_data)
    response.assert_status_code(status_code)
