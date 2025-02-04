#include <iostream>
#include <vector>
#include <string>

using namespace std;

int djsFind(int x, vector<int> &parent);
void djsUnion(int x, int y, vector<int> &parent, vector<int> &rank);
bool djsSame(int x, int y, vector<int> &parent);

int main() {
    ios::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);
    int N, Q;
    char o;
    int x, y;
    vector<int> parent;
    vector<int> rank;
    string output;
    cin >> N >> Q;

    for (size_t i = 0; i <= N; i++) {
        parent.push_back(i);
        rank.push_back(0);
    }
    
    while (cin >> o >> x >> y) {
        if (o == '?') {
            output += djsSame(x, y, parent) ? "yes\n" : "no\n";
        } else {
            djsUnion(x, y, parent, rank);
        }
    }

    cout << output;

    return 0;
}

int djsFind(int x, vector<int> &parent) {
    if (x == parent[x]) return x;
    parent[x] = djsFind(parent[x], parent);
    return parent[x];
}

void djsUnion(int x, int y, vector<int> &parent, vector<int> &rank) {
    int xParent = djsFind(x, parent);
    int yParent = djsFind(y, parent);

    if (xParent == yParent) return;
    if (rank[xParent] < rank[yParent]) swap(xParent, yParent);
    parent[yParent] = xParent;
    if (rank[xParent] == rank[yParent]) rank[xParent]++;
}

bool djsSame(int x, int y, vector<int> &parent) {
    return djsFind(x, parent) == djsFind(y, parent);
}