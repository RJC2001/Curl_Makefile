# API Test Script

## Opis
Skrypt `api_test.py` automatyzuje testowanie różnych endpointów API przy użyciu narzędzia `curl`. Skrypt wysyła żądania HTTP do publicznego API JSONPlaceholder i sprawdza, czy odpowiedzi są poprawne (statusy HTTP i kluczowe elementy w odpowiedziach JSON np. userId).

## Wymagania
- Python 3.x
- `curl`

## Instrukcja użycia
1. Upewnij się, że masz zainstalowany Python 3.x oraz `curl`.
2. Pobierz plik `api_test.py`.
3. Uruchom skrypt:
   ```bash
   python api_test.py

### Kroki do uruchomienia projektu:

1. Upewnij się, że masz zainstalowany Python i `pip`.
2. Skopiuj zawartość powyższych plików do odpowiednich plików w swoim systemie.
3. Utwórz plik `requirements.txt` (jeśli wymagane są dodatkowe zależności, na przykład `unittest` jest wbudowany w Pythona, więc nie trzeba go dodawać).
4. W katalogu projektu uruchom następujące polecenia, aby sprawdzić, czy Makefile działa poprawnie:

```bash
# Instalacja zależności
make install

# Uruchamianie testów
make test

# Uruchamianie aplikacji
make run
