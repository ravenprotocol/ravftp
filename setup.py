from setuptools import setup, find_packages

setup(
    name="ravftp",
    version="0.1-alpha",
    packages=find_packages(),
    install_requires=[
        "pyftpdlib==1.5.6"
    ],
)
