#
# Copyright (C) 2011 OpenWrt.org
#
# This is free software, licensed under the GNU General Public License v2.
# See /LICENSE for more information.
#

include $(TOPDIR)/rules.mk

PKG_NAME:=libvdpau
PKG_VERSION:=0.4.1

PKG_SOURCE:=$(PKG_NAME)-$(PKG_VERSION).tar.gz
PKG_SOURCE_URL:=http://people.freedesktop.org/~aplattner/vdpau/
PKG_MD5SUM:=8e1f0639bea4e4a842aee93ab64406cc

PKG_INSTALL=1

include $(INCLUDE_DIR)/package.mk

define Package/libvdpau
  SECTION:=libs
  CATEGORY:=Libraries
  TITLE:=Nvidia VDPAU library
  URL:=http://freedesktop.org/wiki/Software/VDPAU
  DEPENDS:=+libX11
endef

define Package/libvdpau/description
  VDPAU is the Video Decode and Presentation API for UNIX. It 
  provides an interface to video decode acceleration and 
  presentation hardware present in modern GPUs
endef

CONFIGURE_ARGS+= \
	--disable-documentation \

define Build/InstallDev
	$(INSTALL_DIR) $(1)/usr/include
	$(CP) $(PKG_INSTALL_DIR)/usr/include/* $(1)/usr/include/

	$(INSTALL_DIR) $(1)/usr/lib
	$(CP) $(PKG_INSTALL_DIR)/usr/lib/libvdpau*.{so*,la} $(1)/usr/lib/

	$(INSTALL_DIR) $(1)/usr/lib/pkgconfig
	$(INSTALL_DATA) $(PKG_INSTALL_DIR)/usr/lib/pkgconfig/* $(1)/usr/lib/pkgconfig/
endef

define Package/libvdpau/install
	$(INSTALL_DIR) $(1)/usr/lib
	$(CP) $(PKG_INSTALL_DIR)/usr/lib/libvdpau*.so.* $(1)/usr/lib
endef
        
$(eval $(call BuildPackage,libvdpau))
