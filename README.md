# Algorytm-Needleman-Wunch
Implementacja algorytmu Needlemana-Wuncha na potrzeby laboratoriów z bioinformatyki strukturalnej.
Został zaprojektowany w celu znalezienia optymalnego globalnego dopasowania dwóch sekwencji DNA, RNA lub aminokwasowych. Działa poprzez budowanie macierzy dopasowań (programowanie dynamiczne), w której każda komórka odpowiada za ocenę dopasowania dwóch pozycji w sekwencjach. Algorytm ocenia trzy możliwe operacje dla każdej pary pozycji w sekwencjach: dopasowanie, niedopasowanie bądź luka.

## Kroki algorytmu Needleman-Wunscha
Inicjalizacja macierzy - tworzona jest macierz o wymiarach (długość sekwencji 1 + 2) x (długość sekwencji 2 + 2), w której pierwszy wiersz i pierwsza kolumna macierzy przechowują oznaczenia literowe nukleotydów lub aminokwasów, a kolejno drugi wiersz oraz druga kolumna odpowiadają karom za luki (gap penalties).

Wypełnianie macierzy - macierz jest wypełniana na podstawie funkcji:

[Mi,j] = max(Mi−1,j−1 + Sxi,yj, Mi−1,j + G, Mi,j−1 + G)

, gdzie Sxi,yj oznacza punktację za dopasowanie lub niedopasowanie, natomiast G jest karą za przerwę.

Śledzenie ścieżki (traceback) - rozpoczynając od prawnego dolnego rogu macierzy (score), algorytm śledzi optymalną ścieżkę wstecz, aż dotrze do lewego górnego rogu, rekonstruując globalne dopasowanie obu sekwencji.

## Sposób użycia
Należy podać na wejściu plik w formacie FASTA, w którm bedą znajdować sie dwie sekwencje nukleotydowe lub aminokwasowe. Przykładowe wywołanie z plikiem sequences.fa: 

nw.py sequqnces.fa

W tym przypadku zostaną użyte domyslne wartości parametrów odpowiedzialnych za punktację: dopasowanie(match_score) = 1, niedopasowanie(mismatch_score) = -1, przerwa(gap_score) = -1.
Można również zastosować algorytm z własnymi preferencjami parametrów, nalezy wtedy podać je na wejściu, przykład:

nw.py sequqnces.fa -s 1 -2 -2

Oznaczają one kolejno przypisanie do dopasowanie(match_score) = 1,  niedopasowanie(mismatch_score) = -2, przerwa(gap_score) = -2.

## Przykładowe wywołanie
W pliku sequqnces.fa znajdują się dwie następujące sekwencje:

>AGCTAGCATG
>ACGGTAGCATT

Wywołujemy algorytm z podanymi parametrami:

nw.py sequqnces.fa -s 1 -2 -1

Otrzymujemy na wyjściu informacje o danych wejściowych, czy na pewno zostały dobrze wprowadzone:

Match_score = 1

Mismatch_score = -2

Gap_score = -1

Sequence 1: AGCTAGCATG
Sequence 2: ACGGTAGCATT

Oraz wynik w formie globalnego dopasowania, gdzie "-" oznacza przerwę:

[ A - - G C T A G C A - T G ]
[ A C G G - T A G C A T T - ]

Score: 3

Algorym wyszukuje jedno z możliwych optymalnych rozwiązań, o czym informuje użytkownika stosownym komunikatem.




