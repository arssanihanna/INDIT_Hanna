import random
i = 0
Lottospiel = []

Ratschlag = int(input("Wie viele Ratschläge willst du haben?"))
if Ratschlag > 0:
    
        while i < Ratschlag:
            Zahl = random.sample(range(1,45),6)
            
            if Zahl in Lottospiel:
                i =i
                
            else:
                Lottospiel.append(Zahl)
                i += 1
                
                
        print(Lottospiel)