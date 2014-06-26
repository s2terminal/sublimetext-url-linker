import sublime, sublime_plugin, re, webbrowser

class OpenLinkCommand(sublime_plugin.TextCommand):
  def __init__(self, v):
    self.prev_url = ''
    sublime_plugin.TextCommand.__init__(self, v)

  def run(self, edit):
    for region in self.view.sel():
      line_contents = self.view.substr(self.view.line(region)) + '\n'
      match = re.match(r'(https?|ftp)://([^:/]+)(?::(¥d+))?(/.*)?', line_contents)
      if match:
        if self.prev_url == match.group():
          self.prev_url = ''
        else:
          webbrowser.open_new_tab(match.group())
          self.prev_url = match.group()