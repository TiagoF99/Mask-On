from twilio.rest import Client


def send_message(phone_number: str, message: str):
    """
    Send message 'message' to phone number 'phone_number'
    """
    # Your Account SID from twilio.com/console
    account_sid = "AC6024b9c33a37e1d8ab6edc2a76f885b7"
    # Your Auth Token from twilio.com/console
    auth_token = "537f8798b1db458f6085e7e8b8fcf06d"

    client = Client(account_sid, auth_token)

    sent_message = client.messages.create(
        to=phone_number,
        from_="+18327304073",
        body=message)

    print(sent_message.sid)


if __name__ == "__main__":
    # sample use
    send_message("+19059020370", "Do you have a mask on?")
