import pandas as pd
import numpy as np
import random

#######################
# FUNCTION DEFINITION #
#######################


def sigmoid(x):
    '''
    This function

    ARGS:
        x

    RETURN:
        return
    '''
    return 1 / (1 + np.exp(-x))


def sigmoidDeriv(x):
    '''
    This function

    ARGS:
        x

    RETURN:
        return
    '''
    return sigmoid(x) * (1 - sigmoid(x))


def cleanData(dataset):
    '''
    This function

    ARGS:
        x

    RETURN:
        return
    '''
    dataset = dataset.replace('yes', 1.0)
    dataset = dataset.replace('no', 0.0)
    dataset = dataset.replace(',', '.')
    return dataset


def generateRandom(rows, columns):
    '''
    This function

    ARGS:
        x

    RETURN:
        return
    '''
    array = np.random.randn(rows, columns)
    return array


def vector(d1Matrix):
    '''
    This function

    ARGS:
        x

    RETURN:
        return
    '''
    size = d1Matrix.size
    d1Matrix = d1Matrix.reshape(size, 1)
    return d1Matrix


def randomSelect(inputArray, expectedArray):
    '''
    This function

    ARGS:
        x

    RETURN:
        return
    '''
    randomNum = random.randint(1, 102) - 1
    inputValue = inputArray[randomNum, :]
    expected = expectedArray[randomNum, :]

    inputValue = vector(inputValue)
    expected = vector(expected)
    return inputValue, expected


def dataAccessing():
    data = pd.read_excel('dataset.xlsx', header=None)
    result = pd.read_excel('decision.xlsx', header=None)

    # table conversion to float and binary values
    data = cleanData(data)
    result = cleanData(result)

    # conversion to numpy array
    inputArray = np.asarray(data)
    expectedArray = np.asarray(result)
    return inputArray, expectedArray


def setting(inputNodes, hiddenNodes, outputNodes, NumOfRepets, learningRate):
    '''
    This function

    ARGS:
        x

    RETURN:
        return
    '''

    # Dataset reading
    inputArray, expectedArray = dataAccessing()
    '''
    INICIALIZATION
    '''

    # Generating weights and bias randomly
    weightsIH = generateRandom(hiddenNodes, inputNodes)
    weightsHO = generateRandom(outputNodes, hiddenNodes)
    biasH = generateRandom(hiddenNodes, 1)
    biasO = generateRandom(outputNodes, 1)
    '''
    TRAINING
    '''
    for i in range(NumOfRepets):
        # Selecting values randomly to use in the training
        inputValue, expected = randomSelect(inputArray, expectedArray)

        # Generating hidden outputs
        hidden = sigmoid(np.dot(weightsIH, inputValue) + biasH)

        # Generating output output
        output = sigmoid(np.dot(weightsHO, hidden) + biasO)

        # ---- HO error calculation --------
        outputError = expected - output

        # Calculate HO gradient
        outputGradient = sigmoidDeriv(output)
        outputGradient = outputGradient * outputError
        outputGradient = outputGradient * learningRate

        # Calculate HO weight's deltas
        weightsHO_d = np.matmul(outputGradient, hidden.transpose())

        # Adjustment HO w/ deltas
        weightsHO = weightsHO + weightsHO_d
        biasO = biasO + outputGradient

        # ----- IH error calculation --------
        hiddenError = np.matmul(weightsHO.transpose(), outputError)

        # Calculate IH gradient
        hiddenGradient = sigmoidDeriv(hidden)
        hiddenGradient = hiddenGradient * hiddenError
        hiddenGradient = hiddenGradient * learningRate

        # Calculate IH weight's deltas
        weightsIH_d = np.matmul(hiddenGradient, inputValue.transpose())

        # Adjustment IH w/ deltas
        weightsIH = weightsIH + weightsIH_d
        biasH = biasH + hiddenGradient
        if i % 50000 == 0:
            print("iteration no.", i)


#   print( "outputError: ", outputError, "\n\n\nhiddenError: ", hiddenError)
    return weightsIH, biasH, weightsHO, biasO


def predict(inputValue, weightsIH, biasH, weightsHO, biasO):
    '''
    This function

    ARGS:
        x

    RETURN:
        return
    '''
    inputValue = vector(inputValue)

    # Generating hidden output
    hidden = sigmoid(np.matmul(weightsIH, inputValue) + biasH)

    # Generating output output
    output = sigmoid(np.matmul(weightsHO, hidden) + biasO)

    print("The machine has made its guess\n", output)
