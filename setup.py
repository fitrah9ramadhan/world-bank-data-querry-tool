from setuptools import setup

with open("README.MD", "r") as fh:
    long_description = fh.read()

setup(
    name='worldbankdatatransform',
    version='0.0.1',
    description='Transform data.worldbank.org/indicator csv files into one variable panel data, multivariable time series data, multivariable cross section data, or multivariable panel data.',
    py_modules=['worldbankdatatransform'],
    package_dir={'':'src'},
    long_description=long_description,
    long_description_content_type="text/markdown",
    install_requires = ["pandas"],
    url="https://github.com/fitrah9ramadhan/world-bank-data-query-tool",
    author="Muhammad Nur Fitrah Ramadhan",
    author_email="fitrah9ramadhan@gmail.com",
)

classifiers=[
    "Development Status :: 5 - Production/Stable",
    "Intended Audience :: Science/Research",
    "License :: OSI Approved :: MIT License",
    "Programming Language :: Python :: 3.9",
    "Operating System :: OS Independent",
]