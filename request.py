import requests
import settings


def request(url, file):
    if not settings.CLIENT_ID or not settings.CLIENT_SECRET:
        raise Exception('Naver API 접속정보를 입력해주세요(settings.py)')
    files = {'image': open(file, 'rb')}
    headers = {'X-Naver-Client-Id': settings.CLIENT_ID, 'X-Naver-Client-Secret': settings.CLIENT_SECRET}
    return requests.post(url, files=files, headers=headers)
