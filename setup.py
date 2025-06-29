from setuptools import setup
from setuptools import find_packages

setup(
    name="dumbwc-cli",
    description="a dumb implementation of wc tool of unix",
    long_description="a dumb implementation of wc tool of unix",
    version="1.0.0",
    url="https://github.com/im-mrnull/dumbwc",
    author="Shourya Rai",
    author_email="reachshourya3010@gmail.com",
    scripts=["scripts/dumbwc"],
    packages=find_packages("src"),
    package_dir={'': 'src'},
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License"
    ],
    install_requires=[]
)