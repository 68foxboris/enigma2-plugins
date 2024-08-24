ACLOCAL_AMFLAGS = -I m4

SUBDIRS = \
	aihdcontroler \
	antiscrollbar \
	ardmediathek \
	audiosync \
	automaticcleanup \
	automaticvolumeadjustment \
	autoresolution \
	autotimer \
	babelzapper \
	blindscan \
	bonjour \
	BTDevicesManager \
	cdinfo \
	DLNABrowser \
	DLNAServer \
	dreamexplorer \
	dreamirc \
	dreammediathek \
	dvdbackup \
	dyndns \
	easyinfo \
	easymedia \
	eibox \
	emailclient \
	epgrefresh \
	epgsearch \
	fancontrol2 \
	filebrowser \
	fstabeditor \
	ftpbrowser \
	growlee \
	HbbTV \
	httpproxy \
	imdb \
	kiddytimer \
	letterbox \
	libvupldemo \
	logomanager \
	mediadownloader \
	mediathekviewweb \
	merlinepg \
	merlinepgcenter \
	merlinmusicplayer \
	mosaic \
	movieretitle \
	movietagger \
	mphelp \
	multirc \
	ncidclient \
	netcaster \
	netzkino \
	ofdb \
	orfat \
	orfteletext \
	partnerbox \
	permanentclock \
	porncenter \
	primetimemanager \
	reconstructapsc \
	recordinfobar \
	srfmediathek \
	satipclient \
	seekbar \
	setpasswd \
	shoutcast \
	showclock \
	simplerss \
	svdrp \
	tageditor \
	trafficinfo \
	transcodingsetup \
	transmission \
	tvcharts \
	unwetterinfo \
	valixdcontrol \
	virtualzap \
	vlcplayer \
	vfdcontrol \
	VuBluetoothSetup \
	VuChromium \
	VuStalker \
	WebBrowser \
	WebkitHbbTV \
	webcamviewer \
	werbezapper \
	witaispeechtotext \
	zapstatistic \
	zdfmediathek

metadir = $(datadir)/meta
meta_DATA = index-enigma2-plugins.xml
CLEANFILES = index-enigma2-plugins.xml

index-enigma2-plugins.xml: $(top_srcdir)/genmetaindex.py $(top_srcdir)/*/meta/plugin_*.xml
	$(AM_V_GEN)$(PYTHON) $^ > $@
