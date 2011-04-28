#
# Copyright (C) 2011 OpenWrt.org
#
# This is free software, licensed under the GNU General Public License v2.
# See /LICENSE for more information.
#

include $(TOPDIR)/rules.mk

PKG_NAME:=libmodplug
PKG_VERSION:=0.8.8

PKG_SOURCE:=$(PKG_NAME)-$(PKG_VERSION).tar.gz
PKG_SOURCE_URL:=@SF/modplug-xmms/$(PKG_NAME)/$(PKG_VERSION)
PKG_MD5SUM:=fa9e5ede2e53d847f288c0315feec275

PKG_INSTALL=1

include $(INCLUDE_DIR)/package.mk

define Package/libmodplug
  SECTION:=sound
  CATEGORY:=Sound
  TITLE:=libmodplug
  URL:=http://sourceforge.net/projects/modplug-xmms/
endef

define Package/libmodplug/description
  ibmodplug renders mod music files as raw audio data, for playing or conversion. 
  libmodplug is based on the fast and high quality mod playing code written and released to the public domain by Olivier Lapicque. 
  mod, .s3m, .it, .xm, and a number of lesser-known formats are supported. 
endef

define Build/InstallDev
	$(INSTALL_DIR) $(1)/usr/include
	$(CP) $(PKG_INSTALL_DIR)/usr/include/* $(1)/usr/include/

	$(INSTALL_DIR) $(1)/usr/lib
	$(CP) $(PKG_INSTALL_DIR)/usr/lib/libmodplug.{so*,la} $(1)/usr/lib/

	$(INSTALL_DIR) $(1)/usr/lib/pkgconfig
	$(INSTALL_DATA) $(PKG_INSTALL_DIR)/usr/lib/pkgconfig/* $(1)/usr/lib/pkgconfig/
endef	
	
define Package/libmodplug/install
	$(INSTALL_DIR) $(1)/usr/lib
	$(CP) $(PKG_INSTALL_DIR)/usr/lib/libmodplug.so* $(1)/usr/lib
endef
        
$(eval $(call BuildPackage,libmodplug))
