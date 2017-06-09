import re
from setuptools import find_packages, setup

try:
    import pypandoc
    readme = pypandoc.convert('README.md', 'rst')
    history = pypandoc.convert('CHANGELOG.md', 'rst')
except (ImportError, OSError):
    with open('README.md') as readme_file, \
            open('CHANGELOG.md') as history_file:
        readme = readme_file.read()
        history = history_file.read()

version_regex = re.compile(r'__version__ = [\'\"]((\d+\.?)+)[\'\"]')
with open('flaskmogrify/__init__.py') as f:
    vlines = f.readlines()
__version__ = next(re.match(version_regex, line).group(1) for line in vlines
                   if re.match(version_regex, line))

with open('requirements.txt') as requirements_file:
    requirements = requirements_file.read().splitlines()

with open('requirements-dev.txt') as dev_requirements_file:
    dev_requirements = dev_requirements_file.read().splitlines()

with open("requirements-test.txt") as test_requirements_file:
    test_requirements = test_requirements_file.read().splitlines()
    dev_requirements.extend(test_requirements)

setup(
    name='flaskmogrify',
    version=__version__,
    description="Flaskmogrify, a simple Flask single page" +
                "application to convert (w/ Ajax) user-pasted text using an arbitrary text conversion function.",
    long_description=readme + '\n\n' + history,
    author='Daniel Langsam',
    author_email='daniel@langsam.org',
    url='https://github.com/danyul/flaskmogrify',
    packages=find_packages(),
    include_package_data=True,
    install_requires=requirements,
    license="MIT",
    zip_safe=False,
    keywords='flask convert text transform ajax single page application',
    classifiers=[
        'Natural Language :: English',
        'Programming Language :: Python :: 3.6',
    ],
    extras_require={
        "dev": dev_requirements
        },
    test_suite='tests',
    tests_require=[].extend(test_requirements),
)
