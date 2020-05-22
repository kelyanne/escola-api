import requests

class TestCursos:
    headers = {'Authorization': 'Token 6bc74f2c80f11962ce0e9329d40be09fab2794ae'}
    url_base_cursos = 'http://127.0.0.1:8000/api/v2/cursos/'

    def test_get_cursos(self):
        cursos = requests.get(url=self.url_base_cursos, headers=self.headers)
        print(cursos.json())
        assert cursos.status_code == 200

    def test_get_curso(self):
        curso = requests.get(url=f'{self.url_base_cursos}/3', headers=self.headers)
        assert curso.status_code == 200

    def test_post_curso(self):
        data = {
            "titulo": "como domar felinos",
            "url": "https://geek.com.br/felinos"
        }

        resultado = requests.post(url=self.url_base_cursos, headers=self.headers, data=data)
        assert resultado.status_code == 201
        assert resultado.json()['titulo'] == data['titulo']

    def test_put_curso(self):
        data = {
            "titulo": "como domar tigrinhos",
            "url": "https://geek.com.br/tigres"
        }

        resultado = requests.put(url=f'{self.url_base_cursos}3/', headers=self.headers, data=data)
        assert resultado.status_code == 201
        assert resultado.json()['titulo'] == data['titulo']

    def test_delete_curso(self):
        resultado = requests.put(url=f'{self.url_base_cursos}1/', headers=self.headers)
        assert resultado.status_code == 204 and len(resultado.text) == 0