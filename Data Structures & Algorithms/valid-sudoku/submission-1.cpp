class Solution {
public:
    bool isValidSudoku(vector<vector<char>>& board) {
        
        for (int row = 0; row < 9; row++) {
            for (int nums = 1; nums < 10; nums++) {
                if (count(board[row].begin(), board[row].end(), nums + '0') > 1) {
                    return false;
                }
            }
        }

        int sq1[9] = {0};
        int sq2[9] = {0};
        int sq3[9] = {0};
        int sq4[9] = {0};
        int sq5[9] = {0};
        int sq6[9] = {0};
        int sq7[9] = {0};
        int sq8[9] = {0};
        int sq9[9] = {0};

        for (int col = 0; col < 9; col++) {
            int columnVals[9] = {0};
            for (int row = 0; row < 9; row++) {
                if (board[row][col] != '.') {
                    if (columnVals[board[row][col]-'0'-1] == 1) {
                        return false;
                    }
                    columnVals[board[row][col]-'0'-1] += 1;
                    if (row < 3 && col < 3) {
                        if (sq1[board[row][col]-'0'-1] == 1) {
                            return false;
                        }
                        sq1[board[row][col]-'0'-1] += 1;
                    }
                    if (2 < row && row < 6 && col < 3) {
                        if (sq2[board[row][col]-'0'-1] == 1) {
                            return false;
                        }
                        sq2[board[row][col]-'0'-1] += 1;
                    }
                    if (5 < row && col < 3) {
                        if (sq3[board[row][col]-'0'-1] == 1) {
                            return false;
                        }
                        sq3[board[row][col]-'0'-1] += 1;
                    }

                    if (row < 3 && col > 2 && col < 6) {
                        if (sq4[board[row][col]-'0'-1] == 1) {
                            return false;
                        }
                        sq4[board[row][col]-'0'-1] += 1;
                    }
                    if (2 < row && row < 6 && col > 2 && col < 6) {
                        if (sq5[board[row][col]-'0'-1] == 1) {
                            return false;
                        }
                        sq5[board[row][col]-'0'-1] += 1;
                    }
                    if (5 < row && col > 2 && col < 6) {
                        if (sq6[board[row][col]-'0'-1] == 1) {
                            return false;
                        }
                        sq6[board[row][col]-'0'-1] += 1;
                    }

                    if (row < 3 && col > 5) {
                        if (sq7[board[row][col]-'0'-1] == 1) {
                            return false;
                        }
                        sq7[board[row][col]-'0'-1] += 1;
                    }
                    if (2 < row && row < 6 && col > 5) {
                        if (sq8[board[row][col]-'0'-1] == 1) {
                            return false;
                        }
                        sq8[board[row][col]-'0'-1] += 1;
                    }
                    if (5 < row && col > 5) {
                        if (sq9[board[row][col]-'0'-1] == 1) {
                            return false;
                        }
                        sq9[board[row][col]-'0'-1] += 1;
                    }
                }
            }
        }
        return true;
    }
};
