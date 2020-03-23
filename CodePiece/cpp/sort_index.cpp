vector<int> data = {5, 16, 4, 7};   
vector<int> index(data.size(), 0);
for (int i = 0 ; i != index.size() ; i++) {
    index[i] = i;
}
sort(index.begin(), index.end(),
    [&](const int& a, const int& b) {
        return (data[a] < data[b]);
    }
);
for (int i = 0 ; i != index.size() ; i++) {
    cout << index[i] << endl;
}
