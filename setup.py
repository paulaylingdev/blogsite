"""Setup package file for blogsite."""

from setuptools import setup


def readme():
    """Read in the readme file."""
    with open('readme.md') as f:
        return f.read()


setup(
    name='blogsite',
    version='0.1.0',
    description='Minimal blogging website',
    long_description=readme(),
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Environment :: Console',
        'Framework :: Flask',
        'Intended Audience :: Education',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.6',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content :: News/Diary',
    ],
    keywords='blog website flask minimal',
    url='https://github.com/paulaylingdev/blogsite',
    author='Paul Ayling',
    author_email='paulayling1@hotmail.com',
    license='MIT',
    packages=['blogsite'],
    include_package_data=True,
    install_requires=[
        'cssmin',
        'flask',
        'flask-sqlalchemy',
        'flask-assets',
        'Flask-HTMLmin',
    ],
    setup_requires=[
        'pytest-runner',
    ],
    tests_require=[
        'pytest',
    ],
)
