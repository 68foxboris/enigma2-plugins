from Components.Language import language
from Tools.Directories import resolveFilename, SCOPE_PLUGINS, SCOPE_LANGUAGE
import os
import gettext

PluginLanguageDomain = "LogoManager"
PluginLanguagePath = "Extensions/LogoManager/locale"


def localeInit():
	gettext.bindtextdomain(PluginLanguageDomain, resolveFilename(SCOPE_PLUGINS, PluginLanguagePath))


def _(txt):
	if gettext.dgettext(PluginLanguageDomain, txt):
		return gettext.dgettext(PluginLanguageDomain, txt)
	else:
		return gettext.gettext(txt)


language.addCallback(localeInit)
