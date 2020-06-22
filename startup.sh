#!/bin/bash
screen -dm bash epics.sh
sleep 5
screen -dm bash cont_fixer.sh
