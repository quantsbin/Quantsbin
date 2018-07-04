"""
    developed by Quantsbin - Jun'18

"""

from distutils.core import setup

try:
    with open('README.md') as file:
        long_description=file.read()
except:
    long_description='Quantitative Finance Tools'

setup(
    name='Quantsbin',
    version='0.0.1',
    description='Quantitative Finance Tools',
    long_description=long_description,
    long_description_content_type="text/markdown",
    author='Quantsbin',
    author_email='contactus@quantsbin.com',
    url='https://github.com/quantsbin/Quantsbin',
    packages=['quantsbin', 'quantsbin.derivativepricing', 'quantsbin.montecarlo'],
    license='MIT'
    )
