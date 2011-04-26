#
# Copyright (C) 2006-2010 OpenWrt.org
#
# This is free software, licensed under the GNU General Public License v2.
# See /LICENSE for more information.
#

include $(TOPDIR)/rules.mk

PKG_NAME:=tvheadend
PKG_REV:=90e35703b9f6fb81df16
PKG_VERSION:=20111704
PKG_RELEASE:=1

PKG_SOURCE_PROTO:=git
PKG_SOURCE_VERSION:=$(PKG_REV)
PKG_SOURCE_SUBDIR:=$(PKG_NAME)-$(PKG_VERSION)
PKG_SOURCE:=$(PKG_NAME)-$(PKG_REV).tar.bz2
PKG_SOURCE_URL:=https://github.com/andoma/tvheadend.git

include $(INCLUDE_DIR)/package.mk
include $(INCLUDE_DIR)/nls.mk

define Package/tvheadend
  SECTION:=multimedia
  CATEGORY:=Multimedia
  DEPENDS:=$(ICONV_DEPENDS) +libopenssl
  TITLE:=Tvheadend is a TV streaming server for Linux
  URL:=https://www.lonelycoder.com/hts/tvheadend_overview.html
endef

define Package/tvheadend/description
  Tvheadend is a TV streaming server for Linux supporting DVB-S, DVB-S2, DVB-C, DVB-T, ATSC, IPTV, and Analog video (V4L) as input sources.
  It also comes with a powerful and easy to use web interface both used for configuration and day-to-day operations,
  such as searching the EPG and scheduling recordings. 
  Even so, the most notable feature of Tvheadend is how easy it is to set up: Install it, navigate to the web user interface, 
  drill into the TV adapters tab, select your current location and Tvheadend will start scanning channels and present them to you in just 
  a few minutes
endef

define Package/tvheadend/config
  menu "Configuration"
  depends on PACKAGE_tvheadend
  source "$(SOURCE)/Config.in"
  endmenu
endef

ifeq ($(CONFIG_TVHEADEND_AVAHI_SUPPORT),)
  CONFIGURE_ARGS+= --disable-avahi
endif

CONFIGURE_ARGS += \
		--release

TARGET_LDFLAGS += \
		-Wl,-rpath-link=$(STAGING_DIR)/usr/lib \
		-liconv
				
define Package/tvheadend/install
	$(INSTALL_DIR) $(1)/etc/init.d
	$(INSTALL_BIN) ./files/tvheadend.init $(1)/etc/init.d/tvheadend

	$(INSTALL_DIR) $(1)/usr/bin
	$(INSTALL_BIN) $(PKG_BUILD_DIR)/build.Linux/tvheadend $(1)/usr/bin/
endef

$(eval $(call BuildPackage,tvheadend))