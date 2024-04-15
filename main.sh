#!/bin/bash

_BASHRC_EXT_MAIN_SCRIPT_DIR=$( cd -- "$( dirname -- "${BASH_SOURCE[0]}" )" &> /dev/null && pwd )

source ${_BASHRC_EXT_MAIN_SCRIPT_DIR}/ccd/main.sh
source ${_BASHRC_EXT_MAIN_SCRIPT_DIR}/dk/main.sh

unset _BASHRC_EXT_MAIN_SCRIPT_DIR
