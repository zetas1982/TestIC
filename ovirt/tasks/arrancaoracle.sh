#!/bin/bash
HOSTNAME=dlioracle01
USERNAME=oracle
SCRIPT="/tss_admin/oracle/oraclectl.sh start tomsci"
sshpass -p 'JaGbsnkYpWshpCNbnE4o' ssh -l ${USERNAME} ${HOSTNAME} "${SCRIPT}" 
