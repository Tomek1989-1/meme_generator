"""This file is to provide class with quote definition."""


class quote_model:
    """This class defines quote's body and author."""

    def __init__(self, body, author):
        """Create quote's body and author."""
        self.body = body
        self.author = author

    def __repr__(self):
        """Quote's representation."""
        return f"{self.body} - {self.author}"
