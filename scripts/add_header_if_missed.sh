#!/bin/bash

set -euo pipefail
shopt -s extglob

HEADER=${1:-HEADER-APACHE2}
START_PATH=${2:-"./!(target)/**/*.rs"}
DRY_RUN=${DRY_RUN:-"false"}

N=`wc -l "${HEADER}" | awk '{print $1}'`


function add_header {
    local path=$1;
    local header=${2:-${HEADER}};

    local tmp=`mktemp`

    # Add \n at the top
    echo "" > "${tmp}"
    # Copy original
    cat "${path}" >> "${tmp}"

    if [ "${DRY_RUN}" == "true" ]; then
        echo "Dry run... '${path}' - '${header}' - '${tmp}'";
        return;
    fi
    # Mix them
    cat "${header}" "${tmp}" > "${path}"
}

for f in ${START_PATH}; do
    if ! diff <(head -n "${N}" "${f}") <(cat "${HEADER}") > /dev/null ; then 
        echo "'${f}' Doesn't start with header from '${HEADER}': Add it";
        add_header "${f}" "${HEADER}"
    fi
done
