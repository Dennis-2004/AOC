import numpy as np

class NN:
    def __init__(self, layerSizes, seed=None):
        self.layerSizes = layerSizes
        self.W = [np.random.randn(layerSizes[i], layerSizes[i+1]) for i in range(len(layerSizes)-1)]
        self.b = [np.zeros((1, layerSizes[i+1])) for i in range(len(layerSizes)-1)]
        self.A = [None] * len(layerSizes)
        self.Z = [None] * len(layerSizes)
        self.D = [None] * (len(layerSizes) - 1)  # Derivatives

        if seed is not None:
            np.random.seed(seed)

    def sigmoid(self, Z):
        return 1 / (1 + np.exp(-Z))

    def sigmoid_derivative(self, A):
        return A * (1 - A)

    def forward_pass(self, X, save=False):
        A = X
        for i in range(len(self.W)):
            Z = A @ self.W[i].T + self.b[i]
            A = self.sigmoid(Z)
            if save:
                self.A[i + 1] = A
                self.Z[i + 1] = Z
        return A

    def calculate_loss(self, Y):
        m = Y.shape[0]
        return np.sum((self.A[-1] - Y) ** 2) / (2 * m)

    def backprop(self, Y):
        m = Y.shape[0]
        dZ = self.A[-1] - Y
        dW = np.dot(self.A[-2].T, dZ) / m
        db = np.sum(dZ, axis=0, keepdims=True) / m
        self.D[-1] = (dW, db)

        for i in range(len(self.W) - 2, 0, -1):
            dZ = np.dot(dZ, self.W[i + 1]) * self.sigmoid_derivative(self.A[i])
            dW = np.dot(self.A[i - 1].T, dZ) / m
            db = np.sum(dZ, axis=0, keepdims=True) / m
            self.D[i] = (dW, db)

    def update_parameters(self, learning_rate):
        for i in range(len(self.W) - 1, -1, -1):
            self.W[i] -= learning_rate * self.D[i][0]
            self.b[i] -= learning_rate * self.D[i][1]

    def predict(self, X, save=False):
        A = X
        for i in range(len(self.W)):
            Z = A @ self.W[i].T + self.b[i]
            A = self.sigmoid(Z)
            if save:
                self.A[i + 1] = A
                self.Z[i + 1] = Z
        return A

# create network (with fixed seed ---needed for automatic grading---)
nn2 = NN(layerSizes=(2, 2, 1), seed=42)

# create test data
X = np.array([[0, 0], [0, 1], [1, 0], [1, 1]]).astype(float)
Y = np.array([[0], [1], [1], [0]])

# save the results of the forward propagation
nn2.predict(X, save=True)

# run back propagation to compute the derivatives
# of the (intermediary) activations
nn2.backprop(Y)

D_layer2 = nn2.D[1]  # these values will be tested
D_layer3 = nn2.D[2]  # these values will be tested

# print the losses
print(D_layer2)
print(D_layer3)
