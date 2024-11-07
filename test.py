from get_data_pdf import load_documents
from processing_data import split_document

documents = load_documents()
chunks = split_document(documents)
print(chunks[0])