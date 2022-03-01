#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""The setup script."""

from setuptools import setup, find_packages

with open('README.md', encoding='utf-8') as readme_file:
    readme = readme_file.read()

with open('HISTORY.md', encoding='utf-8') as history_file:
    history = history_file.read()

requirements = [
    'cookiecutter',
    'Click >= 6.0',
    'funcy >= 1.14',
    'scikit_learn >= 0.20',
    'sklearn_pandas ~= 1.0',
    'stacklog',
    'pandas ~= 1.0',
    'numpy',
]

extras = {
    'category_encoders': ['category_encoders >= 2.2.2'],
    'feature_engine': ['feature_engine ~= 1.0'],
    'featuretools': ['featuretools_sklearn_transformer >= 0.1'],
    'skits': ['skits >= 0.1.2'],
    'tsfresh': ['tsfresh >= 0.16'],
}
extras['all'] = [dep for deps in extras.values() for dep in deps]

test_requirements = [
    'coverage >= 4.5.1',
    'pytest >= 6',
    'pytest-cov >= 2.6',
    'pytest-virtualenv >= 1.7.0',
    'tox >= 2.9.1',
    'responses >= 0.13.2',
]

setup(
    author="Eleve Yuan",
    author_email='eleveyuane@gmail.com',
    description='a ligthweight feature manage framework',
    install_requires=requirements,
    license='MIT license',
    keywords='pada',
    name='pada',
    python_requires='>=3.7.0',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
    ],
    url='https://github.com/eleveyuan/pada',
    long_description=readme + '\n\n' + history,
    long_description_content_type='text/markdown',
    version='0.1.0',
    zip_safe=False,
    packages=find_packages(include=['pada', 'pada.*']),
    extras_require={
        **extras,
    }
)
