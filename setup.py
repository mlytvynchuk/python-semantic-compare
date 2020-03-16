import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="semantic_compare",
    version="0.9",
    author="Planeks",
    author_email="maxlytvynchuk@planeks.net",
    description="Library for sentence deconstruction",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/planeks-admin/NLP-spacy",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
    install_requires=[
        'tensorflow>=2.1.0',
        'tensorflow-hub>=0.7.0',
        'spacy>=2.2.3',
        'seaborn>=0.10.0'
    ],
)

