# read the string filename
filename = input()

def readLogFile(logFile): 
  """
  reads log file for large response and return a dictionary with the count and sum of bytes greater than 5000

  :param: logfile: logfile input
  :return: response: dictory of the count and sum of the bytes greater than 5000
  """

  response = {
    "count": 0,
    "bytes": 0
  }

  # Reads the input from user
  with open(logFile) as f:
      # Goes through the line
      for line in f:
          lineList = line.strip().split()
          if(lineList[-1].isdigit()):
              num = (int)(lineList[-1])

          # Check if the
          if(num > 5000):
              response["count"] += 1
              response["bytes"] += num    

  return response  


def writeOutFile(outFile, data): 
  with open(outFile, "w") as f:
    f.write(data["count"])            
    f.write(data["bytes"])            

data = readLogFile(filename)
writeOutFile(f"bytes_{filename}", data)