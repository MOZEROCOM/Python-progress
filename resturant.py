rating={'Georgie Porgie':97,
        'Queen St. Cafe':84 ,
        'Dumplings R Us':71,
        'Deep Fried Everything':62,
        'Mexican Grill':55}

price={'$':['Queen St. Cafe', 'Dumplings R Us', 'Deep Fried Everything'],
        '$$':[ 'Mexican Grill'],
        '$$$': ['Georgie Porgie','Deep Fried Everything'],
        '$$$$':['Queen St. Cafe']}

cuisines={'Canadian': ['Georgie Porgie'],
        'Pub Food':['Georgie Porgie', 'Deep Fried Everything'],
        'Malaysian':['Queen St. Cafe'],
        'Thai':['Queen St. Cafe'],
        'Chinese':['Dumplings R Us'],
        'Mexican':['Mexican Grill']}

rate=int(input('Enter desired rating: '))
def rank(rate):
    rank_rating=dict(sorted(rating.items(),key=lambda item:item[1],reverse=True))
    if rate <= 100 and rate>=0:    
        high_rated =list( {name: score for name, score in rank_rating.items() if score >= rate})
        # print(high_rated)
        
    else:
        print('Enter the right rating.')
        rate=int(input())
        rank(rate)
    return high_rated
rank(rate) 
  

cost=input('Enter pricing as $ or $$ or $$$ or $$$$: ')
def pricing(cost):
    
    if cost=='$':    
        a= price['$']
        b= rank(rate)
        common=list(set(a)&set(b)) 
        # print(common)
    elif cost=='$$':
        a=  price['$$']
        b= rank(rate)
        common=list(set(a)&set(b)) 
        # print(common)
    elif cost=='$$$':
        a=  price['$$$']
        b= rank(rate)
        common=list(set(a)&set(b)) 
        # print(common)
    elif cost=='$$$$':
        a=  price['$$$$']
        b= rank(rate)
        common=list(set(a)&set(b)) 
        # print(common)
    else:
        print('Enter right pricing.')
        cost=input()
        pricing(cost)              
    return common
pricing(cost)
print('''Available Cuisines
      Canadian
      Pub Food
      Malaysian
      Chinese
      Thai
      Mexican''')

cuisine =input('Enter desired cuisine: ').title()        
def cuisine_type(cuisine):
    if cuisine=='Canadian':
        c=cuisines['Canadian']
        d=pricing(cost)
        final=str(set(c)&set(d))
        print ("According to your criteria this are/is the resturant you should visit {}".format(final))    

    elif cuisine=='Pub Food':
        c=cuisines['Pub Food']
        d=pricing(cost)
        final=list(set(c)&set(d))
        print ("According to your criteria this are/is the resturant you should visit {}".format(final))    

    elif cuisine=='Malaysian':
        c=cuisines['Malaysian']
        d=pricing(cost)
        final=str(set(c)&set(d))
        print ("According to your criteria this are/is the resturant you should visit {}".format(final))    

    elif cuisine=='Chinese':
        c=cuisines['Chinese']
        d=pricing(cost)
        final=str(set(c)&set(d))
        print ("According to your criteria this are/is the resturant you should visit {}".format(final))    

    elif cuisine=='Thai':
        c=cuisines['Thai']
        d=pricing(cost)
        final=str(set(c)&set(d))
        print ("According to your criteria this are/is the resturant you should visit {}".format(final))    

    elif cuisine=='Mexican':
        c=cuisines['Mexican']
        d=pricing(cost)
        final=str(set(c)&set(d))
        print ("According to your criteria this are/is the resturant you should visit {}".format(final))
    else:
        print('Enter among mentioned cuisines.')
        cuisine=input()
        cuisine_type(cuisine)
    return print
cuisine_type(cuisine)

