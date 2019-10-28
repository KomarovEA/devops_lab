from setuptools import setup, find_packages

setup(
name="snapshot",
packages=find_packages(),
scripts=["snapshot.py"],
version="2.0",
author="Egor Komarov",
author_email="egor_komarov@epam.com",
description="sysinfo console utility",
#long_description=long_description,
long_description_content_type="text/markdown",
license="EPAM",
python_requires='>=3.7.5',
install_requires=['psutil'])
