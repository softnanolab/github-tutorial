import setuptools

with open('README.md', 'r') as f:
    long_description = f.read()

setuptools.setup(
    name="softnanoexample",
    version="0.0.1",
    author="Debesh Mandal",
    description="Example Package",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/softnanolab/github-tutorial",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3"
)