import sublime, sublime_plugin, webbrowser

class DjPreviewCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        full_range = sublime.Region(0, self.view.size())
        vt_url = 'http://vt-learn.de/didplanapp/stable/index.html'
        sublime.set_clipboard(self.view.substr(full_range))
        webbrowser.open(vt_url, 1, True)
        
    def set_clipboard(self, cp):
        from Tkinter import Tk
        r = Tk()
        r.withdraw()
        r.clipboard_clear()
        r.clipboard_append('i can has clipboardz?')
        r.destroy()