#
# Copyright (C) 2011 OpenWrt.org
#
# This is free software, licensed under the GNU General Public License v2.
# See /LICENSE for more information.
#

include $(TOPDIR)/rules.mk

PKG_NAME:=SDL_net
PKG_VERSION:=1.2.7

PKG_SOURCE:=$(PKG_NAME)-$(PKG_VERSION).tar.gz
PKG_SOURCE_URL:=http://www.libsdl.org/projects/$(PKG_NAME)/release/
PKG_MD5SUM:=6bd4662d1423810f3140d4da21b6d912

PKG_INSTALL=1

include $(INCLUDE_DIR)/package.mk

define Package/libsdl-net
  SECTION:=libs
  CATEGORY:=Libraries
  TITLE:=A cross-platform networking library
  URL:=http://www.libsdl.org/projects/SDL_net/
  DEPENDS:=+libsdl
endef

define Package/libsdl-net/description
  This is a small sample cross-platform networking library, with a sample chat client and server application. 
  The chat client uses the GUIlib GUI framework library.
endef

CONFIGURE_ARGS+= \
	--disable-gui \
	--with-sdl-prefix="$(STAGING_DIR)/usr"

define Build/InstallDev
	$(INSTALL_DIR) $(1)/usr/include/SDL
	$(CP) $(PKG_INSTALL_DIR)/usr/include/SDL $(1)/usr/include/SDL/
	
	$(INSTALL_DIR) $(1)/usr/lib
	$(CP) $(PKG_INSTALL_DIR)/usr/lib/libSDL_net*.{la,so*} $(1)/usr/lib/
endef

define Package/libsdl_net/install
	$(INSTALL_DIR) $(1)/usr/lib
	$(CP) $(PKG_INSTALL_DIR)/usr/lib/*.so* $(1)/usr/lib
endef
        
$(eval $(call BuildPackage,libsdl-net))
