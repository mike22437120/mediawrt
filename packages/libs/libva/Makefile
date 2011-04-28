#
# Copyright (C) 2011 OpenWrt.org
#
# This is free software, licensed under the GNU General Public License v2.
# See /LICENSE for more information.
#

include $(TOPDIR)/rules.mk

PKG_NAME:=libva
PKG_VERSION:=1.0.12

PKG_SOURCE:=$(PKG_NAME)-$(PKG_VERSION).tar.bz2
PKG_SOURCE_URL:=http://cgit.freedesktop.org/libva/snapshot/
PKG_MD5SUM:=84408a0746a63b8cf308dc7b9f2451cf
PKG_FIXUP:=autoreconf

PKG_INSTALL=1

include $(INCLUDE_DIR)/package.mk

define Package/libva
  SECTION:=libs
  CATEGORY:=Libraries
  TITLE:=Video Acceleration (VA) API for Linux
  URL:=http://freedesktop.org/wiki/Software/vaapi
  DEPENDS:=+libX11 +libXext +libXfixes +libdrm +libgl-mesa @FEATURE_drawing-backend_libX11
endef

define Package/libva/description
  Libva is a library providing the VA API video acceleration API.
endef

CONFIGURE_ARGS+= \
	--enable-glx \
	--disable-dummy-driver \
	--enable-i965-driver \
	--with-drivers-path="/usr/lib/va" \

TARGET_LDFLAGS += \
	-Wl,-rpath-link=$(STAGING_DIR)/usr/lib
	
define Build/InstallDev
	$(INSTALL_DIR) $(1)/usr/include
	$(CP) $(PKG_INSTALL_DIR)/usr/include/* $(1)/usr/include/

	$(INSTALL_DIR) $(1)/usr/lib
	$(CP) $(PKG_INSTALL_DIR)/usr/lib/libva.{so*,la} $(1)/usr/lib/

	$(INSTALL_DIR) $(1)/usr/lib/pkgconfig
	$(INSTALL_DATA) $(PKG_INSTALL_DIR)/usr/lib/pkgconfig/* $(1)/usr/lib/pkgconfig/
endef

define Package/libva/install
	$(INSTALL_DIR) $(1)/usr/lib
	$(CP) $(PKG_INSTALL_DIR)/usr/lib/libva*.so* $(1)/usr/lib
	
	$(INSTALL_DIR) $(1)/usr/bin
	$(CP) $(PKG_INSTALL_DIR)/usr/bin/vainfo $(1)/usr/bin	
endef
        
$(eval $(call BuildPackage,libva))
