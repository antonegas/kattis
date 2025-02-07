#include <iostream>
#include <vector>
#include <queue>
#include <string>
#include <unordered_map>
#include <unordered_set>
#include <tuple>

using namespace std;

int main() {
    long long c, n, a;
    long long cacheMisses = 0;
    cin >> c >> n >> a;
    vector<long long> accesses(a, 0);
    unordered_set<long long> cache;
    priority_queue<tuple<long long, long long>> furthestAccess;
    unordered_map<long long, queue<long long>> nextAccess;
    long long i = 0;
    while (cin >> accesses[i]) i++;
    for (size_t i = 0; i < a; i++) nextAccess[accesses[i]].push(i);

    for (long long &access : accesses) {
        nextAccess[access].pop();
        while (!furthestAccess.empty() && cache.count(get<1>(furthestAccess.top())) == 0) furthestAccess.pop();
        if (cache.count(access) > 0) continue;
        if (cache.size() >= c) cache.erase(get<1>(furthestAccess.top()));
        cacheMisses++;
        furthestAccess.emplace(make_tuple(nextAccess[access].front(), access));
        cache.insert(access);
    }

    cout << cacheMisses << endl;

    return 0;
}