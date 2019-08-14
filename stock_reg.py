from scipy.stats import linregress
import numpy as np


class Errors:

    def finderrors(self, y, x, timer, position ,n):

        model = linregress(x,y)
        slope = model.slope
        intercept = model.intercept
        line = slope*x + intercept

          #Calculate the standard error in the regression model
        avgx = sum(x)/len(x)
        devx = (x - avgx)**2
        devx = sum(devx)
        devx = (devx)**0.5

        error = (y - line)**2
        error = sum(error)/n
        error = (error)**(.5)
        error = 4.957*error/devx

        ##Append the appropriate lists and delete a couple to keep 35 points
        toperror = error+slope
        bottomerror = slope-error
        return toperror, bottomerror, line , slope






