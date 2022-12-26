import numpy as np

def calculate(list):
  
 
    
     
    if len(list)<9:
      raise ValueError ( "List must contain nine numbers.")
   
      
    arr = np.array(list).reshape(3,3)  
    meanAxis1 = np.mean(arr, axis = 0)
    meanAxis2 = np.mean(arr, axis = 1)
    meanFlattened = np.mean(arr)
    Mmean = [meanAxis1.tolist(), meanAxis2.tolist(), meanFlattened.tolist() ]
    print(arr) 
    print(Mmean)
    
    varAxis1 = np.var(arr, axis = 0)
    varAxis2 = np.var(arr, axis = 1)
    varFlattened = np.var(arr)
    variance = [varAxis1.tolist(), varAxis2.tolist(), varFlattened.tolist() ]
  
    STDAxis1 = np.std(arr, axis = 0)
    STDAxis2 = np.std(arr, axis = 1)
    STDFlattened = np.std(arr)
    STD = [STDAxis1.tolist(), STDAxis2.tolist(), STDFlattened.tolist() ]

    maxAxis1 = np.max(arr, axis = 0)
    maxAxis2 = np.max(arr, axis = 1)
    maxFlattened = np.max(arr)
    max = [maxAxis1.tolist(), maxAxis2.tolist(), maxFlattened.tolist() ]
  
    minAxis1 = np.min(arr, axis = 0)
    minAxis2 = np.min(arr, axis = 1)
    minFlattened = np.min(arr)
    min = [minAxis1.tolist(), minAxis2.tolist(), minFlattened.tolist() ]
  
    sumAxis1 = np.sum(arr, axis = 0)
    sumAxis2 = np.sum(arr, axis = 1)
    sumFlattened = np.sum(arr)
    summarise = [sumAxis1.tolist(), sumAxis2.tolist(), sumFlattened.tolist() ]
  
    calculations = {
  'mean': Mmean,
  'variance': variance,
  'standard deviation': STD,
  'max': max,
  'min': min,
  'sum': summarise
 }



    return calculations
