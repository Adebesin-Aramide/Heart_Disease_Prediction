import joblib
import os
import numpy as np

def predict(features):
    #encoding dictionaries
    encoding_sex = {"Male": 0, "Female": 1}
    encoding_chestpain_type = {"Asymptomatic": 0, "Atypical Angina": 1, "Non Angina Pain": 2, "Typical Angina": 3}
    encoding_fastingbs = {"Otherwise": 0, "FastingBS > 120":1}
    encoding_exercise_angina = {"No": 0, "Yes": 1}
    encoding_ST_Slope = {"Downsloping": 0, "Flat": 1, "Upsloping": 2}
    
    
    
    
    features= np.array(features)
    
    features[:, 0] = [encoding_sex.get(item, -1) for item in features[:, 0]]
    features[:, 1] = [encoding_chestpain_type.get(item, -1) for item in features[:, 1]]
    features[:, 2] = [encoding_fastingbs.get(item, -1) for item in features[:, 2]]
    features[:, 3] = [encoding_exercise_angina.get(item, -1) for item in features[:, 3]]
    features[:, 4] = [encoding_ST_Slope.get(item, -1) for item in features[:, 5]]
    
    
    features = features.astype(float)
    
    model_path = os.path.join(os.path.dirname(__file__), "ensemble_pred2.pkl")
    ensembled_model = joblib.load(model_path)
    result = ensembled_model.predict(features)
    
    if result == 0:
        return "Normal"
    else:
        return "Heart Disease"