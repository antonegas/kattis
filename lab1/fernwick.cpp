#include <iostream>
#include <vector>
#include <string>

using namespace std;

void fenwickAdd(int index, int delta, vector<int> &tree);
int fenwickSum(int index, vector<int> &tree);

int main() {
    // ios::sync_with_stdio(false);
    // cin.tie(NULL);
    // cout.tie(NULL);
    int N, Q;
    char o;
    int i, delta;
    cin >> N >> Q;
    vector<int> tree(N, 0);
    while (true) {
        cin >> o;
        // if (o == '+') {
        //     cin >> delta;
        // } else if (o == '?') {

        // }
    }

    return 0;
}

void fenwickAdd(int index, int delta, vector<int> &tree) {
    while (index < tree.size()) {
        tree[index] += delta;
        index += index & (-index);
    } 
}

int fenwickSum(int index, vector<int> &tree) {
    int sum;
    while (index > 0) {
        sum += tree[index];
        index -= index & (-index);
    }
    return sum;
}