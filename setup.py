from distutils.core import setup
from setuptools import find_packages

version = '0.2.3'
setup(
  name = 'walkscore-api-binding',
  version = version,
  description = 'Unofficial WalkScore API binding',
  author = 'Jay Zeng',
  author_email = 'jayzeng@jay-zeng.com',
  url = 'https://github.com/knockrentals/walkscore',
  packages = find_packages(),
  download_url = (
      'https://github.com/knockrentals/walkscore/releases/tag/%s' % version
  ),
  keywords = ['walkscore', 'api', 'binding'],
  classifiers = [
      "Development Status :: 5 - Production/Stable",
      "Intended Audience :: Developers",
      "License :: OSI Approved :: MIT License",
      "Operating System :: OS Independent",
      "Programming Language :: Python",
      "Topic :: Scientific/Engineering :: GIS",
      "Topic :: Software Development :: Libraries :: Python Modules",
      "Programming Language :: Python :: 3 :: Only",
  ],
  test_suite='nose.collector',
  tests_require=['nose'],
)
