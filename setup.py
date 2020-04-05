from setuptools import setup

long_description = open("README.md", "r").read()

setup(
    name="roblopy",
    packages=["roblopy", "roblopy.utils"],
    version="3.5",
    license="MIT",
    description="Roblox API built in Python",
    long_description=long_description,
    long_description_content_type="text/markdown",
    author="Jack Murrow",
    author_email="jack.murrow122005@gmail.com",
    url="https://github.com/jackprogramsjp/Roblopy",
    keywords=["Roblox", "Roblox Python", "Roblox Api"],
    install_requires=[
        "requests"
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License"
    ]
)
