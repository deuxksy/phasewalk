#!/usr/bin/env bash

export ZZIZILY_PHASEWALK_MODE=prod
export ZZIZILY_PHASEWALK_CRYPTO=${ZZIZILY_BTA_CRYPTO}
export ZZIZILY_PHASEWALK_HOME=${HOME}/apps/phasewalk

cd ${ZZIZILY_PHASEWALK_HOME}

source ${ZZIZILY_PHASEWALK_HOME}/scripts/init.sh && ${ZZIZILY_PHASEWALK_HOME}/scripts/run.sh && ${ZZIZILY_PHASEWALK_HOME}/scripts/destroy.sh
