#
# Copyright (C) 2011 OpenWrt.org
#
# This is free software, licensed under the GNU General Public License v2.
# See /LICENSE for more information.
#

include $(TOPDIR)/rules.mk

PKG_NAME:=SDL_ttf
PKG_VERSION:=2.0.10

PKG_SOURCE:=$(PKG_NAME)-$(PKG_VERSION).tar.gz
PKG_SOURCE_URL:=http://www.libsdl.org/projects/$(PKG_NAME)/release/
PKG_MD5SUM:=814e6e17e8879254208d23b3b7e0354b

PKG_INSTALL=1

include $(INCLUDE_DIR)/package.mk

define Package/libsdl-ttf
  SECTION:=libs
  CATEGORY:=Libraries
  TITLE:=Simple DirectMedia Layer True Type Fony library
  DEPENDS:=+libsdl +libICE +libX11 +libfreetype +libgl-mesa
  URL:=http://www.libsdl.org/projects/SDL_ttf/
endef

define Package/libsdl-ttf/description
  This library allows you to use TrueType fonts to render text in SDL applications.
endef

TARGET_CFLAGS += \
	-I$(STAGING_DIR)/usr/include/SDL

TARGET_LDFLAGS += \
	-Wl,-rpath-link=$(STAGING_DIR)/usr/lib
	    
define Build/InstallDev
	$(INSTALL_DIR) $(1)/usr/include/SDL
	$(CP) $(PKG_INSTALL_DIR)/usr/include/SDL $(1)/usr/include/SDL/
	
	$(INSTALL_DIR) $(1)/usr/lib
	$(CP) $(PKG_INSTALL_DIR)/usr/lib/libSDL_ttf*.{la,so*} $(1)/usr/lib/
	
	$(INSTALL_DIR) $(1)/usr/lib/pkgconfig
	$(INSTALL_DATA) $(PKG_INSTALL_DIR)/usr/lib/pkgconfig/* $(1)/usr/lib/pkgconfig/
endef

define Package/libsdl-ttf/install
	$(INSTALL_DIR) $(1)/usr/lib
	$(CP) $(PKG_INSTALL_DIR)/usr/lib/*.so* $(1)/usr/lib
endef
        
$(eval $(call BuildPackage,libsdl-ttf))
