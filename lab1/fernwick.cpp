#include <iostream>
#include <vector>
#include <string>

using namespace std;

void fenwickAdd(long long index, long long delta, vector<long long> &tree);
long long fenwickSum(long long index, vector<long long> &tree);

int main() {
    ios::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);
    long long N, Q;
    char o;
    long long i, d;
    cin >> N >> Q;
    vector<long long> tree(N + 1, 0);

    while (cin >> o >> i) {
        if (o == '+') {
            cin >> d;
            fenwickAdd(i + 1, d, tree);
        } else if (o == '?') {
            cout << fenwickSum(i, tree) << "\n";
        }
    }

    return 0;
}

void fenwickAdd(long long index, long long delta, vector<long long> &tree) {
    while (index < tree.size()) {
        tree[index] += delta;
        index += index & (-index);
    } 
}

long long fenwickSum(long long index, vector<long long> &tree) {
    long sum = 0;
    while (index > 0) {
        sum += tree[index];
        index -= index & (-index);
    }
    return sum;
}