from setuptools import setup

setup(
    name="streetviewext",
    version="0.0.1",
    description="Extensions for streetview module",
    author="hhe1ibeb",
    author_email="yeelainehou@gmail.com",
    url="https://github.com/hhe1ibeb/streetviewext",
    packages=["streetviewext"],
    install_requires=[
        'numpy',
        'pandas==1.2.3',
        'matplotlib==3.4.0'
    ],
)
