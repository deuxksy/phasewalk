#!/usr/bin/env bash

export ZZIZILY_PHASEWALK_CRYPTO=FJnIOiEXv4owpcej6zFrBEGhwRG8oNVI-3yonQu9vN8=
export ZZIZILY_PHASEWALK_HOME=${HOME}/apps/phasewalk
export ZZIZILY_PHASEWALK_MODE=prod

cd ${ZZIZILY_PHASEWALK_HOME}

source ${ZZIZILY_PHASEWALK_HOME}/scripts/init.sh && ${ZZIZILY_PHASEWALK_HOME}/scripts/run.sh && ${ZZIZILY_PHASEWALK_HOME}/scripts/destroy.sh
