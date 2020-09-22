import pickle

# need to run in Python 3

with open("FRB/190303.J1353+48.pkl", "rb") as f:
    data = pickle.load(f)

with open("FRB/190303.J1353+48.pkl", "wb") as f:
    pickle.dump(data, f, protocol=2)