"""Setup package file for blogsite."""

from setuptools import setup


def readme():
    """Read in the readme file."""
    with open('readme.md') as f:
        return f.read()


setup(
    name='blogsite',
    version='0.1',
    description='Minimal blogging website',
    long_description=readme(),
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Environment :: Console',
        'Framework :: Flask',
        'Intended Audience :: Education',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Programming Language :: Python :: 2.7'
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content :: News/Diary',
    ],
    keywords='blog website flask minimal',
    url='https://github.com/paulaylingdev/blogsite',
    author='Paul Ayling',
    author_email='paulayling.dev@gmail.com',
    license='MIT',
    packages=['blogsite'],
    include_package_data=True,
    install_requires=[
        'flask',
        'flask-sqlalchemy',
    ],
)
