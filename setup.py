from setuptools import setup, find_packages

# Package metadata
NAME = "random_gen"
VERSION = "1.0.0"
DESCRIPTION = "A simple random number generator package"
AUTHOR = "Yichi.Zhang"
AUTHOR_EMAIL = "yichizhang2021@outlook.com"
URL = "https://github.com/yz611/random_gen"

# Define package dependencies, if any
INSTALL_REQUIRES = []

# Load long description from README.md
with open("README.md", "r", encoding="utf-8") as f:
    LONG_DESCRIPTION = f.read()

setup(
    name=NAME,
    version=VERSION,
    description=DESCRIPTION,
    long_description=LONG_DESCRIPTION,
    long_description_content_type="text/markdown",
    author=AUTHOR,
    author_email=AUTHOR_EMAIL,
    url=URL,
    packages=find_packages(),  # Automatically find and include all packages
    install_requires=INSTALL_REQUIRES,
    python_requires=">=3.6",
)
