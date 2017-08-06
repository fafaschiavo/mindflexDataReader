import serial
import numpy as np
import pylab as plt
import time
import matplotlib.gridspec as gridspec
import pandas as pd
import sys

with serial.Serial('/dev/tty.HC-05-DevB', 9600, timeout=1) as ser: