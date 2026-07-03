
import pytest
from math import gcd


class TestGcdDueNumeri:
    """Test con due numeri interi"""

    def test_gcd_numeri_con_divisore_comune(self):
        assert gcd(12, 18) == 6

    def test_gcd_numeri_primi_tra_loro(self):
        assert gcd(7, 11) == 1

    def test_gcd_numeri_uguali(self):
        assert gcd(15, 15) == 15

    def test_gcd_uno_multiplo_dellaltro(self):
        assert gcd(10, 50) == 10

    def test_gcd_con_uno(self):
        assert gcd(1, 100) == 1
        assert gcd(100, 1) == 1


class TestGcdConZero:
    """Test con zero come argomento"""

    def test_gcd_zero_e_numero(self):
        assert gcd(0, 5) == 5
        assert gcd(5, 0) == 5

    def test_gcd_zero_e_zero(self):
        assert gcd(0, 0) == 0


class TestGcdNumeriNegativi:
    """Test con numeri negativi (gcd restituisce sempre valore assoluto)"""

    def test_gcd_entrambi_negativi(self):
        assert gcd(-12, -18) == 6

    def test_gcd_uno_negativo(self):
        assert gcd(-12, 18) == 6
        assert gcd(12, -18) == 6


class TestGcdMultipliArgomenti:
    """Test con più di due argomenti (Python 3.9+)"""

    def test_gcd_tre_numeri(self):
        assert gcd(12, 18, 24) == 6

    def test_gcd_quattro_numeri(self):
        assert gcd(24, 36, 48, 60) == 12

    def test_gcd_numeri_primi_tra_loro_multipli(self):
        assert gcd(7, 11, 13) == 1

    def test_gcd_tutti_uguali(self):
        assert gcd(10, 10, 10, 10) == 10


class TestGcdSingoloArgomento:
    """Test con un solo argomento (Python 3.9+)"""

    def test_gcd_singolo_positivo(self):
        assert gcd(42) == 42

    def test_gcd_singolo_negativo(self):
        assert gcd(-42) == 42

    def test_gcd_singolo_zero(self):
        assert gcd(0) == 0


class TestGcdNessunArgomento:
    """Test senza argomenti (Python 3.9+)"""

    def test_gcd_nessun_argomento(self):
        assert gcd() == 0


class TestGcdNumeriGrandi:
    """Test con numeri grandi"""

    def test_gcd_numeri_grandi(self):
        assert gcd(123456789, 987654321) == 9

    def test_gcd_potenze_di_due(self):
        assert gcd(1024, 4096) == 1024

    def test_gcd_numeri_molto_grandi(self):
        assert gcd(10**18, 10**15) == 10**15


class TestGcdCasiSpeciali:
    """Test per casi speciali e proprietà matematiche"""

    def test_gcd_commutativo(self):
        """gcd(a, b) == gcd(b, a)"""
        assert gcd(24, 36) == gcd(36, 24)

    def test_gcd_associativo(self):
        """gcd(gcd(a, b), c) == gcd(a, gcd(b, c))"""
        assert gcd(gcd(12, 18), 24) == gcd(12, gcd(18, 24))

    def test_gcd_con_numero_primo(self):
        """gcd con un numero primo restituisce 1 o il primo stesso"""
        assert gcd(17, 34) == 17
        assert gcd(17, 35) == 1


class TestGcdErrori:
    """Test per verificare che vengano sollevati errori appropriati"""

    def test_gcd_con_float_solleva_errore(self):
        with pytest.raises(TypeError):
            gcd(3.5, 7)

    def test_gcd_con_stringa_solleva_errore(self):
        with pytest.raises(TypeError):
            gcd("12", 18)

    def test_gcd_con_none_solleva_errore(self):
        with pytest.raises(TypeError):
            gcd(None, 5)
