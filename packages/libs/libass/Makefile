#
# Copyright (C) 2011 OpenWrt.org
#
# This is free software, licensed under the GNU General Public License v2.
# See /LICENSE for more information.
#

include $(TOPDIR)/rules.mk

PKG_NAME:=libass
PKG_VERSION:=0.9.11

PKG_SOURCE:=$(PKG_NAME)-$(PKG_VERSION).tar.bz2
PKG_SOURCE_URL:=http://libass.googlecode.com/files/
PKG_MD5SUM:=f9042884397002ba40aa89dc7d34f59f

PKG_INSTALL=1

include $(INCLUDE_DIR)/package.mk

define Package/libass
  SECTION:=libs
  CATEGORY:=Libraries
  TITLE:=Portable library for SSA/ASS subtitles rendering
  URL:=http://libass.googlecode.com/
  DEPENDS:=+libfreetype +fontconfig
endef

define Package/libass/description
  Libass is a portable library for SSA/ASS subtitles rendering.
endef

define Build/InstallDev
	$(INSTALL_DIR) $(1)/usr/include
	$(CP) $(PKG_INSTALL_DIR)/usr/include/* $(1)/usr/include/
	
	$(INSTALL_DIR) $(1)/usr/lib
	$(CP) $(PKG_INSTALL_DIR)/usr/lib/libass.{la,so*} $(1)/usr/lib	

	$(INSTALL_DIR) $(1)/usr/lib/pkgconfig
	$(CP) $(PKG_INSTALL_DIR)/usr/lib/pkgconfig/*.pc $(1)/usr/lib/pkgconfig	
endef

define Package/libass/install
	$(INSTALL_DIR) $(1)/usr/lib
	$(CP) $(PKG_INSTALL_DIR)/usr/lib/libass.so.* $(1)/usr/lib
endef
        
$(eval $(call BuildPackage,libass))
