#!/usr/bin/env python3
"""Package configuration."""
from setuptools import find_packages, setup


with open('README.rst', 'r') as readme:
    long_description = readme.read()

# Required dependencies
install_requires = [
    'apt',
    'requests'
]

# Extra dependencies
extras_require = {
    'tests': [  # Test dependencies
        'flake8>=3.5.0',
        'pytest>=3.5.0',
        'pytest-cov>=2.5.1',
        'requests-mock>=1.3.0',
    ],
}

setup_requires = [
    'pytest-runner>=4.2',
]

setup(
    author='Riccardo Coccioli',
    author_email='rcoccioli@wikimedia.org',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: System Administrators',
        'License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)',
        'Natural Language :: English',
        'Operating System :: POSIX :: Linux',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
        'Topic :: System :: Software Distribution',
        'Topic :: System :: Systems Administration',
    ],
    description='Client for Debmonitor, a Debian package tracker',
    keywords=['debmonitor', 'apt', 'deb'],
    license='GPLv3+',
    long_description=long_description,
    name='debmonitor-client',
    packages=find_packages(exclude=['tests']),
    platforms=['GNU/Linux', ],
    extras_require=extras_require,
    setup_requires=setup_requires,
    url='https://gerrit.wikimedia.org/g/operations/software/debmonitor-client',
    use_scm_version=True,
    zip_safe=False,
    entry_points={
        'console_scripts': [
            'debmonitor-client = debmonitor_client.cli:run_cli'
        ],
    }
)
