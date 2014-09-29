from distutils.core import setup


setup(name = "pymagento",
      author = "russ-",
      author_email = "russminus@gmail.com",
      url = "http://github.com/supplybuy/pymagento",
      version = "1.0.1",
      packages = [
          'pymagento',
      ],
      install_requires=[
          'xmlrpclib',
      ],
)
