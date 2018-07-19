#include<cstdio>
#include<cstdlib>
#include<ctime>
#include<cmath>
#include<vector>

using namespace std;

typedef vector<int> vi;

inline int LSOne(int n) {
    return n & -n;
}

class FenwickTree {
    private:
        int len;
        vi ft;
        vi ori;
    public:
        FenwickTree() {
            FenwickTree(32);
        }

        FenwickTree(int n) {
            len = n;
            ft.assign(n + 1, 0);
            ori.assign(n + 1, 0);
        }

        int size() {
            return len;
        }

        void set_all(int v) {
            for (int i = 1; i <= len; i++)
                ori[i] = v, ft[i] = LSOne(i) * v;
        }

        int val(int k) {
            return ori[k];
        }

        void remove(int k) {
            set(k, val(len)); pop();
        }

        // pushing value to fenwick tree costs O(lg n)
        void push(int x) {
            len++;
            ori.push_back(x);
            ft.push_back(rsq(len - LSOne(len) + 1, len - 1) + x);
        }

        int pop() {
            int v = ori[len--];
            ori.pop_back(); 
            ft.pop_back();
            return v;
        }

        int rsq(int b) {
            int sum = 0;
            for (; b; b -= LSOne(b))
                sum += ft[b];
            return sum;
        }

        int rsq(int a, int b) {
            return rsq(b) - rsq(a - 1);
        }

        // OPTIMIZE: change from O(lg n * lg n) to O(lg n) solution
        int lower_bound(int l, int r, int v) {
            if (l == r) return rsq(l) - l < v ? l + 1 : l;

            int piv = (l + r) / 2;
            if (rsq(piv) - piv >= v)
                return lower_bound(l, piv, v);
            return lower_bound(piv + 1, r, v);
        }

        int lower_bound(int v) {
            return lower_bound(1, len, v);
        }

        void adjust(int k, int v) {
            ori[k] += v;
            for (; k < ft.size(); k += LSOne(k))  ft[k] += v;
        }

        void set(int k, int v) {
            adjust(k, v - val(k));
        }

        void print() {
            for (int i = 1; i <= len; i++) {
                if (i != 1) printf(", ");
                printf("%d", ori[i]);
            }printf("\n");
        }
};

class Polymer {
    private:
        FenwickTree molecules;
        int size;
        double dis;
        double ass;
    public:
        Polymer(int _size, double _dis, double _ass) {
            size = _size;
            dis = _dis;
            ass = _ass;
            molecules = FenwickTree(size);
            molecules.set_all(1);
        }

        FenwickTree simulate(int duration) {
            double r;
            while (duration--) { 
                // disassociation
                r = 1.0 * rand() / RAND_MAX;
                int n_bond = size - molecules.size();
                if (r > pow(1 - dis, n_bond)) {
                    int p = rand() % n_bond + 1;
                    int k = molecules.lower_bound(p);
                    p -= molecules.rsq(k) - k + 1;
                    molecules.adjust(k, p);
                    molecules.push(-p);
                }

                // association
                r = 1.0 * rand() / RAND_MAX;
                int n_mol = molecules.size();
                if (r > pow(1 - ass, n_mol * (n_mol - 1) / 2)) {
                    int p = rand() % n_mol + 1;
                    int q = rand() % (n_mol - 1) + 1;
                    q = p > q ? q : q + 1; 
                    molecules.adjust(p, molecules.val(q));
                    molecules.remove(q);
                }
            }
            return molecules;
        }
};

int size, dur;
double dis, ass;
int main() {
    printf("size: "); scanf("%d", &size);
    printf("disassociation prob: "); scanf("%lf", &dis);
    printf("association prob: "); scanf("%lf", &ass);
    printf("duration: "); scanf("%d", &dur);
    srand(time(NULL));
    Polymer p(size, dis, ass);
    p.simulate(dur).print();
}
