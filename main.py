import requests
import json

def dataChannelUrl(url):
    headers = {
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
        "Accept-Language": "ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7",
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36"
    }

    response = requests.get(url=url + '/about', headers=headers)

    # with open('index.html', 'w') as file:
    #     file.write(response.text)


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
    dataInfo = dataStatJson['contents']['twoColumnBrowseResultsRenderer']['tabs'][7]['tabRenderer']['content']['sectionListRenderer']['contents'][0]['itemSectionRenderer']['contents'][0]['channelAboutFullMetadataRenderer']
    # дата регистрации
    regDate = dataInfo['joinedDateText']['runs'][1]['text']
    # дата регистрации
    viewCount = dataInfo['viewCountText']['simpleText'].split(' ')[0]


    


    # данные с параметрами
    # data = response.text.split('(function() {window.ytplayer={};')[1].split('ytcfg.set(')[1].split(
    #     '); window.ytcfg.obfuscatedData_ = [];')[0]
    # dataJson = json.loads(data)
    # # ключ
    # dataKey = dataJson['INNERTUBE_API_KEY']

    # данные по статистики
    # responseStatist = requests.post(url='https://www.youtube.com/youtubei/v1/browse?key=AIzaSyAO_FJ2SlqU8Q4STEHLGCilw_Y9_11qcW8&prettyPrint=false', json={
    #     "context": {
    #         "client": {"hl": "ru", "gl": "UA", "remoteHost": "91.234.25.202", "deviceMake": "Apple", "deviceModel": "",
    #                    "visitorData": "CgtXLWZOQkNLSlNzYyiChrenBjIICgJSVRICGgA%3D",
    #                    "userAgent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.1 Safari/605.1.15,gzip(gfe)",
    #                    "clientName": "WEB", "clientVersion": "2.20230828.01.00", "osName": "Macintosh",
    #                    "osVersion": "10_15_7", "originalUrl": "https://www.youtube.com/@PythonToday/about",
    #                    "screenPixelDensity": 2, "platform": "DESKTOP", "clientFormFactor": "UNKNOWN_FORM_FACTOR",
    #                    "configInfo": {
    #                        "appInstallData": "CIKGt6cGEIjjrwUQ4tSuBRC4i64FEIbZ_hIQ3OOvBRDqw68FEKXC_hIQ7NivBRCI2K8FEIPfrwUQwt7-EhCXz68FEMfmrwUQgaWvBRDZya8FEOPmrwUQ5LP-EhDS4a8FENuvrwUQpN6vBRDE3a8FELzM_hIQ7qKvBRCU2f4SEL22rgUQ57qvBRDd6P4SEMzfrgUQlOj-EhDUoa8FEPq-rwUQtaavBRDzqK8FEIzLrwUQzK7-EhCst68FEInorgUQtMmvBRDV5a8F"},
    #                    "screenDensityFloat": 2, "userInterfaceTheme": "USER_INTERFACE_THEME_DARK",
    #                    "timeZone": "Europe/Kiev", "browserName": "Safari", "browserVersion": "16.1",
    #                    "acceptHeader": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
    #                    "deviceExperimentId": "ChxOekkzTWpZNE16TTRPRGN5T0RJMU1UTTFNdz09EIKGt6cGGIKGt6cG",
    #                    "screenWidthPoints": 1440, "screenHeightPoints": 313, "utcOffsetMinutes": 180,
    #                    "mainAppWebInfo": {"graftUrl": "/@PythonToday/about",
    #                                       "webDisplayMode": "WEB_DISPLAY_MODE_BROWSER",
    #                                       "isWebNativeShareAvailable": True}}, "user": {"lockedSafetyMode": False},
    #         "request": {"useSsl": True,
    #                     "internalExperimentFlags": [{"key": "force_enter_once_in_webview", "value": "true"}],
    #                     "consistencyTokenJars": []},
    #         "clickTracking": {"clickTrackingParams": "CCcQ8JMBGA0iEwic0_bNwI6BAxUmg_QHHXZxBaA="}, "adSignalsInfo": {
    #             "params": [{"key": "dt", "value": "1693303554973"}, {"key": "flash", "value": "0"},
    #                        {"key": "frm", "value": "0"}, {"key": "u_tz", "value": "180"},
    #                        {"key": "u_his", "value": "14"}, {"key": "u_h", "value": "900"},
    #                        {"key": "u_w", "value": "1440"}, {"key": "u_ah", "value": "900"},
    #                        {"key": "u_aw", "value": "1440"}, {"key": "u_cd", "value": "24"},
    #                        {"key": "bc", "value": "31"}, {"key": "bih", "value": "313"},
    #                        {"key": "biw", "value": "1424"},
    #                        {"key": "brdim", "value": "0,0,0,0,1440,0,1440,900,1440,313"}, {"key": "vis", "value": "1"},
    #                        {"key": "wgl", "value": "true"}, {"key": "ca_type", "value": "image"}]}},
    #     "browseId": "UCWnqnojAgMdN0fQpr_xByJw", "params": "EgVhYm91dPIGBAoCEgA%3D"
    # }, headers={
    #     "Accept": "*/*",
    #     "Accept-Language": "ru",
    #     "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.1 Safari/605.1.15",
    #     "X-Client-Data": "CIq2yQEIorbJAQipncoBCLqBywEIlaHLAQiEk80BCIagzQEI47HNAQjcvc0BCLu+zQEI4MTNAQi2xc0BCMTIzQEIucrNAQjxys0BCLfLzQEIz8vNAQi3zc0BCJLPzQEI1NDNARj4yc0B Decoded:",
    #     "Cookie": "YSC=wLJ3gfabrVA; VISITOR_INFO1_LIVE=Mrpqmra7vKI; VISITOR_PRIVACY_METADATA=CgJVQRICGgA%3D; PREF=f4=4000000&f6=40000000&tz=Europe.Kiev; ST-liaiy3=itct=CBwQ8JMBGAsiEwjezZfOmo6BAxXFabIKHWhKCMM%3D&csn=MC42MzMxNTg1NzI0OTE1MDk0&endpoint=%7B%22clickTrackingParams%22%3A%22CBwQ8JMBGAsiEwjezZfOmo6BAxXFabIKHWhKCMM%3D%22%2C%22commandMetadata%22%3A%7B%22webCommandMetadata%22%3A%7B%22url%22%3A%22%2F%40mmdcrew%2Fchannels%22%2C%22webPageType%22%3A%22WEB_PAGE_TYPE_CHANNEL%22%2C%22rootVe%22%3A3611%2C%22apiUrl%22%3A%22%2Fyoutubei%2Fv1%2Fbrowse%22%7D%7D%2C%22browseEndpoint%22%3A%7B%22browseId%22%3A%22UCWnqnojAgMdN0fQpr_xByJw%22%2C%22params%22%3A%22EghjaGFubmVsc_IGBAoCUgA%253D%22%2C%22canonicalBaseUrl%22%3A%22%2F%40mmdcrew%22%7D%7D; ST-pigqmq=itct=CBMQ8JMBGAwiEwiJi9GvvY6BAxX3mfQHHSZSDSU%3D&csn=MC4yNzE1ODU2NDc0MTI3MDY5Nw..&endpoint=%7B%22clickTrackingParams%22%3A%22CBMQ8JMBGAwiEwiJi9GvvY6BAxX3mfQHHSZSDSU%3D%22%2C%22commandMetadata%22%3A%7B%22webCommandMetadata%22%3A%7B%22url%22%3A%22%2F%40mmdcrew%2Fabout%22%2C%22webPageType%22%3A%22WEB_PAGE_TYPE_CHANNEL%22%2C%22rootVe%22%3A3611%2C%22apiUrl%22%3A%22%2Fyoutubei%2Fv1%2Fbrowse%22%7D%7D%2C%22browseEndpoint%22%3A%7B%22browseId%22%3A%22UCWnqnojAgMdN0fQpr_xByJw%22%2C%22params%22%3A%22EgVhYm91dPIGBAoCEgA%253D%22%2C%22canonicalBaseUrl%22%3A%22%2F%40mmdcrew%22%7D%7D",
    #     "Sec-Ch-Ua": 'Chromium";v="116", "Not)A;Brand";v="24", "Google Chrome";v="116',
    #     "Sec-Ch-Ua-Arch": "arm",
    #     "Sec-Ch-Ua-Bitness": "64",
    #     "Sec-Ch-Ua-Full-Version": "116.0.5845.140",
    #     "Sec-Ch-Ua-Full-Version-List": 'Chromium";v="116.0.5845.140", "Not)A;Brand";v="24.0.0.0", "Google Chrome";v="116.0.5845.140',
    #     "Sec-Ch-Ua-Mobile": "?0",
    #     "Sec-Ch-Ua-Model": "",
    #     "Sec-Ch-Ua-Platform": "macOS",
    #     "Sec-Ch-Ua-Platform-Version": "13.0.0",
    #     "X-Goog-Visitor-Id": "CgtNcnBxbXJhN3ZLSSiWudGnBjIICgJVQRICGgA%3D",
    #     "X-Youtube-Client-Version": "2.20230831.09.00"
    # })


def main():
    dataChannelUrl('https://www.youtube.com/@mmdcrew')


if __name__ == "__main__":
    main()



