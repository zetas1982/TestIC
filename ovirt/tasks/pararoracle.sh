#!/bin/bash
HOSTNAME=dlioracle01
USERNAME=oracle
SCRIPT="/tss_admin/oracle/oraclectl.sh stop tomsci"
sshpass -p 'JaGbsnkYpWshpCNbnE4o' ssh -l ${USERNAME} ${HOSTNAME} "${SCRIPT}" 
