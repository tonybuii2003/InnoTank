import os
import json


def generate_negative_file():
    with open('negativeTXT', 'w') as f:
        for name in os.listdir('/Volumes/GoogleDrive/My Drive/SBU/CS_project/RoboTech/project/src/negative'):
            print(type(name))
            f.write('negative/' + name + '\n')
    print('Done writing negativeTXT')


def generate_positive_file():
    with open('positiveTXT', 'w') as f:
        for file in os.listdir('/Volumes/GoogleDrive/My Drive/SBU/CS_project/RoboTech/project/src/pos'):
            if file == 'annotations.json':
                json_f = open(
                    '/Volumes/GoogleDrive/My Drive/SBU/CS_project/RoboTech/project/src/pos/'+file, "r")
                data = json.load(json_f)
        for i in data:
            posStr = ''
            loc = ""
            if i != '___sa_version___':
                loc = 'positive/'
                posStr += f'{i} '
                for j in data[i]['instances']:
                    for k in j:
                        if k == "classId":
                            posStr += f'{j[k]} '
                        if k == "points":
                            for point in j[k]:
                                posStr += f'{str(j[k][point])} '
                f.write(loc + str(posStr[0:-1]) + '\n')
        print(f'Done writing positiveTXT')


generate_negative_file()
generate_positive_file()
