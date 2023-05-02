# coding: utf-8
from PyQt6.QtCore import QTranslator, QLocale


class FluentTranslator(QTranslator):
    """ Translator of fluent widgets """

    def __init__(self, locale: QLocale, parent=None):
        super().__init__(parent=parent)
        self.load(locale)

    def load(self, locale: QLocale):
        """ load translation file """
        super().load(f":/qfluentwidgets/i18n/qfluentwidgets.{locale.name()}.qm")