#
# Copyright (C) 2011 OpenWrt.org
#
# This is free software, licensed under the GNU General Public License v2.
# See /LICENSE for more information.
#

include $(TOPDIR)/rules.mk

PKG_NAME:=libssh
PKG_VERSION:=0.4.8

PKG_SOURCE:=$(PKG_NAME)-$(PKG_VERSION).tar.gz
PKG_SOURCE_URL:=http://www.libssh.org/files/0.4/
PKG_MD5SUM:=d97b3feea1abe047ca8cf86d06e4b789

PKG_INSTALL=1

include $(INCLUDE_DIR)/package.mk
include $(INCLUDE_DIR)/cmake.mk

define Package/libssh
  SECTION:=libs
  CATEGORY:=Libraries
  TITLE:=SSH libraryrm -rf 
  URL:=http://www.libssh.org/
  DEPENDS:=+libopenssl +zlib
endef

define Package/libssh/description
    libssh is a mulitplatform C library implementing the SSHv2 and SSHv1 protocol on client and server side. 
	With libssh, you can remotely execute programs, transfer files, use a secure and transparent tunnel for 
	your remote applications.
endef

MAKE_PATH:=build

CMAKE_OPTIONS += \
				..

define Build/Configure
	mkdir $(PKG_BUILD_DIR)/build; \
	$(call Build/Configure/Default, )
endef

define Build/InstallDev
	$(INSTALL_DIR) $(1)/usr/include
	$(CP) $(PKG_INSTALL_DIR)/usr/include/* $(1)/usr/include
	
	$(INSTALL_DIR) $(1)/usr/lib
	$(CP) $(PKG_INSTALL_DIR)/usr/lib/libssh.so* $(1)/usr/lib	
endef

define Package/libssh/install
	$(INSTALL_DIR) $(1)/usr/lib
	$(CP) $(PKG_INSTALL_DIR)/usr/lib/libssh.so* $(1)/usr/lib
endef
        
$(eval $(call BuildPackage,libssh))
