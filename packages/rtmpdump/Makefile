#
# Copyright (C) 2011 OpenWrt.org
#
# This is free software, licensed under the GNU General Public License v2.
# See /LICENSE for more information.
#

include $(TOPDIR)/rules.mk

PKG_NAME:=rtmpdump
PKG_VERSION:=2.3

PKG_SOURCE:=$(PKG_NAME)-$(PKG_VERSION).tgz
PKG_SOURCE_URL:=http://rtmpdump.mplayerhq.hu/download/
PKG_MD5SUM:=eb961f31cd55f0acf5aad1a7b900ef59

PKG_INSTALL=1

include $(INCLUDE_DIR)/package.mk

define Package/rtmpdump
  SECTION:=utils
  CATEGORY:=Utilities
  TITLE:=RTMP streaming media client
  URL:=http://rtmpdump.mplayerhq.hu/
  DEPENDS:=+zlib +libopenssl
endef

define Package/rtmpdump/description
  RTMPdump is a tool for dumping media content streamed over RTMP.
endef

MAKE_FLAGS += \
	INC="$(TARGET_CPPFLAGS)" \
	XLDFLAGS="$(TARGET_LDFLAGS)"

define Build/InstallDev
	$(INSTALL_DIR) $(1)/usr/local/include/
	$(CP) $(PKG_INSTALL_DIR)/usr/local/include/ $(1)/usr/include/
	
	$(INSTALL_DIR) $(1)/usr/lib/
	$(CP) $(PKG_INSTALL_DIR)/usr/local/lib/librtmp.so* $(1)/usr/lib/
	
	$(INSTALL_DIR) $(1)/usr/lib/pkgconfig/
	$(CP) $(PKG_INSTALL_DIR)/usr/local/lib/pkgconfig/* $(1)/usr/lib/pkgconfig/
endef

define Package/rtmpdump/install
	$(INSTALL_DIR) $(1)/usr/lib
	$(CP) $(PKG_INSTALL_DIR)/usr/local/lib/librtmp.so* $(1)/usr/lib
endef
        
$(eval $(call BuildPackage,rtmpdump))
