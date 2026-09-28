feedback_data = { 'S_No': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
                  'Name': ['Ravi', 'Meera', 'Sam', 'Anu', 'Raj', 'Divya',
                           'Arjun', 'Kiran', 'Leela', 'Nisha'],
                  'Feedback': [ ' Very GOOD Service!!!',
                                'poor support, not happy    ',                            
                                'GREAT experience! will come again.',
                                'okay okay...',
                                ' not BAD',
                                'Excellent care, excellent staff!',
                                'good food and good ambience!',
                                'Poor response and poor handling of issue',
                                'Satisfied. But could be better.',
                                'Good support... quick service.' ],
                  'Rating': [5, 2, 5, 3, 2, 5, 4, 1, 3, 4]}
f=int(input("Enter the number of feedbacks you want to enter "))
i=1
while(i<=f):
    s=(feedback_data['S_No'][-1])+1
    n=input("Enter name: ")
    e=input("Enter feedback: ")
    r=int(input("Enter rating between 1-5 "))
    feedback_data['S_No'].append(s)
    feedback_data['Name'].append(n)
    feedback_data['Feedback'].append(e)
    feedback_data['Rating'].append(r)
    i=i+1
for j in range(len(feedback_data['Feedback'])):
    h=feedback_data['Feedback'][j]
    h=h.replace('.','')
    h=h.replace(',','')
    h=h.replace('!','')
    h=h.replace('?','')
    h=' '.join(h.split())
    h=h.lower()
    feedback_data['Feedback'][j]=h
    
def count_word_in_feedbacks(word):
    c=0
    word=word.lower()
    
    for k in feedback_data['Feedback']:
        
        u=k.split()
        if word in u:
            c=c+1
    return c     
       
print("\n \n Number of feedbacks containing 'good':",
      count_word_in_feedbacks('good'))

print("\n \n Number of feedbacks containing 'poor':",
      count_word_in_feedbacks('poor'))

print("\n \n Number of feedbacks containing 'excellent':",
      count_word_in_feedbacks('excellent'))

print("\n \n Final Cleaned Feedback Data: \n")

print(feedback_data)



avg = sum(feedback_data['Rating'])/len(feedback_data['Rating'])
print("\n \n Average Rating: ", avg)

longestfeed=""
longest=0
for feed in feedback_data['Feedback']:
    feedl=len(feed.split())
    if feedl>longest:
        longest =feedl
        longestfeed=feed
print("\n \n  Longest Feedback: ")
print(longestfeed)

print("\n \n Number of words in longest feedback: ", longest)

uni=set()
for wor in feedback_data['Feedback']:
    wlist=wor.split()
    for word in wlist:
         uni.add(word)
   

print("\n \n Unique words: ",uni)

print("\n \n")
combine = zip(feedback_data['Rating'],feedback_data['S_No'], feedback_data['Name'],
              feedback_data['Feedback'])
sdata=sorted(combine,reverse=True)
print(f"{'Rating':<7}|{'S_No':<5}|{'Name':<7}|{'Feedback'}")
print("-"*65)
for rate, sl,nam,feedb in sdata:
    print(f"{rate:<7}|{sl:<5}|{nam:<7}|{feedb.strip()}")
    
    
    
   

