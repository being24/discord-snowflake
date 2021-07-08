import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="discosnow",
    version="0.0.5",
    author="being24",
    author_email="being24@gmail.com",
    description="A simple tools comvert from discord id to datetime",
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
