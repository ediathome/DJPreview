import sublime, sublime_plugin
import webbrowser, sys, os
import tempfile
import codecs
import re

from .markdown2 import Markdown

def count_stunden(view):
  std_count = 0
  functionRegs = view.find_by_selector('markup.list.stunden')
  pattern = re.compile(r"\d+", re.MULTILINE)
  for r in functionRegs:
    std_match = pattern.findall(view.substr(r))
    if std_match:
      std_count = std_count + addup_list(std_match)
  return std_count

def addup_list(mlist):
  rv = 0
  for l in mlist:
    rv += int(l)
  return rv

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
      output_str += "<div id='stunden'>" + str(count_stunden(self.view)) + " Stunden gesamt</div>"
      output_str += markdowner.convert(md_string)
      output_str += self.html_footer()
      self.write_str_to_file(tmp_name, output_str)
      webbrowser.open("file://" + tmp_name)
      True

    def write_str_to_file(self, file_name, output_str):
      with codecs.open(file_name, 'w', encoding='utf-8')as f:
        f.write(output_str)
      True

    def read_file_to_str(self, file_name):
      with codecs.open(file_name, 'r', encoding='utf-8')as f:
        return f.read()

    def temp_preview_path(self, view):
        tmp_filename = '%s.html' % view.id()
        tmp_dir = tempfile.gettempdir()
        if not os.path.isdir(tmp_dir):
            os.makedirs(tmp_dir)
        tmp_fullpath = os.path.join(tmp_dir, tmp_filename)
        return tmp_fullpath

    def html_head(self):
      css_path = os.path.dirname(__file__) + '/css/default_style.css'
      print(css_path)
      h = '<!DOCTYPE html><html lang="de"><HEAD><TITLE>DJPreview</TITLE><META http-equiv="Content-Type" content="text/html; charset=utf-8">'
      h += '<STYLE>' + self.read_file_to_str(css_path) + '</STYLE>'
      h += '</HEAD><div id="preview">'
      return h

    def html_footer(self):
      return '</div></html>'


class DjCountStundenInStatusListener(sublime_plugin.EventListener):
  def on_deactived(self, view):
    erase_status('count_stunden')

  def on_modified(self, view):
    self.display_stunden_count(view)

  def display_stunden_count(self, view):
    std_count = str(count_stunden(view))
    view.set_status('count_stunden', std_count + " Stunden")
