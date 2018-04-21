"""A Python-based script to interact with Polarion."""
from setuptools import find_packages, setup

setup(
    name='Polarizer',
    author='Og Maciel',
    author_email='omaciel@redhat.com',
    version='0.0.1',
    packages=find_packages(include=['polarizer', 'polarizer.*']),
    # See https://pypi.python.org/pypi?%3Aaction=list_classifiers
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
        'Programming Language :: Python :: 3.6',
    ],
    install_requires=[
        'Click',
        'rows',
        'suds-py3'
    ],
    entry_points='''
        [console_scripts]
        polarizer=polarizer:cli
    ''',
    include_package_data=True,
    license='GPLv3',
    description=('Performs queries and actions against a '
                 'Polarion instance.'),
    package_data={'': ['LICENSE']},
    url='https://github.com/omaciel/polarizer',
)
