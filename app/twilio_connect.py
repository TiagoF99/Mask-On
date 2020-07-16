from twilio.rest import Client


def send_message(phone_number: str, message: str):
    """
    Send message 'message' to phone number 'phone_number'
    """
    # Your Account SID from twilio.com/console
    account_sid = ""
    # Your Auth Token from twilio.com/console
    auth_token = ""

    client = Client(account_sid, auth_token)

    sent_message = client.messages.create(
        to=phone_number,
        from_="+18327304073",
        body=message)

    print(sent_message.sid)


if __name__ == "__main__":
    # sample use
    send_message("", "Do you have a mask on?")
