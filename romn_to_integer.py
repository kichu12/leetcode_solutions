class Solution:
    def romanToInt(self, s: str) -> int:
        Z=0
        r=["IV","IX","XL","XC","CD","CM"]
        skip= False
        for i in range(len(s)):
            if skip:
                skip=False
                continue
            if i != (len(s)-1):
                if (s[i]+s[i+1]) not in r:
                    if s[i] =="I":
                            Z=Z+1
                    elif s[i]=="V":
                        Z=Z+5
                    elif s[i]=="X":
                        Z=Z+10
                    elif s[i]=="L":
                        Z=Z+50
                    elif s[i]=="C":
                        Z=Z+100
                    elif s[i]=="D":
                        Z=Z+500
                    else:
                        Z=Z+1000
                else:
                    if (s[i]+s[i+1])=="IV":
                        Z=Z+4
                    elif (s[i]+s[i+1])=="IX":
                        Z=Z+9
                    elif (s[i]+s[i+1])=="XL":
                        Z=Z+40
                    elif (s[i]+s[i+1])=="XC":
                        Z=Z+90
                    elif (s[i]+s[i+1])=="CD":
                        Z=Z+400
                    else:
                        Z=Z+900
                    skip= True
                    
                    

            
            else:
                if s[i] =="I":
                    Z=Z+1
                elif s[i]=="V":
                    Z=Z+5
                elif s[i]=="X":
                    Z=Z+10
                elif s[i]=="L":
                    Z=Z+50
                elif s[i]=="C":
                    Z=Z+100
                elif s[i]=="D":
                    Z=Z+500
                else:
                    Z=Z+1000

          
        return Z
            

        