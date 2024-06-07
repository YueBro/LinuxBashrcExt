#!/bin/bash

_BASHRC_EXT_MAIN_SCRIPT_DIR=$( cd -- "$( dirname -- "${BASH_SOURCE[0]}" )" &> /dev/null && pwd )

for sub_dir in $_BASHRC_EXT_MAIN_SCRIPT_DIR/*; do
    if [ -d $sub_dir ] && [ -f $sub_dir/main.sh ]; then
        source $sub_dir/main.sh
    fi
done

unset _BASHRC_EXT_MAIN_SCRIPT_DIR
