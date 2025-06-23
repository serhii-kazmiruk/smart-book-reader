from pathlib import Path
from typing import Any

from langchain.embeddings.base import Embeddings
from sentence_transformers import SentenceTransformer


class E5Embeddings(Embeddings):
    def __init__(self, model_name: str = 'multilingual-e5-large', **kwargs: Any) -> None:
        """Initialize the E5 embeddings model"""
        super().__init__(**kwargs)

        self.model = SentenceTransformer(str(Path(__file__).parent.parent / 'models' / model_name))

    def embed_documents(self, texts: list[str]) -> list[list[float]]:
        """Embed search docs.

        Args:
            texts: List of text to embed.

        Returns:
            List of embeddings.
        """
        # Add passage prefix for documents as recommended by E5
        prefixed_texts = [f'passage: {text}' for text in texts]
        embeddings = self.model.encode(prefixed_texts, convert_to_numpy=True)
        return embeddings.tolist()

    def embed_query(self, text: str) -> list[float]:
        """Embed query text.

        Args:
            text: Text to embed.

        Returns:
            Embedding.
        """
        # Add query prefix as recommended by E5
        prefixed_text = f'query: {text}'
        embedding = self.model.encode([prefixed_text], convert_to_numpy=True)
        return embedding[0].tolist()

    async def aembed_documents(self, texts: list[str]) -> list[list[float]]:
        """Asynchronous Embed search docs.

        Args:
            texts: List of text to embed.

        Returns:
            List of embeddings.
        """
        return self.embed_documents(texts)

    async def aembed_query(self, text: str) -> list[float]:
        """Asynchronous Embed query text.

        Args:
            text: Text to embed.

        Returns:
            Embedding.
        """
        return self.embed_query(text)
