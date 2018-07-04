"""
    developed by Quantsbin - Jun'18

"""

from distutils.core import setup

setup(
    name='Quantsbin',
    version='0.1.0',
    description='Quantitative Finance Tools',
    long_description=open('README.md').read(),
    long_description_content_type="text/markdown",
    author='Quantsbin',
    author_email='contactus@quantsbin.com',
    url='https://github.com/quantsbin/Quantsbin',
    packages=['quantsbin', 'quantsbin.derivativepricing', 'quantsbin.montecarlo'],
    license='MIT'
    )
