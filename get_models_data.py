import pandas as pd
import utils
def get_models_withdata():

    Model_data_file_path = utils.notebook+'/Telemetry_ModelPair.csv'

    data = pd.read_csv(Model_data_file_path, delimiter='\t', header=None)

    models = []

    for index, row in data.iterrows():
        model = {
            'Model': row[0],
            'training_data': row[1],
            'training_method': row[3].split('.')[1],
            'eval_data': row[6],
            'eval_method': row[8].split('.')[1]
        }
        models.append(model)


    return models


