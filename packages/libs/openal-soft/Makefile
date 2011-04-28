#
# Copyright (C) 2011 OpenWrt.org
#
# This is free software, licensed under the GNU General Public License v2.
# See /LICENSE for more information.
#

include $(TOPDIR)/rules.mk

PKG_NAME:=openal-soft
PKG_VERSION:=1.12.854

PKG_SOURCE:=$(PKG_NAME)-$(PKG_VERSION).tar.bz2
PKG_SOURCE_URL:=http://kcat.strangesoft.net/openal-releases/
PKG_MD5SUM:=fbf36451fdebd6466edbdc0ee7db9603

PKG_INSTALL=1

include $(INCLUDE_DIR)/package.mk
include $(INCLUDE_DIR)/cmake.mk

define Package/openal-soft
  SECTION:=libs
  CATEGORY:=Libraries
  TITLE:=Open Audio Library
  URL:=http://www.openal.org/
  DEPENDS:=+alsa-lib
endef

define Package/openal-soft/description
  OpenAL, the Open Audio Library, is a joint effort to create an open, vendor- neutral, cross-platform API for interactive, 
  primarily spatialized audio. OpenAL's primary audience are application developers and desktop users that rely on portable standards like OpenGL, 
  for games and other multimedia applications. OpenAL is already supported by a number of hardware vendors and developers.
endef

define Package/openal-soft/install
	$(INSTALL_DIR) $(1)/usr/lib
	$(CP) $(PKG_INSTALL_DIR)/usr/lib/*.so* $(1)/usr/lib
endef
        
$(eval $(call BuildPackage,openal-soft))
