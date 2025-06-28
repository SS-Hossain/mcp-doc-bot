def send_email(to_email, subject, message):
    """
    Send an email with the given subject and message.
    """
    return f"Email sent to {to_email} with subject '{subject}'"

class EmailClient:
    """
    Simple email client for sending and receiving emails.
    """

    def __init__(self, smtp_server):
        """
        Initialize with SMTP server.
        """
        self.smtp_server = smtp_server

    def connect(self):
        """
        Connect to the SMTP server.
        """
        return f"Connected to {self.smtp_server}"
