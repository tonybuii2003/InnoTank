import os
import json


def generate_negative_file():
    with open('negativeTXT', 'w') as f:
        for name in os.listdir('/Volumes/GoogleDrive/My Drive/SBU/CS_project/RoboTech/project/src/negative'):
            print(type(name))
            f.write('negative/' + name + '\n')
    print('Done')


def generate_positive_file():
    with open('positiveTXT', 'w') as f:
        for file in os.listdir('/Volumes/GoogleDrive/My Drive/SBU/CS_project/RoboTech/project/src/pos'):
            if file == 'annotations.json':
                f = open(
                    '/Volumes/GoogleDrive/My Drive/SBU/CS_project/RoboTech/project/src/pos/'+file, "r")
                data = json.load(f)
        for i in data:
            posStr = ''
            if i != '___sa_version___':
                posStr += f'{i} '
                for j in data[i]['instances']:
                    for k in j:
                        if k == "classId":
                            posStr += f'{j[k]} '
                        if k == "points":
                            for point in j[k]:
                                posStr += f'{str(j[k][point])} '
            print(posStr[0:-1])
            #f.write('positive/' + str(posStr[0:-1]) + '\n')


generate_negative_file()
generate_positive_file()
