import numpy as np;

def simple_regression_parameters(x,y,x_mean,y_mean):
    '''
    returns beta_hat1, beta_hat0
    '''
    beta_hat1 = np.sum((x - x_mean)*(y - y_mean)) / np.sum((x - x_mean)**2);
    beta_hat0 = y_mean - beta_hat1 * x_mean;
    return  beta_hat1, beta_hat0;

# def hypothesis_testing_p_value():
    