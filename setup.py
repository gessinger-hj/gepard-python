from setuptools import setup

setup(
    name="gepard-python",
    version="1.0",
    install_requires=[
        "python-dateutil"
    ],
    author = 'Hans-Juergen Gessinger',
    author_email = 'gessinger.hj@gmail.com',
    url = 'https://github.com/paulgessinger/gepard-python',
    py_modules=['gepard'],
    entry_points= {
    }
)
