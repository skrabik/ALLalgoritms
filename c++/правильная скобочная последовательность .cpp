#include <iostream>
#include <vector>
#include <set>

using namespace std;

int length;
void copy(int m)
{
    length = m;
}

bool true_queele(vector<char> data)
{
    set<char> open = {'(', '['};
    vector<char> stack;

    for (int i = 0; i < data.size(); i++)
    {
        if (open.find(data[i]) != open.end())
        {
            stack.push_back(data[i]);
        }
        else
        {
            if (stack.size() == 0)
            {
                return false;
            }
            else if (data[i] == ')' && stack[stack.size() - 1] == '[')
            {
                return false;
            }
            else if (data[i] == ']' && stack[stack.size() - 1] == '(')
            {
                return false;
            }
            else
            {
                stack.pop_back();
            }
        }
    }
    return true;
}

void generate_permutations(vector<char> n, int m, vector<char> prefix, int c_open)
{

    if (c_open > length / 2)
    {
        return;
    }
    if (m == 0)
    {
        for (auto i : prefix)
        {
            cout << i;
        }
        cout << '\n';
        return;
    }
    for (auto digit : n)
    {
        prefix.push_back(digit);
        if (digit == '(' || digit == '[')
        {
            c_open++;
        }
        if (!true_queele(prefix))
        {
            prefix.pop_back();
            continue;
        }
        generate_permutations(n, m - 1, prefix, c_open);
        if (digit == '(' || digit == '[')
        {
            c_open--;
        }
        prefix.pop_back();
    }
}

int main()
{
    vector<char> n = {'(', '[', ']', ')'};
    int m;
    cin >> m;
    copy(m);
    vector<char> prefix;
    int c_open = 0;
    if (m % 2 == 1)
    {
        cout << '\n';
    }
    else
    {
        generate_permutations(n, m, prefix, c_open);
    }
}