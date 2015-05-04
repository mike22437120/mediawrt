# Multimedia support for [OpenWrt](https://openwrt.org/) #

Install all packages:(Ubuntu)
```
sudo apt-get install build-essential subversion libncurses5-dev zlib1g-dev gawk flex gettext git gperf nasm mercurial
```

Download files from openwrt
```
svn co svn://svn.openwrt.org/openwrt/trunk
cd trunk/
```

Download feeds config (openwrt packages, X-Wrt and MediaWrt)
```
svn export https://mediawrt.googlecode.com/svn/trunk/config/feeds.conf
./scripts/feeds update
./scripts/feeds install -a
```

Select your target and compile openwrt
```
make menuconfig
make
```

**You are finished!!**

You can find the image in the bin folder

**Please follow next steps when you need DVB drivers**

Add patches
```
svn co https://mediawrt.googlecode.com/svn/trunk/patches
find patches/ -name "*.patch" -exec bash -c 'patch -p0 < $1' {} {} \;
```

Generate Makefile for DVB kernel modules (dvb.mk)
```
svn export https://mediawrt.googlecode.com/svn/trunk/scripts/generate_dvbmk.py
./generate_dvbmk.py
```

Select dvb devices and compile openwrt again
```
make menuconfig
make V=99
```