  def countdown(n):
        if n<=0:
            print ('Blastoff!!')
            else:
                print(n)
                countdown(n-1)
  def countup(n):
        if n>=0:
            print ('Blastoff!!')
            else:
                print(n)
                countup(n+1)
                #Ask user to input the number
                num=int(input('Enter number'))

                num=int(num)
                if num>=0:
                    #count down positive numbers including zero
                    countdown(num)
                    elif num<0:
                        #count up negative number
                        countup(num)
                        else:
                            print('Blastoff!!')
        