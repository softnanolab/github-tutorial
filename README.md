# Github Tutorial

## Summary

A tutorial for new students learning how to use Github and Python

## Pre-requisities

- Python
- Git
- Basic understanding of your terminal

This tutorial uses WSL (Windows Subsystem for Linux) - using the BASH terminal.

## Quick Start

### Step 0 - Create a GitHub account and an access token

### Step 1 - Cloning the test repository

```bash
git clone https://<username>:<token>@github.com/softnanolab/github-tutorial
```

### Step 2 - Create your own branch

```bash
git checkout -b <name>
```

### Step 3 - Create a file

```bash
touch softnanoexample/test_function.py
```

### Step 4 - Add some code

```python
#!/usr/bin/env python
"""Am example function"""

def example_function():
    print("This is a test function!")
    return

def main():
    example_function()
    return

if __name__ == '__main__':
    main()
```

### Step 5 - Add your file to the repository and commit

```bash
git add softnanoexample/example.py
git commit softnanoexample/example.py -m 'Adding example function'
```

### Step 6 - Push your changes to GitHub

```bash
git push --set-upstream origin <name>
```

### Step 7 - Create a new branch for package initialisation

```bash
git checkout -b <name>-package
```

### Step 8 - Create a `setup.py` file then commit and push

```python
import setuptools

with open("README.md", "r", encoding='utf-8') as f:
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
```

```bash
pip install .
python -c "import softnanoexample"
```

```bash
git commit -a -m 'added setup.py'
git push -u origin <name>-package
```

### Step 9 - Create a tests ready for running `pytest` (then commit and push)

```bash
mkdir test
touch test/test_example.py
```

```python
from softnanoexample.example import function
def test_function():
    assert function() == "This is a test function!"
    return
```

```bash
pip install . 
pytest
git commit -a -m 'added tests'
```

### Step 10 - Create a pull request

### Step 11 - Add Continuous Integration

```bash
mkdir .github
mkdir .github/workflows
touch .github/workflows/quick-test.yml
```

```yml
```

```bash
git add .github
git commit -a -m 'added CI'
git push
```