from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in report_generator/__init__.py
from report_generator import __version__ as version

setup(
	name="report_generator",
	version=version,
	description="Tools for report generate",
	author="zubairmazhar23@gmail.com",
	author_email="zubairmazhar23@gmail.com",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
