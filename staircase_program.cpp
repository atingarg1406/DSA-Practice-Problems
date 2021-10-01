#include <iostream>
using namespace std;

// Count total number of ways to reach at the top using 1, 2, 3 steps
int countWays(int steps)
{
    int totalWays[steps + 1]; 
    totalWays[0] = 1;
    totalWays[1] = 1;
    totalWays[2] = 2;
    for (int i = 3; i <= steps; i++)
        totalWays[i] = totalWays[i - 1] + totalWays[i - 2] + totalWays[i - 3];

    return totalWays[steps];
}

int main()
{
    int totalSteps = 0; // Total number of steps in the staircase
    cin >> totalSteps;

    cout << countWays(totalSteps) << endl;

    return 0;
}

