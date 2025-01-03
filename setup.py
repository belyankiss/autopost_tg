from setuptools import setup, find_packages

setup(
    name="autopost_tg",
    version="0.0.1",
    description="Библиотека для создания автопостинга в чате",
    long_description=open("README.md", encoding="utf-8").read(),
    long_description_content_type="text/markdown",
    author="PyExecutor",
    author_email="belyankiss@gmail.com",
    url="https://github.com/belyankiss/autopost_tg",
    license="MIT",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
    install_requires=[
        "aiogram",
        "pydantic",
        "python-dateutil"
    ],
)