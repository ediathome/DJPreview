import sublime, sublime_plugin, webbrowser

class DjPreviewCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        full_range = sublime.Region(0, self.view.size())
        txt = self.view.substr(full_range)
        self.view.insert(edit, 0, txt + txt)
        vt_url = 'http://vt-learn.de/didplanapp/stable/index.html'
        webbrowser.open(vt_url, 1, True)

