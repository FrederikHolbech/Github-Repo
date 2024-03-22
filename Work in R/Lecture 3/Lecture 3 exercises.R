install.packages("isdals")
library(isdals)
data(tartar)
boxplot(tartar$index ~ tartar$treat,
        main = "Parallel boxplots of dogs and treats")
group_means <-lm(tartar$index ~ 0+tartar$treat)

summary(tartar$index ~ 0+tartar$treat)
mean(80, 75, 82, 78, 85, 77, 73, 80, 76, 83, 81, 77, 84, 79, 86, 79, 76,
     83, 78, 85, 82, 78, 85, 80, 87)
mean(70, 65, 72, 68, 75, 74, 69, 76, 72, 78, 68, 63, 70, 66, 73, 72, 67,
     74, 70, 77, 71, 66, 73, 69, 76)
