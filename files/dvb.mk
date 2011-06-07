
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
  KCONFIG:= \
	CONFIG_MEDIA_SUPPORT \
	CONFIG_INPUT=y \
	CONFIG_IR_CORE=y	\
	CONFIG_RC_CORE=y
ifneq ($(CONFIG_LINUX_2_6_35)$(CONFIG_LINUX_2_6_36)$(CONFIG_LINUX_2_6_37),)
	FILES:= $(LINUX_DIR)/drivers/media/IR/ir-core.$(LINUX_KMOD_SUFFIX) \
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
  KCONFIG:= \
	CONFIG_MEDIA_SUPPORT \
	CONFIG_DVB_CORE \
	CONFIG_DVB_CAPTURE_DRIVERS=y \
	CONFIG_MEDIA_TUNER_CUSTOMIZE=y \
	CONFIG_DVB_FE_CUSTOMISE=y \
	CONFIG_DVB_DYNAMIC_MINORS=n \
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
  KCONFIG:= \
	CONFIG_DVB_USB \
	CONFIG_IR_CORE 	\
	CONFIG_INPUT=y \
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


define KernelPackage/dvb-usb-dib0700
  SUBMENU:=$(DVB_MENU)
  TITLE:=DiBcom DiB0700 USB DVB devices 
  KCONFIG:= CONFIG_DVB_USB_DIB0700 \
	CONFIG_DVB_DIB7000P \
	CONFIG_DVB_DIB7000M \
	CONFIG_DVB_DIB8000 \
	CONFIG_DVB_DIB9000 \
	CONFIG_DVB_DIB3000MC \
	CONFIG_DVB_S5H1411 \
	CONFIG_DVB_LGDT3305 \
	CONFIG_DVB_TUNER_DIB0070 \
	CONFIG_DVB_TUNER_DIB0090 \
	CONFIG_MEDIA_TUNER_MT2060 \
	CONFIG_MEDIA_TUNER_MT2266 \
	CONFIG_MEDIA_TUNER_XC2028 \
	CONFIG_MEDIA_TUNER_XC5000 \
	CONFIG_MEDIA_TUNER_MXL5007T
  DEPENDS:=+kmod-dvb-usb
  FILES:= $(LINUX_DIR)/drivers/media/dvb/dvb-usb/dvb-usb-dib0700.$(LINUX_KMOD_SUFFIX) \
	$(LINUX_DIR)/drivers/media/dvb/frontends/dib7000p.$(LINUX_KMOD_SUFFIX) \
	$(LINUX_DIR)/drivers/media/dvb/frontends/dibx000_common.$(LINUX_KMOD_SUFFIX) \
	$(LINUX_DIR)/drivers/media/dvb/frontends/dib7000m.$(LINUX_KMOD_SUFFIX) \
	$(LINUX_DIR)/drivers/media/dvb/frontends/dibx000_common.$(LINUX_KMOD_SUFFIX) \
	$(LINUX_DIR)/drivers/media/dvb/frontends/dib8000.$(LINUX_KMOD_SUFFIX) \
	$(LINUX_DIR)/drivers/media/dvb/frontends/dib9000.$(LINUX_KMOD_SUFFIX) \
	$(LINUX_DIR)/drivers/media/dvb/frontends/dibx000_common.$(LINUX_KMOD_SUFFIX) \
	$(LINUX_DIR)/drivers/media/dvb/frontends/dib3000mc.$(LINUX_KMOD_SUFFIX) \
	$(LINUX_DIR)/drivers/media/dvb/frontends/dibx000_common.$(LINUX_KMOD_SUFFIX) \
	$(LINUX_DIR)/drivers/media/dvb/frontends/s5h1411.$(LINUX_KMOD_SUFFIX) \
	$(LINUX_DIR)/drivers/media/dvb/frontends/lgdt3305.$(LINUX_KMOD_SUFFIX) \
	$(LINUX_DIR)/drivers/media/dvb/frontends/dib0070.$(LINUX_KMOD_SUFFIX) \
	$(LINUX_DIR)/drivers/media/dvb/frontends/dib0090.$(LINUX_KMOD_SUFFIX) \
	$(LINUX_DIR)/drivers/media/common/tuners/mt2060.$(LINUX_KMOD_SUFFIX) \
	$(LINUX_DIR)/drivers/media/common/tuners/mt2266.$(LINUX_KMOD_SUFFIX) \
	$(LINUX_DIR)/drivers/media/common/tuners/tuner-xc2028.$(LINUX_KMOD_SUFFIX) \
	$(LINUX_DIR)/drivers/media/common/tuners/xc5000.$(LINUX_KMOD_SUFFIX) \
	$(LINUX_DIR)/drivers/media/common/tuners/mxl5007t.$(LINUX_KMOD_SUFFIX)
  AUTOLOAD:=$(call AutoLoad,65,mxl5007t xc5000 tuner-xc2028 mt2266 mt2060 dib0090 dib0070 lgdt3305 s5h1411 dibx000_common dib3000mc dib7000m dib7000p dib8000 dib9000 dvb-usb-dib0700/force_lna_activation=1)
endef

define KernelPackage/dvb-usb-dib0700/description
 Say Y here to support the DiBcom DiB0700 USB DVB devices .
The following modules will be compiled for this device :  mxl5007t xc5000 tuner-xc2028 mt2266 mt2060 dib0090 dib0070 lgdt3305 s5h1411 dibx000_common dib3000mc dibx000_common dib8000 dibx000_common dib7000m dibx000_common dib7000p dvb-usb-dib0700
You have to put the firmware files in the download dir : dvb-usb-dib0700-1.20.fw
They can be found in the package http://packages.ubuntu.com/jaunty/linux-firmware .
endef

DVB_USB_DIB0700_1_20_FW:=dvb-usb-dib0700-1.20.fw

define Download/dvb_usb_dib0700_1_20
    FILE:=$(DVB_USB_DIB0700_1_20_FW)
    URL:=http://code.google.com/p/wl-700ge/source/browse/trunk/firmware/
endef


define KernelPackage/dvb-usb-dib0700/install
	$(INSTALL_DIR) $(1)/lib/firmware
	$(INSTALL_DATA) $(DL_DIR)/$(DVB_USB_DIB0700_1_20_FW) $(1)/lib/firmware/
endef

$(eval $(call Download,dvb_usb_dib0700_1_20))

$(eval $(call KernelPackage,dvb-usb-dib0700))
