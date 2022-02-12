from importlib.metadata import entry_points
from setuptools import setup, find_packages

with open('README.rst', encoding='UTF-8') as f:
    readme = f.read()


setup(
    name='pgbackup',
    version='1.0.1',
    description='Database backups locally or to AWS S3.',
    long_description=readme,
    author='Kaushal',
    author_email='kaushalsharma880@gmail.com',
    url="https://github.com/iamkaushal/pg_backup",
    instal_requires=['boto3'],
    packages=find_packages('src'),
    package_dir={'': 'src'},


    # https://pypi.python.org/pypi?%3Aaction=list_classifiers
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Libraries',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
    ],


    entry_points={
        'console_scripts': [
            'pgbackup=pgbackup.cli:main',
        ]
    }
)
