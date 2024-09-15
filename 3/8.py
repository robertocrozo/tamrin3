def nickname():
    trav = input()
    
    haji_cond = ['YYY', 'YYN', 'YNY', 'YNN']
    karbalaee_cond = ['NYY', 'NYN']
    mashti_cond = 'NNY'
    agha_cond = 'NNN'

    
    if trav in haji_cond:
        print('Haji')
    elif trav in karbalaee_cond:
        print('Karbalaee')
    elif trav == mashti_cond:
        print('Mashti')
    elif trav == agha_cond:
        print('Agha')
    else:
        return


nickname()