#
# Copyright (C) 2011 OpenWrt.org
#
# This is free software, licensed under the GNU General Public License v2.
# See /LICENSE for more information.
#

include $(TOPDIR)/rules.mk

PKG_NAME:=SDL_image
PKG_VERSION:=1.2.10

PKG_SOURCE:=$(PKG_NAME)-$(PKG_VERSION).tar.gz
PKG_SOURCE_URL:=http://www.libsdl.org/projects/$(PKG_NAME)/release/
PKG_MD5SUM:=6c06584b31559e2b59f2b982d0d1f628

PKG_INSTALL=1

include $(INCLUDE_DIR)/package.mk

define Package/libsdl-image
  SECTION:=libs
  CATEGORY:=Libraries
  TITLE:=SDL_image is an image file loading library
  URL:=http://www.libsdl.org/projects/SDL_image/
  DEPENDS:=+libsdl +libjpeg +libpng +libtiff
endef

define Package/libsdl-image/description
  SDL_image is an image loading library that is used with the SDL library, and almost as portable. 
  It allows a programmer to use multiple image formats without having to code all the loading and conversion algorithms themselves.
endef

CONFIGURE_ARGS+= \
	--enable-bmp \
	--enable-gif \
	--enable-jpg \
	--enable-jpg-shared \
	--disable-lbm \
	--enable-pcx \
	--enable-png \
	--enable-png-shared \
	--enable-pnm \
	--enable-tga \
	--enable-tif \
	--enable-tif-shared \
	--enable-xcf \
	--enable-xpm \
	--enable-xv \

TARGET_CFLAGS += \
		-I$(STAGING_DIR)/usr/include/SDL

TARGET_LDFLAGS += \
		-Wl,-rpath-link=$(STAGING_DIR)/usr/lib

define Build/InstallDev
	$(INSTALL_DIR) $(1)/usr/include/SDL
	$(CP) $(PKG_INSTALL_DIR)/usr/include/SDL/SDL_image.h $(1)/usr/include/SDL/
	
	$(INSTALL_DIR) $(1)/usr/lib
	$(CP) $(PKG_INSTALL_DIR)/usr/lib/libSDL_image*.{la,so*} $(1)/usr/lib/
	
	$(INSTALL_DIR) $(1)/usr/lib/pkgconfig
	$(INSTALL_DATA) $(PKG_INSTALL_DIR)/usr/lib/pkgconfig/* $(1)/usr/lib/pkgconfig/
endef

define Package/libsdl-image/install
	$(INSTALL_DIR) $(1)/usr/lib
	$(CP) $(PKG_INSTALL_DIR)/usr/lib/*.so* $(1)/usr/lib
endef
        
$(eval $(call BuildPackage,libsdl-image))
