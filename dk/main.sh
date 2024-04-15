#!/bin/bash


function dk_list()
{
    echo "---- Images ----"
    docker image list
    echo ""
    echo "---- Containers ----"
    docker ps -a
}


function dk_run()
{
    _SCRIPT_DIR=$( cd -- "$( dirname -- "${BASH_SOURCE[0]}" )" &> /dev/null && pwd )
    python3 $_SCRIPT_DIR/_dk_run.py "$@"
}


function dk_exec()
{
    _SCRIPT_DIR=$( cd -- "$( dirname -- "${BASH_SOURCE[0]}" )" &> /dev/null && pwd )
    python3 $_SCRIPT_DIR/_dk_exec.py "$@"
}


function dk_rm()
{
    _SCRIPT_DIR=$( cd -- "$( dirname -- "${BASH_SOURCE[0]}" )" &> /dev/null && pwd )
    python3 $_SCRIPT_DIR/_dk_rm.py "$@"
}


function dk_rmi()
{
    _SCRIPT_DIR=$( cd -- "$( dirname -- "${BASH_SOURCE[0]}" )" &> /dev/null && pwd )
    python3 $_SCRIPT_DIR/_dk_rmi.py "$@"
}
