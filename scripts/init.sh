#!/usr/bin/env bash

export PATH="${HOME}/.pyenv/bin:$PATH"
export ZZIZILY_PHASEWALK_CRYPTO=FJnIOiEXv4owpcej6zFrBEGhwRG8oNVI-3yonQu9vN8=
export ZZIZILY_PHASEWALK_HOME=${HOME}/apps/phasewalk

cd ${ZZIZILY_PHASEWALK_HOME}

eval "$(pyenv init -)"
eval "$(pyenv virtualenv-init -)"
source `which activate.sh`

pyenv shell 3.5.3
pyenv virtualenvwrapper
workon phasewalk
