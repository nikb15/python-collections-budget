from . import Expense
import collections
import matplotlib.pyplot as plt

class BudgetList:
    def __init__(self ,budget):
        self.budget = budget
        self.sum_expenses=[]
        self.expenses=0
        self.overage=[]
        sum_overage=0

def append(self,item):
    if self.sum_expenses+item< self.budget:
        self.sum_expenses+=item
    else:
        self.overage.append(item)
        self.sum_overage+=item

def __len__(self):
    return self.expenses.__len__() + self.overages.__len__()


def main():
    myBudgetList= BudgetList(1200)