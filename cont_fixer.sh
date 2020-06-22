#!/bin/bash
# This script reads 13ARV1:ChangeCam continuously and, if changed,
# takes the features of the new camera from camera_list.txt and generates
# a new st_CN.cmd file (copy from st.cmd)
# (added to crontab)
#
# Ali Can Canbay 09/01/2020
while true; do
#################
#################Choose Camera
#################
	NAME=( $(cut -d ',' -f1 camera_list ) )
	SN=( $(cut -d ',' -f2 camera_list ) )
	FNA=$(echo $(caget 13ARV1:ChangeCam))
	FN=$(echo $FNA| cut -d' ' -f 2)
	if [[ "${CN}" != "${FN}" ]]; then
		CN=$FN
		if [[ "${CN}" == "OFF" ]]; then
			caput 13ARV1:image1:EnableCallbacks 0
			caput 13ARV1:Stats1:EnableCallbacks 0
			caput 13ARV1:Stats1:ComputeProfiles 0
			caput 13ARV1:cam1:Acquire 0
			pkill -9 aravisGigEApp
			sleep 10
			caput 13ARV1:ChangeCam $CN
		elif [[ ${CN} == "13ARV1:ChangeCam" ]]; then
			CN="OFF"
			caput 13ARV1:ChangeCam $CN
		else
			for i in ${!NAME[@]}; do
				if [[ "${NAME[$i]}" == "${CN}" ]]; then
					rm st_CN.cmd
					cp st.cmd st_CN.cmd
					sed_CAMERA_param=s/CAMERA_VARIABLE/Optronic-${SN[$i]}/g
					sed -i "$sed_CAMERA_param" st_CN.cmd
					caput 13ARV1:image1:EnableCallbacks 0
					caput 13ARV1:Stats1:EnableCallbacks 0
					caput 13ARV1:Stats1:ComputeProfiles 0
					caput 13ARV1:cam1:Acquire 0
					pkill -9 aravisGigEApp
					sleep 10
					caput 13ARV1:image1:EnableCallbacks 1
					caput 13ARV1:Stats1:EnableCallbacks 1
					caput 13ARV1:Stats1:ComputeProfiles 1
					caput 13ARV1:cam1:Acquire 1
					caput 13ARV1:ChangeCam $CN
				fi
			done
		fi
	fi
#################
#################Check Status of Camera
#################
	if [[ "${CN}" == "OFF" ]]; then
		STATUS="OFF"
	else
		CHA=$(echo $(caget 13ARV1:cam1:SerialNumber_RBV))
		CH=$(echo $CHA| cut -d' ' -f 2)
		IFS=' ' read -a CHECK  <<< $( /home/cam/epicsv3/support/areaDetector/aravisGigE/bin/linux-x86_64/arv-tool-0.6 )
		for i in ${!CHECK[@]}; do
			if [[ "${CHECK[$i]}" == "Optronic-${CH}" ]]; then
				CH_V="present"
			fi
		done
		if [[ "${CH_V}" == "present" ]]; then
			STATUS="Connected"
		else
			STATUS="Disconnected"
		fi
		CH_V="absent"
	fi
	if [[ "${STATUS}" != "${STAT}" ]]; then	
		caput 13ARV1:Status $STATUS
		STAT=$STATUS
	fi
	while [[ ("${STAT}" == "Disconnected") && ("${CN}" == "${FN}") ]]; do
		FNA=$(echo $(caget 13ARV1:ChangeCam))
		FN=$(echo $FNA| cut -d' ' -f 2)
		CHA=$(echo $(caget 13ARV1:cam1:SerialNumber_RBV))
		CH=$(echo $CHA| cut -d' ' -f 2)
		IFS=' ' read -a CHECK  <<< $( /home/cam/epicsv3/support/areaDetector/aravisGigE/bin/linux-x86_64/arv-tool-0.6 )
		for i in ${!CHECK[@]}; do
			if [[ "${CHECK[$i]}" == "Optronic-${CH}" ]]; then
				caput 13ARV1:image1:EnableCallbacks 0
				caput 13ARV1:Stats1:EnableCallbacks 0
				caput 13ARV1:Stats1:ComputeProfiles 0
				caput 13ARV1:cam1:Acquire 0
				pkill -9 aravisGigEApp
				sleep 10
				caput 13ARV1:image1:EnableCallbacks 1
				caput 13ARV1:Stats1:EnableCallbacks 1
				caput 13ARV1:Stats1:ComputeProfiles 1
				caput 13ARV1:cam1:Acquire 1
				caput 13ARV1:ChangeCam $CN
				STAT="Connected"
				caput 13ARV1:Status $STAT
			fi
		done
	done
	sleep 1
done
