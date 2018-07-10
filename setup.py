"""
    developed by Quantsbin - Jun'18

"""
import setuptools
from distutils.core import setup


# try:
#     with open('README.md') as file:
#         long_description=file.read()
# except:
#     long_description='Quantitative Finance Tools'

try:
    import pypandoc
    long_description = pypandoc.convert('README.md', 'rst')
except(IOError, ImportError):
    long_description = open('README.md').read()

setup(
    name='Quantsbin',
    version='1.0.2',
    description='Quantitative Finance Tools',
    long_description=long_description,
    long_description_content_type='text/markdown',
    author='Quantsbin',
    author_email='contactus@quantsbin.com',
    url='https://github.com/quantsbin/Quantsbin',
    packages=['quantsbin', 'quantsbin.derivativepricing', 'quantsbin.montecarlo'],
    license='MIT',
    classifiers=[ 'Development Status :: 3 - Beta', 
                  'Programming Language :: Python :: 3.4',
                  'Programming Language :: Python :: 3.5',
                  'Programming Language :: Python :: 3.6']
    )
