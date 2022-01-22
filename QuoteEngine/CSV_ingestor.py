"""This file is to create list of quotes based on CSV file."""
from ingestor_interface import IngestorInterface
import pandas as pd
from quotemodel import quote_model


class csvIngestor(IngestorInterface):
    """This class inherits from IngestorInterface."""
    
    allowed_extension = 'csv'

    @classmethod
    def parse(cls, path: str):
        """List of quotes creation."""
        df = pd.read_csv(path, header=0, sep=',')
        quotes = []
        for index, row in df.iterrows():
            quotes.append(quote_model(row['body'], row['author']))
        return quotes
