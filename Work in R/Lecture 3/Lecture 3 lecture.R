
#Let's have a look at our data
head(heifers_dung)

#but we would like our groups to be one long column with the marking of each group.

#load required library
library(tidyr)

#the gather function is nice, https://www.statology.org/gather-function-in-r/
dung_long <- gather(heifers_dung, group, value, control:spira)

head(dung_long)

library(dplyr)
#find mean and sd
#The %>% operator in R is called the pipe operator. 
#It's part of the magrittr package and is used for chaining together multiple operations*
#in a sequence, making your code more readable and easier to understand, especially
#when performing multiple transformations on data.
dung_long %>%
  group_by(group) %>%
  summarise(mean = mean(value),
            sd = sd(value))

#create boxplots -plots in alphabetacal order(!)
boxplot(value ~ group,
        data = dung_long,
        main = "Heifers",
        xlab = "Group",
        ylab = "Value",
        col = "steelblue",
        border = "black")

#strip chart 
#all values together

stripchart(dung_long$value,
           main = 'Heifers',
           xlab = 'Value',
           col = 'red',
           pch = 1,
           method = 'stack')

#seperated values into groups

x <- list('Control Group' = heifers_dung$control, 'alpha' = heifers_dung$alpha,
          'enro'= heifers_dung$enro,  'fenben' = heifers_dung$fenben,
          'iver' = heifers_dung$Iver, 'spira' = heifers_dung$spira)

#create plot that contains one strip chart per variable
stripchart(x, main = 'Strip chart of groups',
           xlab = 'Groups', 
           ylab = 'Value',
           col = c('steelblue', 'coral2'),
           pch = 16,
           vertical = TRUE)

# Back to slides




#fit the one-way ANOVA model

model <- aov(value ~ group, data = dung_long)

#view the model output
summary(model)

#significant difference between the groups
