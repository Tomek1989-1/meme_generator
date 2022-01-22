"""This file it to provide interface for file ingestors."""
from abc import ABC, abstractmethod


class IngestorInterface(ABC):
    """Reference class for different ingestor types."""

    @classmethod
    def can_ingest(cls, path: str):
        """To check if file can be used."""
        return path.split('.')[-1] == cls.allowed_extension

    @abstractmethod
    def parse(self, path: str):
        """To create instant objects list."""
        pass
