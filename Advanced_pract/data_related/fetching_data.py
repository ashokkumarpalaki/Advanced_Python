import pandas as pd

class FetchingData():
    def __init__(self):
        pass

    def data_frame(self):
        df = pd.read_csv('/home/ashok/Desktop/Python_II/Advanced_Python/Advanced_pract/files/reddit_vm.csv')

        # print(df.columns)
        # print(df)
        print(df.count())

    def main(self):
        data = {'Name':pd.Series(['Tom','James','Ricky','Vin','Steve','Smith','Jack',
   'Lee','David','Gasper','Betina','Andres']),
   'Age':pd.Series([25,26,25,23,30,29,23,34,40,30,51,46]),
   'Rating':pd.Series([4.23,3.24,3.98,2.56,3.20,4.6,3.8,3.78,2.98,4.80,4.10,3.65])
}
        df=pd.DataFrame(data)
        # print(df.sum(1))
        self.data_frame()



if __name__ == '__main__':
    fd = FetchingData()
    fd.main()
