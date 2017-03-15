#!/usr/bin/env bash

export PATH="${HOME}/.pyenv/bin:$PATH"

cd ${ZZIZILY_PHASEWALK_HOME}

eval "$(pyenv init -)"
eval "$(pyenv virtualenv-init -)"
source `which activate.sh`

pyenv shell 3.5.3
pyenv virtualenvwrapper
workon phasewalk
