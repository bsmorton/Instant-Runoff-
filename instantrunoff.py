import goody


def read_voter_preferences(file : open):
    d={}
    for line in file:
        temp=line.split(';')
        d.update({temp[0]:[item.strip('\n') for item in temp[1:]]})
    return d


def dict_as_str(d : {None:None}, key : callable=None, reverse : bool=False) -> str:
    return ''.join(['  '+name + ' -> ' + str(d[name])+'\n' for name in sorted(d.keys(),key = key ,reverse = reverse)])
        


def evaluate_ballot(vp : {str:[str]}, cie : {str}) -> {str:int}:
    c=cie.copy()
    d={c.pop():0 for val in range(len(c))}
    for item in vp.keys():
        for val in vp[item]:
            if val in cie:
                d[val]+=1
                break
    return d
                


def remaining_candidates(vd : {str:int}) -> {str}:
    return {item for item in vd.keys() if vd[item] != min(vd.values())}
    
        
            
        


def run_election(vp_file : open) -> {str}:
    d1=read_voter_preferences(vp_file)
    d2=evaluate_ballot(d1,{item1 for item1 in [item2 for item2 in d1.values()][0]})
    d4=sorted([item for item in d2.keys()])
    print('Vote count on ballot #1 with candidates (alphabetical order); remaining candidate set = ',{item for item in d4})
    for item in d4:
        print(item,'->',d2[item])
    print()
    d5=[item2[1] for item2 in sorted([(d2[item],item)for item in d4],reverse=True)]
    print('Vote count on ballot #1 with candidates (numerical order); remaining candidate set = ',set(d5))
    for item in d5:
        print(item,'->',d2[item])
    print()
    d3=remaining_candidates(d2)
    while len(d3)>1:
        d2=evaluate_ballot(d1,d3)
        d4=sorted(list(d3))
        print('Vote count on ballot #1 with candidates (alphabetical order); remaining candidate set = ',set(d4))
        for item in d4:
            print(item,'->',d2[item])
        print()
        d5=[item2[1] for item2 in sorted([(d2[item],item)for item in d4],reverse=True)]
        print('Vote count on ballot #1 with candidates (numerical order); remaining candidate set = ',set(d5))
        for item in d5:
            print(item,'->',d2[item])
        print()
        
        d3=remaining_candidates(d2)
        
    if len(d3)==1:
        print('Winner is  ',d3)
    else:
        print('Winner is None')  
    return d3    
    

  
  
  
  
    
if __name__ == '__main__':
    # Write script here
    file=input('Enter the name of any file with voter preferences:')
    prefs=read_voter_preferences(open(file))
    print()
    print('Voting Preferences')
    print(dict_as_str(prefs))
    print()
    run_election(open(file))
              
    # For running batch self-tests
    print()
    #import driver
    #driver.default_file_name = "bsc2.txt"
#     driver.default_show_traceback = True
#     driver.default_show_exception = True
#     driver.default_show_exception_message = True
    #driver.driver()
