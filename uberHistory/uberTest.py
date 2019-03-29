from uber_rides.session import Session
from uber_rides.client import UberRidesClient

session = Session(server_token='b8gGghhhPxZ49QKfaXK_mKM9M3TG5aYJOQZ7chYg')
client = UberRidesClient(session)

response = client.get_products(37.77, -122.41)
products = response.json.get('products')
print products