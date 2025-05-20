#!/usr/bin/env python3
"""Package configuration."""
from setuptools import find_packages, setup


with open('README.rst', 'r') as readme:
    long_description = readme.read()

# Required dependencies
INSTALL_REQUIRES = [
    # 'apt',  # Not present by choice on pypi.org, it must be installed via debian package
    'requests',
    'setuptools',
]

# Extra dependencies
EXTRAS_REQUIRE = {
    'tests': [  # Test dependencies
        'flake8>=3.5.0',
        'pytest>=3.5.0',
        'pytest-cov>=2.5.1',
        'requests-mock>=1.3.0',
    ],
}

SETUP_REQUIRES = [
    'setuptools_scm>=3.2.0',
]

setup(
    author='Riccardo Coccioli',
    author_email='rcoccioli@wikimedia.org',
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: System Administrators',
        'License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)',
        'Natural Language :: English',
        'Operating System :: POSIX :: Linux',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
        'Programming Language :: Python :: 3.12',
        'Programming Language :: Python :: 3.13',
        'Topic :: System :: Software Distribution',
        'Topic :: System :: Systems Administration',
    ],
    description='Client for Debmonitor, a Debian package tracker',
    keywords=['debmonitor', 'apt', 'deb'],
    install_requires=INSTALL_REQUIRES,
    license='GPLv3+',
    long_description=long_description,
    name='debmonitor-client',
    packages=find_packages(exclude=['tests']),
    platforms=['GNU/Linux', ],
    python_requires='>=3.7',
    extras_require=EXTRAS_REQUIRE,
    setup_requires=SETUP_REQUIRES,
    url='https://gerrit.wikimedia.org/g/operations/software/debmonitor-client',
    use_scm_version=True,
    zip_safe=False,
    entry_points={
        'console_scripts': [
            'debmonitor-client = debmonitor_client.cli:run_cli'
        ],
    }
)
