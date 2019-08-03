#PERCEPTRON: ACUTE INFLAMMATIONS DATA SET
source: https://archive.ics.uci.edu/ml/datasets/Acute+Inflammations

# Final project of Programming: Data 2A. Oswaldo Chan, Alan Peraza, Luis Zapata.

1. Abstract.

- A perceptron is perhaps one of the most time-consuming forms of neural networks. Its implementation is present in some U.S. government documents in the 1960s.
Its function is to divide two classes (or variables) according to a series of discriminants already defined. This separation is represented by a straight line. This method is useful to be able to place a population in a certain group of characteristics, as well as possible predictions (of basic character, of course).



2. Objectives.

  - Understand the perceptron algorithm.
  - Choose two variables in the "Acute Inflamations Data Set" provided by the UCI machine learning repository using the perceptron.<-
  - Apply the perceptron algorithm in the data set mentioned before.
  
  
 3. Steps.
 
  - Understand the theoretical framework (Perceprton algorithm, correlation coeficient and neural network basic-concepts).
  - Understand the practical part (How it is applied, and what sort of result can we expect from it).
  - Understand how it is applied in Python and start coding the algorithm.
  - .Download the data set, convert it into a .dat file in order to be processed.
  - .Clean the data by deleting some extra characters (such as tabs an "\n" characters).
    - .Convert all alphabetic data into 1's and 0's (where 1 = True and 0 = False), in order to be easier to analyze and perform operations.
 
 
 4. Motivation(s).
 
 - To understand the machine learning and neural network basics.
 - To apply some of the topics seen in previous probability classes. 
 - To understand the relations between statistics and data science in their applications in the real-world problem solutions.
 - To learn how the databases can be applied for prediction-algorithms.
  
  
5. Description.

The description provided by UCI is as follows:
"The data was created by a medical expert as a data set to test the expert system, which will perform the presumptive diagnosis of two diseases of the urinary system."

Therefore, with the perceptron created, it is possible to predict whether a patient suffers from a certain urinary tract infection thanks to the symptoms present.

  °Variables to consider:
a1 Temperature of patient { 35C-42C }
a2 Occurrence of nausea { yes, no }
a3 Lumbar pain { yes, no }
a4 Urine pushing (continuous need for urination) { yes, no }
a5 Micturition pains { yes, no }
a6 Burning of urethra, itch, swelling of urethra outlet { yes, no }
d1 decision: Inflammation of urinary bladder { yes, no }
d2 decision: Nephritis of renal pelvis origin { yes, no } 

**As mentioned before, some parameter required a change to numerical values. Such cases are the "yes/no" form-provided information**

The team will proceed to choose the two most important variables in order to carry out the project (as mentioned in the objectives).

