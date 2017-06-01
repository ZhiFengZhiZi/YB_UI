

class LogC(object):

    """description of class"""

    def __init__(self,filename='',message=''):
        self.filename = filename
        self.message = message



    # use nosetests command to execute test case list
    def LoadAndRunTestCases(self):

        print("2")
        f = open('D:\Python_Log.'+ self.filename +'.txt','w+')
        f.write(self.message)
        f.close()


if __name__ == "__main__":
    newrun = LogC()
    newrun.LoadAndRunTestCases()


