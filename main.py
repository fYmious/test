questions = {"How many elements are in the periodic table?: ": 'A',
             "Which animal lays the largest eggs?: ": 'B',
             "What is the most abundant gas in Earth's atmosphere?: ": 'C',
             "How many bones are in the human body?: ": 'D',
             "Which planet in the solar system is the hottest?: ": 'A'}

options = (("A. 116", "B. 117", "C. 118", "D. 119"),
           ("A. Whale", "B. Crocodile", "C. Elephant", "D. Ostrich"),
           ("A. Nitrogen", "B. Oxygen", "C. Carbon-Dioxide", "D. Hydrogen"),
           ("A. 206", "B. 207", "C. 208", "D. 209"),
           ("A. Mercury", "B. Venus", "C. Earth", "D. Mars"))
x = True
while x:
    ra = []
    for key, value in questions.items():
        ra.append(value)

    a = 0
    k = 0
    b = []
    for i in questions:
        print('_____________________')
        print(i)
        print('_____________________')
        for j in options[a]:
            print(j)
        a += 1
        print('_____________________')
        g = input('chose the right answer: ').upper()
        while not (g.upper() in 'ABCD'):
            g = input('please choose a, b, c or d: ')
        b.append(g.upper())
    print('_____________________')
    print('your choices: ' + ' '.join(b))
    print('right answers: ' + ' '.join(ra))
    print('_____________________')
    for i in range(len(b)):
        if b[i] == ra[i]:
            k += 1
    print('your score: ' + str(int(k)) + '/5')
    print('_____________________')
    if input('do you want to play once more: (yes/no) ').upper() == 'YES':
        pass
    else:
        x = False
