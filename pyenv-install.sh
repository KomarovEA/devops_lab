#!/bin/bash
## this script installs pythn's pyenv 
yum -y -d1 install epel-release
yum -y -d1 install git gcc zlib-devel bzip2-devel readline-devel sqlite-devel openssl-devel
git clone https://github.com/pyenv/pyenv.git $HOME/.pyenv
git clone https://github.com/pyenv/pyenv-virtualenv.git $HOME/.pyenv/plugins/pyenv-virtualenv
## configuring environment
echo 'export PYENV_ROOT="$HOME/.pyenv"' >> $HOME/.bashrc 
echo 'export PATH="$PYENV_ROOT/bin:$PATH"' >> $HOME/.bashrc
echo 'eval "$($PYENV_ROOT/bin/pyenv init -)"' >> $HOME/.bashrc
echo 'eval "$($PYENV_ROOT/bin/pyenv virtualenv-init -)"' >> $HOME/.bashrc
source $HOME/.bashrc

