# class

def gcd(m,n):
    
    while m%n != 0:
        
        oldm = m
        oldn = n
        
        m = oldn
        n = oldm%oldn
        
    return n

class fraction:
    
    def __init__(self,top,bottom):
        self.num = top
        self.deno = bottom
        
    def show(self):
        print(self.num,'/',self.deno)
        
    def __str__(self):
        return str(self.num)+'/'+str(self.deno)
    
    def __add__(self,otherfraction):
        newdeno = (self.deno * otherfraction.deno)
        newnum = self.num*otherfraction.deno + otherfraction.num*self.deno       
        gdc_val = gcd(newnum,newdeno)   
        newnum = newnum//gdc_val
        newdeno = newdeno//gdc_val
        return str(newnum)+'/'+str(newdeno)
    
    
    def __eq__(self,other):
        
        firstnum = self.num * other.deno
        secondnum = other.num * self.deno
        
        return firstnum == secondnum


    def __mul__(self,other):

        num1 = self.num * other.num
        den1 = self.deno * other.deno
        gcd_val = gcd(num1,den1)

        num1 = num1//gcd_val
        den1 = den1//gcd_val

        return str(num1)+'/'+str(den1)


    def __truediv__(self,other):

        num1 = self.num * other.deno
        den1 = self.deno * other.num
        
        gcd_val = gcd(num1,den1)
        num1 = num1//gcd_val
        den1 = den1//gcd_val

        return str(num1)+'/'+str(den1)


    def __sub__(self,other):

        num1 = self.num * other.deno - other.num * self.deno
        den1 = self.deno * other.deno

        gcd_val = gcd(num1,den1)
        num1 = num1//gcd(num1,den1)
        den1 = den1//gcd(num1,den1)

        return str(num1)+'/'+str(den1)


    def __lt__(self,other):

        num1 = self.num / self.deno
        num2 = other.num / other.deno

        return num1 < num2


    def __gt__(self,other):

        num1 = self.num / self.deno
        num2 = other.num / other.deno

        return num1 > num2

    
frac1 = fraction(3,7)
frac2 = fraction(1,5)

print("Fraction Addition Result:")
print(frac1 + frac2)

print("Fraction Equality Check:")
print(frac1 == frac2)

print("Fraction Multiplication result:")
print(frac1*frac2) 

print("Fraction Division Result:")
print(frac1/frac2)

print("Fraction Subtraction Result:")
print(frac1-frac2)

print("Fraction Less Than Result:")
print(frac1 < frac2)

print("Fraction Greater Than Result:")
print(frac1 > frac2)