#
# Copyright (C) 2011 OpenWrt.org
#
# This is free software, licensed under the GNU General Public License v2.
# See /LICENSE for more information.
#
include $(TOPDIR)/rules.mk

PKG_NAME:=glew
PKG_VERSION:=1.5.8

PKG_SOURCE:=$(PKG_NAME)-$(PKG_VERSION).tgz
PKG_SOURCE_URL:=@SF/$(PKG_NAME)/
PKG_MD5SUM:=342c8dc64fb9daa6af245b132e086bdd

include $(INCLUDE_DIR)/package.mk

define Package/glew
  SECTION:=libs
  CATEGORY:=Libraries
  TITLE:=OpenGL Extension Wrangler Library
  URL:=http://glew.sourceforge.net/
  DEPENDS:=+libX11 +libXext +libXi +libXmu +libgl-mesa
endef

define Package/glew/description
  The OpenGL Extension Wrangler Library (GLEW) is a cross-platform open-source C/C++ extension loading library. 
  GLEW provides efficient run-time mechanisms for determining which OpenGL extensions are supported on the target platform. 
  OpenGL core and extension functionality is exposed in a single header file. 
endef

TARGET_CONFIGURE_OPTS += \
	SYSTEM=linux \
	LD="$(TARGET_CC)" \
	CFLAGS.EXTRA="$(TARGET_CFLAGS) $(TARGET_CPPFLAGS)" \
	LDFLAGS.EXTRA="$(TARGET_LDFLAGS) -Wl,-rpath-link=$(STAGING_DIR)/usr/lib" \
	GLEW_DEST=$(STAGING_DIR)/usr
	
define Build/InstallDev
	$(INSTALL_DIR) $(1)/usr/include/GL
	$(CP) $(PKG_BUILD_DIR)/include/GL/*.h $(1)/usr/include/GL/
	
	$(INSTALL_DIR) $(1)/usr/lib
	$(CP) $(PKG_BUILD_DIR)/lib/libGLEW.{a,so*} $(1)/usr/lib/
	
	$(INSTALL_DIR) $(1)/usr/lib/pkgconfig
	$(INSTALL_DATA) $(PKG_BUILD_DIR)/glew.pc $(1)/usr/lib/pkgconfig/
endef

define Package/glew/install
	$(INSTALL_DIR) $(1)/usr/lib
	$(CP) $(PKG_BUILD_DIR)/lib/libGLEW.so* $(1)/usr/lib
endef
        
$(eval $(call BuildPackage,glew))
