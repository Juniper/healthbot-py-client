__author__ = "Nitin Kumar"
__author_email__ = "nitinkr@juniper.net"
__licence__ = "Apache 2.0"

from setuptools import setup, find_packages

import versioneer


def requirements(filename='requirements.txt'):
    return open(filename.strip()).readlines()


with open("README.md", "r") as fh:
    long_description = fh.read()


install_requires = requirements()

setup(
    name='hbez',
    version=versioneer.get_version(),
    description='Healthbot Python Client',
    long_description=long_description,
    long_description_content_type="text/markdown",
    author=__author__,
    package_dir={'': 'lib'},
    packages=find_packages('lib'),
    install_requires=install_requires,
    include_package_data=True,
    license=__licence__,
    keywords=['Juniper HealthBot'],
    python_requires='>=3.4',
    classifiers=[
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Topic :: System :: Networking',
        'Operating System :: OS Independent',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ]
)
