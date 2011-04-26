#
# Copyright (C) 2011 OpenWrt.org
#
# This is free software, licensed under the GNU General Public License v2.
# See /LICENSE for more information.
#

include $(TOPDIR)/rules.mk

PKG_NAME:=v4l-dvb
PKG_REV:=e7d0ae06c74f55562c1589feb5a6802d77c14dbc
PKG_VERSION:=20112303
PKG_RELEASE:=1

PKG_SOURCE_PROTO:=git
PKG_SOURCE_VERSION:=$(PKG_REV)
PKG_SOURCE_SUBDIR:=$(PKG_NAME)-$(PKG_VERSION)
PKG_SOURCE:=$(PKG_NAME)-$(PKG_REV).tar.bz2
PKG_SOURCE_URL:=git://linuxtv.org/media_build.git

PKG_INSTALL:=1

include $(INCLUDE_DIR)/package.mk
include $(INCLUDE_DIR)/kernel.mk


define Package/v4l-dvb
  SECTION:=utils
  CATEGORY:=Utilities
  DEPENDS:=+@KERNEL_KALLSYMS
  TITLE:=v4l-dvb
  URL:=http://www.linuxtv.org/
endef

define Package/v4l-dvb/description
 todo
endef

MAKE_VARS += \
	TOPDIR="" \
	KDIR=$(LINUX_DIR) \
	DIR=$(LINUX_DIR)\
	SRCDIR=$(LINUX_DIR)

define Build/Configure
	$(call Build/Compile/Default,download)
	$(call Build/Compile/Default,untar)
	$(CP) ./config/v4l-dvb_config $(PKG_BUILD_DIR)/v4l/.config
endef

define Package/v4l-dvb/install
	$(INSTALL_DIR) $(1)/lib/firmware
	$(CP) $(PKG_INSTALL_DIR)/lib/firmware/* $(1)/lib/firmware/

	$(INSTALL_DIR) $(1)/lib/modules
	$(CP) $(PKG_INSTALL_DIR)/lib/modules/* $(1)/lib/modules/
endef

$(eval $(call BuildPackage,v4l-dvb))
