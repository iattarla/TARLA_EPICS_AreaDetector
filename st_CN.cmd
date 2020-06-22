< envPaths
errlogInit(20000)

dbLoadDatabase("$(TOP)/dbd/aravisGigEApp.dbd")
aravisGigEApp_registerRecordDeviceDriver(pdbbase) 

epicsEnvSet("PREFIX", "13ARV1:")
epicsEnvSet("PORT",   "ARV1")
epicsEnvSet("QSIZE",  "20")
epicsEnvSet("XSIZE",  "1624")
epicsEnvSet("YSIZE",  "1228")
epicsEnvSet("NCHANS", "2048")
epicsEnvSet("CBUFFS", "500")
epicsEnvSet("EPICS_DB_INCLUDE_PATH", "$(ADCORE)/db")

dbLoadRecords("$(ARAVISGIGE)/iocs/aravisGigEIOC/iocBoot/iocAravisGigE/change.db")
aravisCameraConfig("$(PORT)", "Baumer Optronic-0402910514")
dbLoadRecords("$(ARAVISGIGE)/db/Baumer_VLG20M.template","P=$(PREFIX),R=cam1:,PORT=$(PORT),ADDR=0,TIMEOUT=1")
dbLoadRecords("$(ARAVISGIGE)/db/aravisCamera.template", "P=$(PREFIX),R=cam1:,PORT=$(PORT),ADDR=0,TIMEOUT=1")
NDStdArraysConfigure("Image1", 5, 0, "$(PORT)", 0, 0)
dbLoadRecords("$(ADCORE)/db/NDStdArrays.template", "P=$(PREFIX),R=image1:,PORT=Image1,ADDR=0,TIMEOUT=1,NDARRAY_PORT=$(PORT),TYPE=Int16,FTVL=SHORT,NELEMENTS=1994272")

< $(ADCORE)/iocBoot/commonPlugins.cmd
set_requestfile_path("$(ADPILATUS)/prosilicaApp/Db")

iocInit()
create_monitor_set("auto_settings.req", 30,"P=$(PREFIX)")
