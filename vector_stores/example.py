from langchain.schema.document import Document
from langchain_community.vectorstores import Qdrant

from embeddings import E5Embeddings
from settings import settings


def save_to_qdrant(documents: list[str], collection_name: str = 'e5_collection') -> Qdrant:
    embeddings = E5Embeddings()

    docs = [Document(page_content=text, metadata={'source': f'doc_{i}'}) for i, text in enumerate(documents)]

    return Qdrant.from_documents(
        documents=docs,
        embedding=embeddings,
        url=f'http://localhost:{settings.qdrant_rest_api}',
        collection_name=collection_name,
        vector_name='e5_vector',
        content_payload_key='content',
        metadata_payload_key='metadata',
    )


def check_similarity(vector_store: Qdrant, query: str, k: int = 3):
    results = vector_store.similarity_search_with_score(query=query, k=k)

    print('\nSimilarity Search Results:')
    for doc, score in results:
        print(f'Document: {doc.page_content}')
        print(f'Metadata: {doc.metadata}')
        print(f'Similarity Score: {score:.4f}')
        print('-' * 50)


if __name__ == '__main__':
    sample_docs = [
        'The quick brown fox jumps over the lazy dog.',
        'Machine learning is a subset of artificial intelligence.',
        'Python is a versatile programming language.',
        'Машинное обучение - это подмножество искусственного интеллекта.',
        'Машине навчання - це підмножина штучного інтелекту.',
        'Привіт, як справи?',
    ]

    vector_store = save_to_qdrant(sample_docs)

    query = 'What is machine learning?'
    check_similarity(vector_store, query, k=6)
