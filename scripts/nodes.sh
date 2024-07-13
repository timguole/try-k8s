#!/bin/bash

########################################
# Start/shutdown/reboot/list all nodes
#
# Usage:
# $ ./nodes.sh [start|shutdown|reboot]

nodes=(km0 kw1 kw2 kw3 registry);

# without any argument, list all nodes and exit.
if [[ "$#" -eq 0 ]]; then
	virsh list --all;
	exit;
fi

case $1 in
start|reboot|shutdown)
	for n in ${nodes[@]}; do
		virsh "$1" --domain $n;
	done
	;;
help)
	echo "$0 [start|shutdown|reboot]"
	;;
*)
	echo "Not supported command: $1"
	exit 1;
esac

exit 0;
