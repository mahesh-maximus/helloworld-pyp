import setuptools
from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="helloworld-pyp",
    version="0.0.7",
    author="Mahesh Maximus",
    author_email="",
    description="My first Python Package",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/mahesh-maximus/helloworld-pyp",
    project_urls={
        "Bug Tracker": "https://github.com/mahesh-maximus/helloworld-pyp/issues",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License"
    ],
    package_dir={'':"src"},
    packages=find_packages("src"),
    python_requires=">=3.6",
    entry_points={
                        'console_scripts': [
                                'hwpypcmd=hwpyp.mypy:sayHello',
                        ]
                }
)
