'''

@Author: Venkatesh
@Date: 2024-08-16 18:00:30
@Last Modified by: Venkatesh
@Last Modified time: 2024-08-16 18:00:30
@Title : Python Program vending machine change

'''


def find_notes(change,notes,note_count,result):
    '''
          Description: 
                this function is getting change of vanding machine
          Parameters: 
                notes: notes list of items
                change: change of vanding machine 
          Return : 
                this function notes 
        '''
    if(change==0):
        return 0,[]
    for note in notes:
        if note<=change:
            note_count= note_count+1
            result.append(note)
            return find_notes(change-note,notes,note_count,result)


def vending_machine(change):
      '''
          Description: 
                this function is getting change of note
          Parameters: 
                change: change  
          Return : 
                this function notes and combination
        '''
      notes=[1000,500,100,50,10,5,2,1]
      note_count=0
      result=[]
      min_notes,combination_notes = find_notes(change,notes,note_count,result)
      return min_notes,combination_notes


def main():
     change=int(input("Enter change in Rs to return by the vending machine:"))
     min_notes,combination_notes=vending_machine(change)
     print(f"minimum notes :{min_notes}")
     print(f"Notes are return :{combination_notes}")


if __name__=="__main__":
    main()