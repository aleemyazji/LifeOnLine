intro = input('type your age please')
age = int(intro)
intro2 = input('are you a girl or a boy ')
s = str(intro2)
intro4 = input('put your height')
intro5re = str(intro4)
intro3 = input('plz enter your chronic diseases such as (Pressure disease) or (diabetes)')
p = str(intro3)
inp = input('now please type every answer correctly and follow the instructions please press any key ')


while True:
    try:
        face = input('Welcom to life on line please describe your feeling     '
                     '  1-headache        2-stomach ache      3-Loss of sense of taste and smell')

        ansuer = int(face)


        if ansuer == 1 and p == 'diabetes':
            print(
                'dont worry its a normal thing happen when u have diabetes you should '
                'take some rest with a 1 pill from painkiller most likely (cetamol)')
        elif ansuer == 2:
            print('you should get chill out and stay in bed your stomach may be '
                  'unstable now so take this medicine (Pepto Bismol) from the closest'
                  ' pharmacist u have in your area and stay in bed for the next few days')
        elif ansuer == 3:
            print('ok now dont try to go out,  stay in home dont worry its ok you might have '
                  'coronavirus but u ll be ok cause we called the emergency you will be safe, '
                  ' put up your mask and stay ready')
    except:
        print('sorry i couldnt understand the problem please try again')
        break
