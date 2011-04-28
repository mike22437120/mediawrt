#
# Copyright (C) 2011 OpenWrt.org
#
# This is free software, licensed under the GNU General Public License v2.
# See /LICENSE for more information.
#

include $(TOPDIR)/rules.mk

PKG_NAME:=w-scan
PKG_VERSION:=20110306
PKG_RELEASE:=1

PKG_SOURCE:=w_scan-$(PKG_VERSION).tar.bz2
PKG_SOURCE_URL:=http://wirbel.htpc-forum.de/w_scan
PKG_BUILD_DIR:=$(BUILD_DIR)/w_scan-$(PKG_VERSION)
PKG_MD5SUM:=bdb8ac0a5e409e060c6ab406b4cfc2c6

include $(INCLUDE_DIR)/package.mk

define Package/w_scan
  SECTION:=utils
  CATEGORY:=Utilities
  TITLE:=w_scan performs frequency scans for DVB and ATSC.
  URL:=http://wirbel.htpc-forum.de/w_scan/index2.html
endef

define Package/w_scan/description
	w_scan is a small command line utility used to perform frequency scans for DVB and ATSC transmissions. It is capable of creating channels.conf files (in different output formats !) as well as initial tuning data for scan. It's based on the utility scan from linuxtv-dvb-apps, but meanwhile it was heavily changed and has different features:
	1. no need for "initial transponders", and such no need for a config file 
	2. w_scan finds automatically the best matching dvb card 
	3. complete different command line options 
	4. a different default output format as well as bunch of output formats.
This package does not include the script file "w_scan_start.sh".
endef

define Package/w_scan/install
	$(INSTALL_DIR) $(1)/usr/bin
	$(INSTALL_BIN) $(PKG_BUILD_DIR)/w_scan $(1)/usr/bin/
endef

$(eval $(call BuildPackage,w_scan))