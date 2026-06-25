# Abstraction

# Reduce Complexity by hiding hidding unnecessary details.


class EmailServices:

    def _connect(self):
        print("Connecting to email server")

    def _authenticate(self):
        print("Authenticating...")
    
    def send_email(self):
        self._connect()
        self._authenticate()
        print("sending emails")
        self._disconnect()

    def _disconnect(self):
        print("Disconnecting from email server...")


email = EmailServices()
email.send_email()