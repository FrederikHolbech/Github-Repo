install.packages("UsingR")
library("UsingR")
data(cats)
weight_male_mean <- mean(cats$Bwt[cats$Sex == "M"])
weight_female_mean <- mean(cats$Bwt[cats$Sex=="F"])
heart_male_mean <- mean(cats$Hwt[cats$Sex == "M"])
heart_female_mean <- mean(cats$Hwt[cats$Sex == "F"])

Bwt_male_sd <- sd(cats$Bwt[cats$Sex == "M"])
Bwt_female_sd <- sd(cats$Bwt[cats$Sex=="F"])
heart_male_sd <- sd(cats$Hwt[cats$Sex == "M"])
heart_female_sd <- sd(cats$Hwt[cats$Sex == "F"])

female_n <- 47
male_n <- 97

interval90_male_Bwt <- t.test(cats$Bwt[cats$Sex == "M"], conf.level = 0.90)$conf.int
interval90_male_Hwt <- t.test(cats$Hwt[cats$Sex == "M"], conf.level = 0.90)$conf.int

interval90_female_Bwt <- t.test(cats$Bwt[cats$Sex == "F"], conf.level = 0.90)$conf.int
interval90_female_Hwt <- t.test(cats$Hwt[cats$Sex == "F"], conf.level = 0.90)$conf.int

c_upper <- weight_male_mean + qnorm(0.95)*Bwt_male_sd/sqrt(male_n)
c_lower <- weight_male_mean - qnorm(0.95)*Bwt_male_sd/sqrt(male_n)
#these results are the same as the ones we got from (a)
