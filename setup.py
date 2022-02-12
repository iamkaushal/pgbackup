from importlib.metadata import entry_points
from setuptools import setup, find_packages

with open('README.rst', encoding='UTF-8') as f:
    readme = f.read()


setup(
    name='pgbackup',
    version='1.0',
    description='Database backups locally or to AWS S3.',
    long_description=readme,
    author='Kaushal',
    author_email='kaushalsharma880@gmail.com',
    instal_requires=['boto3'],
    packages=find_packages('src'),
    package_dir={'': 'src'},
    entry_points={
        'console_scripts': [
            'pgbackup=pgbackup.cli:main',
        ]
    }
)
