#!/usr/bin/env bash

export ZZIZILY_KIKI_CRYPTO=X_AEu2y68Q91Hmf4ooi7vUKkT5msSMvDEHDcVp-EFEI=
export ZZIZILY_PHASEWALK_MODE=dev
export ZZIZILY_PHASEWALK_HOME=${HOME}/apps/phasewalk
export ZZIZILY_PHASEWALK_CRYPTO=FJnIOiEXv4owpcej6zFrBEGhwRG8oNVI-3yonQu9vN8=

cd ${ZZIZILY_PHASEWALK_HOME}

source ./scripts/init.sh && ./scripts/run.sh && ./scripts/destroy.sh