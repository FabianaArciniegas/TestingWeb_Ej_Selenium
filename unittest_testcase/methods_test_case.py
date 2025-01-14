import unittest


class MethodsTestCase(unittest.TestCase):

    # Se ejecuta antes y unica vez de la ejecución de todas las pruebas
    @classmethod
    def setUpClass(cls):
        print("Open Application")

    # Se ejecuta antes de la ejecucion de cada prueba
    def setUp(self):
        print("Login on Application")

    def test_create(self):
        print("Test create")

    def test_update(self):
        print("Test update")

    def test_search(self):
        print("Test search")

    def test_delete(self):
        print("Test delete")

    # Cada vez que se termina una prueba, despues se ejecuta lo que esta dentro de este metodo "tearDown"
    def tearDown(self):
        print("Logout Application")

    # Se ejecuta despues y unica vez de la ejecución de todas las pruebas
    @classmethod
    def tearDownClass(cls):
        print("Close Application")


if __name__ == "__main__":
    unittest.main()
