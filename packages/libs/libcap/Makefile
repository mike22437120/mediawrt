#
# Copyright (C) 2011 OpenWrt.org
#
# This is free software, licensed under the GNU General Public License v2.
# See /LICENSE for more information.
#

include $(TOPDIR)/rules.mk

PKG_NAME:=libcap
PKG_VERSION:=2.20
PKG_RELEASE:=1

PKG_SOURCE:=$(PKG_NAME)-$(PKG_VERSION).tar.bz2
PKG_SOURCE_URL:=http://www.kernel.org/pub/linux/libs/security/linux-privs/libcap2/
PKG_MD5SUM:=10e47ed32ca2214eb0e58780282d27b4

PKG_INSTALL:=1

include $(INCLUDE_DIR)/package.mk

define Package/libcap
  SECTION:=libs
  CATEGORY:=Libraries
  TITLE:=POSIX 1003.1e capabilities
  URL:=http://www.kernel.org/pub/linux/libs/security/linux-privs/libcap2/
endef

HOST_CFLAGS += \
	-I$(PKG_BUILD_DIR)/libcap/include

TARGET_LDFLAGS += \
		-Wl,-rpath-link=$(STAGING_DIR)/usr/lib

MAKE_VARS = \
	
MAKE_FLAGS = \
	BUILD_CC="$(HOSTCC)" \
	BUILD_CFLAGS="$(HOST_CFLAGS)" \
	CC="$(TARGET_CC)" \
	LDFLAGS="$(TARGET_LDFLAGS)" \
	RAISE_SETFCAP=no \
	LIBATTR=no

define Build/InstallDev
	$(INSTALL_DIR) $(1)/usr/include/sys
	$(INSTALL_BIN) $(PKG_INSTALL_DIR)/usr/include/sys/capability.h $(1)/usr/include/sys/

	$(INSTALL_DIR) $(1)/usr/lib
	$(INSTALL_BIN) $(PKG_BUILD_DIR)/libcap/libcap.{a,so*} $(1)/usr/lib/
endef

define Package/libcap/install
	$(INSTALL_DIR) $(1)/usr/lib
	$(CP) $(PKG_BUILD_DIR)/libcap/libcap.so.* $(1)/usr/lib/
endef


$(eval $(call BuildPackage,libcap))
