class Phone:
    def __init__(self,os,num,is_waterproof):
        self.os =os
        self.num = num
        self.is_waterproof=is_waterproof

    def is_ios(self):
        if self.os == 'ios':
            return True
        else:
            return False
    
    def add(self,num1,num2):
        return num1+num2
    
phone1=Phone('ios',14,False)
print(phone1.is_ios())

print(phone1.add(5,6))