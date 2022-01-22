"""This file is to create list of quotes based on TXT file."""
from ingestor_interface import IngestorInterface
from quotemodel import quote_model


class txtIngestor(IngestorInterface):
    """This class inherits from IngestorInterface."""

    allowed_extension = 'txt'

    @classmethod
    def parse(cls, path: str):
        """List of quotes creation."""
        quotes = []
        with open(path, 'r') as infile:
            read = infile.read().strip()
        entries = read.split('\n')
        for i in entries:
            quotes.append(quote_model(i.split(' - ')[0], i.split(' - ')[1]))
        return quotes
