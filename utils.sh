#!/bin/sh

export PODMAN_IGNORE_CGROUPSV1_WARNING=""

print_log()
{
  message=$1
  echo "`date +"%Y-%m-%d %H-%M-%S - "`${message}"
}




