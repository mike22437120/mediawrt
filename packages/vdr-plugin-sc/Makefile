#
# Copyright (C) 2006-2010 OpenWrt.org
#
# This is free software, licensed under the GNU General Public License v2.
# See /LICENSE for more information.
#

include $(TOPDIR)/rules.mk

PKG_NAME:=vdr-plugin-sc
PKG_REV:=61975953edd0
PKG_VERSION:=r$(PKG_REV)
PKG_RELEASE:=1

PKG_SOURCE_PROTO:=hg
PKG_SOURCE_VERSION:=$(PKG_REV)
PKG_SOURCE_SUBDIR:=sc-$(PKG_VERSION)
PKG_SOURCE:=sc-$(PKG_REV).tar.bz2
PKG_SOURCE_URL:=http://85.17.209.13:6100/sc
PKG_BUILD_DIR:=$(BUILD_DIR)/sc-$(PKG_VERSION)

include $(INCLUDE_DIR)/package.mk

define Package/vdr-plugin-sc
  SECTION:=multimedia
  CATEGORY:=Multimedia
  TITLE:=VDR Software Conditional Access Module Plugin
  DEPENDS:=vdr +libopenssl
  URL:=http://85.17.209.13:6100/sc
endef

define Package/vdr-plugin-sc/description
  This VDR plugin provides a software emulated CAM. Software
  decryption with ffdecsa for budget cards is also available. With
  this plugin you can, for example, use your pay-tv subscription with
  a smart card reader/programmer without expensive CI and CAM devices.
endef

define Build/Compile
endef

define Build/Install
endef

define Package/vdr-plugin-sc/install
	$(INSTALL_DIR) $(1)/etc/config/vdr/plugins/sc
	$(CP) ./files/*.conf $(1)/etc/config/vdr/plugins/sc/
endef

$(eval $(call BuildPackage,vdr-plugin-sc))
