from epics import caget, caput, cainfo
import commands, time

MODE_TEMP="None"
CAM_SELECTOR1_TEMP="0"
CAM_SELECTOR2_TEMP="0"
CAM_SELECTOR3_TEMP="0"
CAM_STATE1_TEMP="OFF"
CAM_STATE2_TEMP="OFF"
CAM_STATE3_TEMP="OFF"

while True:
###################################################################
################# Image (Single or Multiple) Mode #################
###################################################################
    while (caget('BL:DCC:ViewerMode') == MODE_TEMP and (caget('BL:DCC:ViewerMode') == "Multiple" or caget('BL:DCC:ViewerMode') == "Single") and caget('BL:DCC:RESTART')!=1 ):
        ##First Camera
        if caget('BL:DCC:CamSelector1')!=CAM_SELECTOR1_TEMP:
            TEMP1=int(caget('BL:DCC:CamSelector1'))
            if caget('BL:DCC:CamSelector2') != CAM_SELECTOR1_TEMP and caget('BL:DCC:CamSelector3') != CAM_SELECTOR1_TEMP:
                if caget('BL:DCC:CamSelector1') != "0":
                    if CAM_SELECTOR1_TEMP != "0":
                        caput('BL:DCC:CCD{}:cam1:Acquire'.format(CAM_SELECTOR1_TEMP),0)
                        caput('BL:DCC:CCD{}:image1:EnableCallbacks'.format(CAM_SELECTOR1_TEMP),0)
                        caput('BL:DCC:CCD{}:image1:ArrayCallbacks'.format(CAM_SELECTOR1_TEMP),0)
                    else:
                        caput('BL:DCC:CCD{}:cam1:Acquire'.format(int(caget('BL:DCC:CamSelector1'))),1)
                        caput('BL:DCC:CCD{}:image1:EnableCallbacks'.format(int(caget('BL:DCC:CamSelector1'))),1)
                        caput('BL:DCC:CCD{}:image1:ArrayCallbacks'.format(int(caget('BL:DCC:CamSelector1'))),1)
                        caput('BL:DCC:CCD{}:cam1:Acquire'.format(CAM_SELECTOR1_TEMP),0)
                        caput('BL:DCC:CCD{}:image1:EnableCallbacks'.format(CAM_SELECTOR1_TEMP),0)
                        caput('BL:DCC:CCD{}:image1:ArrayCallbacks'.format(CAM_SELECTOR1_TEMP),0)
                else:
                    caput('BL:DCC:CCD{}:cam1:Acquire'.format(int(caget('BL:DCC:CamSelector1'))),1)
                    caput('BL:DCC:CCD{}:image1:EnableCallbacks'.format(int(caget('BL:DCC:CamSelector1'))),1)
                    caput('BL:DCC:CCD{}:image1:ArrayCallbacks'.format(int(caget('BL:DCC:CamSelector1'))),1)
                CAM_SELECTOR1_TEMP=TEMP1
        ##Second Camera
        if caget('BL:DCC:CamSelector2')!=CAM_SELECTOR2_TEMP:
            TEMP2=int(caget('BL:DCC:CamSelector2'))
            if caget('BL:DCC:CamSelector1') != CAM_SELECTOR2_TEMP and caget('BL:DCC:CamSelector3') != CAM_SELECTOR2_TEMP:
                if caget('BL:DCC:CamSelector2') != "0":
                    if CAM_SELECTOR2_TEMP != "0":
                        caput('BL:DCC:CCD{}:cam1:Acquire'.format(CAM_SELECTOR2_TEMP),0)
                        caput('BL:DCC:CCD{}:image1:EnableCallbacks'.format(CAM_SELECTOR2_TEMP),0)
                        caput('BL:DCC:CCD{}:image1:ArrayCallbacks'.format(CAM_SELECTOR2_TEMP),0)
                    else:
                        caput('BL:DCC:CCD{}:cam1:Acquire'.format(int(caget('BL:DCC:CamSelector2'))),1)
                        caput('BL:DCC:CCD{}:image1:EnableCallbacks'.format(int(caget('BL:DCC:CamSelector2'))),1)
                        caput('BL:DCC:CCD{}:image1:ArrayCallbacks'.format(int(caget('BL:DCC:CamSelector2'))),1)
                        caput('BL:DCC:CCD{}:cam1:Acquire'.format(CAM_SELECTOR2_TEMP),0)
                        caput('BL:DCC:CCD{}:image1:EnableCallbacks'.format(CAM_SELECTOR2_TEMP),0)
                        caput('BL:DCC:CCD{}:image1:ArrayCallbacks'.format(CAM_SELECTOR2_TEMP),0)
                else:
                    caput('BL:DCC:CCD{}:cam1:Acquire'.format(int(caget('BL:DCC:CamSelector2'))),1)
                    caput('BL:DCC:CCD{}:image1:EnableCallbacks'.format(int(caget('BL:DCC:CamSelector2'))),1)
                    caput('BL:DCC:CCD{}:image1:ArrayCallbacks'.format(int(caget('BL:DCC:CamSelector2'))),1)
                CAM_SELECTOR2_TEMP=TEMP2
        ##Third Camera
        if caget('BL:DCC:CamSelector3')!=CAM_SELECTOR3_TEMP:
            TEMP3=int(caget('BL:DCC:CamSelector3'))
            if caget('BL:DCC:CamSelector1') != CAM_SELECTOR3_TEMP and caget('BL:DCC:CamSelector2') != CAM_SELECTOR3_TEMP:
                if caget('BL:DCC:CamSelector3') != "0":
                    if CAM_SELECTOR3_TEMP != "0":
                        caput('BL:DCC:CCD{}:cam1:Acquire'.format(CAM_SELECTOR3_TEMP),0)
                        caput('BL:DCC:CCD{}:image1:EnableCallbacks'.format(CAM_SELECTOR3_TEMP),0)
                        caput('BL:DCC:CCD{}:image1:ArrayCallbacks'.format(CAM_SELECTOR3_TEMP),0)
                    else:
                        caput('BL:DCC:CCD{}:cam1:Acquire'.format(int(caget('BL:DCC:CamSelector3'))),1)
                        caput('BL:DCC:CCD{}:image1:EnableCallbacks'.format(int(caget('BL:DCC:CamSelector3'))),1)
                        caput('BL:DCC:CCD{}:image1:ArrayCallbacks'.format(int(caget('BL:DCC:CamSelector3'))),1)
                        caput('BL:DCC:CCD{}:cam1:Acquire'.format(CAM_SELECTOR3_TEMP),0)
                        caput('BL:DCC:CCD{}:image1:EnableCallbacks'.format(CAM_SELECTOR3_TEMP),0)
                        caput('BL:DCC:CCD{}:image1:ArrayCallbacks'.format(CAM_SELECTOR3_TEMP),0)
                else:
                    caput('BL:DCC:CCD{}:cam1:Acquire'.format(int(caget('BL:DCC:CamSelector3'))),1)
                    caput('BL:DCC:CCD{}:image1:EnableCallbacks'.format(int(caget('BL:DCC:CamSelector3'))),1)
                    caput('BL:DCC:CCD{}:image1:ArrayCallbacks'.format(int(caget('BL:DCC:CamSelector3'))),1)
                CAM_SELECTOR3_TEMP=TEMP3
#################Check State of Camera
        ##First Camera
        if caget('BL:DCC:CamSelector1')=="0":
            CAM_STATE1="OFF"
            CAM_STATE1A="0"
        else:
            CONNECTED_CAMERAS=commands.getstatusoutput('/home/cam/epicsv3/support/areaDetector/aravisGigE/bin/linux-x86_64/arv-tool-0.6')[1].split("\n")
            if 'Optronic-{}'.format(caget('BL:DCC:CCD{}:cam1:SerialNumber_RBV'.format(int(caget('BL:DCC:CamSelector1'))))) in CONNECTED_CAMERAS:
                CAM_CHECK1="present"
            if CAM_CHECK1=="present":
                CAM_STATE1="Connected"
                CAM_STATE1A="1"
            elif CAM_CHECK1=="absent":
                CAM_STATE1="Disconnected"
                CAM_STATE1A="2"
            CAM_CHECK1="absent"
        if CAM_STATE1!=CAM_STATE1_TEMP:
            caput('BL:DCC:CamState1',CAM_STATE1)
            caput('BL:DCC:CamState1A',int(CAM_STATE1A))
            CAM_STATE1_TEMP=CAM_STATE1
        ##Second Camera
        if caget('BL:DCC:CamSelector2')=="0":
            CAM_STATE2="OFF"
            CAM_STATE2A="0"
        else:
            CONNECTED_CAMERAS=commands.getstatusoutput('/home/cam/epicsv3/support/areaDetector/aravisGigE/bin/linux-x86_64/arv-tool-0.6')[1].split("\n")
            if 'Optronic-{}'.format(caget('BL:DCC:CCD{}:cam1:SerialNumber_RBV'.format(int(caget('BL:DCC:CamSelector2'))))) in CONNECTED_CAMERAS:
                CAM_CHECK2="present"
            if CAM_CHECK2=="present":
                CAM_STATE2="Connected"
                CAM_STATE2A="1"
            elif CAM_CHECK2=="absent":
                CAM_STATE2="Disconnected"
                CAM_STATE2A="2"
            CAM_CHECK2="absent"
        if CAM_STATE2!=CAM_STATE2_TEMP:
            caput('BL:DCC:CamState2',CAM_STATE2)
            caput('BL:DCC:CamState2A',int(CAM_STATE2A))
            CAM_STATE2_TEMP=CAM_STATE2
        ##Third Camera
        if caget('BL:DCC:CamSelector3')=="0":
            CAM_STATE3="OFF"
            CAM_STATE3A="0"
        else:
            CONNECTED_CAMERAS=commands.getstatusoutput('/home/cam/epicsv3/support/areaDetector/aravisGigE/bin/linux-x86_64/arv-tool-0.6')[1].split("\n")
            if 'Optronic-{}'.format(caget('BL:DCC:CCD{}:cam1:SerialNumber_RBV'.format(int(caget('BL:DCC:CamSelector3'))))) in CONNECTED_CAMERAS:
                CAM_CHECK3="present"
            if CAM_CHECK3=="present":
                CAM_STATE3="Connected"
                CAM_STATE3A="1"
            elif CAM_CHECK3=="absent":
                CAM_STATE3="Disconnected"
                CAM_STATE3A="2"
            CAM_CHECK2="absent"
        if CAM_STATE3!=CAM_STATE3_TEMP:
            caput('BL:DCC:CamState3',CAM_STATE3)
            caput('BL:DCC:CamState3A',int(CAM_STATE3A))
            CAM_STATE3_TEMP=CAM_STATE3
#################################################
################# Statistic Mod #################
#################################################
    while (caget('BL:DCC:ViewerMode') == MODE_TEMP and caget('BL:DCC:ViewerMode') == "Statistic" and caget('BL:DCC:RESTART')!=1 ):
        data = np.genfromtxt('camera_list',delimiter=',')
        CAMERAS=data[:,0]
        CAMERA_SERI_NO=data[:,1]
        if caget('BL:DCC:CamSelector1')!=CAM_SELECTOR1_TEMP:
            TEMP1=int(caget('BL:DCC:CamSelector1'))
            if caget('BL:DCC:CamSelector2') != CAM_SELECTOR1_TEMP and caget('BL:DCC:CamSelector3') != CAM_SELECTOR1_TEMP:
                if caget('BL:DCC:CamSelector1') != "0":
                    commands.getstatusoutput('pkill -9 aravisGigEApp')
                    time.sleep(9)
                else:
                    if 'CCD{}'.format(int(caget('BL:DCC:CamSelector1'))) in CAMERAS:
                        commands.getstatusoutput('rm st_Cam.cmd')
                        commands.getstatusoutput('cp st_Statistic.cmd st_Cam.cmd')
                        sed_CAMERA_param='s/CAMERA_VARIABLE/Optronic-{}/g'.format(CAMERA_SERI_NO[CAMERAS.index['CCD{}'.format(int(caget('BL:DCC:CamSelector1')))]])
                        commands.getstatusoutput('sed -i {} st_Cam.cmd'.format(sed_CAMERA_param))
                        caput('BL:DCC:AMode',3)
                        commands.getstatusoutput('pkill -9 aravisGigEApp')
                        time.sleep(9)
                        caput('BL:DCC:image1:ArrayCallbacks',1)
                        caput('BL:DCC:image1:EnableCallbacks',1)
                        caput('BL:DCC:Stats1:ArrayCallbacks',1)
                        caput('BL:DCC:Stats1:EnableCallbacks',1)
                        caput('BL:DCC:Stats1:ComputeProfiles',1)
                        caput('BL:DCC:Stats1:ComputeStatistics',1)
                        caput('BL:DCC:Stats1:ComputeCentroid',1)
                        caput('BL:DCC:Stats1:ComputeProfiles',1)
                        caput('BL:DCC:cam1:Acquire',1)
                CAM_SELECTOR1_TEMP=TEMP1
                caput('BL:DCC:CamSelector1',int(CAM_SELECTOR1_TEMP))
                caput('BL:DCC:ViewerMode','Statistic')
                caput('BL:DCC:ViewerModeA',3)
#################Check State of Camera
        if caget('BL:DCC:CamSelector1')=="0":
            CAM_STATE1="OFF"
            CAM_STATE1A="0"
        else:
            CONNECTED_CAMERAS=commands.getstatusoutput('/home/cam/epicsv3/support/areaDetector/aravisGigE/bin/linux-x86_64/arv-tool-0.6')[1].split("\n")
            if 'Optronic-{}'.format(caget('BL:DCC:CCD{}:cam1:SerialNumber_RBV'.format(int(caget('BL:DCC:CamSelector1'))))) in CONNECTED_CAMERAS:
                CAM_CHECK1="present"
            if CAM_CHECK1=="present":
                CAM_STATE1="Connected"
                CAM_STATE1A="1"
            elif CAM_CHECK1=="absent":
                CAM_STATE1="Disconnected"
                CAM_STATE1A="2"
            CAM_CHECK1="absent"
        if CAM_STATE1!=CAM_STATE1_TEMP:
            caput('BL:DCC:CamState1',CAM_STATE1)
            caput('BL:DCC:CamState1A',int(CAM_STATE1A))
            CAM_STATE1_TEMP=CAM_STATE1
###############################################
################# Change Mode #################
###############################################
if caget('BL:DCC:ViewerMode') == MODE_TEMP:
    caput('BL:DCC:ViewerModeA',9999999)
    if caget('BL:DCC:ViewerMode')=="Single":
        if MODE_TEMP=="Multiple":
            caput('BL:DCC:CamSelector1',0)
            caput('BL:DCC:CamSelector2',0)
            caput('BL:DCC:CamSelector3',0)
            caput('BL:DCC:CamState1','OFF')
            caput('BL:DCC:CamState1A',0)
            caput('BL:DCC:CamState2','OFF')
            caput('BL:DCC:CamState2A',0)
            caput('BL:DCC:CamState3','OFF')
            caput('BL:DCC:CamState3A',0)
            caput('BL:DCC:CCD{}:cam1:Acquire'.format(int(caget('BL:DCC:CamSelector1'))),0)
            caput('BL:DCC:CCD{}:image1:EnableCallbacks'.format(int(caget('BL:DCC:CamSelector1'))),0)
            caput('BL:DCC:CCD{}:image1:ArrayCallbacks'.format(int(caget('BL:DCC:CamSelector1'))),0)
            caput('BL:DCC:CCD{}:cam1:Acquire'.format(int(caget('BL:DCC:CamSelector2'))),0)
            caput('BL:DCC:CCD{}:image1:EnableCallbacks'.format(int(caget('BL:DCC:CamSelector2'))),0)
            caput('BL:DCC:CCD{}:image1:ArrayCallbacks'.format(int(caget('BL:DCC:CamSelector2'))),0)
            caput('BL:DCC:CCD{}:cam1:Acquire'.format(int(caget('BL:DCC:CamSelector3'))),0)
            caput('BL:DCC:CCD{}:image1:EnableCallbacks'.format(int(caget('BL:DCC:CamSelector3'))),0)
            caput('BL:DCC:CCD{}:image1:ArrayCallbacks'.format(int(caget('BL:DCC:CamSelector3'))),0)
        else:
            commands.getstatusoutput('rm st_Cam.cmd')
            commands.getstatusoutput('cp st_Image.cmd st_Cam.cmd')
            commands.getstatusoutput('pkill -9 aravisGigEApp')
            time.sleep(15)
        caput('BL:DCC:ViewerMode','Single')
        caput('BL:DCC:ViewerModeA',1)
        MODE_TEMP="Single"
        CAM_SELECTOR1_TEMP="0"
        CAM_STATE1_TEMP=OFF""
    elif caget('BL:DCC:ViewerMode')=="Multiple":
        if MODE_TEMP=="Single":
            caput('BL:DCC:CamSelector1',0)
            caput('BL:DCC:CamState1','OFF')
            caput('BL:DCC:CamState1A',0)
            caput('BL:DCC:CCD{}:cam1:Acquire'.format(int(caget('BL:DCC:CamSelector1'))),0)
            caput('BL:DCC:CCD{}:image1:EnableCallbacks'.format(int(caget('BL:DCC:CamSelector1'))),0)
            caput('BL:DCC:CCD{}:image1:ArrayCallbacks'.format(int(caget('BL:DCC:CamSelector1'))),0)
        else:
            commands.getstatusoutput('rm st_Cam.cmd')
            commands.getstatusoutput('cp st_Image.cmd st_Cam.cmd')
            commands.getstatusoutput('pkill -9 aravisGigEApp')
            time.sleep(15)
        caput('BL:DCC:ViewerMode','Multiple')
        caput('BL:DCC:ViewerModeA',2)
        MODE_TEMP="Multiple"
        CAM_SELECTOR1_TEMP="0"
        CAM_SELECTOR2_TEMP="0"
        CAM_SELECTOR3_TEMP="0"
        CAM_STATE1_TEMP=OFF""
        CAM_STATE2_TEMP=OFF""
        CAM_STATE3_TEMP=OFF""
    elif caget('BL:DCC:ViewerMode')=="Statistic":
        commands.getstatusoutput('rm st_Cam.cmd')
        commands.getstatusoutput('cp st_Statistic.cmd st_Cam.cmd')
        commands.getstatusoutput('pkill -9 aravisGigEApp')
        time.sleep(15)
        caput('BL:DCC:ViewerMode','Statistic')
        caput('BL:DCC:ViewerModeA',3)
        MODE_TEMP="Statistic"
        CAM_SELECTOR1_TEMP="0"
        CAM_STATE1_TEMP=OFF""
    elif caget('BL:DCC:ViewerMode')=="None":
        commands.getstatusoutput('rm st_Cam.cmd')
        commands.getstatusoutput('cp st_None.cmd st_Cam.cmd')
        commands.getstatusoutput('pkill -9 aravisGigEApp')
        time.sleep(15)
        caput('BL:DCC:ViewerModeA',0)
        MODE_TEMP="None"
###########################################
################# Restart #################
###########################################
    if caget('BL:DCC:RESTART')=="1":
        MODE_TEMP=caget('BL:DCC:ViewerMode')
        CAM_SELECTOR1_TEMP=caget('BL:DCC:CamSelector1')
        CAM_SELECTOR2_TEMP=caget('BL:DCC:CamSelector2')
        CAM_SELECTOR3_TEMP=caget('BL:DCC:CamSelector3')
        CAM_STATE1_TEMP=caget('BL:DCC:CamState1')
        CAM_STATE1A_TEMP=caget('BL:DCC:CamState1A')
        CAM_STATE2_TEMP=caget('BL:DCC:CamState2')
        CAM_STATE2A_TEMP=caget('BL:DCC:CamState2A')
        CAM_STATE3_TEMP=caget('BL:DCC:CamState3')
        CAM_STATE3A_TEMP=caget('BL:DCC:CamState3A')
        commands.getstatusoutput('pkill -9 aravisGigEApp')
        time.sleep(15)
        caput('BL:DCC:ViewerMode',MODE_TEMP)
        if MODE_TEMP=="Single":
            caput('BL:DCC:ViewerModeA',1)
        elif MODE_TEMP=="Multiple":
            caput('BL:DCC:ViewerModeA',2)
        elif MODE_TEMP=="Statistic":
            caput('BL:DCC:ViewerModeA',3)
        caput('BL:DCC:CamSelector1',int(CAM_SELECTOR1_TEMP))
        caput('BL:DCC:CamSelector2',int(CAM_SELECTOR2_TEMP))
        caput('BL:DCC:CamSelector3',int(CAM_SELECTOR3_TEMP))
        caput('BL:DCC:CamState1',CAM_STATE1_TEMP)
        caput('BL:DCC:CamState1A',int(CAM_STATE1A_TEMP))
        caput('BL:DCC:CamState2',CAM_STATE2_TEMP)
        caput('BL:DCC:CamState2A',int(CAM_STATE2A_TEMP))
        caput('BL:DCC:CamState3',CAM_STATE3_TEMP)
        caput('BL:DCC:CamState3A',int(CAM_STATE3A_TEMP))



