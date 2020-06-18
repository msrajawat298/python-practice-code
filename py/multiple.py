class CompanyOne:
    def getProductionUnitOne(self):
        self.totalproductionUnitOne=int(input("Enter Production of Unit One:"))
    def putProductionUnitOne(self):
        print('Unit One:',self.totalproductionUnitOne)
class CompanyTwo:
    def getProductionUnitTwo(self):
        self.totalproductionUnitTwo=int(input("Enter Production of Unit Two:"))
    def putProductionUnitTwo(self):
        print('Unit Two:',self.totalproductionUnitTwo)

class NetProduction(CompanyOne,CompanyTwo):
    def totalProduction(self):
        self.getProductionUnitOne()
        self.getProductionUnitTwo()
        self.total=self.totalproductionUnitOne+self.totalproductionUnitTwo
    def showTotalProduction(self):
        self.putProductionUnitOne()
        self.putProductionUnitTwo()
        print('Total Production:',self.total)

C=NetProduction()
C.totalProduction()
C.showTotalProduction()