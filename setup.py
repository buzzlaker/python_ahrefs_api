from setuptools import setup

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name='python_ahrefs_api',
    packages=['python_ahrefs_api'],
    version='0.0.2',
    description='Python library for using the ahrefs.com API',
    long_description=long_description,
    long_description_content_type="text/markdown",
    author='buzzlaker',
    author_email='john@techsystems.io',
    url='https://github.com/buzzlaker/python_ahrefs_api',
    classifiers=[
        'Environment :: Console',
        'Intended Audience :: End Users/Desktop',
        'License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)',
    ]
)
