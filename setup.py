from setuptools import setup, find_packages

setup(
    name="ravftp",
    version="0.4",
    license='MIT',
    author="Raven Protocol",
    author_email='kailash@ravenprotocol.com',
    packages=find_packages(),
    url='https://github.com/ravenprotocol/ravftp',
    keywords='Ravftp, ftp server, flask server',
    install_requires=[
        "pyftpdlib==1.5.6",
        "flask",
        "python-dotenv"
    ],
)
