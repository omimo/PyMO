import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="pymo",
    version="0.0.1",
    author="Omid Alemi",
    author_email="omid.alemi@gmail.com",
    description="A library for using motion capture data",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://omid.al/projects/PyMO.html",
    packages=setuptools.find_packages(),
    include_package_data=True,    # include files in MANIFEST.in
    classifiers=(
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ),
    install_requires=[    # dependencies
        'numpy',
        'pandas',
        'matplotlib',
        'scikit-learn'
    ]
)