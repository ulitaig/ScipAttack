import random
from pyscipopt import Model


#x = model.addVar("x")
#y = model.addVar("y", vtype="INTEGER")
#model.setObjective(x + y)
#model.addCons(2*x - y*y >= 0)
#model.optimize()
def Random_delCons(Problem, Times):
    maxT = 0.0
    oriT = 0.0

    for i in range(Times):
        model = Model("Random_delCons")
        model.readProblem(Problem)
        Conss = model.getConss()


        #print(model.getCons(model.getConss()[0]))
        if(i != 0):
            model.delCons(Conss[random.randint(0,len(Conss)-1)])
        T = model.getTotalTime()
        model.optimize()
        T = T - model.getTotalTime()
        maxT = max(maxT, T)
        if(i == 0):
            oriT = T

    print(maxT, oriT)

if __name__ == "__main__":
    Random_delCons("./pk1.mps", 10)