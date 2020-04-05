
"""

opening file to readlines

"""

a = open('date_and_timing.txt' , 'r')

doc = a.readlines()
print(doc)

while True :
 requested = input('Enter request:')
 request = requested.lower()
 request = request.replace(' ' , '')

 if request == 'groupmembers' or request == 'group' or request == 'developers' or request == 'groupmember':
      print ( 'MAYUR' )
      print ( 'ROUNIK SAHA' )
      print ( 'KUNGA TOPGAYAL' )

 if request == "what'smyname?" or request == "whatsmyname?" or request == "whatsmyname" or request == 'myname?' or request =='myname' :
                    ##    my name entered by user
      print (myname)

 if request == "what'syourname?" or request == "whatsyourname?" or request == "whatsyourname" or request == 'yourname?' or request =='yourname' :
                    ##    chatbot name entered by user
      print (chatbot)

 if request == 'bye' or request == 'goodbye' or request == 'exit' or request == 'close' or request == 'end' :
      print ('Bye')
      break       ##    to end the conversation
     

 i = 0
 j = 0
 for lines in doc:
     stats = lines [:-1]
     stat = stats.replace(' ','')
     i += 1
     if stat == request :
         response = doc[i]
         print(response)
         break
     else:
         j += 1
 if i == j :
     print("I don't understand")