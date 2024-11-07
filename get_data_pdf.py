from langchain_community.document_loaders import PyPDFDirectoryLoader

data_path = "./data"

def load_documents():
    document_loader = PyPDFDirectoryLoader(data_path)
    return document_loader.load()
