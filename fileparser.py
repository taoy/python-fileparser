#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# CmdFileParser: Read Option/Command File and Parse contents.
# 
__author__ = 'https://github.com/taoy'

import re

#{{{ - Support Functions and Constraints
sectre = re.compile("^\[.*]")

def read(conffile):
  #{{{
  f = open(conffile, 'r')
  r = f.readlines()
  return r
  #}}}

def getsections(lines):
  #{{{
  sections = [] 
  for line in lines:
    s = sectre.match(line)
    if s != None:
      data = s.group(0)
      sections.append(data[1:-1])
    else:
      continue
  return sections
  #}}}
#}}}

class CmdFileParser(object):
  """ Read Setting/Command File with sections and options. """
  #{{{
  def __init__(self, conffile = None):
    """ Initialize. """
    if conffile != None:
      self.conffile = conffile
    else:
      self.conffile = False
    self.lines = read(conffile)
    self.sections = getsections(self.lines)
  #}}}
  #{{{
  def read(self, conffile):
    #{{{
    f = open(conffile, 'r')
    r = f.readlines()
    return r
    #}}}

  def optread(self, section):
    #{{{
    options = {} 
    chk = False
    for line in self.lines:
      if line != '[%s]\n' % section and chk != True:
        continue
      elif line == '[%s]\n' % section :
        chk = True
      elif line == '\n':
        chk = False
      else:
        data = line.replace('\n', '')
        params = data.split(' = ')
        paramdata = params[1].split(', ')
        options[params[0]] = paramdata
    return options
    #}}}

  def getopt(self, section, opt):
    #{{{
    options = optread(section, self.lines)
    if opt in options:
      return options[opt]
    else:
      return False
    #}}}

  def has_section(self, section):
    #{{{
    if section in self.sections:
      return section
    else:
      return False
    #}}}

  def dataread(self, section):
    #{{{
    data = []
    chk = False
    for line in self.lines:
      if line != '[%s]\n' % section and chk != True:
        continue
      elif line == '[%s]\n' % section :
        chk = True
      elif line == '\n':
        chk = False
      else:
        lindata = line.replace('\n', '')
        data.append(lindata)
    return data
    #}}}
  #}}}
  # vim:set sw=2 ts=8 sts=8 expandtab foldmethod=marker:
