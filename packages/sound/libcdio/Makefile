#
# Copyright (C) 2011 OpenWrt.org
#
# This is free software, licensed under the GNU General Public License v2.
# See /LICENSE for more information.
#

include $(TOPDIR)/rules.mk

PKG_NAME:=libcdio
PKG_VERSION:=0.82

PKG_SOURCE:=$(PKG_NAME)-$(PKG_VERSION).tar.bz2
PKG_SOURCE_URL:=@GNU/$(PKG_NAME)/
PKG_MD5SUM:=988a3923254c2c7d3fd89f8586f580d2

PKG_INSTALL=1

include $(INCLUDE_DIR)/package.mk
include $(INCLUDE_DIR)/nls.mk

define Package/libcdio
  SECTION:=sound
  CATEGORY:=Sound
  TITLE:=Compact Disc Input and Control library
  URL:=http://www.gnu.org/software/libcdio/
  DEPENDS:=$(ICONV_DEPENDS)
endef

define Package/libcdio/description
  The GNU Compact Disc Input and Control library (libcdio) contains a library for CD-ROM and CD image access. 
  Applications wishing to be oblivious of the OS- and device-dependent properties of a CD-ROM or of the specific 
  details of various CD-image formats may benefit from using this library.
endef

define Build/InstallDev
	$(INSTALL_DIR) $(1)/usr/include
	$(CP) $(PKG_INSTALL_DIR)/usr/include/* $(1)/usr/include/

	$(INSTALL_DIR) $(1)/usr/lib
	$(CP) $(PKG_INSTALL_DIR)/usr/lib/libcdio.{a,so*} $(1)/usr/lib/
	
	$(INSTALL_DIR) $(1)/usr/lib/pkgconfig
	$(CP) $(PKG_BUILD_DIR)/*.pc $(1)/usr/lib/pkgconfig/
endef
	
define Package/libcdio/install
	$(INSTALL_DIR) $(1)/usr/lib
	$(CP) $(PKG_INSTALL_DIR)/usr/lib/libcdio*so* $(1)/usr/lib
endef
        
$(eval $(call BuildPackage,libcdio))
