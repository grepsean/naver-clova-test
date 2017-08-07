import ujson

import sys

from request import request
from urls import URLS


def face_recognize(file):
    response = request(URLS.CFR.face, file)
    if response.status_code == 200:
        json = ujson.loads(response.text)
        face = json['faces'][0]
        print('나이: {}세, 성별: {}, 표정: {}'.format(face['age']['value'], face['gender']['value'], face['emotion']['value']))
    else:
        print('얼굴 인식 에러({})'.format(response.status_code))


def face_celebrity(file):
    response = request(URLS.CFR.celebrity, file)
    if response.status_code == 200:
        json = ujson.loads(response.text)
        face = json['faces'][0]
        print('닯은 연예인: {} ({}%)'.format(face['celebrity']['value'], int(float(face['celebrity']['confidence']) * 100)))
    else:
        print('유명인사 인식 에러({})'.format(response.status_code))


if __name__ == '__main__':
    pic = sys.argv[1] if len(sys.argv) else 'iu.jpg'
    face_recognize(pic)
    face_celebrity(pic)
