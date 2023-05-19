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
        "googlemaps",
        "polyline", 
        "shapely"
    ],
)
