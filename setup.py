import setuptools

#with open("README.md", "r") as fh:
#    long_description = fh.read()

setuptools.setup(
    name="pygrim",
    version="0.0.1",
    author="Fredrik Johansson",
    author_email="fredrik.johansson@gmail.com",
    description="Python library for Fungrim",
    url="https://github.com/fredrik-johansson/fungrim",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 2",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=2.7,>=3.6',
)

