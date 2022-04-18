from setuptools import setup

setup(
    name='convenience',
    version='0.0.2',
    packages=['ExtendedNumpy', 'Tex', 'Commons', 'Data'],
    install_requires=[
        'requests',
        'numpy',
        'fraction',
        'importlib; python_version == "3.8"',
    ],
)