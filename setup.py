from setuptools import setup, find_packages

setup(
    name="biolib",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[],
    author="Dariusz Lenart",
    author_email="dariusz@lenart-it.pl",
    description="A library for biology computing and data manipulation",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/yourusername/biolib",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
    entry_points={
        "console_scripts": [
            "biolib-cli=biolib.cli:main",
        ],
    },
)