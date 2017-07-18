from setuptools import setup

import os
longdescription = 'Add a fallback short description here'
if os.path.exists('README.rst'):
    longdescription = open('README.rst').read()

setup(
    name="gepard-python",
    version="1.0.19",
    license='MIT',
    install_requires=[
        "python-dateutil"
    ],
    author = 'Hans-Juergen Gessinger',
    author_email = 'gessinger.hj@gmail.com',
    url = 'https://github.com/gessinger-hj/gepard-python',
    py_modules=['gepard'],
    entry_points= {
    },
    keywords = "distributed-applications events semaphores locks messages JavaScript Java Python PHP messages",
    description = "Python client for gepard:General purpose communications for distributed applications / Microservices / events, semaphores and messages for JavaScript, Java, Python and PHP",
    long_description = longdescription
)
