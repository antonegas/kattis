#include <iostream>
#include <vector>
#include <queue>
#include <string>
#include <unordered_map>
#include <unordered_set>
#include <tuple>

using namespace std;

int main() {
    int c, n, a;
    int cacheMisses = 0;
    int totalCached = 0;
    cin >> c >> n >> a;
    vector<int> accesses(a, 0);
    vector<bool> cache(n, false);
    vector<queue<int>> nextAccess(n, queue<int>());
    priority_queue<tuple<int, int>> furthestAccess;
    int i = 0;
    while (cin >> accesses[i]) i++;
    for (size_t i = 0; i < a; i++) nextAccess[accesses[i]].push(i);

    for (int &access : accesses) {
        nextAccess[access].pop();
        while (!furthestAccess.empty() && !cache[get<1>(furthestAccess.top())]) furthestAccess.pop();
        if (cache[access]) continue;
        if (cache.size() >= c) cache[get<1>(furthestAccess.top())] = false;
        totalCached++;
        cacheMisses++;
        furthestAccess.emplace(make_tuple(nextAccess[access].front(), access));
        cache[access] = true;
    }

    cout << cacheMisses << endl;

    return 0;
}