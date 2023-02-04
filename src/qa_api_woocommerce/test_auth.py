from enums.list_codes import ListStatusCodes
from woocommerce import API
from configuration import ENDPOINT,CONSUMER_KEY,SECRET_KEY

wcapi = API(
    url=ENDPOINT,
    consumer_key=CONSUMER_KEY,
    consumer_secret=SECRET_KEY,
    wp_api=True,
    version="wc/v3"
)

def test_auth():
    responce = wcapi.get("")
    assert responce.status_code == ListStatusCodes.SUCCES.value, responce.status_code 





