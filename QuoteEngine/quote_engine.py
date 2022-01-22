"""This file creates list of quotes based on input file."""
from PDF_ingestor import pdfIngestor
from CSV_ingestor import csvIngestor
from DOCX_ingestor import docxIngestor
from TXT_ingestor import txtIngestor


class Ingestor:
    """This class creates list of quotes."""

    ingestors = [csvIngestor, docxIngestor, pdfIngestor, txtIngestor]

    @classmethod
    def parse(cls, path: str):
        """Check which ingestor should be used & returns list of quotes."""
        for ingestor in cls.ingestors:
            if ingestor.can_ingest(path):
                return ingestor.parse(path)
