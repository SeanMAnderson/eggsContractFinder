import requests
import ei_pb2
import base64
from google.protobuf.json_format import MessageToJson

contract_id = 'storage-storage-2022'
coop_id = 'shippingrun'
user_id = 'EI6593731765207040'

coop_status_request = ei_pb2.ContractCoopStatusRequest()
coop_status_request.contract_identifier = contract_id
coop_status_request.coop_identifier = coop_id
coop_status_request.user_id = user_id

url = 'https://www.auxbrain.com/ei/coop_status'
data = { 'data' : base64.b64encode(coop_status_request.SerializeToString()).decode('utf-8') }
response = requests.post(url, data = data)

authenticated_message = ei_pb2.AuthenticatedMessage()
authenticated_message.ParseFromString(base64.b64decode(response.text))

coop_status_response = ei_pb2.ContractCoopStatusResponse()
coop_status_response.ParseFromString(authenticated_message.message)

print("===")
print("")
print(MessageToJson(coop_status_response))
