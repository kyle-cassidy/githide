from setuptools import setup, find_packages

setup(
    name='githide',
    version='0.1',
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            'githide=githide.cli:main',
        ],
    },
    install_requires=[
        # Add any dependencies here
    ],
)
