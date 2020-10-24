#!/bin/bash

set -e

trap 'last_command=$current_command; current_command=$BASH_COMMAND' DEBUG
trap 'echo "\"${role}\" role tests was failed."' EXIT

for role in ./roles/*/ ; do
    if [[ -d "$role/molecule" ]]
    then
        cd $role
        molecule test
        cd ../..
    fi    
done