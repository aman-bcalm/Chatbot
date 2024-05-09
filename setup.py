from setuptools import find_packages,setup

setup(
    name='chatbot',
    version='0.0.1',
    author='max payne',
    author_email='amanbon@gmail.com',
    install_requires=["ctransformers","sentence-transformers","pinecone-client","langchain","flask","pypdf","python-dotenv"],
    packages=find_packages(),
)