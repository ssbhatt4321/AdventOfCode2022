#include <bits/stdc++.h>
using namespace std;

typedef long long ll;

unordered_map<string,int> inds;
vector<int> val;
vector<vector<string>> adj;
vector<string> poss;

vector<int> perm;
vector<vector<int>> dist;

vector<vector<vector<ll>>> states(16,vector<vector<ll>>(31,vector<ll>(1 << 15, -1)));

ll rec(int posi, int time, ll perm_mask) {
	if (states[posi][time][perm_mask] != -1)
		return states[posi][time][perm_mask];
	
	if (time <= 1) return 0;
	ll ans = 0;
	int pos = perm[posi];
	for(int j = 0; j < perm.size()-1; j++) {
		int i = perm[j];
		if ((perm_mask >> j) % 2 == 0) {
			time -= dist[pos][i];
			if (time <= 0) {
				time += dist[pos][i];
				continue;
			}
			ans = max(ans, rec(j, time-1, perm_mask | (1 << j)) + val[i] * (time-1));
			time += dist[pos][i];
		}
	}

	return states[posi][time][perm_mask] = ans;
}

int main() {
	string line, s, pos, rate, neigh;
	while (getline(cin, line)) {
		stringstream sin(line);
		sin >> s >> pos;
		poss.push_back(pos);
		sin >> s >> s >> rate;
		rate.pop_back();
		val.push_back(stoi(rate.substr(5,rate.size()-5)));
		sin >> s >> s >> s >> s;
		adj.push_back({});
		while (sin >> neigh) {
			if (neigh.back() == ',') neigh.pop_back();
			adj.back().push_back(neigh);
		}
	}

	int i = 0;
	for(auto pos : poss)
		inds[pos] = i++;

	int n = poss.size();
	dist.assign(n, vector<int>(n,1000));
	for(int i = 0; i < n; i++) {
		dist[i][i] = 0;
		for(auto neigh : adj[i])
			dist[i][inds[neigh]] = 1;
	}

	for(int k = 0; k < n; k++)
		for(int i = 0; i < n; i++)
			for(int j = 0; j < n; j++)
				dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j]);
	
	for(int i = 0; i < n; i++)
		if (val[i])
			perm.push_back(i);
	perm.push_back(inds["AA"]);
	
	cout << rec(perm.size()-1, 30, 0) << endl;

	ll ans = 0;
	for (int i = 0; i < 1 << (perm.size()-1); i++)
		ans = max(ans, rec(perm.size()-1, 26, i) + rec(perm.size()-1, 26, ((1 << (perm.size()-1)) - 1) & ~i));
	cout << ans << endl;
}