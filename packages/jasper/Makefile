#
# Copyright (C) 2011 OpenWrt.org
#
# This is free software, licensed under the GNU General Public License v2.
# See /LICENSE for more information.
#

include $(TOPDIR)/rules.mk

PKG_NAME:=jasper
PKG_VERSION:=1.900.1

PKG_SOURCE:=$(PKG_NAME)-$(PKG_VERSION).zip
PKG_SOURCE_URL:=http://www.ece.uvic.ca/~mdadams/jasper/software
PKG_MD5SUM:=a342b2b4495b3e1394e161eb5d85d754

PKG_INSTALL=1

include $(INCLUDE_DIR)/package.mk

define Package/jasper
  SECTION:=libs
  CATEGORY:=Libraries
  TITLE:=jasper
  URL:=http://www.ece.uvic.ca/~mdadams/jasper/
endef

define Package/jasper/description
  A software-based implementation of the codec specified in the emerging JPEG-2000 Part-1 standard
endef

define Build/InstallDev
	$(INSTALL_DIR) $(1)/usr/include/
	$(CP) $(PKG_INSTALL_DIR)/usr/include/jasper $(1)/usr/include/

	$(INSTALL_DIR) $(1)/usr/lib/
	$(CP) $(PKG_INSTALL_DIR)/usr/lib/libjasper.{la,a} $(1)/usr/lib/
endef

define Package/jasper/install
	$(INSTALL_DIR) $(1)/usr/lib
	$(CP) $(PKG_INSTALL_DIR)/usr/lib/libjasper.{la,a} $(1)/usr/lib
endef
        
$(eval $(call BuildPackage,jasper))
