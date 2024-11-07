# Algorytm-Needleman-Wunch
Implementacja algorytmu Needlemana-Wuncha na potrzeby laboratoriów z bioinformatyki strukturalnej.
Został zaprojektowany w celu znalezienia optymalnego globalnego dopasowania dwóch sekwencji DNA, RNA lub aminokwasowych. Działa poprzez budowanie macierzy dopasowań (programowanie dynamiczne), w której każda komórka odpowiada za ocenę dopasowania dwóch pozycji w sekwencjach. Algorytm ocenia trzy możliwe operacje dla każdej pary pozycji w sekwencjach: dopasowanie, niedopasowanie bądź luka.

## Kroki algorytmu Needleman-Wunscha
Inicjalizacja macierzy - tworzona jest macierz o wymiarach (długość sekwencji 1 + 2) x (długość sekwencji 2 + 2), w której pierwszy wiersz i pierwsza kolumna macierzy przechowują oznaczenia literowe nukleotydów lub aminokwasów, a kolejno drugi wiersz oraz druga kolumna odpowiadają karom za luki (gap penalties).

Wypełnianie macierzy - macierz jest wypełniana na podstawie funkcji [Mi,j] = max(Mi−1,j−1 + Sxi,yj, Mi−1,j + G, Mi,j−1 + G), gdzie Sxi,yj oznacza punktację za dopasowanie lub niedopasowanie, natomiast G jest karą za przerwę.

Śledzenie ścieżki (traceback) - rozpoczynając od prawnego dolnego rogu macierzy (score), algorytm śledzi optymalną ścieżkę wstecz, aż dotrze do lewego górnego rogu, rekonstruując globalne dopasowanie obu sekwencji.

## Sposób użycia
Należy podać na wejściu plik w formacie FASTA, w którm bedą znajdować sie dwie sekwencje nukleotydowe lub aminokwasowe. Przykładowe wywołanie z plikiem sequences.fa: 
nw.py sequqnces.fa
W tym przypadku zostaną użyte domyslne wartości parametrów odpowiedzialnych za punktację: dopasowanie(match_score) = 1, niedopasowanie(mismatch_score) = -1, przerwa(gap_score) = -1.
Można również zastosować algorytm z własnymi preferencjami parametrów, nalezy wtedy podać je na wejściu, przykład:
nw.py sequqnces.fa -s 1 -2 -2
Oznaczają one kolejno przypisanie do dopasowanie(match_score) = 1,  niedopasowanie(mismatch_score) = -2, przerwa(gap_score) = -2.
