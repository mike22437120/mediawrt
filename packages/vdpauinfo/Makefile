#
# Copyright (C) 2011 OpenWrt.org
#
# This is free software, licensed under the GNU General Public License v2.
# See /LICENSE for more information.
#

include $(TOPDIR)/rules.mk

PKG_NAME:=vdpauinfo
PKG_VERSION:=0.0.6

PKG_SOURCE:=$(PKG_NAME)-$(PKG_VERSION).tar.gz
PKG_SOURCE_URL:=http://people.freedesktop.org/~aplattner/vdpau/
PKG_MD5SUM:=513df206613cbd061b6d49cdbfe927ef

PKG_INSTALL=1

include $(INCLUDE_DIR)/package.mk

define Package/vdpauinfo
  SECTION:=utils
  CATEGORY:=Utilities
  TITLE:=vdpauinfo
  URL:=http://people.freedesktop.org/~aplattner/vdpau/
  DEPENDS:=+libvdpau +libX11
endef

define Package/vdpauinfo/description
  vdpauinfo is a command line utility for querying the capabilities of a VDPAU device
endef

TARGET_LDFLAGS += \
		-Wl,-rpath-link=$(STAGING_DIR)/usr/lib

define Package/vdpauinfo/install
	$(INSTALL_DIR) $(1)/usr/bin
	$(CP) $(PKG_INSTALL_DIR)/usr/bin/vdpauinfo $(1)/usr/bin/
endef
        
$(eval $(call BuildPackage,vdpauinfo))
