from setuptools import setup

setup(
    name='convenience',
    version='0.0.1',
    packages=['ExtendedNumpy'],
    install_requires=[
        'requests',
        'numpy',
        'importlib; python_version == "3.8"',
    ],
)