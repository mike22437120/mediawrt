#
# Copyright (C) 2011 OpenWrt.org
#
# This is free software, licensed under the GNU General Public License v2.
# See /LICENSE for more information.
#

include $(TOPDIR)/rules.mk

PKG_NAME:=vdr-plugin-femon
PKG_VERSION:=1.7.9
PKG_RELEASE:=1

PKG_SOURCE:=vdr-femon-$(PKG_VERSION).tgz
PKG_SOURCE_URL:=http://www.saunalahti.fi/~rahrenbe/vdr/femon/files/
PKG_MD5SUM:=d30be2d93b572ce16b77cadf381d3ddc
PKG_BUILD_DIR:=$(BUILD_DIR)/femon-$(PKG_VERSION)

include $(INCLUDE_DIR)/package.mk

define Package/vdr-plugin-femon
  SECTION:=multimedia
  CATEGORY:=Multimedia
  TITLE:=VDR Frontend Status Monitor
  DEPENDS:=vdr
  URL:=http://www.saunalahti.fi/~rahrenbe/vdr/femon/
endef

define Package/vdr-plugin-femon/description
  DVB Frontend Status Monitor is a plugin that displays some signal information
  parameters of the current tuned channel on OSD. You can zap through all your
  channels and the plugin should be monitoring always the right frontend. The
  transponder and stream information are also available in advanced display modes.
endef

define Build/Compile
endef

define Build/Install
endef

define Package/vdr-plugin-femon/install
	$(INSTALL_DIR) $(1)/usr/bin
endef

$(eval $(call BuildPackage,vdr-plugin-femon))
