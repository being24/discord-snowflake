import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="discosnow",
    version="0.0.1",
    author="being24",
    description="A simple tool from discord-snowflake to time",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/being24/discord-snowflake",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3.7",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
