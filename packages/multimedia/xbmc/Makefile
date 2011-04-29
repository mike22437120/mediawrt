#
# Copyright (C) 2011 OpenWrt.org
#
# This is free software, licensed under the GNU General Public License v2.
# See /LICENSE for more information.
#

include $(TOPDIR)/rules.mk

PKG_NAME:=xbmc
PKG_VERSION:=10.1
PKG_REV:=c39220420ea927639b3f

PKG_SOURCE_PROTO:=git
PKG_SOURCE_VERSION:=$(PKG_REV)
PKG_SOURCE_SUBDIR:=$(PKG_NAME)-$(PKG_VERSION)
PKG_SOURCE_URL:=git://github.com/xbmc/xbmc.git
PKG_SOURCE:=$(PKG_SOURCE_SUBDIR).tar.bz2

PKG_INSTALL=1

include $(INCLUDE_DIR)/package.mk
include $(INCLUDE_DIR)/nls.mk

define Package/xbmc
  SECTION:=multimedia
  CATEGORY:=Multimedia
  TITLE:=XBMC Mediacenter
  URL:=http://www.xbmc.org
  DEPENDS:= @BUILD_NLS +boost +python +zlib +bzip2 +liblzo +libpcre +alsa-lib +libass +enca +curl +rtmpdump +dbus +libXt +libXtst +samba3-libs \
	   +libXmu +libXrandr +libgl-mesa +glew +fontconfig +fribidi +libjpeg +libpng +libtiff +libfreetype +jasper +libmad +libsamplerate \
	   +libogg +libvorbis +libcdio +libmms +libmodplug +faad2 +libflac +wavpack +libmpeg2 +libbluray +libsdl +libsdl-mixer +libsdl-image +libsqlite3 +libmysqlclient +libssh \
	   +libvdpau +libXinerama +libreadline $(ICONV_DEPENDS) $(INTL_DEPENDS)
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

TARGET_CFLAGS:=$(subst -Os,-O2,$(TARGET_CFLAGS))
TARGET_CXXFLAGS:=$(subst -Os,-O2,$(TARGET_CXXFLAGS))

EXTRA_CFLAGS+= \
	-I$(STAGING_DIR)/usr/include \
	-I$(STAGING_DIR)/usr/lib/libintl/include

EXTRA_LDFLAGS= \
	-Wl,-rpath-link=$(STAGING_DIR)/usr/lib \
	-Wl,-rpath=/usr/lib \
	-L$(STAGING_DIR)/usr/lib/libintl/lib \
	-L$(STAGING_DIR)/usr/lib

CONFIGURE_ARGS+= \
            --with-arch=i686 \
            --with-cpu=i686 \
            --disable-debug \
            --disable-optimizations \
            --enable-gl \
            --disable-vdadecoder \
            --disable-profiling \
            --enable-joystick \
            --enable-xrandr \
            --disable-goom \
            --disable-xbmcprojectm \
            --disable-rsxs \
            --disable-ccache \
            --enable-ffmpeg-libvorbis \
            --disable-mid \
            --disable-hal \
            --disable-asap-codec \
            --disable-libdts \
            --disable-liba52 \
			--enable-libbluray \
            --disable-external-ffmpeg \
            --disable-external-liba52 \
            --disable-external-libdts \
            --enable-external-python \
			--enable-external-libraries

ifneq ($(CONFIG_PULSEAUDIO_SUPPORT),)
CONFIGURE_ARGS+= --enable-pulse
else
CONFIGURE_ARGS+= --disable-pulse
endif

ifneq ($(CONFIG_NONFREE_SUPPORT),)
CONFIGURE_ARGS+= --enable-non-free
else
CONFIGURE_ARGS+= --disable-non-free
endif
	    
ifneq ($(CONFIG_DVDCSS_SUPPORT),)
CONFIGURE_ARGS+= --enable-dvdcss
else
CONFIGURE_ARGS+= --disable-dvdcss
endif 
   
ifneq ($(CONFIG_FAAC_SUPPORT),)
CONFIGURE_ARGS+= --enable-faac
else
CONFIGURE_ARGS+= --disable-faac
endif

ifneq ($(CONFIG_AVAHI_DAEMON),)
CONFIGURE_ARGS+= --enable-avahi
else
CONFIGURE_ARGS+= --disable-avahi
endif

ifneq ($(CONFIG_WEBSERVER),)
CONFIGURE_ARGS+= --enable-webserver
else
CONFIGURE_ARGS+= --disable-webserver
endif
	    
ifneq ($(CONFIG_VDPAU),)
CONFIGURE_ARGS+= --enable-vdpau
else
CONFIGURE_ARGS+= --disable-vdpau
endif

ifneq ($(CONFIG_VAAPI),)
CONFIGURE_ARGS+= --enable-vaapi
else
CONFIGURE_ARGS+= --disable-vaapi
endif

ifneq ($(CONFIG_CRYSTALHD),)
CONFIGURE_ARGS+= \
	--enable-crystalhd
else
CONFIGURE_ARGS+= \
	--disable-crystalhd
endif

define Build/Configure
	(cd $(PKG_BUILD_DIR); \
		rm -rf config.{status,cache} ; \
		./bootstrap ; \
		$(call Build/Configure/Default, ) \
	)
endef

define Build/Compile
	$(MAKE) -C $(PKG_BUILD_DIR) externals 
	$(MAKE) -C $(PKG_BUILD_DIR) xbmc.bin
	$(MAKE) -C $(PKG_BUILD_DIR) xbmc-xrandr
endef

define Package/xbmc/install
	$(INSTALL_DIR) $(1)/usr/lib
	$(CP) $(PKG_INSTALL_DIR)/usr/lib/xbmc $(1)/usr/lib
endef
        
$(eval $(call BuildPackage,xbmc))
