#
# Copyright (C) 2011 OpenWrt.org
#
# This is free software, licensed under the GNU General Public License v2.
# See /LICENSE for more information.
#

include $(TOPDIR)/rules.mk

PKG_NAME:=vdr-plugin-vnsiserver
PKG_REV:=35744
PKG_VERSION:=r$(PKG_REV)
PKG_RELEASE:=1

PKG_SOURCE_PROTO:=svn
PKG_SOURCE_VERSION:=$(PKG_REV)
PKG_SOURCE_SUBDIR:=vnsiserver-$(PKG_VERSION)
PKG_SOURCE:=vnsiserver-$(PKG_VERSION).tar.bz2
PKG_SOURCE_URL:=https://xbmc.svn.sourceforge.net/svnroot/xbmc/branches/pvr-testing2/xbmc/pvrclients/vdr-vnsi/vdr-plugin-vnsiserver/
PKG_BUILD_DIR:=$(BUILD_DIR)/vnsiserver-$(PKG_VERSION)

include $(INCLUDE_DIR)/package.mk

define Package/vdr-plugin-vnsiserver
  SECTION:=multimedia
  CATEGORY:=Multimedia
  TITLE:=VDR Network Streaming Interface
  DEPENDS:=vdr
  URL:=http://www.vdr-portal.de/board/thread.php?threadid=95292
endef

define Package/vdr-plugin-vnsiserver/description
  A VNSI server for VDR, allowing the use of VDR via VNSI PVR addon of XBMC.
endef

define Build/Compile
endef

define Build/Install
endef

define Package/vdr-plugin-vnsiserver/install
	$(INSTALL_DIR) $(1)/etc/config/vdr/plugins/vnsiserver
	$(CP) $(PKG_BUILD_DIR)/vnsiserver/* $(1)/etc/config/vdr/plugins/vnsiserver/
endef

$(eval $(call BuildPackage,vdr-plugin-vnsiserver))
