from setuptools import setup

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name='py_kr_number',
    version='0.0.2',
    description='Simple Korean unit conversion module',
    url='https://github.com/yeokyoomin/py_kr_number.git',
    author='yeokyoomin',
    author_email='msdhgoom@gmail.com',
    long_description=long_description,
    long_description_content_type="text/markdown",
    license='yeokyoomin',
    zip_safe=False
)
