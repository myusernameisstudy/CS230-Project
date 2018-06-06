import h5py
import numpy as np
from scipy.signal import decimate

r = 4


def decimate_helper(arr):
    return decimate(arr, r, axis=0)

def load_h5(h5_path):
  # load training data
  with h5py.File(h5_path, 'r') as hf:
    print 'List of arrays in input file:', hf.keys()
    X = np.array(hf.get('data'))
    Y_HR = np.array(hf.get('label'))
    Y_LR = np.apply_along_axis(decimate_helper, 1, Y_HR)
    #print Y.shape
    return Y_HR, Y_LR
    #really sketchy, but begins the concatenation so that vstack can be done later
    # x_hr0 = Y[0]
    # print x_hr0.shape
    # x_hr1 = Y[1]
    # print x_hr1.shape
    # x_lr0 = decimate(x_hr0, r, axis=0)
    # x_lr1 = decimate(x_hr1, r, axis=0)
    # print (Y_out[0] == x_lr0)
    # print (Y_out[1] == x_lr1)

    # X_hr = np.vstack((x_hr0, x_hr1))
    # X_lr = np.vstack((x_lr0, x_lr1))

    # for i in range(2, Y.shape[0]):
    #     newx_hr = Y[i]
    #     newx_lr = decimate(newx_hr, r, axis=0)
    #     X_hr = np.vstack((X_hr, newx_hr))
    #     X_lr = np.vstack((X_lr, newx_lr))
    # print(X_hr.shape)
    # print(X_lr.shape)
    # print(X_lr == Y_out)
    # print 'Shape of X:', X.shape
    # print 'Shape of Y:', Y.shape

def main():
    load_h5('./data/vctk/speaker1/vctk-speaker1-train.4.16000.8192.4096.h5')

if __name__ == '__main__':
    main()
