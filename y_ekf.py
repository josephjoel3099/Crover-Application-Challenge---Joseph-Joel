import numpy as np
from numpy.linalg import inv
import pandas

gnss = pandas.read_csv("gnss.csv")
odom = pandas.read_csv("odom.csv")

x_observations = []
v_observations = []
y = []


def prediction2d(x, v, t, a):
    A = np.array([[1, t],
                  [0, 1]])
    X = np.array([[x],
                  [v]])
    B = np.array([[0.5 * t ** 2],
                  [t]])
    X_prime = A.dot(X) + B.dot(a)
    return X_prime


def covariance2d(sigma1, sigma2):
    cov1_2 = sigma1 * sigma2
    cov2_1 = sigma2 * sigma1
    cov_matrix = np.array([[sigma1 ** 2, cov1_2],
                           [cov2_1, sigma2 ** 2]])
    return np.diag(np.diag(cov_matrix))


for i in range(0, len(gnss["real_time"])):
    x_observations.append(gnss["position_y"][i])
    v_observations.append(odom["linear_y"][i * 5])

print(len(x_observations))
print(len(v_observations))

for i in range(0, len(x_observations) - 2):
    print(i)
    z = np.c_[x_observations[i:2 + i], v_observations[i:2 + i]]

    # Initial Conditions
    a = 1
    v = 0.1
    t = 1

    # Process / Estimation Errors
    error_est_x = 20  # Tuning param
    error_est_v = 10  # Tuning param

    # Observation Errors
    error_obs_x = 26  # Tuning param
    error_obs_v = 2   # Tuning param

    P = covariance2d(error_est_x, error_est_v)
    A = np.array([[1, t],
                  [0, 1]])

    X = np.array([[z[0][0]],
                  [v]])
    n = len(z[0])

    for data in z[1:]:
        X = prediction2d(X[0][0], X[1][0], t, a)
        P = np.diag(np.diag(A.dot(P).dot(A.T)))
        H = np.identity(n)
        R = covariance2d(error_obs_x, error_obs_v)
        S = H.dot(P).dot(H.T) + R
        K = P.dot(H).dot(inv(S))
        Y = H.dot(data).reshape(n, -1)
        X = X + K.dot(Y - H.dot(X))
        P = (np.identity(len(K)) - K.dot(H)).dot(P)

    print("Kalman Filter State Matrix:\n", X)
    y.append(X[0][0])

data = {
    'y': y}

df = pandas.DataFrame(data)
df.to_csv('y.csv')
