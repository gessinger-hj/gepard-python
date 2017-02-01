from setuptools import setup

setup(
    name="gepard-python",
    version="1.0.1",
    install_requires=[
        "python-dateutil"
    ],
    author = 'Hans-Juergen Gessinger',
    author_email = 'gessinger.hj@gmail.com',
    url = 'https://github.com/paulgessinger/gepard-python',
    py_modules=['gepard'],
    entry_points= {
    },
    keywords = [
    "distributed-applications",
    "events",
    "semaphores",
    "locks",
    "messages",
    "JavaScript",
    "Java",
    "Python",
    "message"
    ],
    description = "Python client for gepard:General purpose communications for distributed applications / Microservices / events, semaphores and messages for JavaScript, Java, Python and PHP",
)
