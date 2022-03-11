import numpy as np
import os
import h5py
import json

if __name__ == '__main__':
    f = h5py.File('../exps/datasets/demo_pick_and_place_bowl/keyboard.hdf5', 'r')
    env_info = json.loads(f['data'].attrs['env_info'])
    print(f['data'].attrs['env_args'])

    # print(f['data'].attrs['env_args'])
    # demos = list(f['data'].keys())
    # inds = np.argsort([int(elem[5:]) for elem in demos])
    # demos = [demos[i] for i in inds]
    # print(demos)

    # for ind in range(2):
    #     ep = demos[ind]
    #     states = f['data/{}/states'.format(ep)][()]
    #     initial_state = dict(states=states[0])
    #     initial_state['model'] = f['data/{}'.format(ep)].attrs['model_file']
    #
    #     actions = f['data/{}/actions'.format(ep)][()]
    #
    #     print(states)
        # break