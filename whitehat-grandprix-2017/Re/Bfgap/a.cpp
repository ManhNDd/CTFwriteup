#include <iostream>
#include <vector>
#include <algorithm>
#include <array>
#include <set>
#include <map>
#include <queue>
#include <tuple>
#include <unordered_set>
#include <unordered_map>
#include <functional>
#include <cassert>
#define repeat(i, n) for (int i = 0; (i) < int(n); ++(i))
#define repeat_from(i, m, n) for (int i = (m); (i) < int(n); ++(i))
#define repeat_reverse(i, n) for (int i = (n)-1; (i) >= 0; --(i))
#define repeat_from_reverse(i, m, n) for (int i = (n)-1; (i) >= int(m); --(i))
#define whole(x) begin(x), end(x)
#define unittest_name_helper(counter) unittest_ ## counter
#define unittest_name(counter) unittest_name_helper(counter)
#define unittest __attribute__((constructor)) void unittest_name(__COUNTER__) ()
using ll = long long;
using namespace std;
template <class T> inline void setmax(T & a, T const & b) { a = max(a, b); }
template <class T> inline void setmin(T & a, T const & b) { a = min(a, b); }
template <typename X, typename T> auto vectors(X x, T a) { return vector<T>(x, a); }
template <typename X, typename Y, typename Z, typename... Zs> auto vectors(X x, Y y, Z z, Zs... zs) { auto cont = vectors(y, z, zs...); return vector<decltype(cont)>(x, cont); }

constexpr int H = 16;
constexpr int W = 16;
vector<string> f;
int main() {
    string f; cin >> f;
    assert (f.size() == H * W);
    const int dy[] = { -1, 1, 0, 0 };
    const int dx[] = { 0, 0, 1, -1 };
    auto is_on_field = [&](int y, int x) { return 0 <= y and y < H and 0 <= x and x < W; };
    int sy[4];
    int sx[4];
    repeat (y, H) {
        repeat (x, W) {
cerr << f[y * W + x];
            int i = f[y * W + x] - '2';
            if (i >= 0) {
                sy[i] = y;
                sx[i] = x;
            }
        }
cerr << endl;
    }
    vector<string> used(H, string(W, '\0'));
    ll result = 0;
    function<void (int, int, int)> go = [&](int y, int x, int stage) {
        if (y == sy[stage] and x == sx[stage]) {
            ++ stage;
            if (stage == 3) {
                result += 1;
                return;
            }
        }
        used[y][x] = true;
        repeat (i, 4) {
            int ny = y + dy[i];
            int nx = x + dx[i];
            if (is_on_field(ny, nx) and f[ny * W + nx] != '0' and not used[ny][nx]) {
                go(ny, nx, stage);
            }
        }
        used[y][x] = false;
    };
    go(sy[0], sx[0], 1);
    cout << result << endl;
cerr << result << endl;
    return 0;
}
