from setuptools import setup, find_packages

setup(
    name="ravftp",
    version="0.3",
    packages=find_packages(),
    install_requires=[
        "pyftpdlib==1.5.6",
        "flask",
        "python-dotenv"
    ],
)
