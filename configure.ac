AC_INIT([enigma2-plugins],[4],[forum@openpli.org])
AM_INIT_AUTOMAKE([dist-bzip2 foreign no-define tar-pax])

# Silent rules are available since 1.11, but older versions
# are still in use. So don't use them unconditionally.
m4_ifdef([AM_SILENT_RULES], [AM_SILENT_RULES([yes])])

AC_SYS_LARGEFILE

AC_PATH_PROG(MSGFMT, msgfmt, AC_MSG_ERROR(Could not find msgfmt))

AM_PATH_PYTHON

AC_ARG_WITH(debug,
	AS_HELP_STRING([--without-debug],[disable debugging code]),
	[with_debug="$withval"],[with_debug="yes"])
if test "$with_debug" = "yes"; then
	AC_DEFINE([DEBUG],[1],[Define to 1 to enable debugging code])
fi

AC_ARG_WITH(po,
	AS_HELP_STRING([--with-po],[enable updating of po files]),
	[with_po="$withval"],[with_po="no"])
if test "$with_po" = "yes"; then
	AC_PATH_PROG(MSGINIT, msginit)
	AC_PATH_PROG(MSGMERGE, msgmerge)
	AC_PATH_PROG(MSGUNIQ, msguniq)
	AC_PATH_PROG(MSGATTRIB, msgattrib)
	AC_PATH_PROG(XGETTEXT, xgettext)
	if test -z "$MSGINIT" -o -z "$MSGMERGE" -o -z "$MSGUNIQ" -o -z "$MSGATTRIB" -o -z "$XGETTEXT"; then
		AC_MSG_ERROR([Could not find required gettext tools])
	fi
fi
AM_CONDITIONAL(UPDATE_PO, test "$with_po" = "yes")

AC_ARG_WITH(boxtype,
	[  --with-boxtype=NAME box type [[none,dm7025,dm800...]]],
	[BOXTYPE="$withval"],[BOXTYPE="dm800"])
AC_SUBST(BOXTYPE)
AC_DEFINE_UNQUOTED(BOXTYPE,"$BOXTYPE",[box type])

AM_CONDITIONAL(DREAMBOX, test `echo "$BOXTYPE" | cut -b 1-2` == "dm")
AM_CONDITIONAL(VUPLUS, test `echo "$BOXTYPE" | cut -b 1-2` == "vu")
AM_CONDITIONAL(XTREND, test `echo "$BOXTYPE" | cut -b 1-2` == "et")
AM_CONDITIONAL(GIGABLUE, test `echo "$BOXTYPE" | cut -b 1-2` == "gb")

AM_CONDITIONAL(DM500HD, test "$BOXTYPE" == "dm500hd")
AM_CONDITIONAL(DM500HDV2, test "$BOXTYPE" == "dm500hdv2")
AM_CONDITIONAL(DM800, test "$BOXTYPE" == "dm800")
AM_CONDITIONAL(DM800SE, test "$BOXTYPE" == "dm800se")
AM_CONDITIONAL(DM800SEV2, test "$BOXTYPE" == "dm800sev2")
AM_CONDITIONAL(DM7020HD, test "$BOXTYPE" == "dm7020hd")
AM_CONDITIONAL(DM7020HDV2, test "$BOXTYPE" == "dm7020hdv2")
AM_CONDITIONAL(DM8000, test "$BOXTYPE" == "dm8000")
AM_CONDITIONAL(E3HD, test "$BOXTYPE" == "e3hd")
AM_CONDITIONAL(ET1x000, test "$BOXTYPE" == "et1x000")
AM_CONDITIONAL(FORMULER1, test "$BOXTYPE" == formuler1)
AM_CONDITIONAL(FORMULER3, test "$BOXTYPE" == formuler3)
AM_CONDITIONAL(FORMULER4, test "$BOXTYPE" == formuler4)
AM_CONDITIONAL(FORMULER1TC, test "$BOXTYPE" == formuler1tc)
AM_CONDITIONAL(FORMULER3IP, test "$BOXTYPE" == formuler3ip)
AM_CONDITIONAL(FORMULER4IP, test "$BOXTYPE" == formuler4ip)
AM_CONDITIONAL(FORMULER4TURBO, test "$BOXTYPE" == formuler4turbo)
AM_CONDITIONAL(HD51, test "$BOXTYPE" == "hd51")
AM_CONDITIONAL(HD60, test "$BOXTYPE" == "hd60")
AM_CONDITIONAL(HD61, test "$BOXTYPE" == "hd61")
AM_CONDITIONAL(HD66SE, test "$BOXTYPE" == "hd66se")
AM_CONDITIONAL(PULSE4K, test "$BOXTYPE" == "pulse4k")
AM_CONDITIONAL(PULSE4KMINI, test "$BOXTYPE" == "pulse4kmini")
AM_CONDITIONAL(VUUNO, test "$BOXTYPE" == vuuno)
AM_CONDITIONAL(VUULTIMO, test "$BOXTYPE" == vuultimo)
AM_CONDITIONAL(VUSOLO, test "$BOXTYPE" == vusolo)
AM_CONDITIONAL(VUSOLOSE, test "$BOXTYPE" == vusolose)
AM_CONDITIONAL(VUDUO, test "$BOXTYPE" == vuduo)
AM_CONDITIONAL(VUSOLO2, test "$BOXTYPE" == vusolo2)
AM_CONDITIONAL(VUSOLO4K, test "$BOXTYPE" == vusolo4k)
AM_CONDITIONAL(VUUNO4K, test "$BOXTYPE" == vuuno4k)
AM_CONDITIONAL(VUUNO4KSE, test "$BOXTYPE" == vuuno4kse)
AM_CONDITIONAL(VUULTIMO4K, test "$BOXTYPE" == vuultimo4k)
AM_CONDITIONAL(VUZERO4K, test "$BOXTYPE" == vuzero4k)
AM_CONDITIONAL(VUDUO2, test "$BOXTYPE" == vuduo2)
AM_CONDITIONAL(VUDUO4K, test "$BOXTYPE" == vuduo4k)
AM_CONDITIONAL(VUDUO4KSE, test "$BOXTYPE" == vuduo4kse)
AM_CONDITIONAL(VUZERO, test "$BOXTYPE" == vuzero)
AM_CONDITIONAL(SF8008, test "$BOXTYPE" == "sf8008")
AM_CONDITIONAL(SF8008M, test "$BOXTYPE" == "sf8008m")
AM_CONDITIONAL(SF8008OPT, test "$BOXTYPE" == "sf8008opt")
AM_CONDITIONAL(SFX6008, test "$BOXTYPE" == "sfx6008")
AM_CONDITIONAL(H17, test `echo "$BOXTYPE"` == "h17")
AM_CONDITIONAL(H9, test `echo "$BOXTYPE"` == "h9")
AM_CONDITIONAL(H9COMBO, test `echo "$BOXTYPE"` == "h9combo")
AM_CONDITIONAL(H10, test `echo "$BOXTYPE"` == "h10")
AM_CONDITIONAL(H11, test `echo "$BOXTYPE"` == "h11")
AM_CONDITIONAL(USTYM4KOTTPREMIUM, test "$BOXTYPE" == "ustym4kottpremium")
AM_CONDITIONAL(USTYM4KPRO, test "$BOXTYPE" == "ustym4kpro")
AM_CONDITIONAL(USTYM4K2OTTX, test "$BOXTYPE" == "ustym4ks2ottx")
AM_CONDITIONAL(VIPER4K, test "$BOXTYPE" == "viper4k")
if test `echo "$BOXTYPE" | cut -b 1-2` == "dm"; then
	AC_DEFINE(DREAMBOX, 1, [Dreambox hardware])
fi

AM_CONDITIONAL(HAVE_TEMPFANCONTROL, test "$BOXTYPE" == dm8000 -o "$BOXTYPE" == dm800se -o "$BOXTYPE" == dm800sev2 -o "$BOXTYPE" == dm500hd -o "$BOXTYPE" == vuuno -o "$BOXTYPE" == vuultimo -o "$BOXTYPE" == vusolo2 -o "$BOXTYPE" == vuduo2 -o "$BOXTYPE" == dags1 -o "$BOXTYPE" == dags2 -o "$BOXTYPE" == dags3 -o "$BOXTYPE" == dags4 -o "$BOXTYPE" == dags5 -o "$BOXTYPE" == dags7335 -o "$BOXTYPE" == dags7362 -o "$BOXTYPE" == dags73625 -o "$BOXTYPE" == dags7356 -o "$BOXTYPE" == dags7252 -o "$BOXTYPE" == triplex)

AM_CONDITIONAL(HAVE_ARMV7A, test "$BOXTYPE" == cube)
AM_CONDITIONAL(HAVE_ARMV7AHF, test "$BOXTYPE" == hd51 -o "$BOXTYPE" == 8100s -o "$BOXTYPE" == vs1500 -o "$BOXTYPE" == vusolo4k -o "$BOXTYPE" == vuuno4k -o "$BOXTYPE" == vuuno4kse -o "$BOXTYPE" == vuzero4k -o "$BOXTYPE" == vuultimo4k -o "$BOXTYPE" == vuduo4k -o "$BOXTYPE" == vuduo4kse -o "$BOXTYPE" == dm900 -o "$BOXTYPE" == dm920 -o "$BOXTYPE" == sf4008 -o "$BOXTYPE" == dags7252 -o "$BOXTYPE" == dags72604 -o "$BOXTYPE" == gb7252 -o "$BOXTYPE" == xc7439 -o "$BOXTYPE" == h7 -o "$BOXTYPE" == h17 -o "$BOXTYPE" == h9 -o "$BOXTYPE" == h9combo -o "$BOXTYPE" == h10 -o "$BOXTYPE" == h11 -o "$BOXTYPE" == sf5008 -o "$BOXTYPE" == et1x000 -o "$BOXTYPE" == et13000 -o "$BOXTYPE" == cc1 -o "$BOXTYPE" == sf8008 -o "$BOXTYPE" == sf8008m -o "$BOXTYPE" == sf8008opt -o "$BOXTYPE" == sx988 -o "$BOXTYPE" == ip8 -o "$BOXTYPE" == gbmv200 -o "$BOXTYPE" == viper4k -o "$BOXTYPE" == hd60 -o "$BOXTYPE" == hd61 -o "$BOXTYPE" == hd66se -o "$BOXTYPE" == i55plus -o "$BOXTYPE" == ustym4kpro -o "$BOXTYPE" == ustym4kottpremium -o "$BOXTYPE" == multiboxpro -o "$BOXTYPE" == multiboxse -o "$BOXTYPE" == multibox -o "$BOXTYPE" == osmio4k -o "$BOXTYPE" == osmio4kplus -o "$BOXTYPE" == osmini4k -o "$BOXTYPE" == pulse4k -o "$BOXTYPE" == pulse4kmini -o "$BOXTYPE" == sfx6008 -o "$BOXTYPE" == sx88v2)
AM_CONDITIONAL(HAVE_CORTEXA9HF, test "$BOXTYPE" == wetekplay)
AM_CONDITIONAL(HAVE_AARCH64, test "$BOXTYPE" == wetekplay2 -o "$BOXTYPE" == alien5 )

AM_CONDITIONAL(HAVE_LIBVUPLDEMO, test "$BOXTYPE" == vusolo2 -o "$BOXTYPE" == vusolose -o "$BOXTYPE" == vuduo2 -o "$BOXTYPE" == vuduo2 )
AM_CONDITIONAL(HAVE_VUSTALKER, test "$BOXTYPE" == vuzero )
AM_CONDITIONAL(HAVE_VUEXTRAS, test "$BOXTYPE" == vusolo4k -o "$BOXTYPE" == vuuno4k -o "$BOXTYPE" == vuzero4k -o "$BOXTYPE" == vuuno4kse -o "$BOXTYPE" == vuultimo4k -o "$BOXTYPE" == vuultimo4k -o "$BOXTYPE" == vuduo4k -o "$BOXTYPE" == vuduo4kse )

AC_CONFIG_FILES([
Makefile

aihdcontroler/Makefile
aihdcontroler/meta/Makefile
aihdcontroler/src/Makefile
aihdcontroler/src/comp/Makefile
aihdcontroler/src/data/Makefile

antiscrollbar/Makefile
antiscrollbar/meta/Makefile
antiscrollbar/src/Makefile

ardmediathek/Makefile
ardmediathek/meta/Makefile
ardmediathek/src/Makefile
ardmediathek/src/img/Makefile

audiosync/Makefile
audiosync/img/Makefile
audiosync/meta/Makefile
audiosync/po/Makefile
audiosync/src/Makefile

automaticcleanup/Makefile
automaticcleanup/meta/Makefile
automaticcleanup/po/Makefile
automaticcleanup/src/Makefile

automaticvolumeadjustment/Makefile
automaticvolumeadjustment/meta/Makefile
automaticvolumeadjustment/src/Makefile
automaticvolumeadjustment/po/Makefile

autoresolution/Makefile
autoresolution/meta/Makefile
autoresolution/src/Makefile
autoresolution/po/Makefile

autotimer/Makefile
autotimer/po/Makefile
autotimer/meta/Makefile
autotimer/src/WebComponents/Makefile
autotimer/src/WebScreens/Makefile
autotimer/src/Makefile
autotimer/src/web-data/Makefile
autotimer/src/WebChilds/Makefile
autotimer/src/web/Makefile

babelzapper/Makefile
babelzapper/etc/Makefile
babelzapper/meta/Makefile
babelzapper/src/Makefile

blindscan/src/Makefile
blindscan/po/Makefile
blindscan/Makefile
blindscan/meta/Makefile
blindscan/src/images/Makefile

bonjour/Makefile
bonjour/meta/Makefile
bonjour/src/Makefile

BTDevicesManager/Makefile
BTDevicesManager/src/Makefile
BTDevicesManager/meta/Makefile
BTDevicesManager/po/Makefile

cdinfo/Makefile
cdinfo/meta/Makefile
cdinfo/src/Makefile

DLNABrowser/Makefile
DLNABrowser/src/Makefile
DLNABrowser/icons/Makefile
DLNABrowser/po/Makefile
DLNABrowser/meta/Makefile

DLNAServer/Makefile
DLNAServer/src/Makefile
DLNAServer/po/Makefile
DLNAServer/meta/Makefile

dreamexplorer/Makefile
dreamexplorer/meta/Makefile
dreamexplorer/po/Makefile
dreamexplorer/src/Makefile
dreamexplorer/src/res/Makefile

dreamirc/Makefile
dreamirc/meta/Makefile
dreamirc/src/Makefile
dreamirc/src/protocols/Makefile

dreammediathek/Makefile
dreammediathek/src/Makefile

dvdbackup/Makefile
dvdbackup/src/Makefile
dvdbackup/po/Makefile
dvdbackup/meta/Makefile

dyndns/Makefile
dyndns/src/Makefile
dyndns/meta/Makefile

easyinfo/Makefile
easyinfo/meta/Makefile
easyinfo/src/Makefile

easymedia/Makefile
easymedia/meta/Makefile
easymedia/po/Makefile
easymedia/src/Makefile

eibox/Makefile
eibox/meta/Makefile
eibox/po/Makefile
eibox/src/Makefile
eibox/src/images/Makefile

emailclient/Makefile
emailclient/meta/Makefile
emailclient/po/Makefile
emailclient/src/Makefile

epgrefresh/Makefile
epgrefresh/meta/Makefile
epgrefresh/po/Makefile
epgrefresh/src/Makefile
epgrefresh/src/webinterface/Makefile

epgsearch/Makefile
epgsearch/meta/Makefile
epgsearch/po/Makefile
epgsearch/src/Makefile
epgsearch/src/icons/Makefile

fancontrol2/Makefile
fancontrol2/meta/Makefile
fancontrol2/po/Makefile
fancontrol2/src/Makefile
fancontrol2/src/data/Makefile

filebrowser/Makefile
filebrowser/meta/Makefile
filebrowser/src/Makefile
filebrowser/po/Makefile

fstabeditor/Makefile
fstabeditor/meta/Makefile
fstabeditor/src/Makefile

ftpbrowser/Makefile
ftpbrowser/meta/Makefile
ftpbrowser/po/Makefile
ftpbrowser/src/Makefile
ftpbrowser/src/images/Makefile

GigaBlueBluetoothSetup/Makefile
GigaBlueBluetoothSetup/src/Makefile
GigaBlueBluetoothSetup/meta/Makefile
GigaBlueBluetoothSetup/po/Makefile

growlee/Makefile
growlee/meta/Makefile
growlee/src/Makefile

HbbTV/Makefile
HbbTV/src/Makefile
HbbTV/meta/Makefile
HbbTV/po/Makefile

WebkitHbbTV/Makefile
WebkitHbbTV/src/Makefile
WebkitHbbTV/bin/Makefile
WebkitHbbTV/po/Makefile

httpproxy/Makefile
httpproxy/meta/Makefile
httpproxy/src/Makefile

imdb/Makefile
imdb/meta/Makefile
imdb/po/Makefile
imdb/src/Makefile

kiddytimer/Makefile
kiddytimer/img/Makefile
kiddytimer/meta/Makefile
kiddytimer/po/Makefile
kiddytimer/src/Makefile

letterbox/Makefile
letterbox/src/Makefile
letterbox/meta/Makefile

libvupldemo/Makefile
libvupldemo/src/Makefile

logomanager/Makefile
logomanager/meta/Makefile
logomanager/po/Makefile
logomanager/src/Makefile

mediadownloader/Makefile
mediadownloader/meta/Makefile
mediadownloader/po/Makefile
mediadownloader/src/Makefile

mediathekviewweb/Makefile
mediathekviewweb/meta/Makefile
mediathekviewweb/src/Makefile
mediathekviewweb/src/img/Makefile

merlinepg/Makefile
merlinepg/meta/Makefile
merlinepg/src/Makefile

merlinepgcenter/Makefile
merlinepgcenter/meta/Makefile
merlinepgcenter/src/Makefile
merlinepgcenter/po/Makefile
merlinepgcenter/skins/Makefile
merlinepgcenter/images/Makefile
merlinepgcenter/images/HD/Makefile
merlinepgcenter/images/HD_BORDER/Makefile
merlinepgcenter/images/SD/Makefile
merlinepgcenter/images/XD/Makefile
merlinepgcenter/images/XD_BORDER/Makefile

merlinmusicplayer/Makefile
merlinmusicplayer/meta/Makefile
merlinmusicplayer/po/Makefile
merlinmusicplayer/src/Makefile
merlinmusicplayer/src/images/Makefile

mosaic/Makefile
mosaic/meta/Makefile
mosaic/po/Makefile
mosaic/src/Makefile

movieretitle/Makefile
movieretitle/meta/Makefile
movieretitle/po/Makefile
movieretitle/src/Makefile

movietagger/Makefile
movietagger/etc/Makefile
movietagger/meta/Makefile
movietagger/po/Makefile
movietagger/src/Makefile

mphelp/Makefile
mphelp/meta/Makefile
mphelp/src/Makefile

multirc/Makefile
multirc/src/Makefile
multirc/meta/Makefile

netcaster/Makefile
netcaster/meta/Makefile
netcaster/src/Makefile
netcaster/src/bin/Makefile
netcaster/src/bin/interface/Makefile
netcaster/src/etc/Makefile

netzkino/Makefile
netzkino/meta/Makefile
netzkino/src/Makefile

ncidclient/Makefile
ncidclient/meta/Makefile
ncidclient/po/Makefile
ncidclient/src/Makefile

ofdb/Makefile
ofdb/meta/Makefile
ofdb/po/Makefile
ofdb/src/Makefile

orfat/Makefile
orfat/meta/Makefile
orfat/src/Makefile

orfteletext/Makefile
orfteletext/meta/Makefile
orfteletext/src/Makefile

partnerbox/Makefile
partnerbox/meta/Makefile
partnerbox/po/Makefile
partnerbox/src/Makefile
partnerbox/src/icons/Makefile

permanentclock/Makefile
permanentclock/meta/Makefile
permanentclock/po/Makefile
permanentclock/src/Makefile
permanentclock/src/trad/Makefile

pluginhider/Makefile
pluginhider/meta/Makefile
pluginhider/po/Makefile
pluginhider/src/Makefile

porncenter/Makefile
porncenter/meta/Makefile
porncenter/po/Makefile
porncenter/src/Makefile
porncenter/src/Additions/Makefile

primetimemanager/Makefile
primetimemanager/meta/Makefile
primetimemanager/po/Makefile
primetimemanager/src/Makefile
primetimemanager/src/images/Makefile

reconstructapsc/Makefile
reconstructapsc/meta/Makefile
reconstructapsc/src_py/Makefile
reconstructapsc/po/Makefile

remotetimer/Makefile
remotetimer/meta/Makefile
remotetimer/po/Makefile
remotetimer/src/Makefile

recordinfobar/Makefile
recordinfobar/meta/Makefile
recordinfobar/po/Makefile
recordinfobar/src/Makefile

satipclient/Makefile
satipclient/meta/Makefile
satipclient/po/Makefile
satipclient/src/Makefile

seekbar/Makefile
seekbar/meta/Makefile
seekbar/po/Makefile
seekbar/src/Makefile

setpasswd/Makefile
setpasswd/meta/Makefile
setpasswd/po/Makefile
setpasswd/src/Makefile

shoutcast/Makefile
shoutcast/meta/Makefile
shoutcast/po/Makefile
shoutcast/src/Makefile

showclock/Makefile
showclock/meta/Makefile
showclock/po/Makefile
showclock/src/Makefile

simplerss/Makefile
simplerss/meta/Makefile
simplerss/po/Makefile
simplerss/src/Makefile

srfmediathek/Makefile
srfmediathek/meta/Makefile
srfmediathek/src/Makefile
srfmediathek/src/img/Makefile

systemtime/Makefile
systemtime/meta/Makefile
systemtime/po/Makefile
systemtime/src/Makefile
systemtime/src/images/Makefile

svdrp/Makefile
svdrp/meta/Makefile
svdrp/src/Makefile

tageditor/Makefile
tageditor/meta/Makefile
tageditor/po/Makefile
tageditor/src/Makefile

trafficinfo/Makefile
trafficinfo/meta/Makefile
trafficinfo/src/Makefile

transcodingsetup/Makefile
transcodingsetup/src/Makefile
transcodingsetup/po/Makefile
transcodingsetup/meta/Makefile

transmission/Makefile
transmission/src/Makefile
transmission/po/Makefile
transmission/meta/Makefile

tvcharts/Makefile
tvcharts/meta/Makefile
tvcharts/src/Makefile

unwetterinfo/Makefile
unwetterinfo/meta/Makefile
unwetterinfo/src/Makefile

valixdcontrol/Makefile
valixdcontrol/meta/Makefile
valixdcontrol/src/Makefile
valixdcontrol/src/comp/Makefile
valixdcontrol/src/data/Makefile

virtualzap/Makefile
virtualzap/meta/Makefile
virtualzap/po/Makefile
virtualzap/src/Makefile

vlcplayer/Makefile
vlcplayer/meta/Makefile
vlcplayer/po/Makefile
vlcplayer/src/Makefile

vfdcontrol/Makefile
vfdcontrol/meta/Makefile
vfdcontrol/po/Makefile
vfdcontrol/src/Makefile

VuBluetoothSetup/Makefile
VuBluetoothSetup/src/Makefile
VuBluetoothSetup/src/vuduo4k/Makefile
VuBluetoothSetup/src/vuduo4kse/Makefile
VuBluetoothSetup/src/vusolo4k/Makefile
VuBluetoothSetup/src/vuultimo4k/Makefile
VuBluetoothSetup/src/vuuno4k/Makefile
VuBluetoothSetup/src/vuuno4kse/Makefile
VuBluetoothSetup/src/vuzero4k/Makefile
VuBluetoothSetup/meta/Makefile
VuBluetoothSetup/po/Makefile

VuStalker/Makefile
VuStalker/src/Makefile
VuStalker/src/vuduo4k/Makefile
VuStalker/src/vuduo4kse/Makefile
VuStalker/src/vusolo4k/Makefile
VuStalker/src/vuultimo4k/Makefile
VuStalker/src/vuuno4k/Makefile
VuStalker/src/vuuno4kse/Makefile
VuStalker/src/vuzero4k/Makefile
VuStalker/src/vuzero/Makefile
VuStalker/meta/Makefile
VuStalker/po/Makefile

VuChromium/Makefile
VuChromium/src/Makefile
VuChromium/meta/Makefile
VuChromium/po/Makefile

webcamviewer/Makefile
webcamviewer/meta/Makefile
webcamviewer/src/Makefile

WebBrowser/Makefile
WebBrowser/src/Makefile
WebBrowser/meta/Makefile
WebBrowser/keymap/Makefile
WebBrowser/icons/Makefile
WebBrowser/po/Makefile

werbezapper/Makefile
werbezapper/meta/Makefile
werbezapper/po/Makefile
werbezapper/src/Makefile

witaispeechtotext/Makefile
witaispeechtotext/src/Makefile

zaphistorybrowser/Makefile
zaphistorybrowser/meta/Makefile
zaphistorybrowser/po/Makefile
zaphistorybrowser/src/Makefile

zapstatistic/Makefile
zapstatistic/meta/Makefile
zapstatistic/po/Makefile
zapstatistic/src/Makefile

zdfmediathek/Makefile
zdfmediathek/meta/Makefile
zdfmediathek/src/Makefile
zdfmediathek/src/img/Makefile

])
AC_OUTPUT
