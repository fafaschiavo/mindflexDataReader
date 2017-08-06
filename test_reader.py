import serial
import numpy as np
import pylab as plt
import time
import matplotlib.gridspec as gridspec
import pandas as pd
import sys
# "signal strength, attention, meditation, delta, theta, low alpha, high alpha, low beta, high beta, low gamma, high gamma"

csv_filename = sys.argv[1]

x=0
attention=0
meditation=0
delta=0
theta=0
low_alpha=0
high_alpha=0
low_beta=0
high_beta=0
low_gamma=0
high_gamma=0
spectrum=np.zeros((1, 12))
fig=plt.figure(1)

ax=plt.subplot2grid((5, 4), (0, 0), colspan=4)
line_object_a,=ax.plot(x,attention,'ko-')

bx=plt.subplot2grid((5, 4), (1, 0), colspan=4)
line_object_b,=bx.plot(x,meditation,'ko-')

cx=plt.subplot2grid((5, 4), (2, 0))
line_object_c,=cx.plot(x,delta,'ko-')

dx=plt.subplot2grid((5, 4), (2, 1))
line_object_d,=dx.plot(x,theta,'ko-')

ex=plt.subplot2grid((5, 4), (2, 2))
line_object_e,=ex.plot(x,low_alpha,'ko-')

fx=plt.subplot2grid((5, 4), (2, 3))
line_object_f,=fx.plot(x,high_alpha,'ko-')

gx=plt.subplot2grid((5, 4), (3, 0))
line_object_g,=gx.plot(x,low_beta,'ko-')

hx=plt.subplot2grid((5, 4), (3, 1))
line_object_h,=hx.plot(x,high_beta,'ko-')

ix=plt.subplot2grid((5, 4), (3, 2))
line_object_i,=ix.plot(x,low_gamma,'ko-')

jx=plt.subplot2grid((5, 4), (3, 3))
line_object_j,=jx.plot(x,high_gamma,'ko-')

with serial.Serial('/dev/tty.HC-06-DevB', 19200, timeout=1) as ser:
	current_timer = 1
	total_samples_collected = 0
	while True:
		try:
			line = ser.readline()
			if 'ERROR' not in line:
				print '------ Here it is ------'
				raw_data = line.replace('\r\n','').split(',')
				converted_data = map(int, raw_data)
				converted_data.append(current_timer)
				print 'Time counter - ' + str(current_timer)
				print 'Total samples collected - ' + str(total_samples_collected)
				print converted_data

				x = np.concatenate((line_object_a.get_xdata(),[current_timer]))
				attention = np.concatenate((line_object_a.get_ydata(),[converted_data[1]]))
				meditation = np.concatenate((line_object_b.get_ydata(),[converted_data[2]]))
				delta = np.concatenate((line_object_c.get_ydata(),[converted_data[3]]))
				theta = np.concatenate((line_object_d.get_ydata(),[converted_data[4]]))
				low_alpha = np.concatenate((line_object_e.get_ydata(),[converted_data[5]]))
				high_alpha = np.concatenate((line_object_f.get_ydata(),[converted_data[6]]))
				low_beta = np.concatenate((line_object_g.get_ydata(),[converted_data[7]]))
				high_beta = np.concatenate((line_object_h.get_ydata(),[converted_data[8]]))
				low_gamma = np.concatenate((line_object_i.get_ydata(),[converted_data[9]]))
				high_gamma = np.concatenate((line_object_j.get_ydata(),[converted_data[10]]))
				current_data_np_array = np.asarray(converted_data)
				current_data_np_array = np.array(current_data_np_array, ndmin=2)
				if converted_data[0] < 100:	
					spectrum = np.concatenate((spectrum, current_data_np_array), axis=0)
					data_frame = pd.DataFrame(spectrum)
					data_frame.columns = ['signal_strength', 'attention', 'meditation', 'delta', 'theta', 'low_alpha', 'high_alpha', 'low_beta', 'high_beta', 'low_gamma', 'high_gamma', 'time']
					data_frame.to_csv(csv_filename, sep=';')
					total_samples_collected = total_samples_collected + 1

				ax.relim()
				ax.autoscale_view()
				line_object_a.set_data(x,attention)

				bx.relim()
				bx.autoscale_view()
				line_object_b.set_data(x,meditation)

				cx.relim()
				cx.autoscale_view()
				line_object_c.set_data(x,delta)

				dx.relim()
				dx.autoscale_view()
				line_object_d.set_data(x,theta)

				ex.relim()
				ex.autoscale_view()
				line_object_e.set_data(x,low_alpha)

				fx.relim()
				fx.autoscale_view()
				line_object_f.set_data(x,high_alpha)

				gx.relim()
				gx.autoscale_view()
				line_object_g.set_data(x,low_beta)

				hx.relim()
				hx.autoscale_view()
				line_object_h.set_data(x,high_beta)

				ix.relim()
				ix.autoscale_view()
				line_object_i.set_data(x,low_gamma)

				jx.relim()
				jx.autoscale_view()
				line_object_j.set_data(x,high_gamma)

				plt.pause(1)

				current_timer = current_timer + 1
				print current_timer
		except Exception as e:
			print e











