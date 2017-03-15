from elizabeth.decorators import romanized


@romanized('ru')
def russian_user():
    return 'Ликид Геимфари'


@romanized('ru')
def russian_mixed_text():
    return 'Что-то там_4352-!@#$%^&*()_+?"<>"'


@romanized('ua')
def ukrainian_text():
    return 'Українська мова!'


def test_russian():
    assert 'Likid Geimfari' == russian_user()


def test_russian_mixed_text():
    assert 'Chto-to tam_4352-!@#$%^&*()_+?"<>"' == russian_mixed_text()


def test_ukrainian():
    assert 'Ukrayins’ka mova!' == ukrainian_text()


print(russian_mixed_text())
