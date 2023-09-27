import numpy
from math import sqrt

class TinyStatistician(object):

    def mean(self, x):
        sum = 0
        for i in x:
            m = len(x)
            sum = sum + i
        mean = sum / m
        print(mean)
        self.mean = mean

    def median(self, x):
        m = len(x)
        new_x = sorted(x) #et non x.sort() qui lui ne return aucune valeur
        median = 0
        if m % 2 == 0:
            median = (new_x[int(m/2) - 1] + new_x[int(m/2)]) / 2
        else:
            median = new_x[int(m/2)]
        print(median)

    def quartile(self, x):
        m = len(x)
        new_x = sorted(x)
        q1 = 0
        q3 = 0
        if m % 2 == 0:
            q1 = new_x[int(m/4 - 1)]
            q3 = new_x[int((3*m)/4 - 1)]
        else:
            q1 = new_x[int(m/4)]
            q3 = new_x[int((3*m)/4)]
        print(q1, q3)

    # def percentile(x, p):
        #### https://www.translatorscafe.com/unit-converter/fr-FR/calculator/percentile/
        
    def var(self, x): #https://stacklima.com/la-correction-de-bessel/
        m = len(x)
        sum = 0 
        for i in range (0, len(x)):
            diff_sqr = (x[i] - self.mean) * (x[i] - self.mean) #(i - moyenne)²
            sum = sum + diff_sqr
        division = sum / m
        print(division)
        self.division = division #division = variance
        
    def std(self, x):
        ecart_type = sqrt(self.division) #division = variance
        print(ecart_type)


stats = TinyStatistician()
x = [12, 15, 5, 10] 
stats.mean(x) #10,5
x = [12, 15, 5, 10] 
stats.median(x) #11
x = [12, 15, 5, 10, 17]
stats.median(x) #12
x = [12, 15, 5, 10] 
stats.quartile(x) #5 12
x = [12, 15, 5, 10, 17]
stats.quartile(x) #10 15
x = [1, 42, 300, 10, 59] 
stats.var(x)
x = [1, 42, 300, 10, 59] 
stats.std(x)
