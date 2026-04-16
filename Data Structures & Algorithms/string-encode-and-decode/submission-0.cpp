class Solution {
public:

    string encode(vector<string>& strs) {
        string result;

        for(const string& s:strs){

             result += to_string(s.size()) + "#" + s;
        }

return result;
    }

    vector<string> decode(string s) {
     vector<string> res;
     int i=0;

     while(i<s.size()){

        int j=i;
        while(s[j]!='#'){
            j++;
        }
        int length=stoi(s.substr(i,j-i));

        i=j+1;
        j=i+length;

        res.push_back(s.substr(i,length));
        i=j;
     }

    return res;
    }
};
