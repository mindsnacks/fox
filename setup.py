from setuptools import setup, find_packages
import sys, os

here = os.path.abspath(os.path.dirname(__file__))
README = open(os.path.join(here, 'README.rst')).read()
NEWS = open(os.path.join(here, 'NEWS.txt')).read()


version = '0.1.5'

install_requires = [
    # List your project dependencies here.
    # For more details, see:
    # http://packages.python.org/distribute/setuptools.html#declaring-dependencies
    "toml==0.8.1",
    "provtool==0.2.2",
    "biplist==0.6",
]


setup(name='fox',
    version=version,
    description="",
    long_description=README + '\n\n' + NEWS,
    classifiers=[
      # Get strings from http://pypi.python.org/pypi?%3Aaction=list_classifiers
      'Programming Language :: Python :: 2.7',
    ],
    keywords='xcode',
    author='Andy Mroczkowski',
    author_email='andy@mrox.net',
    url='',
    license='BSD',
    packages=find_packages('src'),
    package_dir = {'': 'src'},include_package_data=True,
    zip_safe=False,
    install_requires=install_requires,
    entry_points={
        'console_scripts':
            ['fox=fox.cli:main']
    }
)
