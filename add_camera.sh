./bin/linux-x86_64/arv-tool-0.6

./bin/linux-x86_64/arv-tool-0.6 -n "Baumer Optronic-0402910514" genicam > "Baumer_VLG20M.xml"

./aravisGigEApp/src/makeDbAndEdl.py Baumer_VLG20M.xml Baumer_VLG20M

./aravisGigEApp/src/makeAdl.py Baumer_VLG20M.xml Baumer_VLG20M

mv ${EPICS_ROOT}/support/areaDetector/ADCore/iocBoot/EXAMPLE_commonPlugins.cmd ${EPICS_ROOT}/support/areaDetector/ADCore/iocBoot/commonPlugins.cmd
mv ${EPICS_ROOT}/support/areaDetector/ADCore/iocBoot/EXAMPLE_commonPlugin_settings.req ${EPICS_ROOT}/support/areaDetector/ADCore/iocBoot/commonPlugin_settings.req 


