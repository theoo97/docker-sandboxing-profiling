import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
import sklearn.metrics as metrics

measurements={
'cpu': {
    'no-sandbox': [1.55, 1.61, 2.15, 2.64, 3.21, 3.76, 4.34, 4.89, 5.35, 6.00, 6.39, 6.85, 7.49, 7.94, 8.48, 9.01, 9.52, 10.08, 10.63],
    'docker': [3.32, 2.74, 3.34, 4.00, 4.85, 5.29, 5.96, 6.89, 7.52, 8.21, 8.84, 8.89, 9.34, 9.99, 10.61, 11.20, 11.76, 12.46, 13.17],
    'gvisor': [3.16, 2.63, 3.07, 3.73, 4.42, 4.94, 5.55, 6.28, 6.89, 7.37, 8.75, 9.24, 9.33, 9.95, 10.78, 12.20, 13.05, 13.68, 14.40],
    'kata': [9.80, 12.61, 14.22, 17.38, 20.00, 21.63, 24.38, 27.34, 29.31, 31.89, 34.83, 37.39, 39.00, 42.08, 44.59, 46.33, 49.08, 51.94, 54.76],
    'firecracker': [12.79, 15.74, 17.62, 20.26, 23.24, 25.09, 27.58, 30.69, 32.18, 34.84, 38.12, 40.57, 42.63, 45.04, 48.26, 49.97, 52.48, 55.13, 58.46]
},

'memory-management': {
    'no-sandbox': [2.50, 1.57, 6.17, 4.88, 5.41, 2.90, 7.08, 5.18, 7.97, 8.26, 8.85, 9.82, 7.13, 6.77, 4.08, 13.49, 10.73, 15.20, 16.11],
    'docker': [1.18, 1.23, 1.32, 1.31, 1.40, 1.64, 1.62, 1.68, 1.79, 1.87, 1.97, 2.08, 2.08, 2.75, 2.24, 2.33, 2.43, 2.49, 2.58],
    'gvisor': [3.05, 1.82, 1.97, 2.20, 2.28, 2.44, 2.56, 2.79, 2.91, 3.01, 3.18, 3.18, 3.40, 4.04, 4.33, 4.50, 4.00, 4.07, 4.18],
    'kata': [4.66, 4.73, 4.80, 4.90, 5.17, 5.21, 5.30, 5.42, 5.48, 5.58, 5.65, 5.74, 5.80, 5.94, 5.96, 6.00, 6.13, 6.26, 6.32],
    'firecracker': [55.92, 68.30, 60.89, 78.32, 79.46, 112.26, 80.95, 106.93, 114.53, 161.91, 153.43, 127.27, 157.76, 181.92, 167.71, 193.89, 187.94, 160.06, 153.22]
},

'process-management': {
    'no-sandbox': [.85, 1.16, 1.53, 1.89, 2.25, 2.65, 3.04, 3.37, 3.76, 4.14, 4.46, 4.88, 5.20, 5.62, 5.91, 6.38, 6.73, 7.07, 7.47],
    'docker': [2.20, 3.20, 3.39, 4.20, 5.43, 5.03, 6.33, 7.43, 7.39, 7.35, 9.38, 9.80, 9.40, 10.75, 11.79, 11.74, 12.83, 12.36, 16.34],
    'gvisor': [8.89, 12.42, 16.81, 26.33, 31.71, 27.34, 34.71, 40.99, 50.08, 53.91, 50.93, 49.40, 59.29, 70.93, 73.52, 66.51, 76.58, 79.36, 84.59],
    'kata': [5.19, 5.71, 6.21, 6.62, 7.18, 7.66, 7.98, 8.55, 8.98, 9.40, 9.86, 10.38, 10.97, 11.31, 11.82, 12.25, 13.67, 13.20, 13.81],
    'firecracker': [10.27, 11.55, 11.40, 11.43, 11.70, 12.66, 13.95, 13.70, 13.24, 13.82, 14.27, 15.80, 15.32, 17.11, 16.09, 16.95, 17.81, 17.24, 19.52]
},

'network': {
    'no-sandbox': [1.08, 1.58, 2.16, 2.88, 3.44, 3.81, 4.68, 5.21, 5.95, 6.28, 7.24, 8.15, 8.79, 9.15, 9.66, 10.63, 10.99, 11.54, 12.06],
    'docker': [1.63, 1.63, 2.09, 2.33, 2.37, 2.70, 3.16, 3.94, 4.01, 4.36, 4.98, 5.04, 4.60, 5.88, 5.04, 6.40, 5.61, 7.11, 7.22],
    'gvisor': [6.26, 9.27, 11.97, 15.01, 17.68, 20.83, 23.67, 26.79, 29.63, 32.77, 35.69, 39.21, 42.07, 45.59, 48.11, 50.86, 53.98, 56.80, 60.75],
    'kata': [4.93, 5.05, 5.33, 5.59, 5.86, 6.03, 6.33, 6.66, 12.97, 7.09, 7.61, 7.61, 7.75, 8.04, 8.21, 8.42, 15.45, 9.53, 9.31],
    'firecracker': [8.70, 8.88, 10.95, 11.49, 11.71, 8.94, 12.70, 14.87, 11.96, 13.28, 13.56, 18.46, 13.87, 10.70, 20.88, 11.13, 22.60, 14.92, 23.74]
},

'file-io': {
    'no-sandbox': [3.21, 4.65, 6.20, 7.24, 8.98, 10.41, 10.51, 11.60, 12.97, 15.46, 17.51, 17.69, 18.84, 23.17, 23.07, 26.18, 27.85, 32.18, 27.54],
    'docker': [4.43, 6.11, 7.88, 9.27, 10.35, 13.32, 13.78, 15.83, 17.56, 18.97, 22.31, 24.87, 25.86, 27.39, 27.65, 32.60, 31.19, 33.74, 36.16],
    'gvisor': [2.11, 2.82, 3.56, 4.26, 4.91, 5.61, 6.29, 7.01, 7.80, 8.45, 9.16, 9.90, 10.48, 11.36, 12.22, 12.63, 13.45, 14.41, 15.19],
    'kata': [5.59, 5.56, 6.13, 6.56, 6.11, 7.62, 7.30, 8.13, 7.06, 9.00, 10.68, 11.80, 13.27, 9.20, 14.52, 12.75, 14.89, 11.31, 11.35],
    'firecracker': [9.69, 9.71, 11.29, 10.74, 11.57, 12.55, 13.70, 14.63, 15.23, 16.31, 17.44, 16.32, 17.73, 19.28, 20.06, 20.19, 21.49, 20.91, 22.27]
}
}

for key in measurements:
    print(key, measurements[key])


def regression_results(y_true, y_pred):
    # Regression metrics
    explained_variance=metrics.explained_variance_score(y_true, y_pred)
    mean_absolute_error=metrics.mean_absolute_error(y_true, y_pred)
    mse=metrics.mean_squared_error(y_true, y_pred)
    mean_squared_log_error=metrics.mean_squared_log_error(y_true, y_pred)
    median_absolute_error=metrics.median_absolute_error(y_true, y_pred)
    r2=metrics.r2_score(y_true, y_pred)

    print('explained_variance: ', round(explained_variance,4))
    print('mean_squared_log_error: ', round(mean_squared_log_error,4))
    print('r2: ', round(r2,4))
    print('MAE: ', round(mean_absolute_error,4))
    print('MSE: ', round(mse,4))
    print('RMSE: ', round(np.sqrt(mse),4))


ops = np.linspace(1, 10, 19)
ops.shape=(19,1)
x_new = np.linspace(1, 10, 19)


def regression(runtimes):
    runtimes = np.array(runtimes)
    runtimes.shape=(19,1)

    # create a linear regression model
    model = LinearRegression()
    reg = model.fit(ops, runtimes)
    # predict y from the data
    y_predict = model.predict(x_new[:, np.newaxis])

    mse=metrics.mean_squared_error(runtimes, y_predict)
    rmse = round(np.sqrt(mse), 2)

    a = round(reg.coef_[0][0], 2)
    b = round(reg.intercept_[0], 2)

    return y_predict, a, b, rmse

fig, axs = plt.subplots(2, 2)
title_font_size=11

def process_subplot(ax, component, env, title):

    ax.set_title(title, fontsize=title_font_size)
    ax.scatter(ops, measurements[component][env])

    y_predict, a, b, rmse = regression(measurements[component][env])
    ax.plot(x_new, y_predict)

    ax.text(x_new[-1] + 0.1, y_predict[-1] + 0.1, env)
    ax.axis('tight')

    print("T_%s_%s(ops)= %f * ops + %f" % (component, env, a, b))

    return a, b, rmse


title1='No Sandbox, Docker - T(ops) - measured in seconds'
title2='gVisor, Kata, Firecracker - T(ops) - measured in seconds'

component='cpu'
a_no_sandbox, b_no_sandbox, rmse = process_subplot(axs[0, 0], component, 'no-sandbox', title1)
a_docker, b_docker, rmse = process_subplot(axs[0, 0], component, 'docker', title1)
a_gvisor, b_gvisor, rmse = process_subplot(axs[0, 1], component, 'gvisor', title2)
a_kata, b_kata, rmse = process_subplot(axs[0, 1], component, 'kata', title2)
a_firecracker, b_firecracker, rmse = process_subplot(axs[0, 1], component, 'firecracker', title2)

print(b_no_sandbox)




environments = ['no-sandbox', 'Docker', 'gVisor', 'Kata', 'Firecracker']
y_intercept = [b_no_sandbox, b_docker, b_gvisor, b_kata, b_firecracker]
axs[1, 0].bar(environments, y_intercept)
axs[1, 0].set_title("Y intercepts (seconds)", fontsize=title_font_size)


environments = ['no-sandbox', 'Docker', 'gVisor', 'Kata', 'Firecracker']
slopes = [a_no_sandbox, a_docker, a_gvisor, a_kata, a_firecracker]
barlist=axs[1, 1].bar(environments, slopes)
axs[1, 1].set_title("Slopes (seconds)", fontsize=title_font_size)


plt.show()


