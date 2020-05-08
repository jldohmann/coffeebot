from twilio.rest import Client
from twilio.base.exceptions import TwilioRestException

accountSID = 'YOUR_ACCOUNT_SID'
authToken = 'YOUR_AUTH_TOKEN'

client = Client(accountSID, authToken)

twilioNumber = 'YOUR_TWILIO_NUMBER'

def valid_number(num):
    try:
        client.lookups.phone_numbers(num).fetch()
    except TwilioRestException:
        pass
    else:
        return num

phoneNumber = valid_number('YOUR_DESTINATION_PHONE_NUMBER')

print(phoneNumber)
