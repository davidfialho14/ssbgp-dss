from setuptools import setup, find_packages

setup(
    name='ssbgp-dss-simulator',
    version='0.1',
    description='Simulator component for SS-BGP distributed simulation system',
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
