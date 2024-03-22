#exercise 2,3

#1. Use data(trees) to get the data into R. Print the dataset to make
#sure that it contains exactly 31 cherry trees.
data(trees)
print(trees)

#2. Make three plots that show volume against height, volume
#against diameter, and height against diameter. You can use the
#function plot() for this.
plot(trees$Volume,trees$Height)
plot(trees$Volume, trees$Girth)
plot(trees$Height, trees$Girth)

#3. Describe the direction, shape, strength, and any strange observations 
#for the three plots made in question 2.
#the first plot has generally positive direction
#the second plot has generally positive direction
#the third plot has generally positive direction

#the first plot doesn't really follow any straight line or curve
#the second plot follows a clear line
#the third plot doesn't really follow any straight line or curve

#the first plot has bad strength since the points are scattered around
#the second plot has good strength, the points are alligned closely to a clear line
#the third plot also has bad strength

#the first plot has a cluster of points over the rest of the points, and also a clear outlier that has a much larger volume and much taller than the rest
#the second plot also has this outlier
#the third plot has a clear outlier that is much taller and much wider

#4Fit a model that describes the volume as a linear function of diameter
#(use lm()). What is the estimated slope of the fitted regression line? 
#What is the estimated intercept?
model <- lm(trees$Girth ~ trees$Volume)
print(model)
#the estimated slope is 0,1846 and intercept 7,6779

#5 Plot the fitted regression line in the same plot as the original data
#(use abline()).
abline(model)

#6 Calculate the correlation coefficient between volume and height,
#volume and diameter, and diameter and height (use the function cor()). 
#Do the results correspond to what you would expect
#from the plots?
cor(trees$Volume,trees$Height) #0,60
cor(trees$Volume, trees$Girth) #0,96
cor(trees$Height, trees$Girth) #0,52
#these coefficients corresponds well with what the plots show

#7. Calculate the correlation between height and volume. Is that
#different from the correlation between volume and height?
#Why/why not?
cor(trees$Height,trees$Volume) #0,60
#it is the same as between volume and height, because the way they
#influence each other doesn't change

#8. We will now examine the influence of a single extreme value on
#the correlation coefficient. Locate the observation in the dataset
#that corresponds to the largest value of volume. Change that
#value to 35. How will this change influence the correlation
#between volume and diameter and between volume and height?
trees$Volume[which.max(trees$Volume)] <- 35
#this makes the correlation coefficient worse, because now we create an outlier that defers from the model

#9How will the changed value influence the estimates of the slope
#and intercept?
lm(trees$Girth ~ trees$Volume)
#now the slope is 0,2 and the intercept is 7,4
#the slope and intercept increase marginally

#Exercise 2,7
#Correlation graphs. Consider the four graphs shown in the figure
#Below. The correlation coefficients for the four graphs are -0.86, -0.25,
#0.17, and 0.70. Determine which graph corresponds to each of the four
#correlation coefficients.
#The first picture has the coefficient 0,7
#The second picture = -0,25
#The third picture = 0,17
#The fourth picture = -0,86

#Exercise 2,10

#1. Which values can the coefficient of determination attain? Is R^2
#symmetric in x and y, i.e., does it change if we interchange the
#variable names?
#the coefficient of determination can attain values between 0 and 1
#the R^2 is symmetric in x and y, since the total amount of deviation still is the same

#2. Assume that we have a coefficient of determination that is 0.83.
#Does that mean that the relationship between x and y is positive?
#Why/why not?
#the coefficient of determination doesn't describe the relationship between x and y

#3  For a linear regression model, would you generally prefer
#higher or lower values of the coefficient of determination? Why?
#For a linear regression model, you prefer a higher value of the coefficient
#of determination, becuase it means that the observations deviate
#a small amount from the model

#4 Which value of R^2 do you get if x is constant? Next, consider a
#situation where x and y are not related. Do you then think that
#R^2 will be close to zero, close to 0.5, or close to 1?
#if x is constant R^2 has the value 0, if x and y are not related, then 
#R^2 will be close to zero

#1. What are the parameter estimates for the three unknown parameters in
#the linear regression model: 1) The intercept, the slope and the error
#standard deviation?
data_polution <- data.frame(
  Distance = c(2,4,6,8,10),
  Concentration = c(11.5,10.2,10.3,9.68,9.32)
)
lm(data_polution$Concentration~data_polution$Distance)
#the intercept is 11,664 and the slope -0,244
SE <- sd(data_polution$Concentration)/sqrt(5)
print(SE)
#the standard error is 0,37

# 2. How large a part of the variation in concentration can be explained by
#the distance?
cor(data_polution$Concentration,data_polution$Distance)^2
#R^2 = 0,87 which tells us about the variation

#3 What is the expected pollution concentration 7 km from the pollution
#source?
11.664-0.244*7 = 9.956
#we follow our formula we got from the slope and interception and plug in 7 

#4 At what distance from the pollution source would you begin the cleaning
#of the pollution?
11.664/0.244
#after 47,8 km I would start cleaning