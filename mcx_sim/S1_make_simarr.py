import json
import os
import numpy as np
import sys
import pandas as pd

TISSUES = ['skin', 'fat', 'muscle', 'ijv', 'cca']

def Get_OPs_set(bound: dict, split_num: list, OP_type: str, savepath: str):
    '''
    bound['tissue'] = [upperbound, lowerbound]
    len(split_num) = len(tissues)
    OP_type = mus or mua
    ijv mus = cca mus
    '''
    assert len(bound) != len(split_num), 'tissues and split size not match'
    if OP_type == 'mus':
        assert split_num[-1] == split_num[-2], 'ijv mus should be same as cca mus'
    
    OPs_table_train = {}
    OPs_table_test = {}
    train_conditions = 1
    test_conditions = 1
    for i, tissue in enumerate(TISSUES):
        if OP_type == 'mus' and tissue == 'cca':
            break
        if OP_type =='mus' and tissue == 'ijv':    
            OPs_table_train[tissue] = list(np.linspace(bound[tissue][0]-20, bound[tissue][1], 2*split_num[i]))[::2]  # simulate low scattering region
            OPs_table_test[tissue] = list(np.linspace(bound[tissue][0]-20, bound[tissue][1], 2*split_num[i]))[1::2]  # simulate low scattering region
        else:
            OPs_table_train[tissue] = list(np.linspace(bound[tissue][0], bound[tissue][1], 2*split_num[i]))[::2]
            OPs_table_test[tissue] = list(np.linspace(bound[tissue][0], bound[tissue][1], 2*split_num[i]))[1::2]
        train_conditions *= len(OPs_table_train[tissue])
        test_conditions *= len(OPs_table_test[tissue])

    # get train set
    OPs_set_train = np.zeros((train_conditions,len(TISSUES)))
    idx = 0
    for skin_OP in OPs_table_train['skin']:
        for subcuit_OP in OPs_table_train['fat']:
            for muscle_OP in OPs_table_train['muscle']:
                for ijv_OP in OPs_table_train['ijv']:
                    if OP_type == 'mus': # cca mus = ijv mus
                        OPs_set_train[idx][0] = skin_OP
                        OPs_set_train[idx][1] = subcuit_OP
                        OPs_set_train[idx][2] = muscle_OP
                        OPs_set_train[idx][3] = ijv_OP
                        OPs_set_train[idx][4] = OPs_set_train[idx][3]
                        idx += 1
                    elif OP_type == 'mua':
                        for cca_OP in OPs_table_train['cca']:
                            OPs_set_train[idx][0] = skin_OP
                            OPs_set_train[idx][1] = subcuit_OP
                            OPs_set_train[idx][2] = muscle_OP
                            OPs_set_train[idx][3] = ijv_OP
                            OPs_set_train[idx][4] = cca_OP
                            idx += 1
    np.save(os.path.join(savepath, f'{OP_type}_set_train.npy'), OPs_set_train)
    OPs_set_train = pd.DataFrame(OPs_set_train, columns=TISSUES)
    OPs_set_train.to_csv(os.path.join(savepath, f'{OP_type}_set_train.csv'), index=False)
    
    # get test set
    OPs_set_test = np.zeros((test_conditions,len(TISSUES)))
    idx = 0
    for skin_OP in OPs_table_test['skin']:
        for subcuit_OP in OPs_table_test['fat']:
            for muscle_OP in OPs_table_test['muscle']:
                for ijv_OP in OPs_table_test['ijv']:
                    if OP_type == 'mus': # cca mus = ijv mus
                        OPs_set_test[idx][0] = skin_OP
                        OPs_set_test[idx][1] = subcuit_OP
                        OPs_set_test[idx][2] = muscle_OP
                        OPs_set_test[idx][3] = ijv_OP
                        OPs_set_test[idx][4] = OPs_set_test[idx][3]
                        idx += 1
                    elif OP_type == 'mua':
                        for cca_OP in OPs_table_test['cca']:
                            OPs_set_test[idx][0] = skin_OP
                            OPs_set_test[idx][1] = subcuit_OP
                            OPs_set_test[idx][2] = muscle_OP
                            OPs_set_test[idx][3] = ijv_OP
                            OPs_set_test[idx][4] = cca_OP
                            idx += 1
    # randomly choose 10% datasize 
    if OP_type == 'mus':
        np.random.shuffle(OPs_set_test)
        OPs_set_test = OPs_set_test[:int(OPs_set_test.shape[0]*0.1)]
        
    np.save(os.path.join(savepath, f'{OP_type}_set_test.npy'), OPs_set_test)
    OPs_set_test = pd.DataFrame(OPs_set_test, columns=TISSUES)
    OPs_set_test.to_csv(os.path.join(savepath, f'{OP_type}_set_test.csv'), index=False)
    
    
    return OPs_set_train,  OPs_set_test

if __name__ == "__main__":
    # Get Mus set
    with open(os.path.join("OPs_used", "mus_bound.json"), "r") as f:
        mus_bound = json.load(f)
    mus_tissues = ['skin', 'fat', 'muscle', 'ijv', 'cca']
    split_num = [5, 5, 3, 3, 3]
    savepath = 'OPs_used'
    mus_set = Get_OPs_set(bound = mus_bound, 
                          split_num = split_num, 
                          OP_type = 'mus', 
                          savepath = savepath)

    # Get Mua set
    with open(os.path.join("OPs_used", "mua_bound.json"), "r") as f:
        mua_bound = json.load(f)
    mua_tissues = ['skin', 'fat', 'muscle', 'ijv', 'cca']
    split_num = [3, 3, 5, 7, 7]
    savepath = 'OPs_used'
    mua_set = Get_OPs_set(bound = mua_bound, 
                          split_num = split_num, 
                          OP_type = 'mua', 
                          savepath = savepath)


