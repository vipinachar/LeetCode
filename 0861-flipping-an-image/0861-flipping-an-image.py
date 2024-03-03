def invert(source: List[int], value:int)->int:
    if source[value] == 0:
        source[value] = 1 
    else:
        source[value] = 0 

class Solution:
    def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:


        
        for row_index in range(0,len(image)): # o(n)
            row = image[row_index]

            start_pointer = 0 
            end_pointer = len(row)-1

            while ( start_pointer < (len(row)//2) ) : # o(n/2)
                tmp = row[start_pointer]
                row[start_pointer] = row[end_pointer]
                row[end_pointer] = tmp 

                invert(row, start_pointer)
                invert(row, end_pointer)

                start_pointer = start_pointer + 1
                end_pointer = end_pointer - 1 
            
            if start_pointer == end_pointer:
                invert(row, start_pointer)
            
        return image  # tc: o(n^2) sc: o(1)
                






        