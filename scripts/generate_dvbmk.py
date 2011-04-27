#!/usr/bin/env python

"""
This script is a generator of OpenWRT's Makefile for DVB USB devices

This script uses the sources of the linux kernel to find what are the different
supported DVB USB devices and the kernel parameters needed to compile them.

In more details it is able to find
 * the module description
 * the module dependancies
 * the frontends needed and the tuner needed
 * the module generated files (including the frontend and the tuners)
 * the firmware needed by the module

And it will generate a dvb.mk file with all these informations

"""
import os
PWD = os.getcwd()
DEST_DIR = PWD + "/package/kernel/modules/"
DEST_FILE = "dvb.mk"
_NEXT_LINE = """ \\
	"""

CONFIG_FILE_HEADER = """
#
# Copyright (C) 2009 Brice DUBOST
#
# This is free software, licensed under the GNU General Public License v2.
# See /LICENSE for more information.
#
#
# !!!! This is a generated file !!!! 
#

DVB_MENU:=DVB support

#
# General section
#

define KernelPackage/ir-core
  SUBMENU:=$(DVB_MENU)
  TITLE:=IR core support
  KCONFIG:= \\
	CONFIG_MEDIA_SUPPORT \\
	CONFIG_INPUT=y \\
	CONFIG_IR_CORE=y	\\
	CONFIG_RC_CORE=y
ifneq ($(CONFIG_LINUX_2_6_35)$(CONFIG_LINUX_2_6_36)$(CONFIG_LINUX_2_6_37),)
	FILES:= $(LINUX_DIR)/drivers/media/IR/ir-core.$(LINUX_KMOD_SUFFIX) \\
		$(LINUX_DIR)/drivers/media/IR/ir-common.$(LINUX_KMOD_SUFFIX)
	AUTOLOAD:=$(call AutoLoad,61,ir-core ir-common)
else
	FILES:=$(LINUX_DIR)/drivers/media/rc/rc-core.$(LINUX_KMOD_SUFFIX)
	AUTOLOAD:=$(call AutoLoad,61,rc-core)
endif
endef

define KernelPackage/ir-core/description
 Kernel module for IR support
endef

$(eval $(call KernelPackage,ir-core))

define KernelPackage/dvb-core
  SUBMENU:=$(DVB_MENU)
  TITLE:=DVB core support
  DEPENDS:=+kmod-i2c-core
  KCONFIG:= \\
	CONFIG_MEDIA_SUPPORT \\
	CONFIG_DVB_CORE \\
	CONFIG_DVB_CAPTURE_DRIVERS=y \\
	CONFIG_MEDIA_TUNER_CUSTOMIZE=y \\
	CONFIG_DVB_FE_CUSTOMISE=y \\
	CONFIG_DVB_DYNAMIC_MINORS=n \\
	CONFIG_CRC32 
  FILES:=$(LINUX_DIR)/drivers/media/dvb/dvb-core/dvb-core.$(LINUX_KMOD_SUFFIX)
  AUTOLOAD:=$(call AutoLoad,60,dvb-core)
endef

define KernelPackage/dvb-core/description
 Kernel module for DVB support
endef

define KernelPackage/dvb-core/install
	$(INSTALL_DIR) $(1)/etc/hotplug.d/dvb
	$(INSTALL_BIN) ./files/10-dvb $(1)/etc/hotplug.d/dvb/
endef

$(eval $(call KernelPackage,dvb-core))

define KernelPackage/dvb-usb
  SUBMENU:=$(DVB_MENU)
  TITLE:=DVB USB Support
  DEPENDS:=@USB_SUPPORT +kmod-dvb-core +kmod-usb-core +kmod-ir-core
  KCONFIG:= \\
	CONFIG_DVB_USB \\
	CONFIG_IR_CORE 	\\
	CONFIG_INPUT=y \\
	CONFIG_RC_CORE=y
  FILES:=$(LINUX_DIR)/drivers/media/dvb/dvb-usb/dvb-usb.$(LINUX_KMOD_SUFFIX)
  AUTOLOAD:=$(call AutoLoad,62, dvb-usb)
endef

define KernelPackage/dvb-usb/description
 Kernel module for DVB USB devices. Note you have to select at least a device.
endef

$(eval $(call KernelPackage,dvb-usb))

#
# Devices section
#

"""


def find_module_files(pre, filename, module):
    """This function is intended to act like a special grep in a Makefile"""
    makefile = open(filename,'r')
    lines_makefile = makefile.readlines()
    makefile.close()
    module_files = []
    for index, line in enumerate(lines_makefile):
        if module in line:
            for module_object in lines_makefile[index].strip().split('=')[1].split(' '):
                #we remove thing without sence
                if len(module_object) <3 :
                    continue
                module_files.append(pre + module_object)
    return module_files


def find_boardtype(path):
    configFile = open(path + "//.config",'r')
    lines_configFile = configFile.readlines()
    configFile.close()
    for index, line in enumerate(lines_configFile):
        if("CONFIG_TARGET_BOARD=" in line): 
	    return line.strip("CONFIG_TARGET_BOARD=").replace("\n","").replace("\"","")

    return ""

def find_subtarget(path,target):
    configFile = open(path + "//.config",'r')
    lines_configFile = configFile.readlines()
    configFile.close()

    subtarget = ""
    for index, line in enumerate(lines_configFile):
       if("CONFIG_HAS_SUBTARGETS=y" in line):
 	    subtarget = "_"

    if (subtarget == ""):
      return ""


    for index, line in enumerate(lines_configFile):
        if("CONFIG_TARGET_"+target+"_" in line and "=y" in line):
 	    return "_" + line.strip("CONFIG_TARGET_"+target).replace("=y\n","")

    return ""


def find_kernel_version(path):
    target = find_boardtype(path)

    configFile = open(path + "/target/linux/" + target + "/Makefile",'r')
    lines_configFile = configFile.readlines()
    configFile.close()

    for index, line in enumerate(lines_configFile):
        if "LINUX_VERSION:=" in line:
	    return line.strip("LINUX_VERSION:=").replace("\n","")

    return ""


def deal_config(config, filedvbmk):
    """This function is called when the user wants to add a new module"""

    firmware_pattern = """%(name)s:=%(filename)s
"""	

    firmware_download_pattern = """define Download/%(name)s
    FILE:=$(%(filename)s)
    URL:=http://code.google.com/p/wl-700ge/source/browse/trunk/firmware/
endef

"""

    firmware_download_call_pattern = """$(eval $(call Download,%(name)s))
"""

    firmware_install_pattern = """	$(INSTALL_DATA) $(DL_DIR)/$(%(name)s) $(1)/lib/firmware/
"""

    firmware_install_main = """define KernelPackage/%(module_name)s/install
	$(INSTALL_DIR) $(1)/lib/firmware
%(firmware_install)s
endef
"""

    device_structure = """
define KernelPackage/%(module_name)s
  SUBMENU:=$(DVB_MENU)
  TITLE:=%(module_title)s
  KCONFIG:= %(kconfig)s
  DEPENDS:=%(depends)s
  FILES:= %(module_files)s
  AUTOLOAD:=$(call AutoLoad,65,%(module_list)s)
endef

define KernelPackage/%(module_name)s/description
 Say Y here to support the %(module_title)s.
The following modules will be compiled for this device :  %(module_list)s
%(firmware_files)s
endef

%(firmware_list)s
%(firmware_download)s
%(firmware_install)s
%(firmware_download_call)s
$(eval $(call KernelPackage,%(module_name)s))
"""

    #We search for the generated files in the main Makefile
    config["files"] = find_module_files("drivers/media/dvb/dvb-usb/", \
                                            KERNEL_PATH + "drivers/media/dvb/dvb-usb/Makefile", \
                                            config["name"])
    config["files"] = [item[:-2] for item in config["files"]]

    print " * We search the needed source files for searching for a firmware"
    config["source_files"] = []
    for obj in config["files"]:
        obj = obj.split('/')[-1]+'-objs'
        config["source_files"] += find_module_files("drivers/media/dvb/dvb-usb/", KERNEL_PATH + "drivers/media/dvb/dvb-usb/Makefile", obj)
        #We replace the .o by a .c
        config["source_files"] = [item[:-2] + ".c" for item in config["source_files"]]

    config["firmwares"] = []
    temp_config_firmwares = []
    for sourcefile in config["source_files"]:
        temp_config_firmwares += find_module_files("", KERNEL_PATH+sourcefile, ".firmware")
    #We remove the probable comma
    temp_config_firmwares = [item.replace(",",'') for item in temp_config_firmwares]
    #Dirty hack, since we don't completely parse the C code, we exclude false positive searching for .fw" in the name
    for item in temp_config_firmwares:
        if ".fw\"" in item and item.replace("\"", "") not in config["firmwares"]:
            config["firmwares"].append(item.replace("\"", ""))
    print " ** This object needs the firmwares : " + str(config["firmwares"]) 
    firmware_list = ""
    firmware_download = ""
    firmware_download_call = ""
    firmware_install = ""
    for index, firmware in enumerate(config["firmwares"]):
	name = firmware.replace("-", "_").replace(".", "_")
        firmware_list += firmware_pattern % {"name" : name.upper(), "filename" : firmware}
        firmware_download += firmware_download_pattern % {"name" : name.strip("_fw"), "filename" : name.upper()}
        firmware_download_call += firmware_download_call_pattern % {"name" : name.strip("_fw")}
        firmware_install += firmware_install_pattern % {"name" : name.upper()}

    #we look on the files needed by the tuners/ frontends
    if len(config["select"]):
        print " * We loop on the selected modules "
    for module in config["select"]:
        print "  Module : " + module
        if(module.find("MEDIA")==0):
            new_files = find_module_files("drivers/media/common/tuners/", KERNEL_PATH+"drivers/media/common/tuners/Makefile", "CONFIG_" + module)
            config["files"] += [item[:-2] for item in new_files]
        elif(module.find("DVB")==0):
            new_files = find_module_files("drivers/media/dvb/frontends/", KERNEL_PATH+"drivers/media/dvb/frontends/Makefile", "CONFIG_" + module)
            config["files"] += [item[:-2] for item in new_files]
        print "    New files : " + str(new_files)

    if len(config["select"]):
        print " * Final module files : " 
        print config["files"]

    
    print " * Depends : " 
    print config["depends"]

    #--------------- GENERATED device dvb.mk part --------------"
    #We have now all the needed information, we generate the config for the mk
    depends = ' '.join(['+kmod-' + item.lower().replace('_','-') for item in config["depends"]])
    kconfig = "CONFIG_"+config["name"]
    if len(config["select"]):
        kconfig += _NEXT_LINE + _NEXT_LINE.join(["CONFIG_" + item for item in config["select"]])
    if(len(config["firmwares"])):
        firmware_files = \
            "You have to put the firmware files in the download dir : " + \
            ' '.join(config["firmwares"]) + \
            "\nThey can be found in the package http://packages.ubuntu.com/jaunty/linux-firmware ."
        firmware_install = firmware_install_main % {"module_name" : config["name"].lower().replace('_','-'),"firmware_install" : firmware_install[:-1]}
    else:
        firmware_files = ""
        firmware_install = ""
    device_mk = device_structure % {"module_name_orig" : config["name"], \
                                       "module_name" : config["name"].lower().replace('_', '-'), \
                                       "module_title" : config["description"].replace('"', '')[:50], \
                                       "kconfig" : kconfig, \
                                       "module_files" : _NEXT_LINE.join(["$(LINUX_DIR)/" + item + ".$(LINUX_KMOD_SUFFIX)" for item in config["files"]]), \
                                       "module_list"  : ' '.join([item.split('/')[-1] for item in reversed(config["files"])]), \
                                       "firmware_list" : firmware_list, \
                                       "firmware_download" : firmware_download, \
                                       "firmware_install" : firmware_install, \
                                       "firmware_files" : firmware_files, \
                                       "firmware_download_call" : firmware_download_call, \
                                       "depends" : depends}
    #print device_mk
    print
    filedvbmk.write(device_mk)
    filedvbmk.flush()

if __name__ == "__main__" :

    target = find_boardtype(PWD)
    subtarget = find_subtarget(PWD,target)
    KERNEL_PATH = PWD + "/build_dir/linux-" + target + subtarget + "/linux-" + find_kernel_version(PWD) + "/"
	
    print "Openning of Kconfig"
    dvb_usb_kconfig = open(KERNEL_PATH+"drivers/media/dvb/dvb-usb/Kconfig",'r')
    print "The generated file will be put in : " + DEST_DIR + DEST_FILE

    dvb_mk = open(DEST_DIR + DEST_FILE,'w')

    #we write the header
    dvb_mk.write(CONFIG_FILE_HEADER)
    haveconfig = False
    current_config = {"name" : ""}

    #We loop on the lines of the Kconfig to find new devices characterized by the keyword "config"
    for line_Kconfig in dvb_usb_kconfig.readlines():
        if(line_Kconfig.find("config")==0):
            if(haveconfig and current_config["name"] != "DVB_USB"):
                #We found a new "config" keyword, we parse the previous one
                print "We found config " + current_config["name"]
                print current_config["description"]
                answer = raw_input( "Do you want it (Y/n) ? ")
                if(answer.lower().find('y')==0 or len(answer)==0):
                    deal_config(current_config, dvb_mk)
                print
            haveconfig = False
            current_config = {"name" : "","select" : [], "depends" : []}
            current_config["name"] = line_Kconfig.split(' ')[1].strip()

        #"real" modules are characterized by a tristate keyword
        if "tristate" in line_Kconfig:
            #Here we get the main CONFIG_ and the module description
            haveconfig = True
            current_config["description"] = line_Kconfig.split("tristate ")[1].strip().replace("support","")
            #We remove stuff between () to shorten the description
            while(current_config["description"].find('(') != -1 and current_config["description"].find(')') != -1):
                current_config["description"] = current_config["description"][:current_config["description"].find('(')] + \
                    current_config["description"][current_config["description"].find(')')+1:]
        #The select keyword allow us to find the tuners and frontends
        if "select" in line_Kconfig:
            current_config["select"].append(line_Kconfig.split("select ")[1].split(' ')[0].strip())
            
        #We add the module dependancies
        if "depends on" in line_Kconfig:
            if line_Kconfig.split("depends on ")[1].split(' ')[0].strip() not in ['EXPERIMENTAL']:
                current_config["depends"].append(line_Kconfig.split("depends on ")[1].split(' ')[0].strip())

    #We deal with the last one
    if(haveconfig and current_config["name"] != "DVB_USB"):
        #We found a new "config" keyword, we parse the previous one
        print "We found config " + current_config["name"]
        print current_config["description"]
        answer = raw_input( "Do you want it (Y/n) ? ")
        if(answer.lower().find('y')==0 or len(answer)==0):
            deal_config(current_config, dvb_mk)
            
    dvb_mk.close()
    dvb_usb_kconfig.close()

