import sublime
import sublime_plugin
import unicodedata


class NfdToNfcPasteCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        paste = sublime.get_clipboard()
        sublime.set_clipboard(unicodedata.normalize('NFC', paste))
        self.view.run_command('paste')
