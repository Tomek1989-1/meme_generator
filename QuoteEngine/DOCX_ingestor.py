"""This file is to create list of quotes based on DOCX file."""
from ingestor_interface import IngestorInterface
import docx
from quotemodel import quote_model


class docxIngestor(IngestorInterface):
    """This class inherits from IngestorInterface."""

    allowed_extension = 'docx'

    @classmethod
    def parse(cls, path: str):
        """List of quotes creation."""
        doc = docx.Document(path)
        quotes = []
        for i in doc.paragraphs:
            if len(i.text) > 0:
                quotes.append(quote_model(i.text.split(' - ')[0],
                                          i.text.split(' - ')[1]))
        return quotes
