__author__ = "Jakob Aungiers"
__copyright__ = "Jakob Aungiers 2018"
__version__ = "2.0.0"
__license__ = "MIT"

import os
import json
import time
import math
import matplotlib.pyplot as plt
from core.data_processor import DataLoader
from core.model import Model
import pandas as pd
import math
from sklearn.metrics import mean_absolute_error
from sklearn.utils.validation import check_array

def plot_results(predicted_data, true_data):

    fig = plt.figure(facecolor='white')

    ax = fig.add_subplot(111)

    ax.plot(true_data, label='True Data')

    plt.plot(predicted_data, label='Prediction')

    plt.legend()
    plt.show()

def main():

    configs = json.load(open('config.json', 'r'))
    if not os.path.exists(configs['model']['save_dir']): os.makedirs(configs['model']['save_dir'])

    data = DataLoader(
        os.path.join('data', configs['data']['filename']),
        configs['data']['train_test_split'],
        configs['data']['columns']
    )

    model = Model()

    # model.build_model(configs)
    model.load_model("saved_models/amazon_60%.h5")

    x, y = data.get_train_data(
        seq_len=configs['data']['sequence_length'],
        normalise=configs['data']['normalise']
    )

    # out-of memory generative training
    steps_per_epoch = math.ceil((data.len_train - configs['data']['sequence_length']) / configs['training']['batch_size'])

    model.train_generator(

        data_gen=data.generate_train_batch(

            seq_len=configs['data']['sequence_length'],
            batch_size=configs['training']['batch_size'],
            normalise=configs['data']['normalise']

        ),

        epochs=configs['training']['epochs'],

        batch_size=configs['training']['batch_size'],

        steps_per_epoch=steps_per_epoch,

        save_dir=configs['model']['save_dir']

    )

    x_test, y_test = data.get_test_data(
        seq_len=configs['data']['sequence_length'],
        normalise=configs['data']['normalise']
    )

    print("x_test.shape")
    print(x_test.shape)

    predictions = model.predict_point_by_point(x_test)

    ########################################################################
    from sklearn.metrics import mean_squared_error
    # loss_final = mean_squared_error(predictions, y_test)
    # print("Testing Loss = " + str(loss_final))
    ########################################################################

    # plot_results_multiple(predictions, y_test, configs['data']['sequence_length'])

    print(predictions.shape)
    print(y_test.shape)

    m = pd.DataFrame(predictions)
    n = pd.DataFrame(y_test)

    m.to_csv("predictions.csv")
    n.to_csv("y_test.csv")

    p = 0
    t = 0

    t_1 = 0

    count = 0

    for a in range(len(predictions)):

        if(a==0):
            t_1 = y_test[a]
            continue

        '''
            1 1 1 1 1 1 1 1 1
            1 1 1 1 1 1 1 1 1
        
        '''

        p = predictions[a]
        t = y_test[a]

        match = (t - t_1)*(p - t_1)

        if(match > 0):
            count += 1

        t_1 = t

    print(  "Good prediction rate = " + str( count/len(predictions) ) )

    plot_results(predictions, y_test)

# "OPEN","HIGH","LOW","CLOSE","VOLUME","NUMBER OF TRADES","WEIGHTED AV. PRICE","YEAR","MONTH","DAY","HOUR","MINUTES","SECONDS",

# "Open", "High","Low",  "Close","Volume" "Net", "%Chg", , "O-C", "H-L", "%CVol", "M", "D", "Y", "H", "Min"

# NAS_Day   "Exchange Date","Close","Net","%Chg","Open","Low","High","Volume","O-C","H-L","%CVol"

# dow_30  "seq", "Close", "Open", "Low", "High", "Volume", "O-C", "H-L", "M", "D", "Y", "H", "Min"


if __name__ == '__main__':
    main()