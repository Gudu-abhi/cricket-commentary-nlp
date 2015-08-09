from .config import assets_path

class Mine(object):
    def __init__(self):
        self.data_file = open(assets_path+'text/data.txt')
        self.out_file = open(assets_path+'text/out.txt','a')
        self.no_run = ["no run"]
        self.one_run = ["1 run"]
        self.two_run = ["2 run"]
        self.four_run = ["FOUR"]
        self.six_run = ["SIX"]
        self.out = [" out Bowled", " out Caught", " out Lbw", "Run Out"]

    def extract(self):
        text = ""
        for line in self.data_file:
            if line == '\n':
                continue
            else:
                text = text+line
        text = text.split('\n')
        self.process(text)


    def process(self,data):
        cont = 0
        print ("ball-no|runs|is-out(Boolean)")
        for i in range(0, len(data)):
            val = data[i].split(' ', 1)[0]
            if self.isfloat(val):
                ball_no = val
                if any(ext in data[i] for ext in self.no_run):
                    runs = "No run"
                elif any(ext in data[i] for ext in self.one_run):
                    runs = 1
                elif any(ext in data[i] for ext in self.two_run):
                    runs = 2
                elif any(ext in data[i] for ext in self.four_run):
                    runs = 4
                elif any(ext in data[i] for ext in self.six_run):
                    runs = 6
                if any(ext in data[i] for ext in self.out):
                    is_out = True
                    cont+=1
                    runs = 0
                elif not any(ext in data[i] for ext in self.out):
                    is_out = False
                print (str(ball_no)+"|"+str(runs)+"|"+str(is_out))
                self.out_file.write(str(ball_no)+"|"+str(runs)+"|"+str(is_out)+"\n")


    def isfloat(self,value):
        try:
            float(value)
            return True
        except:
            return False
