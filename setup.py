import setuptools

with open("README.md", "r") as f:
    long_description = f.read()

setuptools.setup(
    name="larix",
    version="0.1a1",
    author="Jérome Eertmans",
    author_email="jeertmans@icloud.com",
    description="TODO",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/jeertmans/Larix",
    install_requires=[
        "Click"
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    license="MIT",
    python_requires=">=3.7",
    entry_points="""
        [console_scripts]
        larix=app:main
    """,
)
