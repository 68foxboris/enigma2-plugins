import gettext

from Components.Language import language
from Tools.Directories import resolveFilename, SCOPE_PLUGINS
from Components.config import config, ConfigSet, ConfigSubsection, ConfigNumber, ConfigYesNo, ConfigSelection


def localeInit():
	gettext.bindtextdomain("EPGSearch", resolveFilename(SCOPE_PLUGINS, "Extensions/EPGSearch/locale"))


def _(txt):
	t = gettext.dgettext("EPGSearch", txt)
	if t == txt:
		t = gettext.gettext(txt)
	return t


# Language
localeInit()
language.addCallback(localeInit)


config.plugins.epgsearch = ConfigSubsection()
config.plugins.epgsearch.history = ConfigSet(choices=[])
config.plugins.epgsearch.history_length = ConfigNumber(default=10)
config.plugins.epgsearch.add_search_to_epg = ConfigYesNo(default=True)
config.plugins.epgsearch.type_button_blue = ConfigSelection([('0', _("only Search")), ('1', _("choice (Search and standard)"))], default='0')
config.plugins.epgsearch.picons = ConfigYesNo(default=False)
config.plugins.epgsearch.bouquet = ConfigYesNo(default=False)
config.plugins.epgsearch.favorit_name = ConfigYesNo(default=False)
config.plugins.epgsearch.include_iptv = ConfigYesNo(default=False)
config.plugins.epgsearch.show_in_furtheroptionsmenu = ConfigYesNo(default=True)
config.plugins.epgsearch.search_in_channelmenu = ConfigYesNo(default=True)
config.plugins.epgsearch.filter_type = ConfigSelection(default="exact", choices=[("partial", _("partial match")), ("exact", _("exact match"))])
config.plugins.epgsearch.search_case = ConfigSelection(default="insensitive", choices=[("insensitive", _("case-insensitive search")), ("sensitive", _("case-sensitive search"))])
config.plugins.epgsearch.search_type = ConfigSelection(default="partial", choices=[("partial", _("partial match")), ("partialdes", _("partial description")), ("exact", _("exact match")), ("start", _("title starts with")), ("end", _("title ends with"))])
