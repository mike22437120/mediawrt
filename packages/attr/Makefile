#
# Copyright (C) 2011 OpenWrt.org
#
# This is free software, licensed under the GNU General Public License v2.
# See /LICENSE for more information.
#

include $(TOPDIR)/rules.mk

PKG_NAME:=attr
PKG_VERSION:=2.4.44
PKG_RELEASE:=1

PKG_SOURCE:=$(PKG_NAME)-$(PKG_VERSION).src.tar.gz
PKG_SOURCE_URL:=http://mirror.its.uidaho.edu/pub/savannah/attr/
PKG_MD5SUM:=d132c119831c27350e10b9f885711adc

PKG_INSTALL:=1

include $(INCLUDE_DIR)/package.mk
include $(INCLUDE_DIR)/nls.mk

define Package/attr
  SECTION:=libs
  CATEGORY:=Libraries
  TITLE:=Filesystem Extended Attributes
  DEPENDS:=$(ICONV_DEPENDS) $(INTL_DEPENDS)
  URL:=
endef

define Package/attr/description
  The extended attribute system calls and library functions.
endef

define Build/InstallDev
	$(INSTALL_DIR) $(1)/usr/include/attr $(1)/usr/lib
	$(CP) $(PKG_BUILD_DIR)/libattr/.libs/libattr.{la,a,so*} $(1)/usr/lib
	$(CP) $(PKG_BUILD_DIR)/include/{attributes,xattr,libattr}.h $(1)/usr/include/attr
endef	 

define Package/attr/install
	$(INSTALL_DIR) $(1)/usr/bin
	$(CP) $(PKG_INSTALL_DIR)/usr/bin/$(PKG_NAME) $(1)/usr/bin/
endef

$(eval $(call BuildPackage,attr))
