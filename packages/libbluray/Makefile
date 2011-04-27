#
# Copyright (C) 2011 OpenWrt.org
#
# This is free software, licensed under the GNU General Public License v2.
# See /LICENSE for more information.
#

include $(TOPDIR)/rules.mk

PKG_NAME:=libbluray
PKG_VERSION:=20100908
PKG_REV:=a58be3302b994623723caa2b691dbda4991e5a8b

PKG_SOURCE_PROTO:=git
PKG_SOURCE_VERSION:=$(PKG_REV)
PKG_SOURCE_SUBDIR:=$(PKG_NAME)-$(PKG_VERSION)
PKG_SOURCE_URL:=git://git.videolan.org/libbluray.git
PKG_SOURCE:=$(PKG_SOURCE_SUBDIR).tar.bz2

PKG_INSTALL:=1
PKG_FIXUP:=libtool

include $(INCLUDE_DIR)/package.mk

define Package/libbluray
  SECTION:=libs
  CATEGORY:=Libraries
  TITLE:=A Blu-Ray Discs playback library
  URL:=http://www.videolan.org/developers/libbluray.html
  DEPENDS:=+libopenssl
endef

define Package/libbluray/description
  libbluray is an open-source library designed for Blu-Ray Discs playback for media players, like VLC or MPlayer.
endef

define Build/Configure
	( cd $(PKG_BUILD_DIR)/bootstrap; \
		$(call Build/Configure/Default, ) \
	)
endef	
	
define Build/InstallDev
	$(INSTALL_DIR) $(1)/usr/include
	$(CP) $(PKG_INSTALL_DIR)/usr/include/* $(1)/usr/include/

	$(INSTALL_DIR) $(1)/usr/lib/
	$(CP) $(PKG_INSTALL_DIR)/usr/lib/libbluray.{a,la,so*} $(1)/usr/lib/
	
	$(INSTALL_DIR) $(1)/usr/lib/pkgconfig/
	$(CP) $(PKG_INSTALL_DIR)/usr/lib/pkgconfig/* $(1)/usr/lib/pkgconfig/
endef

define Package/libbluray/install
	$(INSTALL_DIR) $(1)/usr/lib
	$(CP) $(PKG_INSTALL_DIR)/usr/lib/libbluray.so* $(1)/usr/lib
endef
        
$(eval $(call BuildPackage,libbluray))
