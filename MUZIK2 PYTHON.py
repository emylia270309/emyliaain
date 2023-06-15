#pyhton quiz game

question=("*sinaran matamu terisi cereka permainan asmara antara kita*\n""Berdasarkan lirik lagu di atas,apakah jenis genre muzik tersebut?:\n",
          "*cindailah mana tidak berkias,Jalinya lalu rentah beribu*\n""Pilih jenis genre lagu di atas.: \n",
          "*Adik pandang-pandang,Pandang pada siapa kalau pada abang hai gembira rasanya*\n""Apakah jenis genre muzik yang diberi?:\n",)

options=(("A.Dangdut ","B.Rock ","C.Jazz ","D.Blues "),
         ("A.Opera ","B.Jiwang ","C.Classical music ","D.Hip hop "),
         ("A.Funk ","B.World music ","C.Dangdut ","D.Zapin music "))

answers =("B","C","D")
guesses=[]
score=0

question_num=0

for question in question:
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        print(question)

        for option in options[question_num]:

            print,'\n',
            print(option)

        guess=input("Enter (A,B,C,D): ").upper()
        
        guesses.append(guess)
        if guess == answers[question_num]:
            score +=1
            
            print("\n^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")
            print("CONGRATULATIONS ON YOUR SUCCES!")
            print("^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")
        else:
            print("\nSORRY YOU DID NOT SUCCEED PLEASE TRY AGAIN!")
            print(f"{answers[question_num]} IS THE CORRECT ANSWER")
        question_num +=1


print("\n<><><><><><><><><><><><><><><><><><>")
print("               RESULT              ")
print("<><><><><><><><><><><><><><><><><><>")

print("ANSWER: ", end="")

for answer in answers:
    print(answer, end="")

print()


print("guesses: ", end="")
for guess in guesses:
     print(guess, end="")

print()

markah = (score / question_num )* 100
print(f"YOUR SCORE IS: ", round (markah,2), "%")
print ("<><><><><><><><><><><><><><><><><><>")
