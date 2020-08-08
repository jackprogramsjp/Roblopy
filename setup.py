import os
from setuptools import setup, find_packages, Extension
from Cython.Build import cythonize

long_description = open("README.md", "r").read()

# https://cython.readthedocs.io/en/latest/src/userguide/source_files_and_compilation.html#distributing-cython-modules
def no_cythonize(extensions, **_ignore):
    for extension in extensions:
        sources = []
        for sfile in extension.sources:
            path, ext = os.path.splitext(sfile)
            if ext in (".pyx", ".py"):
                if extension.language == "c++":
                    ext = ".cpp"
                else:
                    ext = ".c"
                sfile = path + ext
            sources.append(sfile)
        extension.sources[:] = sources
    return extensions

extensions = [
    Extension("roblopy.assets", ["roblopy/assets.pyx"]),
    Extension("roblopy.friends", ["roblopy/friends.pyx"]),
    Extension("roblopy.groups", ["roblopy/groups.pyx"]),
    Extension("roblopy.user", ["roblopy/user.pyx"]),
]

CYTHONIZE = bool(int(os.getenv("CYTHONIZE", 0))) and cythonize is not None

if CYTHONIZE:
    compiler_directives = {"language_level": 3, "embedsignature": True}
    extensions = cythonize(extensions, compiler_directives=compiler_directives)
else:
    extensions = no_cythonize(extensions)

setup(
    name="roblopy",
    packages=["roblopy", "roblopy.utils"],
    ext_modules=extensions,
    version="5.1",
    license="MIT",
    description="Roblox API built in Python",
    long_description=long_description,
    long_description_content_type="text/markdown",
    author="Jack Murrow",
    author_email="jack.murrow122005@gmail.com",
    url="https://github.com/jackprogramsjp/Roblopy",
    keywords=["Roblox", "Roblox Python", "Roblox Api"],
    install_requires=[
        "requests",
        "beautifulsoup4"
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License"
    ]
)

