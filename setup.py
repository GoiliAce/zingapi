from setuptools import setup

setup(
   name='zingapi',
   version="0.1.1",
   description='A light weight Python library for the ZingMp3 API',
   author='The DT',
   author_email='zombizombi51@gmail.com',
   packages=["zingapi"],
   install_requires=["aiohttp", "requests"]
)