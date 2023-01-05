#include <iostream>
#include<cmath>
#include<algorithm>
using namespace std;

int main() {
	ios_base::sync_with_stdio(false);
	int n;
	long dp[101] = { 0 };
	
	cin >> n;
	//vector<int> num(n);
	int* num = new int[n+1];
	for (int i = 1; i <= n; i++) {
		cin >> num[i];
	}
	//dp[0] = 1;
	dp[1] = 1;
	dp[2] = 1;
	dp[3] = 1;
	dp[4] = 2;
	dp[5] = 2;
	for (int i = 1; i <= n; i++) {
		
		for (int j = 6; j <= num[i]; j++) {
			dp[j] = dp[j - 5] + dp[j - 1];
		}
		cout << dp[num[i]]<<'\n';
	}
	
	
}
