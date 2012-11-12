/* gcc -o xorSwap xorSwap.c */

#include <stdio.h>

void xorSwap(int *x, int *y)
{
  *x ^= *y;
  *y ^= *x;
  *x ^= *y;
}

int main() {
  int i = 1;
  printf("before swap i:%d\n", i);
  xorSwap(&i, &i);
  printf("after  swap i:%d\n", i);
}
