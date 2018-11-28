grade_one= {'Sami': [19, 18, 19.5, 30, 10],
             'Ahmad': [15, 14, 16, 21, 7],
             'Faris': [18, 19, 17, 26, 9],
             'Salem': [20, 20, 19, 30, 10],
             'Mahmoud': [12, 13, 11, 18, 7]}

grade_two= {'Lana': [17, 19, 20, 28, 9],
            'Dina': [18.5, 19.5, 20, 29, 10],
            'Maha': [20, 20, 18, 26, 9],
            'Abeer': [16, 18, 19.5, 25, 8]}

grade_three= {'Rima': [18, 19, 18, 26, 9],
              'Tala': [20, 20, 19, 29, 10],
              'Lamar': [19, 20, 18, 26, 9],
              'Rola': [15, 14, 16, 19, 7],
              'Naya': [9, 6, 11, 14, 7],
              'Dalal': [1, 5, 2, 6, 7],
              'Ola': [19.5, 20, 20, 29.5, 10]}
#) students_names
#تظهر قائمة بأسماء الطلاب في الصف٫ تأخذ ١ argument: اسم الصف

def students_names(grade):
      a=list(grade.keys())
      return a
#) student_score
#تظهر مجموع علامات طالب في صف معين٫ تأخذ ٢ arguments: اسم الصف، واسم الطالب

def student_score(grade,i):
      b=sum(grade.get(i,'not excit'))
      return b
#students_count
#تظهر عدد الطلاب في الصف، تأخذ ١ argument: اسم الصف
def students_count(grade):
      c=len(students_names(grade))
      return c

z="more"
while z=="more":
  print("Choose one: students_names, student_score, students_count")
  x=input()
  if x=="students_names":
    grade=input("Enter grade :")
    if grade =='grade_one':
       print (students_names(grade_one))
    elif  grade =='grade_two':
       print (students_names(grade_two))
    else:
       print (students_names(grade_three))

  elif x=="student_score":
     grade=input("Enter grade :")
     name=input("Enter student name :")
     if grade =='grade_one':
         for i in students_names(grade_one) :
             if name==i:

               print('score sum=',student_score(grade_one,i))

               break

     elif grade =='grade_two':
        for i in students_names(grade_two) :
            if name==i:

              print('score sum=',student_score(grade_two,i))

              break

     elif grade =='grade_three':
        for i in students_names(grade_three) :
            if name==i:
              print('score sum=',student_score(grade_three,i))

              break

     else :
        print ('end')


  elif x=="students_count":
     grade=input("Enter grade :")
     if grade =='grade_one':
       print (students_count(grade_one))
     elif  grade =='grade_two':
       print (students_count(grade_two))
     else:
       print (students_count(grade_three))
  else :
     print('try again')

  print("To finish enter done  To continue enter more")
  z=input()
  if z=="done" :
     print('Thank you')
     break
  elif z=="more" :
       continue
  else :
      print('Thank you')
