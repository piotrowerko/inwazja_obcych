import sys
import pygame
from settings import Settings
from ship import Ship

class AlienInvasion():
    """Ogólna klasa przeznaczona do zarządzania zasobami i sposobem działania gry."""

    def __init__(self):
        """Inicjalizacja gry i utworzenie jej zasobów."""
        pygame.init()
        self.settings = Settings() #EGZEMPLARZ KLASY JAKO ATRYBUT !!
        self.screen = pygame.display.set_mode((0,0), pygame.FULLSCREEN)
        # Uaktulanienie usatawień ekranu w oparciu o pomiar mojego monitora:
        self.settings.screen_width = self.screen.get_rect().width
        self.settings.screen_height = self.screen.get_rect().height

        pygame.display.set_caption("Inwazja obcych")
        self.ship = Ship(self)  # WAŻNE !!!! EGZEMPLARZ KLASY JAKO ATRYBUT !!, ale i Z POWROTEM !
        self.bullets = pygame.sprite.Group()

    def run_game(self):
        """Rozpoczęcie pętli głównej gry"""
        while True:
            self._check_events()
            self.ship.update()
            self.bullets.update()
            self._update_screen()

    def _check_events(self):
        """Rekacja na zdarzenia generowane przez klawiaturę i mysz."""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)
            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)

    def _check_keydown_events(self, event):
        """Reakcja na nacieśnięcie klawisza"""
        if event.key == pygame.K_RIGHT:
            # Przesunięcie statku w prawą stronę.
            self.ship.moving_right = True
        elif event.key == pygame.K_LEFT:
            # Przesunięcie statku w lewą stronę.
            self.ship.moving_left = True
        elif event.key == pygame.K_q:
            sys.exit()

    def _check_keyup_events(self, event):
        """Reakcja na zwolnienie (odpuszczenie) klawisza"""
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = False
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = False

    def _update_screen(self):
        """Uaktualnienie obrazów na ekranie i przejście do nowego ekranu"""
        self.screen.fill(self.settings.bg_color)
        self.ship.blitme()

        pygame.display.flip()


if __name__ == '__main__':
    # Utworzenie egzemplarza gry i jej uruchomienie.
    ai = AlienInvasion()
    ai.run_game()

