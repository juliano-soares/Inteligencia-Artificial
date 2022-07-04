Rosenbrock <- function(Z) 
{
  x = Z[1]
  y = Z[2]
  
  return((1-x)^2 + 100*(y-x^2)^2)
}