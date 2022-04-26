from setuptools import setup

setup(
    name='personal',
    version='0.0.6',
    packages=['Basis',
            'Commons', 
            'Crunch', 'Crunch.Train',
            'Tex'],
    install_requires=[
        'requests',
        'numpy',
        'fraction',
        'IPython',
        'torch',
        'importlib; python_version == "3.8"',
    ],
)