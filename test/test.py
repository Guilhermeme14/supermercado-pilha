import unittest
from supermercado.supermercado import Compra, PilhaDeCompras, Supermercado  # Substitua 'supermercado' pelo nome correto do seu arquivo


class TestCompra(unittest.TestCase):
    def test_compra(self):
        compra = Compra("2024-03-10", "Arroz", 10.50, 15.00, 5, 5)

        self.assertEqual(compra.data, "2024-03-10")
        self.assertEqual(compra.produto, "Arroz")
        self.assertEqual(compra.valor_compra, 10.50)
        self.assertEqual(compra.valor_venda, 15.00)
        self.assertEqual(compra.quantidade_comprada, 5)
        self.assertEqual(compra.quantidade_estoque, 5)
        self.assertIn("Arroz", str(compra))


class TestPilhaDeCompras(unittest.TestCase):
    def test_pilha_de_compras(self):
        pilha = PilhaDeCompras()
        compra1 = Compra("2024-03-10", "Arroz", 10.50, 15.00, 5, 5)
        compra2 = Compra("2024-03-11", "Feijão", 12.00, 18.00, 3, 3)

        pilha.adicionar_compra(compra1)
        pilha.adicionar_compra(compra2)

        self.assertEqual(pilha.obter_ultima_compra(), compra2)

        pilha.limpar_registros()
        self.assertIsNone(pilha.obter_ultima_compra())


class TestSupermercado(unittest.TestCase):
    def setUp(self):
        self.supermercado = Supermercado()

    def test_validar_data(self):
        self.assertTrue(self.supermercado.validar_data("2024-03-10"))
        self.assertFalse(self.supermercado.validar_data("2026-03-10"))
        self.assertFalse(self.supermercado.validar_data("2024-13-10"))
        self.assertFalse(self.supermercado.validar_data("2024-02-30"))
        self.assertFalse(self.supermercado.validar_data("10/03/2024"))

    def test_registrar_compra(self):
        self.supermercado.registrar_compra("2024-03-10", "Arroz", 10.50, 15.00, 5)
        self.assertIn("Arroz", self.supermercado.produtos)
        self.assertEqual(len(self.supermercado.produtos["Arroz"].compras), 1)

    def test_limpar_registro_produto(self):
        self.supermercado.registrar_compra("2024-03-10", "Arroz", 10.50, 15.00, 5)
        self.supermercado.limpar_registro_produto("Arroz")
        self.assertEqual(len(self.supermercado.produtos["Arroz"].compras), 0)

    def test_limpar_todos_registros(self):
        self.supermercado.registrar_compra("2024-03-10", "Arroz", 10.50, 15.00, 5)
        self.supermercado.limpar_todos_registros()
        self.assertEqual(len(self.supermercado.produtos), 0)


if __name__ == "__main__":
    unittest.main()
