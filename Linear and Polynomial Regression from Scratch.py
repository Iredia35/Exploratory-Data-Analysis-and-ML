from math import sqrt, log
class Regression: 

     def __init__(self, X_axis, y_axis):
          self.X_axis = X_axis
          self.y_axis = y_axis

          self._no_of_observations = len(self.X_axis)
     def check(self):
          n = len(self.y_axis)
          y = self.y_axis
          smallest = y[0]

          for i in range(0, n):
               if y[i] < smallest:
                   print('Its is a linear regression')
               else:
                   print('Its is a polynomial regression')

class LinearRegression(Regression):

     def __init__(self, X_axis, y_axis):
          super(LinearRegression, self).__init__(X_axis, y_axis)


          self._summation_X_y = self.sum_array(self.multiply_arrays(self.X_axis, self.y_axis))
          self._summation_X = self.sum_array(self.X_axis)
          self._summation_y = self.sum_array(self.y_axis)
          self._summation_X_squared = self.sum_array(self.squared_array(self.X_axis))
          self._squared_array_sum = self._summation_X**2

     @staticmethod
     def multiply_arrays(x, y):
          multiple = []
          for i in range(len(x)):
               multiple.append(x[i] * y[i])
          return multiple

     @staticmethod
     def add_arrays(x, y):
          add = []
          for i in range(len(x)):
              add.append(x[i] + y[i])
          return add

     @staticmethod
     def sub_arrays(x, y):
          sub = []
          for i in range(len(x)):
               sub.append(x[i] - y[i])
          return sub

     @staticmethod
     def sum_array(x):
          sum = 0
          for i in x:
               sum += i
          return sum     

     @staticmethod
     def squared_array(x):
          squares = []
          for i in x:
               squares.append(i**2)
          return squares

     def slope(self):
          
          _b_numerator = ((self._no_of_observations * self._summation_X_y) - (self._summation_X * self._summation_y))
          _b_deniminator = ((self._no_of_observations * self._summation_X_squared) - self._squared_array_sum)

          slopes = _b_numerator/_b_deniminator
          return slopes
          
     def intercept(self):
          _otherPart = self._summation_y / self._no_of_observations
          _otherPart2 = (self.slope() * (self._summation_X/self._no_of_observations))

          _intercepts = _otherPart - _otherPart2

          return _intercepts

     def upScale(self, x, scale):
          res = []
          for i in x:
               res.append(i * scale)
          return res

     def downScale(self, x, scale):
          res = []
          for i in x:
               res.append(i / scale)
          return res

     def report(self):
       return ("The regression funtion is: ", "y = ", self.intercept(), " + ", self.slope())
       
     def standard_error_estimate(self):
          _SEE_upper = ((self.sum_array(self.squared_array(self.y_axis))) - (self.intercept()*self.sum_array(self.y_axis)) - (self.slope()* self._summation_X_y))
          _SEE_lower = self._no_of_observations - 2

          div = _SEE_upper / _SEE_lower

          return sqrt(div)

     def inference_about_regression(self, alpha, t_des):
          lower_lower1 = sqrt(self._summation_X_squared - (self._summation_X**2/(self._no_of_observations)))
          lower = self.standard_error_estimate()/lower_lower1

          res = self.slope()/ lower

          if res != t_des:
              print("Reject Ho, the regression relationship does not exist")

          return res

     def confidenceInterval_Yc(self, X_value, con_inv):
          first_part = self.intercept() + (self.slope() * X_value)
          second_path = con_inv * self.standard_error_estimate()

          third_part1 = (1/self._no_of_observations)
          third_part2 = (X_value - (self._summation_X/self._no_of_observations))**2
          third_part3 = self._summation_X_squared - (self._summation_X**2/self._no_of_observations)

          total_left = sqrt(third_part1 + (third_part2/third_part3)) * second_path

          upperBound = first_part + total_left
          lowerBound = first_part - total_left

          ans = lowerBound, '<= Yc <=', upperBound

          return ans

     def confidenceInterval_Y(self, X_value, con_inv):
          first_part = self.intercept() + (self.slope() * X_value)
          second_path = con_inv * self.standard_error_estimate()

          third_part1 = (1 / self._no_of_observations) + 1
          third_part2 = (X_value - (self._summation_X / self._no_of_observations)) ** 2
          third_part3 = self._summation_X_squared - (self._summation_X ** 2 / self._no_of_observations)

          total_left = sqrt(third_part1 + (third_part2 / third_part3)) * second_path

          upperBound = first_part + total_left
          lowerBound = first_part - total_left

          ans = lowerBound, '<= Yc <=', upperBound

          return ans

     def variation_analysis(self):
         yca = []
         for i in self.X_axis:
              add = (self.intercept() + (self.slope() * i))
              yca.append(add)

         meanYc = []
         mean = self.sum_array(self.y_axis) / self._no_of_observations
         for i in self.y_axis:
              solve = (i - mean)
              meanYc.append(solve)

         SST = 'SST: ', self.sum_array(self.squared_array(meanYc))
         SSR = []
         for i in yca:
              arr = (i - mean)
              SSR.append(arr)
         SSR = 'SSR: ', self.sum_array(self.squared_array(SSR))

         SSRE = 'SSRE', self.sum_array(self.squared_array(self.sub_arrays(self.y_axis, yca)))

         return (SST,SSR,SSRE)

class PolynomialRegression(LinearRegression):
     def __init__(self, X_axis, y_axis):
          super(PolynomialRegression, self).__init__(X_axis, y_axis)

          self._summation_logY = self.sum_array(self.logList(y_axis))
          self._summation_XlogY = self.sum_array(self.multiply_arrays(X_axis , self.logList(y_axis)))
          self._summation_logY_squares = self.sum_array(self.squared_array(self.logList(y_axis)))

     @staticmethod
     def logList(y_axis):
          arr = []
          for i in y_axis:
               arr.append(log(i, 10))
          return arr

     def slope(self):
          upper_part = (self._no_of_observations * self._summation_XlogY) - (self._summation_X * self._summation_logY)
          lower_part = (self._no_of_observations * self._summation_X_squared) - self._summation_X**2

          ans = upper_part/lower_part
          return ans

     def intercept(self):
          first_part = self._summation_logY / self._no_of_observations
          second_part = self.slope() * (self._summation_X /self._no_of_observations)
          ans = first_part - second_part

          return ans

     def co_eff(self):
          upper_part = (self._no_of_observations * self._summation_XlogY) - self._summation_X * (self._summation_logY)
          lower_part1 = (self._no_of_observations * self.sum_array(self.squared_array(self.X_axis))) - self._summation_X**2
          lower_part2 = (self._no_of_observations * self._summation_logY_squares) - self._summation_logY**2
          t_lower = sqrt(lower_part1 * lower_part2)

          ans = (upper_part / t_lower)**2

          return ans

