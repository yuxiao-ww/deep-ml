import numpy as np
def precision(y_true, y_pred):
	tp = np.sum((y_true == 1) & (y_pred == 1))
	fp = np.sum((y_true == 0) & (y_pred == 1))
	fn = np.sum((y_true == 1) & (y_pred == 0))

	precision = tp / (tp + fp) if tp+fp else 0.0
	return precision
