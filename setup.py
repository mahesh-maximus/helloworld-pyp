import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="helloworld-pyp",
    version="0.0.1",
    author="Mahesh Maximus",
    author_email="",
    description="helloworld pyp",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/mahesh-maximus/helloworld-pyp",
    project_urls={
        "Bug Tracker": "https://github.com/mahesh-maximus/helloworld-pyp/issues",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    package_dir={"": "hwpyp"},
    packages=setuptools.find_packages(where="hwpyp"),
    python_requires=">=3.6",
    entry_points={
                        'console_scripts': [
                                'hwpypcmd=hwpyp:sayHello',
                        ]
                }
)
