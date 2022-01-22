"""This file is to create list of quotes based on PDF file."""
from ingestor_interface import IngestorInterface
import subprocess
import os
import random
from quotemodel import quote_model


class pdfIngestor(IngestorInterface):
    """This class inherits from IngestorInterface."""

    allowed_extension = 'pdf'

    @classmethod
    def parse(cls, path: str):
        """List of quotes creation."""
        tmp = f'{random.randint(1,100000)}.txt'
        call = subprocess.run(['pdftotext', path, tmp])
        quotes = []
        file_ref = open(tmp, "r")
        with file_ref as infile:
            read = infile.read().strip()
        entries = read.split('\n')
        for i in entries:
            quotes.append(quote_model(i.split(' - ')[0], i.split(' - ')[1]))
        file_ref.close()
        os.remove(tmp)
        return quotes
