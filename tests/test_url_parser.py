

def url_parser(url):
    if len(url) > 255:
        return {'result': False, 'message': 'URL превышает 255 символов'}
    else:
        return {'result': True, 'message': 'URL валидный'}


def test_url_parser():
    link_1 = (
        'https://google.com/111111111'
        '1111111111111111111111111111'
        '1111111111111111111111111111'
        '1111111111111111111111111111'
        '1111111111111111111111111111'
        '1111111111111111111111111111'
        '1111111111111111111111111111'
        '1111111111111111111111111111'
        '1111111111111111111111111111'
        '1111111111111111111111111111'
    )
    assert url_parser(link_1) == {'result': False, 'message': 'URL превышает 255 символов'}

    link_2 = 'google.con'
    assert url_parser(link_2) == {'result': True, 'message': 'URL валидный'}

    link_3 = 'google.com'
    assert url_parser(link_3) == {'result': True, 'message': 'URL валидный'}

    link_4 = 'https://google.com'
    assert url_parser(link_4) == {'result': True, 'message': 'URL валидный'}

    link_5 = 'https://www.google.com/search?q=flask'
    assert url_parser(link_5) == {'result': True, 'message': 'URL валидный'}
