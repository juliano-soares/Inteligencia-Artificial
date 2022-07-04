#install.packages("tabuSearch")

library(tabuSearch)

Z = tabuSearch(size = 12, iters = 100, objFunc = compras, listSize = 9,  nRestarts = 10, repeatAll = 1, verbose = T)

plot(Z)
summary(Z)

Z$configkeep[299,]
summary(Z, verbose = TRUE)
