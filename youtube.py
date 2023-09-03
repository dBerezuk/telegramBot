import requests
import json

class Youtube():

    def __init__(self):
        self.headers = {
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
            "Accept-Language": "ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7",
            "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36"
        }

    def channelData(self, url):
        response = requests.get(url=url + '/about', headers=self.headers)
        # данные о аккаунте
        content = response.text.split('var ytInitialData =')[1].split(';</script>')[0]
        contentJson = json.loads(content)

        # имя
        channelName = contentJson['metadata']['channelMetadataRenderer']['title']

        # описание
        channelDescription = contentJson['metadata']['channelMetadataRenderer']['description']

        # количество видео на канале
        videoCount = contentJson['header']['c4TabbedHeaderRenderer']['videosCountText']['runs'][0]['text']

        # количество подписчиков
        subscribersCount = contentJson['header']['c4TabbedHeaderRenderer']['subscriberCountText']['simpleText'].split(' подписчиков')[0]

        # о канале - статистика
        dataStat = response.text.split('var ytInitialData = ')[1].split(';</script>')[0]
        dataStatJson = json.loads(dataStat)

        dataInfo = dataStatJson['contents']['twoColumnBrowseResultsRenderer']['tabs'][-2]['tabRenderer']['content']['sectionListRenderer']['contents'][0]['itemSectionRenderer']['contents'][0]['channelAboutFullMetadataRenderer']

        # дата регистрации
        regDate = dataInfo['joinedDateText']['runs'][1]['text']
        # всего просмотров на канале
        try:
            viewCountAll = dataInfo['viewCountText']['simpleText']
        except:
            viewCountAll = 0

        return {
            "name": channelName,
            "descr": channelDescription,
            "videCount": videoCount,
            "subscribersCount": subscribersCount,
            "regDate": regDate,
            "viewCountAll": viewCountAll
        }
