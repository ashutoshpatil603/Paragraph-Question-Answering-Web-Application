import joblib
from model import Model

if __name__=="__main__":
    model = Model()
    joblib.dump(model,'QAmodel5_jlib')
