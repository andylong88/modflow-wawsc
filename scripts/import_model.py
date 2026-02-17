# This code imports a MODFLOW model as ml and saves it to 

import pickle
import flopy

model_ws = r"../imported_models/SES_example/model/SES_ss" 
namfile = "SES_ss.nam"  # your name file

ml = flopy.modflow.Modflow.load(
    namfile,
    model_ws=model_ws,
    version="mfnwt",   # or "mf2k", "mfnwt", "mfusg"
    verbose=True,
    check=False         # often helpful to bypass strict checks
)

with open("../imported_models/SES_example/model.pkl", "wb") as f:
    pickle.dump(ml, f)
