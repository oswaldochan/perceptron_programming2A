import functions as f
import warnings
warnings.filterwarnings("ignore")


def main():
    for i in range(111, 112):
        numberOfRepets = 800000
        learningRate = 5
        inputNodes = 6
        hiddenNodes = 13
        outputNodes = 2
        print(
            "numOfCycles:\tLearningRate:\tinputNodes:\thiddenNodes:\toutputNodes:"
        )
        print("-->", numberOfRepets, "\t-->", learningRate, "\t\t--> 6\t\t-->",
              hiddenNodes, "\t\t--> 2")

        weightsIH, biasH, weightsHO, biasO = f.setting(inputNodes, hiddenNodes,
                                                       outputNodes,
                                                       numberOfRepets,
                                                       learningRate)

        inputArray, expectedArray = f.dataAccessing()
        testinput = inputArray[i, :]
        print("\n\n\ttestinput:\t\t\texpectedArray:")
        print(testinput, "\t", expectedArray[i, :])
        print("\n\n\n")
        f.predict(testinput, weightsIH, biasH, weightsHO, biasO)
        print("\n\n\n\n\n\n\n\n\n")

    input("press any key to finish the program")


main()
