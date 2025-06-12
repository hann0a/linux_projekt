Program do analizy jakości zdjęć - Projekt na przedmiot "Programy użytkowe w systemie GNU/Linux"
------------------------------------------------------------------------------------------------
Program służy do automatycznej analizy i selekcji zdjęć z jednej serii fotograficznej. Użytkownik 
wskazuje jedno zdjęcie wzorcowe, które stanowi punkt odniesienia pod względem jasności (ekspozycji). 
Na jego podstawie, poprzez analizę wartości jasności pikseli (tzw. składowych RGB), wyznaczane są 
dynamiczne progi prześwietlenia i niedoświetlenia.Każde zdjęcie z serii jest następnie 
przekształcane do skali szarości, a jego piksele są analizowane oraz obliczany jest odsetek zbyt 
jasnych lub zbyt ciemnych punktów. Jeżeli ich liczba przekroczy określony próg, zdjęcie zostaje 
uznane za niepoprawne i automatycznie przeniesione do osobnego katalogu.

Program został zrealizowany w języku Python i Bash. Do analizy danych obrazowych wykorzystano 
biblioteki NumPy (do obliczeń numerycznych) oraz Pillow (do przetwarzania obrazów).

Autorzy: Hanna Milnikel, Agata Zając
