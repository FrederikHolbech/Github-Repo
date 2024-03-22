#1.2 blood pressure

#1 Determine the median, the range, and the quartiles

blood_pressure <- c(96, 119, 119, 108, 126, 128, 110, 105, 94)
median(blood_pressure)
range(blood_pressure)
quantile(blood_pressure)
# 2 Determine the inter quartile range
IQR(blood_pressure)

# 3 construct a boxplot
boxplot(blood_pressure)

# 4 calculate the mean, the standard deviation,and the variance.
mean(blood_pressure)
sd(blood_pressure)
var(blood_pressure)

# 5 What are the units for the mean, standard deviation, and variance?
#mean is mmHg, standard deviation is mmHg, variance is squared mmHg

# 6 How will the mean change if we add 10mmHg to each of the measurements ?
# How will this change the standard deviation and the variance? 
#the mean would change to the mean plus 10 so 120, the standard deviation will not change, neither will the variance

# 7 I think the mean would increase because of a few outliers with high blood pressure would increase the mean
# I think that the standard deviation would increase as well

#1.7
#1 Read the data into R
data_1 <- c(125.1, 114.6, 99.3, 119.1, 109.6, 102.0,
            104.9, 109.6, 134.0, 108.6,
            120.3, 98.7, 104.2, 91.4, 115.3,
            107.7, 97.8, 126.4, 104.8, 118.8)
#2 calculate the standard deviation and variance f the cone lengths.
#what is the relationship between the two numbers?
sd(data_1)
var(data_1)
#the relationship between them is, that the variance is the standard deviation squared

#3 . Use hist() to plot a histogram of the cone lengths. Use
#boxplot() to plot a modified boxplot. What can you discern
#about the cone lengths from the two figures?
hist(data_1)
boxplot(data_1)
#from the Histogram, it is clear that most of the cones are between 100 and 110 mm
#from the Boxplot, it is clear that the median is around 110

#4  Construct a new vector with the name conelenm which contains
#the same lengths but now measured in centimeters. How will
#the mean and standard deviation change after we change the
#units?
data_2 <- data_1 / 10
mean(data_2)
sd(data_2)
#the mean and standard deviation also are divided by 10

# 5 Plot a histogram and boxplot of the transformed data (use
#hist()). You can choose if you want to change the intervals on
#the x-axis or if you want frequencies or relative frequencies on
#the y-axis. What can you say about the shape of the distribution?
#Is it symmetric, skewed to the right, or skewed to the left?
hist(data_2, freq = FALSE)
boxplot(data_2)
#the data is skewed to the right since the tail is longer on the right side of the plot

#1.8
# 1 and y match together, you can see the minimum value being around -4
# 2 and z match together, you can see the outliers
# 3 and x match together, the only pair left

#The following table displays the prevalence of autism per 10,000 ten-year-old
#children in the United States from 1992 - 2000. (Data from C. J. Newshaffer,
#M. D. Falb, and J. G. Gurney, ”National Autism Prevalence Trends From
1
#United States Special Education Data”, Pediatrics, 115 (2205): e277-e282.).
#Year Prevalence
#1992 3.5
#1994 5.3
#1996 7.8
#1998 11.8
#2000 18.3

# 1 enter the data set directly into R.
autism_data <- data.frame(
  Year = c(1992, 1994, 1996, 1998, 2000),
  Prevalence = c(3.5, 5.3, 7.8, 11.8, 18.3))

# 2 Enter the values of the table into an Excel sheet, then import the data
#set to RStudio. Use Google (or other search engines) to find out how to
#import data sets from Excel into RStudio.
library(readxl)
autism_excel_data <- read_excel("/Users/Frederik/OneDrive/Dokumenter/autism_data.xlsx")
print(autism_excel_data)

#3. Make a scatter plot of the data set. Add labels for each of the axes as
#well as a title. Again, Google is your friend.
plot(autism_excel_data$year, autism_excel_data$prevalence, 
     xlab = "year", 
     ylab = "prevalence", 
     main = "Scatter plot of Autism")
  

#Set the seed for reproducibility
set.seed(123)

# Define the population as a vector based on given probabilities
population <- c(rep(2, 25), rep(6, 75)) # 25% twos and 75% sixes

# Function to take a sample and calculate its variance
sample_variance <- function(population, sample_size) {
  sample <- sample(population, sample_size)
  return(var(sample))
}

# Simulate taking 1000 samples of size 3 and calculate their variances
sample_variances <- replicate(1000, sample_variance(population, 3))

# Calculate the average of the sample variances
average_sample_variance <- mean(sample_variances)

# Output the average sample variance
average_sample_variance

hist(sample_variances, breaks = 50, main = "Distribution of Sample Variances", xlab="Sample Variance")
