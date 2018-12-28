#include <stdio.h>

int main()
{
  float penny = 0.01;
  float amount_to_change = 1;
  int num_pennies = 0;
  while (amount_to_change > 0)
    {
      amount_to_change -= penny;
      ++num_pennies;
    }
  printf("%d pennies; %f left over\n", num_pennies, amount_to_change);
}
