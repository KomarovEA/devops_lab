#!/bin/bash
## this script installs python interpreters 2.7.0 and 3.7.0 using pyenv
yum -y -d1 install patch
pyenv install 2.7.0
pyenv install 3.7.5
# Create 2 virtualenv environments (1st for python2, 2nd for python3) 
pyenv global 3.7.5
pyenv virtualenv 3.7.5 python3env​
pyenv global 2.7.0
pip install virtualenv
pyenv virtualenv 2.7.0 python2env​
