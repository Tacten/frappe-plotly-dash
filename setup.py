# -*- coding: utf-8 -*-
from setuptools import setup, find_packages

with open('requirements.txt') as f:
	install_requires = f.read().strip().split('\n')

# get version from __version__ variable in dash_integration/__init__.py
from dash_integration import __version__ as version

setup(
	name='dash_integration',
	version=version,
	description='Integration for Plotly Dash',
	author='SpaceCode Co., Ltd.',
	author_email='poranut@spacecode.co.th',
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
