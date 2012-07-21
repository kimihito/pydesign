#!/usr/bin/env python
# coding: utf-8
class Report(object):
  def __init__(self):
    self.title = u"月次報告"
    self.text = [u"順調", u"最高"]

  def output_report(self):
    self.output_start()
    self.output_head()
    self.output_body_start()
    self.output_body()
    self.output_body_end()
    self.output_end()

  def output_body(self):
    for line in self.text:
      self.output_line(line)

  def output_start(self):
    assert False, "called abstruct method output_start"

  def output_head(self):
    print(self.title)

  def output_body_start(self):
    assert False, "called abstruct method output_body_start"

  def output_line(self, line):
    assert False, "called abstruct method output_body"

  def out_body_end(self):
    assert False, "called abstruct method output_body_end"

  def output_end(self):
    assert False, "called abstruct method output_end"

class HTMLReport(Report):
  def output_start(self):
    print("<html>")

  def output_head(self):
    print("<head>")

    print("<title>%s</title>"%(self.title,))

    print("</head>")

  def output_body_start(self):
    print("<body>")
  
  def output_line(self, line):
    print("<p>%s</p>" %(line,))

  def output_body_end(self):
    print("</body>")

  def output_end(self):
    print("</html>")

class PlainTextReport(Report):
  def output_start(self):
    pass
  
  def output_head(self):
    print("***%s***"%(self.title,))

  def output_body_start(self):
    pass

  def output_line(self, line):
    print(line)

  def output_body_end(self):
    pass

  def output_end(self):
    pass

if __name__ == "__main__":
  report = PlainTextReport()
  report.output_report()

  report = HTMLReport()
  report.output_report()

