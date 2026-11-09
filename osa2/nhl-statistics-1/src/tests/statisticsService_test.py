import unittest
from statistics_service import StatisticsService
from player import Player

class PlayerReaderStub:
    def get_players(self):
        return [
            Player("Semenko", "EDM", 4, 12),
            Player("Lemieux", "PIT", 45, 54),
            Player("Kurri", "EDM", 37, 53),
            Player("Yzerman", "DET", 42, 56),
            Player("Gretzky", "EDM", 35, 89)
        ]

class TestStatisticsService(unittest.TestCase):
    def setUp(self):
        # Annetaan StatisticsService-luokan oliolle "stub"-luokan olio
        self.stats = StatisticsService(
            PlayerReaderStub()
        )

    def test_kurri_loytyy(self):
        player = self.stats.search("Kurri")
        
        self.assertIsNotNone(player)
        self.assertEqual(player.name, "Kurri")

    def test_glensky_ei_loydy(self):
        player = self.stats.search("Glensky")
        
        self.assertIsNone(player)

    def test_kurri_oikea_joukkue(self):
        players = self.stats.team("EDM")
        kurri_found = False
        for player in players:
            if player.name == "Kurri":
                kurri_found = True
                
        self.assertTrue(kurri_found)

    def test_gretzky_ei_loydy_det(self):
            players = self.stats.team("DET")
            gretzky_found = False
            for player in players:
                if player.name == "Gretzky":
                    gretzky_found = True
                    
            self.assertFalse(gretzky_found)

    def test_top_palauttaa_parhaan_ekana(self):
        top_players = self.stats.top(0)
        
        self.assertEqual(top_players[0].name, "Gretzky")

    def test_top_palauttaa_parhaus_jarjestyksessa(self):
        top_players = self.stats.top(2)
        
        self.assertEqual(top_players[0].name, "Gretzky")
        self.assertEqual(top_players[1].name, "Lemieux")
        self.assertEqual(top_players[2].name, "Yzerman")
