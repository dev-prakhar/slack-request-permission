import io

import setuptools


def readme():
    with io.open('README.md', 'r', encoding='utf8') as f:
        return f.read()


def requirements():
    req = []
    for line in open('requirements.txt', 'r'):
        req.append(line.split()[0])
    return req


setuptools.setup(
    name='slack-request-permission',
    version='1.0.3',
    author="Prakhar Shrivastava",
    author_email="prakhars1996@gmail.com",
    description="A python package that authenticates that the request is coming from slack",
    long_description=readme(),
    long_description_content_type="text/markdown",
    url="https://github.com/dev-prakhar/slack-request-permission",
    packages=setuptools.find_packages(),
    install_requires=requirements(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
