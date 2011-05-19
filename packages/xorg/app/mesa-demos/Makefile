#
# Copyright (C) 2011 OpenWrt.org
#
# This is free software, licensed under the GNU General Public License v2.
# See /LICENSE for more information.
#

include $(TOPDIR)/rules.mk

PKG_NAME:=mesa-demos
PKG_VERSION:=8.0.1
PKG_RELEASE:=1

PKG_SOURCE_URL:=ftp://ftp.freedesktop.org/pub/mesa/demos/$(PKG_VERSION)
PKG_SOURCE:=$(PKG_NAME)-$(PKG_VERSION).tar.bz2
PKG_BUILD_DIR:=$(BUILD_DIR)/Xorg/$(PKG_NAME)-$(PKG_VERSION)/
PKG_MD5SUM:=320c2a4b6edc6faba35d9cb1e2a30bf4

PKG_FIXUP:=autoreconf
PKG_INSTALL:=1

include $(INCLUDE_DIR)/package.mk

define Package/mesa-demos
  SECTION:=xorg-app
  CATEGORY:=Xorg
  SUBMENU:=app
  TITLE:=Mesa Demos
  DEPENDS:=+libX11 +libgl-mesa +glew
  URL:=http://www.mesa3d.org/
endef

define Package/mesa-demos/description
  Mesa's OpenGL utility and demo programs (glxgears and glxinfo)
endef

TARGET_LDFLAGS += \
		-Wl,-rpath-link=$(STAGING_DIR)/usr/lib

TARGET_CONFIGURE_OPTS += \
	GLU_CFLAGS="-I$(STAGING_DIR)/usr/include" \
	GLU_LIBS="-lGLU" \
	GL_CFLAGS="-I$(STAGING_DIR)/usr/include" \
	GL_LIBS="-lGL"

define Package/mesa-demos/install
	$(INSTALL_DIR) $(1)/usr/bin
	$(CP) $(PKG_INSTALL_DIR)/usr/bin/glxdemo $(1)/usr/bin/
	$(CP) $(PKG_INSTALL_DIR)/usr/bin/glxgears $(1)/usr/bin/
	$(CP) $(PKG_INSTALL_DIR)/usr/bin/glxinfo $(1)/usr/bin/
endef

$(eval $(call BuildPackage,mesa-demos))
