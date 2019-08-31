# -*- coding:utf-8 -*-

'''
 MIT License

 Copyright (C) <2019> <@DFRobot Frank>

　Permission is hereby granted, free of charge, to any person obtaining a copy of this
　software and associated documentation files (the "Software"), to deal in the Software
　without restriction, including without limitation the rights to use, copy, modify,
　merge, publish, distribute, sublicense, and/or sell copies of the Software, and to
　permit persons to whom the Software is furnished to do so.

　The above copyright notice and this permission notice shall be included in ALL copies or
　substantial portions of the Software.
 THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED,
 INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR
 PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE
 FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE,
 ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
'''

import serial
import time

class DFRobot_A02_Distance:

  ''' Board status '''
  STA_OK = 0x00
  STA_ERR_CHECKSUM = 0x01
  STA_ERR_SERIAL = 0x02
  STA_ERR_CHECK_OUT_LIMIT = 0x03
  STA_ERR_CHECK_LOW_LIMIT = 0x04

  ''' last operate status, users can use this variable to determine the result of a function call. '''
  last_operate_status = STA_OK

  ''' variable '''
  distance = 0

  '''Maximum range'''
  distance_max = 4500
  distance_min = 0

  def __init__(self):
    self.ser = serial.Serial("dev/ttyAMA0", 9600)
    if !self.ser.isOpen():
      self.last_operate_status = STA_ERR_SERIAL

  def check_sum(self, l):
    return (l[0] + l[1] + l[2])&0x00ff

  def set_dis_rang(self, min, max):
    distance_max = max
    distance_min = min

  def measure(self):
    data = []
    i = 0
    while ser.inWaiting() > 0:
      data[i] = ser.read()
      i += 1
      if data[0] != 0xff:
        i = 0
      if i == 4:
        break
    sum = check_sum(data)
    if sum != data[3]
      self.last_operate_status = STA_ERR_CHECKSUM
    else:
      self.distance = data[1] << 8 + data[2]
    if self.distance > self.distance_max:
      self.last_operate_status = STA_ERR_CHECK_OUT_LIMIT
      self.distance = self.distance_max
    elif self.distance < self.distance_min
      self.last_operate_status = STA_ERR_CHECK_low_LIMIT
      self.distance = self.distance_min

  def getDistance(self):
    measure()
    return self.distance