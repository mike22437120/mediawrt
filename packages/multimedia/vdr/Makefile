#
# Copyright (C) 2011 OpenWrt.org
#
# This is free software, licensed under the GNU General Public License v2.
# See /LICENSE for more information.
#

include $(TOPDIR)/rules.mk

PKG_NAME:=vdr
PKG_VERSION:=1.7.17
PKG_RELEASE:=1

PKG_SOURCE:=vdr-$(PKG_VERSION).tar.bz2
PKG_SOURCE_URL:=ftp://ftp.tvdr.de/vdr/Developer
PKG_MD5SUM:=c53a9505b891414e36f7bccad3bd1235

PKG_INSTALL:=1

include $(INCLUDE_DIR)/package.mk
include $(INCLUDE_DIR)/nls.mk

PKG_BUILD_DEPENDS:= \
		vdr-plugin-femon \
		vdr-plugin-sc \
		vdr-plugin-vnsiserver

plugin-y :=
plugin-$(CONFIG_PACKAGE_vdr-plugin-femon) += femon
plugin-$(CONFIG_PACKAGE_vdr-plugin-sc) += sc
plugin-$(CONFIG_PACKAGE_vdr-plugin-vnsiserver) += vnsiserver
		
define Package/vdr
  SECTION:=multimedia
  CATEGORY:=Multimedia
  DEPENDS:=+@BUILD_NLS +libfreetype +fontconfig +dejavu-fonts-ttf +libjpeg +libcap +libncurses +libncursesw +librt $(ICONV_DEPENDS) $(INTL_DEPENDS) +libstdcpp
  TITLE:=Video Disk Recorder
  URL:=http://www.tvdr.de/
  MENU:=1
endef

define Package/vdr/description
  Video Disk Recorder (VDR) is a digital sat-receiver program using Linux and DVB technologies. 
  It allows one to record MPEG2 streams, as well as output the stream to TV. 
  It is also possible to watch DVDs (hardware accelerated) with some comfort and use an IR remote control.
endef

TARGET_LDFLAGS += \
		-Wl,-rpath-link=$(STAGING_DIR)/usr/lib \
		-lintl \
		-liconv

EXTRA_CFLAGS += \
		-I$(STAGING_DIR)/usr/include/freetype2 \
		-fPIC
		
MAKE_FLAGS += \
		VDRDIR=$(PKG_BUILD_DIR) \
		LIBDIR=$(PKG_BUILD_DIR)/PLUGINS/lib \
		PLUGINLIBDIR=/usr/lib/vdr/plugins \
		LOCDIR=/usr/share/vdr/locale \
		VIDEODIR=/media/video \
		CONFDIR=/etc/config/vdr

define Build/Configure
	$(call Build/Configure/Default,)
	
	#make symlink to plugins
	for tmp in $(plugin-y); do \
		ln -s $(BUILD_DIR)/$$$$tmp-* $(PKG_BUILD_DIR)/PLUGINS/src/$$$$tmp; \
	done
endef		
		
		
define Package/vdr/install
	$(INSTALL_DIR) $(1)/etc/init.d
	$(INSTALL_BIN) ./files/vdr.init $(1)/etc/init.d/vdr

	$(INSTALL_DIR) $(1)/etc/config/vdr/
	for tmp in $(plugin-y); do \
		echo $$$$tmp >> $(1)/etc/config/vdr/plugins.conf ; \
	done	
	
	$(INSTALL_DIR) $(1)/usr/bin
	$(INSTALL_BIN) ./files/runvdr $(1)/usr/bin/
	$(INSTALL_BIN) $(PKG_INSTALL_DIR)/usr/local/bin/vdr $(1)/usr/bin/
	
	$(INSTALL_DIR) $(1)/usr/lib/vdr/plugins
	$(CP) $(PKG_INSTALL_DIR)/usr/lib/vdr/plugins/* $(1)/usr/lib/vdr/plugins/

	$(INSTALL_DIR) $(1)/usr/share/vdr/locale
	$(CP) $(PKG_INSTALL_DIR)/usr/share/vdr/locale/* $(1)/usr/share/vdr/locale/
endef

$(eval $(call BuildPackage,vdr))
