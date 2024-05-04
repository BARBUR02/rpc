
#ifndef CALC_ICE
#define CALC_ICE

module Demo
{
  enum operation { MIN, MAX, AVG };

  sequence<long> arr;

  //exception NoInput {};

  exception EmptyArray {};

  interface Calc
  {
    long add(int a, int b);
    long subtract(int a, int b);
    double avg(arr a) throws EmptyArray;
  };

};

#endif
