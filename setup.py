from distutils.core import setup
import pymagento


setup(name = "pymagento",
      author = "russ-",
      author_email = "russminus@gmail.com",
      url = "http://github.com/supplybuy/pymagento",
      version = pymagento.__version__,
      packages = [
          'pymagento',
      ],
      install_requires=[
          'xmlrpclib',
      ],
)
