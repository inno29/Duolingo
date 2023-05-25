import random               #imports needed modules
import operator
family_members={"le père":"father","la mère":"mother","le frère":"brother","la soeur":"sister","le grand-père":"grandpapi","la grand-mère":"grandmami"} #dictionaries for the foreign words and meaning
animals={"chameau":"camel","loup":"wolf","renard":"fox","ours":"bear","singe":"monkey"}
phrases={"je t'aime":"I love you","bonjour mon ami":"hello my friend","allons-y":"let's go","je te hais":"I hate you"}
family_members_hard={"tante":"aunt","petite fille":"grand daughter","ainee":"older brother/sister","cadette":"younger brother/sister"}
animals_hard={"chien":'dog','poisson rouge':'goldfish','souris':'mouse','lapin':'rabbit'}
phrases_hard={'au revoir':'goodbye',"c'est trop cher":"it's too expensive",'Je suis ravi de vous rencontrer':'I am pleased to meet you','comment ca va':'how are you'}

leaderboard={'Boss Inno':99999999}#dictionary for the scores

final_scores=[]#empty list for appending the scores

def menu():                       #function for the menu
    print('DUOLINGO MENU\n[1] New Game\n[2] View Leaderboards\n[3] How to Play?\n[4] Add Words\n[0] Exit\n')
    while True:
        x=(input('Enter choice: '))
        valid=['0','1','2','3','4']
        if x not in valid:
            print('invalid entry')
            continue
        break
    return x                                        

def reviewer():
    print('family members(normal)') #function for the list of words that will appear in the beginning
    for i in family_members:
        print(i+'=>'+family_members[i]+"\n") 
    print('animals(normal)')
    for i in animals:
        print(i+'=>'+animals[i]+"\n") 
    print ('phrases(normal')      
    for i in phrases:
        print(i+'=>'+phrases[i]+"\n") 
    print('family members(hard)')
    for i in family_members_hard:
         print(i+'=>'+family_members_hard[i]+"\n") 
    print('animals(hard)')
    for i in animals_hard:
         print(i+'=>'+animals_hard[i]+"\n") 
    print('phrases(hard)')
    for i in phrases_hard:
         print(i+'=>'+phrases_hard[i]+"\n") 
def family_question_hard_generator():
  
    new_list=random.sample(family_members_hard.keys(),k=len(family_members_hard))
    random_key=random.choice(new_list)
    choice1=family_members_hard[random_key]
    choice2=family_members_hard[new_list[0]]
    choice3=family_members_hard[new_list[1]]
    choice4=family_members_hard[new_list[2]]
    list_of_choice=[choice1,choice2,choice3,choice4]
    y=sorted(list_of_choice, key=lambda k: random.random())
    correct=0
    past_answer=[]
    possible_choices=[]
    for i in family_members_hard:
        random_key=random.choice(new_list)
        new_list.remove(random_key)
        past_answer.append(random_key)
        if len(past_answer)>=1:
            include_answer=new_list+past_answer
            choice1=family_members_hard[random_key]
            choice2=family_members_hard[include_answer[0]]
            choice3=family_members_hard[include_answer[1]]
            choice4=family_members_hard[include_answer[2]]
            include_answer=[choice1,choice2,choice3,choice4]
            y=sorted(include_answer, key=lambda k: random.random())
        else:
            choice1=family_members_hard[random_key]
            choice2=family_members_hard[new_list[0]]
            choice3=family_members_hard[new_list[1]]
            choice4=family_members_hard[new_list[2]]
            list_of_choice=[choice1,choice2,choice3,choice4]
            y=sorted(list_of_choice, key=lambda k: random.random())
    
        print('What is the meaning of '+random_key+'?')
        print('A. '+y[0])
        print('B. '+y[1])
        print('C. '+y[2])
        print('D. '+y[3]) 
        a=y[0]
        b=y[1]
        c=y[2]
        d=y[3]
        while True:
            final_choice=input("Enter your answer here: ").lower()

            if final_choice=="a":
                final_choice=a
                break
                
            if final_choice=="b":
                final_choice=b
                break
                
            if final_choice=="c":
                final_choice=c
                break
                
            if final_choice=="d":
                final_choice=d
                break
                
            if final_choice not in possible_choices:
                print('invalid answer')

            else:
                print('incorrect')
                break
        if (final_choice==choice1):
                correct=correct+2
        else:
            print('incorrect')
    if len(past_answer)==len(family_members_hard):
         print("You've finished all the questions!")  
         score=str(int(correct/2))
         total=str(len(phrases))
         print("you answered "+score+'/'+total+" items correctly")
         return correct

def animals_hard_question_generator():                                #functions for the question generators
    new_list=random.sample(animals_hard.keys(),k=len(animals_hard))  #creates a list from the keys of a select dictionary which are randomly positioned
    random_key=random.choice(new_list)                                 #chooses a random key
    choice1=animals_hard[random_key]                                    #assign the value of the chosen key to a variable
    choice2=animals_hard[new_list[0]]                                   #assign the other keys to other variables. The index chosen does not matter since they are all randomly positioned
    choice3=animals_hard[new_list[1]]
    choice4=animals_hard[new_list[2]]
    list_of_choice=[choice1,choice2,choice3,choice4]                   #creates a list of the choices
    y=sorted(list_of_choice, key=lambda k: random.random())             #changes the position of each keys
    correct=0                                                      
    past_answer=[]                                                        #creates an empty list for past answers
    possible_choices=[]                                                    #creates a list for the possible choices
    for i in animals_hard:                                                  #iterates over a dictionary
        random_key=random.choice(new_list)                           #chooses a random key fom the list of keys
        new_list.remove(random_key)                                #removes the key in new list and prevents it from being chosen
        past_answer.append(random_key)                           
        if len(past_answer)>=1:                                           #if the length of the list 'past_answer' is greater than or equal to one, reuse the elements in past_answer
            include_answer=new_list+past_answer                           #include_answer will be the possible choices for the question
            choice1=animals_hard[random_key]                               #assign to variables
            choice2=animals_hard[include_answer[0]]                             
            choice3=animals_hard[include_answer[1]]
            choice4=animals_hard[include_answer[2]]
            list_of_choice=[choice1,choice2,choice3,choice4]                      
            y=sorted(list_of_choice, key=lambda k: random.random())
        else:                                                
            choice1=animals_hard[random_key]
            choice2=animals_hard[new_list[0]]
            choice3=animals_hard[new_list[1]]
            choice4=animals_hard[new_list[2]]
            list_of_choice=[choice1,choice2,choice3,choice4]
            y=sorted(list_of_choice, key=lambda k: random.random())

        print('What is the meaning of '+random_key+'?')                   #sets up a question using the random key
        print('A. '+y[0])                                                 #randomized choices since y is sorted
        print('B. '+y[1])
        print('C. '+y[2])
        print('D. '+y[3]) 
        a=y[0]                                                           #assign variables
        b=y[1]
        c=y[2]
        d=y[3]
        while True:                                                      #loop to prevent faulty entries
            final_choice=input("Enter your answer here: ").lower()           #conditional  statments for choosing letter

            if final_choice=="a":
                final_choice=a
                break
                
            if final_choice=="b":
                final_choice=b
                break
                
            if final_choice=="c":
                final_choice=c
                break
                
            if final_choice=="d":
                final_choice=d
                break
                
            if final_choice not in possible_choices:             
                print('invalid answer')               

    
        if (final_choice==choice1):                                #checks if answer is correct
                correct=correct+2
    if len(past_answer)==len(animals_hard):                    #checks if all the questions have been asked
        print("You've finished all the questions!")  
        score=str(int(correct/2))                            
        total=str(len(animals))                                      
        print("you answered "+score+'/'+total+" items correctly")   #displays the score
        return correct                                          #returns the total correct answers
    
def phrases_hard_question_generator():                              #apply to all dictionaries except for leaderboards
 
    new_list=random.sample(phrases_hard.keys(),k=len(phrases_hard))
    random_key=random.choice(new_list)
    choice1=phrases_hard[random_key]
    choice2=phrases_hard[new_list[0]]
    choice3=phrases_hard[new_list[1]]
    choice4=phrases_hard[new_list[2]]                                   
    list_of_choice=[choice1,choice2,choice3,choice4]
    y=sorted(list_of_choice, key=lambda k: random.random())
    correct=0
    past_answer=[]
    possible_choices=[]
    for i in phrases_hard:
        random_key=random.choice(new_list)
        new_list.remove(random_key)
        past_answer.append(random_key)
        if len(past_answer)>=1:
            include_answer=new_list+past_answer
            choice1=phrases_hard[random_key]
            choice2=phrases_hard[include_answer[0]]
            choice3=phrases_hard[include_answer[1]]
            choice4=phrases_hard[include_answer[2]]
            include_answer=[choice1,choice2,choice3,choice4]
            y=sorted(include_answer, key=lambda k: random.random())
        else:
            choice1=phrases_hard[random_key]
            choice2=phrases_hard[new_list[0]]
            choice3=phrases_hard[new_list[1]]
            choice4=phrases_hard[new_list[2]]
            list_of_choice=[choice1,choice2,choice3,choice4]
            y=sorted(list_of_choice, key=lambda k: random.random())
    
        print('What is the meaning of '+random_key+'?')
        print('A. '+y[0])
        print('B. '+y[1])
        print('C. '+y[2])
        print('D. '+y[3]) 
        a=y[0]
        b=y[1]
        c=y[2]
        d=y[3]
        while True:
            final_choice=input("Enter your answer here: ").lower()

            if final_choice=="a":
                final_choice=a
                break
                
            if final_choice=="b":
                final_choice=b
                break
                
            if final_choice=="c":
                final_choice=c
                break
                
            if final_choice=="d":
                final_choice=d
                break
                
            if final_choice not in possible_choices:
                print('invalid answer')

            else:
                print('incorrect')
                break
        if (final_choice==choice1):
                correct=correct+2
    if len(past_answer)==len(phrases_hard):
         print("You've finished all the questions!")  
         score=str(int(correct/2))
         total=str(len(phrases))
         print("you answered "+score+'/'+total+" items correctly")
         return correct

def family_question_generator():
    new_list=random.sample(family_members.keys(),k=len(family_members))
    random_key=random.choice(new_list)
    choice1=family_members[random_key]
    choice2=family_members[new_list[0]]
    choice3=family_members[new_list[1]]
    choice4=family_members[new_list[2]]
    list_of_choice=[choice1,choice2,choice3,choice4]
    correct=0
    past_answer=[]
    possible_choices=[]
    y=sorted(list_of_choice, key=lambda k: random.random())
    for i in family_members:
        random_key=random.choice(new_list)
        new_list.remove(random_key)
        past_answer.append(random_key)
        if len(past_answer)>=2:
            include_answer=new_list+past_answer
            choice1=family_members[random_key]
            choice2=family_members[include_answer[0]]
            choice3=family_members[include_answer[1]]
            choice4=family_members[include_answer[2]]
            include_answer=[choice1,choice2,choice3,choice4]
            y=sorted(include_answer, key=lambda k: random.random())
        else:
            choice1=family_members[random_key]
            choice2=family_members[new_list[0]]
            choice3=family_members[new_list[1]]
            choice4=family_members[new_list[2]]
            list_of_choice=[choice1,choice2,choice3,choice4]
            y=sorted(list_of_choice, key=lambda k: random.random())
        print('What is the meaning of '+random_key+'?')
        print('A. '+y[0])
        print('B. '+y[1])
        print('C. '+y[2])
        print('D. '+y[3]) 
        a=y[0]
        b=y[1]
        c=y[2]
        d=y[3]
        while True:
            final_choice=input("Enter your answer here: ").lower()

            if final_choice=="a":
                final_choice=a
                break
                
            if final_choice=="b":
                final_choice=b
                break
                
            if final_choice=="c":
                final_choice=c
                break
                
            if final_choice=="d":
                final_choice=d
                break
                
            if final_choice not in possible_choices:
                print('invalid answer')

            else:
                print('incorrect')
                break
        if (final_choice==choice1):
                correct=correct+1
    if len(past_answer)==len(family_members):
        print("You've finished all the questions!")  
        score=str(correct)
        total=str(len(family_members))
        print("you answered "+score+'/'+total+" items correctly")
        return correct
    

def animals_question_generator():
    new_list=random.sample(animals.keys(),k=len(animals))
    random_key=random.choice(new_list)
    choice1=animals[random_key]
    choice2=animals[new_list[0]]
    choice3=animals[new_list[1]]
    choice4=animals[new_list[2]]
    list_of_choice=[choice1,choice2,choice3,choice4]
    y=sorted(list_of_choice, key=lambda k: random.random())
    correct=0
    past_answer=[]
    possible_choices=[]
    for i in animals:
        random_key=random.choice(new_list)
        new_list.remove(random_key)
        past_answer.append(random_key)
        if len(past_answer)>=2:
            include_answer=new_list+past_answer
            choice1=animals[random_key]
            choice2=animals[include_answer[0]]
            choice3=animals[include_answer[1]]
            choice4=animals[include_answer[2]]
            include_answer=[choice1,choice2,choice3,choice4]
            y=sorted(include_answer, key=lambda k: random.random())
        else:
            choice1=animals[random_key]
            choice2=animals[new_list[0]]
            choice3=animals[new_list[1]]
            choice4=animals[new_list[2]]
            list_of_choice=[choice1,choice2,choice3,choice4]
            y=sorted(list_of_choice, key=lambda k: random.random())

        print('What is the meaning of '+random_key+'?')
        print('A. '+y[0])
        print('B. '+y[1])
        print('C. '+y[2])
        print('D. '+y[3]) 
        a=y[0]
        b=y[1]
        c=y[2]
        d=y[3]
        while True:
            final_choice=input("Enter your answer here: ").lower()

            if final_choice=="a":
                final_choice=a
                break
                
            if final_choice=="b":
                final_choice=b
                break
                
            if final_choice=="c":
                final_choice=c
                break
                
            if final_choice=="d":
                final_choice=d
                break
                
            if final_choice not in possible_choices:
                print('invalid answer')

            else:
                print('incorrect')
                break
        if (final_choice==choice1):
                correct=correct+1
    if len(past_answer)==len(animals):
        print("You've finished all the questions!")  
        score=str(correct)
        total=str(len(animals))
        print("you answered "+score+'/'+total+" items correctly")
        return correct

def phrases_question_generator():
    new_list=random.sample(phrases.keys(),k=len(phrases))
    random_key=random.choice(new_list)
    choice1=phrases[random_key]
    choice2=phrases[new_list[0]]
    choice3=phrases[new_list[1]]
    choice4=phrases[new_list[2]]
    list_of_choice=[choice1,choice2,choice3,choice4]
    y=sorted(list_of_choice, key=lambda k: random.random())
    correct=0
    past_answer=[]
    possible_choices=[]
    for i in phrases:
        random_key=random.choice(new_list)
        new_list.remove(random_key)
        past_answer.append(random_key)
        if len(past_answer)>=1:
            include_answer=new_list+past_answer
            choice1=phrases[random_key]
            choice2=phrases[include_answer[0]]
            choice3=phrases[include_answer[1]]
            choice4=phrases[include_answer[2]]
            include_answer=[choice1,choice2,choice3,choice4]
            y=sorted(include_answer, key=lambda k: random.random())
        else:
            choice1=phrases[random_key]
            choice2=phrases[new_list[0]]
            choice3=phrases[new_list[1]]
            choice4=phrases[new_list[2]]
            list_of_choice=[choice1,choice2,choice3,choice4]
            y=sorted(list_of_choice, key=lambda k: random.random())
        print('What is the meaning of '+random_key+'?')
        print('A. '+y[0])
        print('B. '+y[1])
        print('C. '+y[2])
        print('D. '+y[3]) 
        a=y[0]
        b=y[1]
        c=y[2]
        d=y[3]
        while True:
            final_choice=input("Enter your answer here: ").lower()

            if final_choice=="a":
                final_choice=a
                break
                
            if final_choice=="b":
                final_choice=b
                break
                
            if final_choice=="c":
                final_choice=c
                break
                
            if final_choice=="d":
                final_choice=d
                break
                
            if final_choice not in possible_choices:
                print('invalid answer')

            else:
                print('incorrect')
                break
        if (final_choice==choice1):
                correct=correct+1
    if len(past_answer)==len(phrases):
         print("You've finished all the questions!")  
         score=str(correct)
         total=str(len(phrases))
         print("you answered "+score+'/'+total+" items correctly")
         return correct

def add_word():                                                       #function for adding the words
    valid=['1','2','3']                                               #makes a list of valid answers
    while True:                                                      
        print('which category would you like to add your word?')        #menu for the choices on what dictionary the word will be added and loop to prevent invalid answers
        print("[1]family\n[2]animal\n[3]phrases\n[4]I'm done")
        x=(input('Enter your choice: '))
        if x=='4':
            break
        if x not in valid:
            print('invalid entry')
        print('choose the difficulty of the word')
        print('[1]Normal\n[2]Hard')
        y=(input('Enter your choice: '))
        if y not in valid:
            print('invalid entry')
        new_word=input('what is the new word? ')
        meaning=input('what is the meaning? ')                     #asks for the word and its meaning
        if (x=='1') and (y=='1'):
            if new_word in family_members:
                print('already added')
            else:
                family_members[new_word]=meaning
                save_word_family()                             #saves the word to a file and loads it
                load_family()
        
        if (x=='1') and (y=='2'):
            if new_word in family_members_hard:
                print('already added')
            else:
                family_members_hard[new_word]=meaning
                save_word_family_hard()
                load_family_hard()
        
        if (x=='2') and (y=='1'):
            if new_word in animals:
                print('already added')
            else:
                animals[new_word]=meaning
                save_word_animals()
                load_animals()
        
        if (x=='2') and (y=='2'):
            if new_word in animals_hard:
                print('already added')
            else:
                animals_hard[new_word]=meaning
                save_word_animals_hard
                load_animals_hard
        
        if (x=='3') and (y=='1'):
            if new_word in phrases:
                print('already added')
            else:
                phrases[new_word]=meaning
                save_word_phrases()
                load_phrases
        
        if (x=='3') and (y=='2'):
            if new_word in phrases_hard:
                print('already added')
            else:
                phrases_hard[new_word]=meaning
                save_word_phrases_hard()
                load_phrases_hard
                
def load_family():                                  
    fileHandle=open('family.txt', 'r')                                #function for loading a file
    for line in fileHandle:
        data=line[:-1].split(",")        
        word=data[0]
        meaning=data[1]
        family_members[word]=meaning
    fileHandle.close()
def load_animals():
    fileHandle=open('animals.txt', 'r')
    for line in fileHandle:
        data=line[:-1].split(",")
        word=data[0]
        meaning=data[1]
        animals[word]=meaning
    fileHandle.close()
def load_phrases():
    fileHandle=open('phrases.txt', 'r')
    for line in fileHandle:
        data=line[:-1].split(",")
        word=data[0]
        meaning=data[1]
        phrases[word]=meaning
    fileHandle.close()
def load_family_hard():
    fileHandle=open('family_hard.txt', 'r')
    for line in fileHandle:
        data=line[:-1].split(",")
        word=data[0]
        meaning=data[1]
        family_members_hard[word]=meaning
    fileHandle.close()
def load_animals_hard():
    fileHandle=open('animals_hard.txt', 'r')
    for line in fileHandle:
        data=line[:-1].split(",")
        word=data[0]
        meaning=data[1]
        animals_hard[word]=meaning
    fileHandle.close()
def load_phrases_hard():
    fileHandle=open('phrases_hard.txt', 'r')
    for line in fileHandle:
        data=line[:-1].split(",")
        word=data[0]
        meaning=data[1]
        phrases_hard[word]=meaning
    fileHandle.close()

def save_word_family():                            #function for saving
    fileHandle=open('family.txt','w' )
    for k in family_members:
        a=family_members[k]
        fileHandle.write(k+","+a+'\n')
    fileHandle.close()

def save_word_animals():
    fileHandle=open('animals.txt','w' )
    for k in animals:
        a=animals[k]
        fileHandle.write(k+","+a+'\n')
    fileHandle.close()

def save_word_phrases():
    fileHandle=open('phrases.txt','w' )
    for k in phrases:
        a=phrases[k]
        fileHandle.write(k+","+a+'\n')
    fileHandle.close()

def save_word_family_hard():
    fileHandle=open('family_hard.txt','w' )
    for k in family_members_hard:
        a=family_members_hard[k]
        fileHandle.write(k+","+a+'\n')
    fileHandle.close()

def save_word_animals_hard():
    fileHandle=open('animals_hard.txt','w' )
    for k in animals_hard:
        a=animals_hard[k]
        fileHandle.write(k+","+a+'\n')
    fileHandle.close()

def save_word_phrases_hard():
    fileHandle=open('phrases_hard.txt','w' )
    for k in phrases_hard:
        a=phrases_hard[k]
        fileHandle.write(k+","+a+'\n')
    fileHandle.close()
    


def difficulty():
        print('choose a difficulty\n[1]Normal\n[2]Hard')  #menu for difficulty
        x=str(input('enter choice: '))
        return x


def category():
    print('Choose a category')
    print("[1]family\n[2]animals\n[3]phrases\n[4]I'm done")  #menu for the category
    x=input("Enter your choice: ")
    return x

def addscore(x): 
    name=input("Enter your name: ")            #function for adding the score to the leaderboard
    leaderboard[name]=x
    save_leaderboard()

def viewleaderboard():
    descending_lb=dict(sorted(leaderboard.items(), key=operator.itemgetter(1),reverse=True))         #prints the leaderboard in descending order
    for i in descending_lb:
        print('Name: ',i)    
        print('Score: ',descending_lb[i])

def save_leaderboard():                                                                                   #function to save the leaderboard
    fileHandle=open('leaderboard.txt','w' )
    descending_lb=dict(sorted(leaderboard.items(), key=operator.itemgetter(1),reverse=True))
    for k in descending_lb:
        a=str(descending_lb[k])
        fileHandle.write(k+","+a+'\n')
    fileHandle.close()

def load_leaderboard():
    fileHandle=open('leaderboard.txt', 'r')                                                         #loads the leaderboard
    reverse_lb=dict(sorted(leaderboard.items(), key=lambda item: item[1]))
    descending_lb=dict(sorted(reverse_lb.items(), key=operator.itemgetter(1),reverse=True))
    for line in fileHandle:
        data=line[:-1].split(",")
        name=data[0]
        score=data[1]
        descending_lb[name]=score
    fileHandle.close()

def clear():
    import os                                                        #function for clearing
    os.system('cls' if os.name=='nt' else 'clear')
    return("   ")
    
def gamestart():                                                                             #function for when the game starts
    reviewer()
    x=input(print('Type DONE if you are done viewing the foreign words:'))
    y=x.lower()
    chosen_categories=[]             
    list_of_scores=[]
    valid=['1','2','3','4']
    if y=="done":
        clear()
        while True:                                                 #loop to prevent invalid questions and conditional statements to prevent repeat of a category
            a=category()                                                   #displays the category
            if a=='1':
                if a in chosen_categories:                               #conditional statements that determine what action to do
                    print('you have already chosen that')
                else:
                    chosen_categories.append('1')
                    b=difficulty()
                    if b=='1':                                     #conditional statement to know what question to generate and appends the scores to be added
                        j=family_question_generator()
                        list_of_scores.append(j)
                    if b=='2':
                        j=family_question_hard_generator()
                        list_of_scores.append(j)
                    else:                                     
                        print('enter a valid choice')
                        chosen_categories.remove('1') 
            if a=='2':                                 
                if a in chosen_categories:
                    print('you have already chosen that')
                else:
                    chosen_categories.append('2')
                    b=difficulty()
                    if b=='1':
                        j=animals_question_generator()
                        list_of_scores.append(j)
                    if b=='2':
                        j=animals_hard_question_generator()
                        list_of_scores.append(j)
                    else:
                        print('enter a valid choice')
                        chosen_categories.remove('2') 
                    
            if a=='3':
                if a in chosen_categories:
                    print('you have already chosen that')            
                else:
                    b=difficulty()
                    chosen_categories.append('3')
                    if b=='1':
                        j=phrases_question_generator()
                        list_of_scores.append(j)
                    if b=='2':
                        j=phrases_hard_question_generator()
                        list_of_scores.append(j)
                    else:
                        print('enter a valid choice')   
                        chosen_categories.remove('3') 
            if a=='4':
                p=sum(list_of_scores)                   #exits the game and adds the scores
                addscore(p)
                home()

            if a not in valid:
                print('bro just follow the instructions') 
        
    else: 
        print('check your spelling!')
        reviewer()
        x=input(print('Type done if you are done viewing the foreign words: '))
        y=x.lower()
    

def home():     #mother function
    c=menu()
    if c=='1':
        gamestart()                   #conditional statements for each choice
        load_leaderboard()
        home()
    if c=='2':                       #views the leaderboards
        viewleaderboard()
        home()
    if c=='3':
        while True:
            print('This is Duolingo!\nChoose a category and difficulty(hard gives you two points each correct answer)\nRemember!in one session, you can only choose a category once! so choose the difficulty wisely! and assess your capabilities\nWhen the game starts you will be given time to review all the words and their meaning\nDuring the game just select the corresponding meaning of the foreign word\nMake sure to save your name so we can save your score in the leaderboards!\nI hope you enjoy the game:)')
            x=input('Enter 1 if done reading: ')
            if x=='1':
                home()
                break
            else:
                print('invalid entry')
    if c=='4':
        add_word()                     #adds a new word
        print('done')
        home()
    if c=='0':
        print('Thank you for playing Duolingo')         #ends the program

home()


