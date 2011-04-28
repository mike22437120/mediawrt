#
# Copyright (C) 2011 OpenWrt.org
#
# This is free software, licensed under the GNU General Public License v2.
# See /LICENSE for more information.
#

include $(TOPDIR)/rules.mk

PKG_NAME:=wavpack
PKG_VERSION:=4.60.1

PKG_SOURCE:=$(PKG_NAME)-$(PKG_VERSION).tar.bz2
PKG_SOURCE_URL:=http://www.wavpack.com/
PKG_MD5SUM:=7bb1528f910e4d0003426c02db856063

PKG_INSTALL=1

include $(INCLUDE_DIR)/package.mk
include $(INCLUDE_DIR)/nls.mk

define Package/wavpack
  SECTION:=sound
  CATEGORY:=Sound
  TITLE:=WavPack Audio Compression
  URL:=http://www.wavpack.com/
  DEPENDS:=$(ICONV_DEPENDS)
endef

define Package/wavpack/description
  WavPack is a completely open audio compression format providing lossless, high-quality lossy, 
  and a unique hybrid compression mode. Although the technology is loosely based on previous versions of WavPack, 
  the new version 4 format has been designed from the ground up to offer unparalleled performance and functionality.
endef

TARGET_LDFLAGS += \
		-liconv

define Build/InstallDev
	$(INSTALL_DIR) $(1)/usr/include/wavpack
	$(INSTALL_DATA) $(PKG_INSTALL_DIR)/usr/include/wavpack/* $(1)/usr/include/wavpack
	
	$(INSTALL_DIR) $(1)/usr/lib/
	$(CP) $(PKG_INSTALL_DIR)/usr/lib/libwavpack.{so*,la} $(1)/usr/lib/
	
	$(INSTALL_DIR) $(1)/usr/lib/pkgconfig/
	$(INSTALL_DATA) $(PKG_INSTALL_DIR)/usr/lib/pkgconfig/* $(1)/usr/lib/pkgconfig/
endef
	
define Package/wavpack/install
	$(INSTALL_DIR) $(1)/usr/lib
	$(CP) $(PKG_INSTALL_DIR)/usr/lib/libwavpack.so* $(1)/usr/lib
endef
        
$(eval $(call BuildPackage,wavpack))
