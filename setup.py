from setuptools import setup
import sys
PY3 = sys.version > '3'

if PY3:
    requires = []
else:
    requires = ['xmlrpclib']

setup(name = "pymagento",
      author = "russ-",
      author_email = "russminus@gmail.com",
      url = "http://github.com/supplybuy/pymagento",
      version = "1.1.1",
      packages = [
          'pymagento',
      ],
      install_requires=requires
)
