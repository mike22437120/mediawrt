#
# Copyright (C) 2011 OpenWrt.org
#
# This is free software, licensed under the GNU General Public License v2.
# See /LICENSE for more information.
#

include $(TOPDIR)/rules.mk

PKG_NAME:=enca
PKG_VERSION:=1.13

PKG_SOURCE:=$(PKG_NAME)-$(PKG_VERSION).tar.bz2
PKG_SOURCE_URL:=http://dl.cihar.com/enca/
PKG_MD5SUM:=762bead5d9a0a5e55024e1102baaa89d

PKG_INSTALL=1

include $(INCLUDE_DIR)/package.mk

define Package/enca
  SECTION:=libs
  CATEGORY:=Libraries
  TITLE:=Extremely Naive Charset Analyser
  URL:=http://freshmeat.net/projects/enca/
endef

define Package/enca/description
  Enca is an Extremely Naive Charset Analyser. It detects character set and 
  encoding of text files and can also convert them to other encodings.
endef

TARGET_CFLAGS+= \
		--std=c99

CONFIGURE_VARS+= \
	ac_cv_file__dev_random=yes \
	ac_cv_file__dev_urandom=no \
	ac_cv_file__dev_srandom=no \
	ac_cv_file__dev_arandom=no \

define Build/Compile
	$(MAKE) -C $(PKG_BUILD_DIR)/tools \
		CC="$(HOSTCC)" \
		CPPFLAGS="$(HOST_CPPFLAGS)" \
		CFLAGS="$(HOST_CFLAGS)" \
		LDFLAGS="$(HOST_LDFLAGS)";

	$(call Build/Compile/Default, )
endef

define Build/InstallDev
	$(INSTALL_DIR) $(1)/usr/include/
	$(CP) $(PKG_INSTALL_DIR)/usr/include/* $(1)/usr/include/

	$(INSTALL_DIR) $(1)/usr/lib
	$(CP) $(PKG_INSTALL_DIR)/usr/lib/libenca.{la,a,so*} $(1)/usr/lib/
	
	$(INSTALL_DIR) $(1)/usr/lib/pkgconfig
	$(INSTALL_DATA) $(PKG_INSTALL_DIR)/usr/lib/pkgconfig/enca.pc $(1)/usr/lib/pkgconfig/
endef

define Package/enca/install
	$(INSTALL_DIR) $(1)/usr/lib
	$(CP) $(PKG_BUILD_DIR)/lib/.libs/*.so* $(1)/usr/lib
endef
        
$(eval $(call BuildPackage,enca))
