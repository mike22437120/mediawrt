#
# Copyright (C) 2008-2010 OpenWrt.org
#
# This is free software, licensed under the GNU General Public License v2.
# See /LICENSE for more information.

include $(TOPDIR)/rules.mk

PKG_NAME:=samba4
PKG_VERSION:=3.5.8
PKG_RELEASE:=7

PKG_SOURCE_URL:=ftp://ftp.easynet.be/samba/stable
PKG_SOURCE:=samba-$(PKG_VERSION).tar.gz
PKG_BUILD_DIR:=$(BUILD_DIR)/samba-$(PKG_VERSION)/
PKG_MD5SUM:=355b4530c20997e94aebc74cd6ea5307

include $(INCLUDE_DIR)/package.mk

define Package/samba4
	SECTION:=net
	CATEGORY:=Network
	SUBMENU:=samba4 - NetBIOS/SMB implementation
	TITLE:=samba - NetBIOS/SMB implementation
	URL:=http://www.samba.org/
endef

define Package/samba4/Description
	The Samba software suite is a collection of programs that implements the \
	SMB protocol for unix systems, allowing you to serve files and printers to \
	Windows, NT, OS/2 and DOS clients. This protocol is sometimes also referred \
	to as the LanManager or Netbios protocol.
endef

define Package/samba4-common
	$(call Package/samba4)
	TITLE:=NetBIOS/SMB server and client shared files
	DEPENDS:=+libgcc
endef

define Package/samba4-server
	$(call Package/samba4)
	TITLE:=NetBIOS/SMB file and print server
	DEPENDS:=samba4-common
endef

define Package/samba4-client
	$(call Package/samba4)
	TITLE:=NetBIOS/SMB simple client
	DEPENDS:=samba4-common
endef

define Package/samba4-smbmount
	$(call Package/samba4)
	TITLE:=NetBIOS/SMB old smbmount
	DEPENDS:=kmod-fs-smbfs
endef

define Package/samba4-cifsmount
	$(call Package/samba4)
	TITLE:=NetBIOS/SMB new cifsmount
	DEPENDS:=kmod-fs-cifs
endef

define Package/samba4-libs
	$(call Package/samba4)
	TITLE:=NetBIOS/SMB libraries for client programs
	DEPENDS:=+libgcc
endef

define Package/samba4-scan
	$(call Package/samba4)
	TITLE:=Automount for samba shares
	DEPENDS:=+nmap +samba4-common +samba4-client
endef

CONFIGURE_VARS+= \
	samba_cv_HAVE_GETTIMEOFDAY_TZ=yes \
	samba_cv_USE_SETREUID=yes \
	samba_cv_HAVE_KERNEL_OPLOCKS_LINUX=yes \
	samba_cv_HAVE_KERNEL_OPLOCKS_LINUX=no \
	samba_cv_HAVE_IFACE_IFCONF=yes \
	samba_cv_CC_NEGATIVE_ENUM_VALUES=yes \
	SMB_BUILD_CC_NEGATIVE_ENUM_VALUES=yes \
	libreplace_cv_READDIR_GETDIRENTRIES=no \
	libreplace_cv_READDIR_GETDENTS=no \
	linux_getgrouplist_ok=no \
	samba_cv_REPLACE_READDIR=no \
	samba_cv_HAVE_WRFILE_KEYTAB=no \

CONFIGURE_ARGS+= \
	--with-lockdir=/var/cache/samba \
	--with-piddir=/var/run \
	--with-privatedir=/etc/samba \
	--with-logfilebase=/var/log/samba \
	--with-configdir=/etc/samba \
	--with-cifsmount \
	--without-libaddns \
	--with-included-popt \
	--with-included-iniparser \
	--disable-cups \
	--disable-static \

MAKE_PATH:=source3
CONFIGURE_PATH:=source3

define Build/Configure
	cd $(PKG_BUILD_DIR)/$(MAKE_PATH); \
	rm -rf config.{cache,status}; \
	./autogen.sh; \
	$(call Build/Configure/Default, )
endef	

define Build/InstallDev
	$(INSTALL_DIR) $(1)/usr/include
	$(CP) $(PKG_BUILD_DIR)/source3/include/libsmbclient.h  $(1)/usr/include

	$(INSTALL_DIR) $(1)/usr/lib
	$(CP) $(PKG_BUILD_DIR)/source3/bin/libtalloc.so* $(1)/usr/lib
	$(CP) $(PKG_BUILD_DIR)/source3/bin/libtdb.so* $(1)/usr/lib
	$(CP) $(PKG_BUILD_DIR)/source3/bin/libwbclient.so* $(1)/usr/lib
	$(CP) $(PKG_BUILD_DIR)/source3/bin/libsmbclient.so* $(1)/usr/lib
	$(CP) $(PKG_BUILD_DIR)/source3/bin/libsmbsharemodes.so* $(1)/usr/lib
endef

define Package/samba4-common/install
	$(INSTALL_DIR) $(1)/etc/samba
	$(INSTALL_DATA) ./files/smb.conf.template $(1)/etc/samba/
	cd $(1)/etc/samba; rm -r smb.conf; ln -s /tmp/smb.conf
endef

define Package/samba4-libs/install
	$(INSTALL_DIR) $(1)/usr/lib
	$(INSTALL_BIN) $(PKG_BUILD_DIR)/source3/bin/libtalloc.so $(1)/usr/lib/libtalloc.so.1
	$(INSTALL_BIN) $(PKG_BUILD_DIR)/source3/bin/libtdb.so $(1)/usr/lib/libtdb.so.1
	$(INSTALL_BIN) $(PKG_BUILD_DIR)/source3/bin/libwbclient.so $(1)/usr/lib/libwbclient.so.0
	$(INSTALL_BIN) $(PKG_BUILD_DIR)/source3/bin/libsmbclient.so* $(1)/usr/lib
	$(INSTALL_BIN) $(PKG_BUILD_DIR)/source3/bin/libsmbsharemodes.so $(1)/usr/lib
endef

define Package/samba4-server/install
	$(INSTALL_DIR) $(1)/etc/init.d
	$(INSTALL_BIN) ./files/samba.init $(1)/etc/init.d/samba
	$(INSTALL_DIR) $(1)/usr/bin
	$(INSTALL_BIN) $(PKG_BUILD_DIR)/source3/bin/smbpasswd $(1)/usr/bin/smbpasswd
	$(INSTALL_DIR) $(1)/usr/sbin
	$(INSTALL_BIN) $(PKG_BUILD_DIR)/source3/bin/nmbd $(1)/usr/sbin/nmbd
	$(INSTALL_BIN) $(PKG_BUILD_DIR)/source3/bin/smbd $(1)/usr/sbin/smbd
endef

define Package/samba4-client/install
	$(INSTALL_DIR) $(1)/usr/bin
	$(INSTALL_BIN) $(PKG_BUILD_DIR)/source3/bin/smbclient $(1)/usr/bin
	$(INSTALL_BIN) $(PKG_BUILD_DIR)/source3/bin/nmblookup $(1)/usr/bin
endef

define Package/samba4-smbmount/install
	$(INSTALL_DIR) $(1)/usr/bin
	#$(INSTALL_BIN) $(PKG_BUILD_DIR)/source3/bin/usr/bin/smbmount $(1)/usr/bin
	#$(INSTALL_BIN) $(PKG_BUILD_DIR)/source3/bin/usr/bin/smbmnt $(1)/usr/bin
endef

define Package/samba4-cifsmount/install
	$(INSTALL_DIR) $(1)/usr/bin
	$(INSTALL_BIN) $(PKG_BUILD_DIR)/source3/bin/mount.cifs $(1)/usr/bin
endef

define Package/samba4-scan/install
	$(INSTALL_DIR) $(1)/usr/bin
	$(INSTALL_BIN) ./files/scan $(1)/usr/bin
	$(INSTALL_BIN) ./files/unscan $(1)/usr/bin
endef

$(eval $(call BuildPackage,samba4-common))
$(eval $(call BuildPackage,samba4-server))
$(eval $(call BuildPackage,samba4-client))
$(eval $(call BuildPackage,samba4-libs))
$(eval $(call BuildPackage,samba4-smbmount))
$(eval $(call BuildPackage,samba4-cifsmount))
$(eval $(call BuildPackage,samba4-scan))

