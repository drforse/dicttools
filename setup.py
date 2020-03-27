import setuptools
import dicttools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="dicttools",
    version=dicttools.__version__,
    author="drforse",
    author_email="george.lifeslice@gmail.com",
    description="A package for iterating over ALL dict's keys and modifying them",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/drforse/dicttools",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)