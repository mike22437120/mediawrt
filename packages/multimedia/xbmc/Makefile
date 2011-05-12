#
# Copyright (C) 2011 OpenWrt.org
#
# This is free software, licensed under the GNU General Public License v2.
# See /LICENSE for more information.
#

include $(TOPDIR)/rules.mk

PKG_NAME:=xbmc
PKG_VERSION:=20110510
PKG_REV:=922e218babbe2358aff4

PKG_SOURCE_PROTO:=git
PKG_SOURCE_VERSION:=$(PKG_REV)
PKG_SOURCE_SUBDIR:=$(PKG_NAME)-$(PKG_VERSION)
PKG_SOURCE_URL:=git://github.com/xbmc/xbmc.git
PKG_SOURCE:=$(PKG_SOURCE_SUBDIR).tar.bz2

PKG_INSTALL:=1

include $(INCLUDE_DIR)/package.mk
include $(INCLUDE_DIR)/nls.mk

define Package/xbmc
  SECTION:=multimedia
  CATEGORY:=Multimedia
  TITLE:=XBMC Mediacenter
  URL:=http://www.xbmc.org
  DEPENDS:= +boost +python +zlib +bzip2 +liblzo +libpcrecpp +alsa-lib +libass +enca +curl +dbus +libXt +libXtst +samba4-libs \
	   +libXmu +libXrandr +libglu-mesa +glew +fontconfig +fribidi +libjpeg +libpng +libtiff +libfreetype +jasper +libmad +libsamplerate \
	   +libogg +libvorbis +libcdio +libmms +libmodplug +faad2 +libflac +wavpack +libmpeg2 +libsdl +libsdl-mixer +libsdl-image \
	   +libsqlite3 +libmysqlclient +librt +libssh +libXinerama +libreadline +uclibcxx +libstdcpp\
	   $(ICONV_DEPENDS) $(INTL_DEPENDS) +@BUILD_NLS +@FEATURE_drawing-backend_libX11 @TARGET_x86
endef

define Package/xbmc/config
  menu "Configuration"
  depends on PACKAGE_xbmc
  source "$(SOURCE)/Config.in"
  endmenu
endef

define Package/xbmc/description
  XBMC Media Center (which was formerly named Xbox Media Center) is a free and open source cross-platform media player 
  and home entertainment system software with a 10-foot user interface designed for the living-room TV. 
  Its graphical user interface allows the user to easily manage video, photos, podcasts, and music from a computer, 
  optical disk, local network, and the internet using a remote control.
endef

EXTRA_CFLAGS+= \
	-I$(STAGING_DIR)/usr/include \

TARGET_LDFLAGS += \
	-L$(STAGING_DIR)/usr/lib \
	-Wl,-rpath-link=$(STAGING_DIR)/usr/lib

CONFIGURE_ARGS+= \
	--with-arch=$(ARCH) \
	--with-cpu=$(ARCH) \


ifneq ($(CONFIG_XBMC_AVAHI),)
CONFIGURE_ARGS+= --enable-avahi
else
CONFIGURE_ARGS+= --disable-avahi
endif	

ifneq ($(CONFIG_XBMC_BLURAY),)
CONFIGURE_ARGS+= --enable-libbluray
else
CONFIGURE_ARGS+= --disable-libbluray
endif

ifneq ($(CONFIG_XBMC_PULSEAUDIO),)
CONFIGURE_ARGS+= --enable-pulse
else
CONFIGURE_ARGS+= --disable-pulse
endif

ifneq ($(CONFIG_XBMC_NONFREE),)
CONFIGURE_ARGS+= --enable-non-free
else
CONFIGURE_ARGS+= --disable-non-free
endif

ifneq ($(CONFIG_XBMC_DVDCSS),)
CONFIGURE_ARGS+= --enable-dvdcss
else
CONFIGURE_ARGS+= --disable-dvdcss
endif

ifneq ($(CONFIG_XBMC_FAAC),)
CONFIGURE_ARGS+= --enable-faac
else
CONFIGURE_ARGS+= --disable-faac
endif

ifneq ($(CONFIG_XBMC_WEBSERVER),)
CONFIGURE_ARGS+= --enable-webserver
else
CONFIGURE_ARGS+= --disable-webserver
endif

ifneq ($(CONFIG_XBMC_VDPAU),)
CONFIGURE_ARGS+= --enable-vdpau
else
CONFIGURE_ARGS+= --disable-vdpau
endif

ifneq ($(CONFIG_XBMC_VAAPI),)
CONFIGURE_ARGS+= --enable-vaapi
else
CONFIGURE_ARGS+= --disable-vaapi
endif

ifneq ($(CONFIG_XBMC_RTMP),)
CONFIGURE_ARGS+= --enable-rtmp
else
CONFIGURE_ARGS+= --disable-rtmp
endif

ifneq ($(CONFIG_XBMC_CRYSTALHD),)
CONFIGURE_ARGS+= --enable-crystalhd
else
CONFIGURE_ARGS+= --disable-crystalhd
endif

ifneq ($(CONFIG_XBMC_HAL),)
CONFIGURE_ARGS+= --enable-hal
else
CONFIGURE_ARGS+= --disable-hal
endif

ifneq ($(CONFIG_XBMC_OPENGL),)
CONFIGURE_ARGS+= --enable-gl
else
CONFIGURE_ARGS+= --disable-gl
endif

ifneq ($(CONFIG_XBMC_XRANDR),)
CONFIGURE_ARGS+= --enable-xrandr
else
CONFIGURE_ARGS+= --disable-xrandr
endif

define Build/Configure
	(cd $(PKG_BUILD_DIR); \
		./bootstrap ; \
		$(call Build/Configure/Default, ) \
	)
endef

define Package/xbmc/install
	$(INSTALL_DIR) $(1)/usr/bin
	$(CP) $(PKG_INSTALL_DIR)/usr/bin/ $(1)/usr/bin

	$(INSTALL_DIR) $(1)/usr/lib
	$(CP) $(PKG_INSTALL_DIR)/usr/lib/xbmc $(1)/usr/lib

	$(INSTALL_DIR) $(1)/usr/share
	$(CP) $(PKG_INSTALL_DIR)/usr/share/ $(1)/usr/share
endef

$(eval $(call BuildPackage,xbmc))
