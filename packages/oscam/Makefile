#
# Copyright (C) 2006-2010 OpenWrt.org
#
# This is free software, licensed under the GNU General Public License v2.
# See /LICENSE for more information.
#

include $(TOPDIR)/rules.mk

PKG_NAME:=oscam
PKG_REV:=5048
PKG_VERSION:=$(PKG_REV)
PKG_RELEASE:=1

PKG_SOURCE_PROTO:=svn
PKG_SOURCE_VERSION:=$(PKG_REV)
PKG_SOURCE_SUBDIR:=$(PKG_NAME)-$(PKG_VERSION)
PKG_SOURCE:=$(PKG_SOURCE_SUBDIR).tar.bz2
PKG_SOURCE_URL:=http://streamboard.gmc.to/svn/oscam/trunk

include $(INCLUDE_DIR)/package.mk
include $(INCLUDE_DIR)/cmake.mk

define Package/oscam
  SECTION:=utils
  CATEGORY:=Utilities
  DEPENDS:=+libopenssl
  TITLE:=OSCam is an Open Source Conditional Access Module software
  URL:=http://streamboard.gmc.to:8001/
endef

define Package/oscam/description
  OSCam is an Open Source Conditional Access Module software
endef

CMAKE_OPTIONS += \
		-DCS_CONFDIR=/etc/config/oscam

define Package/oscam/install
	$(INSTALL_DIR) $(1)/usr/bin
	$(INSTALL_BIN) $(PKG_INSTALL_DIR)/usr/bin/oscam $(1)/usr/bin/

	$(INSTALL_DIR) $(1)/etc/config/oscam
	$(INSTALL_DATA) $(PKG_INSTALL_DIR)/usr/share/doc/oscam/example/* $(1)/etc/config/oscam/

endef

$(eval $(call BuildPackage,oscam))