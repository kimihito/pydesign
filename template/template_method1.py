#!/usr/bin/env python
# coding: utf-8
class Report:
  def __init__(self):
    self.title = u"月次報告"
    self.text = [u"順調",u"最高"]
  
  def output_report(self, format):
    if format == "plain":
      print("*** %s ***" % (self.title))
    elif format == "html":
      print("<html>")
      print("<head>")
      print("<title>%s</title>" % (self.title,))
      print("</head>")
      print("<body>")

    for line in self.text:
      if format == "plain":
        print(line)
      else:
        print("<p>%s</p>" %(line,))

    if format == "html":
      print("</body>")
      print("</html>")

if __name__ == "__main__":
  report = Report()
  report.output_report("plain")
  report.output_report("html")

