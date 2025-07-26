
// Fails at condition like "aa" and "a"
class Solution {
public:
    bool isAnagram(string s, string t) {
        return set<char>(s.begin(), s.end()) == set<char>(t.begin(), t.end());   
    }
};

// Approach using unordered_map to count character frequencies

class Solution {
public:
    bool isAnagram(string s, string t) {
        if(s.length() != t.length()) return false;

        unordered_map<char, int> freq;

        for(char c : s) freq[c]++;
        for(char c : t) freq[c]--;

        for(auto [ch, count] : freq) {
            if(count != 0) return false;
        }
        return true;
    }
};

// Another approach using sorting

class Solution {
public:
    bool isAnagram(string s, string t) {
        sort(s.begin(), s.end());
        sort(t.begin(), t.end());
        return s == t;
    }
};