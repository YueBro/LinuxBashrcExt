#!/bin/bash


function _conda_deactivate_all()
{
    # Deactivate all
    while [[ $CONDA_DEFAULT_ENV != "" ]]; do
        echo -e "\e[34m- Deactivating (${CONDA_DEFAULT_ENV})...\e[0m"
        conda deactivate
    done
}


function ccd()
{
    _SCRIPT_DIR=$( cd -- "$( dirname -- "${BASH_SOURCE[0]}" )" &> /dev/null && pwd )

    cd $1

    env_name=$(python3 ${_SCRIPT_DIR}/detector.py $(pwd))

    if [[ $? -ne 0 ]]; then
        echo $env_name
    elif [[ $env_name == "<null>" ]]; then

        _conda_deactivate_all

    elif [[ env_name != "" && $CONDA_DEFAULT_ENV != $env_name ]]; then

        _conda_deactivate_all

        echo -e "\e[36m- Activating ($env_name)...\e[0m"
        conda activate $env_name

    fi
}
