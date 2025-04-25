class Path_plan:
    def __init__(self, gcp):
        """
        :param gcp- gcp pooints of path or boundary
        """
        self.gcp = gcp

        
    def path(self):

        k=[]
        for i in self.gcp:
            print("i :" ,i)
            k.append(i)
        
        self.save_path(k)
        return k

    def save_path(self, data):
        f = open('../data/path_points.txt', 'w')
        for item in data:
            print(item)
            f.write(str(item[0])+","+str(item[1])+"\r\n")
        f.close()
        print("path data stored to file in data/path_points.txt")
