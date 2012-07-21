#!/usr/bin/env python
# coding: utf-8
class Report(object):
  def __init__(self):
    self.title = u"月次報告"
    self.text = [u"順調",u"最高"]

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
    pass

  def output_head(self):
    print(self.title)

  def output_body_start(self):
    pass
  
  def output_line(self, line):
    assert False, "called abstruct method output_body"

  def output_body_end(self):
    pass

  def output_end(self):
    pass

class PlainTextReport(Report):
  def output_head(self):
    print("***%s***"%(self.title,))

  def output_line(self, line):
    print(line)

if __name__ == "__main__":
  report = PlainTextReport()
  report.output_report()

  report = Report()
  report.output_report()
