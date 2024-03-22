method_A_scores <- c(65, 75, 80, 90, 70, 85, 95, 78, 88, 92)
method_B_scores <- c(60, 70, 75, 85, 72, 82, 88, 76, 90, 85)


#combine the data into a data frame
data <- data.frame(Method = rep(c("A", "B"), each = 10), Scores = c(method_A_scores, method_B_scores))

#Display the first row in the data set
head(data)

#boxplot using boxplot()
boxplot(Scores~Method, data = data)

#Frequency plot using hist()
hist(data$Scores, col = "lightblue")
