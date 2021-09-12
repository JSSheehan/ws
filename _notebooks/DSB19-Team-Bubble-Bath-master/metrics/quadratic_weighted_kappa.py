from sklearn.metrics import cohen_kappa_score

def quadratic_weighted_kappa(actual, pred):
    return cohen_kappa_score(actual, pred, weights='quadratic')