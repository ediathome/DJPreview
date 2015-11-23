import sublime, sublime_plugin
import webbrowser, sys, os
import tempfile
import codecs

# Add the directory containing your module to the Python path (wants absolute paths)
# sys.path.append(os.path.abspath('.'))
from .markdown2 import Markdown

class DjPreviewCommand(sublime_plugin.TextCommand):
    def run(self, edit):
      full_range = sublime.Region(0, self.view.size())
      convert_str = self.view.substr(full_range)
      vt_url = 'http://vt-learn.de/didplanapp/stable/index.html'
      sublime.set_clipboard(convert_str)
      self.create_html_tmp_file(convert_str)

    def create_html_tmp_file(self, md_string):
      markdowner = Markdown()
      tmp_name = self.temp_preview_path(self.view)
      output_str = self.html_head()
      output_str += markdowner.convert(md_string)
      output_str += self.html_footer()
      self.write_str_to_file(tmp_name, output_str)
      webbrowser.open("file://" + tmp_name)
      True

    def write_str_to_file(self, file_name, output_str):
      with codecs.open(file_name, 'w', encoding='utf-8')as f:
        f.write(output_str)
      True

    def temp_preview_path(self, view):
        tmp_filename = '%s.html' % view.id()
        tmp_dir = tempfile.gettempdir()
        if not os.path.isdir(tmp_dir):
            os.makedirs(tmp_dir)
        tmp_fullpath = os.path.join(tmp_dir, tmp_filename)
        return tmp_fullpath

    def html_head(self):
        return '<!DOCTYPE html><html lang="de"><HEAD><TITLE>DJPreview</TITLE><META http-equiv="Content-Type" content="text/html; charset=utf-8"></HEAD>'

    def html_footer(self):
        return '</html>'