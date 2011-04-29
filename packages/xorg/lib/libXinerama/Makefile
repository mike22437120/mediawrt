#
# Copyright (C) 2011 OpenWrt.org
#
# This is free software, licensed under the GNU General Public License v2.
# See /LICENSE for more information.
#

include $(TOPDIR)/rules.mk

PKG_NAME:=libXinerama
PKG_RELEASE:=1
PKG_VERSION:=1.1.1

PKG_SOURCE_URL:=http://xorg.freedesktop.org/releases/individual/lib/
PKG_SOURCE:=$(PKG_NAME)-$(PKG_VERSION).tar.bz2
PKG_BUILD_DIR:=$(BUILD_DIR)/Xorg/$(PKG_NAME)-$(PKG_VERSION)/
PKG_MD5SUM:=ecd4839ad01f6f637c6fb5327207f89b

PKG_FIXUP:=libtool

PKG_INSTALL:=1
PKG_BUILD_DEPENDS:=xineramaproto xextproto

include $(INCLUDE_DIR)/package.mk

define Package/libXinerama
  SECTION:=xorg-libraries
  CATEGORY:=Xorg
  SUBMENU:=libraries
  TITLE:=libXinerama
  DEPENDS:=+libX11 +libXext
  URL:=http://xorg.freedesktop.org/
endef

CONFIGURE_ARGS += \
	--enable-malloc0returnsnull

define Build/InstallDev
	$(INSTALL_DIR) $(1)/usr/lib
	$(CP) $(PKG_INSTALL_DIR)/usr/lib/*.{so*,a,la} $(1)/usr/lib/
	
	$(INSTALL_DIR) $(1)/usr/lib/pkgconfig
	$(INSTALL_DATA) $(PKG_INSTALL_DIR)/usr/lib/pkgconfig/* $(1)/usr/lib/pkgconfig/
	
	$(INSTALL_DIR) $(1)/usr/include/X11/extensions
	$(INSTALL_DATA) $(PKG_INSTALL_DIR)/usr/include/X11/extensions/* $(1)/usr/include/X11/extensions/
endef

define Package/libXinerama/install
	$(INSTALL_DIR) $(1)/usr/lib
	$(CP) $(PKG_INSTALL_DIR)/usr/lib/*.so* $(1)/usr/lib/
endef

$(eval $(call BuildPackage,libXinerama))
