#!/usr/bin/env python
# coding: utf-8
from abc import abstractmethod, ABCMeta
class Report(object):
  __metaclass__ = ABCMeta
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

  @abstractmethod
  def output_start(self):pass
  @abstractmethod
  def output_head(self):pass
  @abstractmethod
  def output_body_start(self):pass
  @abstractmethod
  def ouput_line(self, line):pass
  @abstractmethod
  def output_body_end(self): pass
  @abstractmethod
  def output_end(self): pass

if __name__ == "__main__":
  report = Report()
  report.output_report()
  
