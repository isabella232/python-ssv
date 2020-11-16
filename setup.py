import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="python-ssv-pablo-vs", # Replace with your own username
    version="0.0.1",
    author="Dankrad Feist",
    description="A python proof of concept of an SSV eth2 node",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/pablo-vs/python-ssv",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
    install_requires=[
        "flask>=1.1.2",
        "py_ecc>=4.1.0",
        "requests>=2.24",
        "grpcio",
        "py_ecc",
        "apscheduler",
        "protobuf",
        "googleapis-common-protos",
        "tzlocal",
        "flask"
    ],
    python_requires='>=3.6',
)
