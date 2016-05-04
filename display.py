class Display():
    def __init__(self):
        self.sides = ["",""]
        self.prev_diff = 0

    def push(self, side, data):
        self.sides[side] = data;
        if len(self.sides[0]) > 0 and len(self.sides[1]) > 0:
            a = self.sides[0].split(":")[1]
            b = self.sides[1].split(":")[1]
           
            x = 0
            y = 0 
            try:
                x = int(a,16)
                y = int(b,16) 

            except:
                pass

            diff = x - y
            delta_diff = diff - self.prev_diff
            self.prev_diff = diff
 
            print(a + "\t" + b + "\t" + ('%8d' % (diff,)) + "\t" + ('%8d' % (delta_diff,)))
            self.sides[0] = ""
            self.sides[1] = ""
