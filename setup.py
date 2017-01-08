from setuptools import setup

setup(
	name='sitestatus',
	packages=['sitestatus'],
	include_package_Data=True,
	install_requires=[
		'flask',
	],
)