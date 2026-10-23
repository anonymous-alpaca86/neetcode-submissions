class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        for row in range(9):
            val_row=self.valid_9(board[row])
            if not val_row:
                return False
        
        for i in range(9):
            column_lst=[]
            for j in range(9):
                column_lst.append(board[j][i])
            val_col=self.valid_9(column_lst)
            if not val_col:
                return False

        for i in range(0,9,3):
            for j in range(0,9,3):
                sqr_lst=[]
                for row in board[i:i+3]:
                    sqr_lst.extend(row[j:j+3])
                print(sqr_lst)
                val_sqr=self.valid_9(sqr_lst)
                if not val_sqr:
                    return False
        return True
    #check if a row/column/square is valid or not
    def valid_9(self,lst):
        bucket=[0,0,0,0,0,0,0,0,0,0]
        for i in range(len(lst)):
            if lst[i]==".":
                continue
            else:
                key=int(lst[i])
                bucket[key]+=1
        print(bucket)
        for count in bucket:
            if count>1:
                return False
        return True

