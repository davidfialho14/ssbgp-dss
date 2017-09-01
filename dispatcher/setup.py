from setuptools import setup, find_packages

setup(
    name='ssbgp-dss-dispatcher',
    version='0.1',
    description='Dispatcher component for SS-BGP distributed simulation system',
    url='',
    license='MIT',
    author='David Fialho',
    author_email='fialho.david@protonmail.com',

    packages=find_packages(),

    install_requires=[],

    extras_require={
        'test': ['pytest'],
    },
)
