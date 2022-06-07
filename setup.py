from setuptools import setup, find_packages
from pathlib import Path
this_directory = Path(__file__).parent
long_description = (this_directory / "README.md").read_text()

setup(
    name="ravftp",
    version="0.4.5",
    license='MIT',
    author="Raven Protocol",
    author_email='kailash@ravenprotocol.com',
    packages=find_packages(),
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/ravenprotocol/ravftp',
    keywords='Ravftp, ftp server, flask server',
    install_requires=[
        "pyftpdlib==1.5.6",
        "flask",
        "python-dotenv"
    ],
)
