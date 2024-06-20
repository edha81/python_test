from a import com
class windows(com):
    def __init__(self,name,num,os,mem):
        self.name =name
        self.num =num
        self.os =os
        self.mem = mem
        
        def p_mem(self):
            print(self.mem)