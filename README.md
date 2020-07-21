|          |                                    |         |                 |          |                                    |         |
|----------|------------------------------------|---------|-----------------|----------|------------------------------------|---------|
|          |                                    |         | **Rankings UD** |          |                                    |         |
| **Rank** | **Name (# of matches)**            | **BAX** |                 | **Rank** | **Name (# of matches)**            | **PBR** |
| 1        | Alexander Voigt               ( 1) | 503.50  |                 | 1        | Alexander Voigt               ( 1) | 57.75   |
| 2        | Laura Preuß                   ( 1) | 496.50  |                 | 2        | Laura Preuß                   ( 1) | 42.25   |
|          |                                    |         | **Rankings MS** |          |                                    |         |
| **Rank** | **Name (# of matches)**            | **BAX** |                 | **Rank** | **Name (# of matches)**            | **PBR** |
| 1        | Johannes Rosenzweig           ( 7) | 512.96  |                 | 1        | Hark Empen                    ( 2) | 54.29   |
| 2        | Alexander Voigt               ( 7) | 501.60  |                 | 2        | Johannes Rosenzweig           ( 7) | 52.31   |
| 3        | Hark Empen                    ( 2) | 500.44  |                 | 3        | Alexander Voigt               ( 7) | 51.25   |
| 4        | Till Staude                   ( 2) | 499.61  |                 | 4        | Till Staude                   ( 2) | 50.29   |
| 5        | Kevin Erkelenz                ( 1) | 497.63  |                 | 5        | Kevin Erkelenz                ( 1) | 49.18   |
| 6        | Durga P.B. Nasika             ( 1) | 496.49  |                 | 6        | Matti Rohlf                   ( 7) | 48.96   |
| 7        | Matti Rohlf                   ( 7) | 491.28  |                 | 7        | Sebastian Mootz               ( 5) | 47.02   |
| 8        | Sebastian Mootz               ( 5) | 489.75  |                 | 8        | Durga P.B. Nasika             ( 1) | 46.75   |
|          |                                    |         | **Rankings MD** |          |                                    |         |
| **Rank** | **Name (# of matches)**            | **BAX** |                 | **Rank** | **Name (# of matches)**            | **PBR** |
| 1        | Hark Empen                    (12) | 519.83  |                 | 1        | Hark Empen                    (12) | 54.09   |
| 2        | Johannes Rosenzweig           ( 9) | 503.34  |                 | 2        | Sebastian Mootz               ( 6) | 52.92   |
| 3        | Arne Wischmann                ( 1) | 501.85  |                 | 3        | Matti Rohlf                   (11) | 52.04   |
| 4        | Kevin Erkelenz                ( 4) | 497.88  |                 | 4        | Arne Wischmann                ( 1) | 51.86   |
| 5        | Matti Rohlf                   (11) | 497.80  |                 | 5        | Kevin Erkelenz                ( 4) | 49.14   |
| 6        | Alexander Voigt               (11) | 494.70  |                 | 6        | Durga P.B. Nasika             ( 3) | 48.60   |
| 7        | Till Staude                   ( 7) | 493.44  |                 | 7        | Johannes Rosenzweig           ( 9) | 48.43   |
| 8        | Durga P.B. Nasika             ( 3) | 492.24  |                 | 8        | Till Staude                   ( 7) | 46.55   |
| 9        | Sebastian Mootz               ( 6) | 490.71  |                 | 9        | Alexander Voigt               (11) | 45.00   |
|          |                                    |         | **Rankings WS** |          |                                    |         |
| **Rank** | **Name (# of matches)**            | **BAX** |                 | **Rank** | **Name (# of matches)**            | **PBR** |
| 1        | Laura Preuß                   ( 1) | 503.50  |                 | 1        | Laura Preuß                   ( 1) | 53.50   |
| 2        | Lea Song-I Park               ( 1) | 496.50  |                 | 2        | Lea Song-I Park               ( 1) | 46.50   |
|          |                                    |         | **Rankings WD** |          |                                    |         |
| **Rank** | **Name (# of matches)**            | **BAX** |                 | **Rank** | **Name (# of matches)**            | **PBR** |
|          |                                    |         | **Rankings MX** |          |                                    |         |
| **Rank** | **Name (# of matches)**            | **BAX** |                 | **Rank** | **Name (# of matches)**            | **PBR** |
| 1        | Divya Sree Madichati          ( 1) | 503.37  |                 | 1        | Divya Sree Madichati          ( 1) | 53.78   |
| 2        | Jan Hoffmann                  ( 1) | 502.24  |                 | 2        | Alexander Voigt               ( 2) | 52.91   |
| 3        | Lea Song-I Park               ( 2) | 500.98  |                 | 3        | Jan Hoffmann                  ( 1) | 51.77   |
| 4        | Alexander Voigt               ( 2) | 500.15  |                 | 4        | Lea Song-I Park               ( 2) | 49.10   |
| 5        | Laura Preuß                   ( 3) | 495.46  |                 | 5        | Laura Preuß                   ( 3) | 46.01   |
# HSC-rankings
These are our internal rankings. Each player gets a BAX \[1\] and a PBR \[2\] for each discipline (Wo/Men's singles, Wo/Men's doubles, mixed doubles). There is also an additional BAX and PBR for each player for matches that are in neihter of the aforementioned disciplines, i.e. a male vs. female singles match.

\[1\]: http://www.badminton-bax.de/index.php

\[2\]: http://badminton-rating.org/

# TODOS
- [ ] Add player statistics plots (radar charts would be nice with each axis representing one discipline)
# Documentation
## Forbidden matches
Players/Pairs whose BAX (PBR) ratings differ by more than 30 (12) points, are not allowed to compete in ranked matches (of course, exceptions can be made). The rating systems are no longer applicable in a meaningful manner when the competing players rating differences are to large.
## Point Based Rating
The Point Based Rating (PBR) is based on score differences of players `A` and `B` of a match `i`. It is based on the the average of the score (`S_i`) differences of the played games of a match. The average score difference,

    asd_i = MEAN( S_i( A ) ) - MEAN( S_i( B ) ),

is the average score of player `B` subtracted from the average score of player `A`, i.e. if a match ends 21:16, 19:21 and 21:15, the `asd` is 3 points.

The performance `P` of player `A` is the matches `asd` added to the `PBR` of player `B`. Consequently, the performance of player `B` is the matches `asd` subtracted from the `PBR` of player `A`,

    P( A )_i = PBR( B ) + asd_i
    P( B )_i = PBR( A ) - asd_i

The new `PBR` of a player `X` is the average players performance over a time period.

    PBR_new( X ) = MEAN( P( X ) )

## Badminton Index
The Badminton Index (BAX) is based on a Gaussian distribution and calculates winning probabilities from the players `BAX` scores.

Using the `BAX` of player `A` and player `B`, the winning probability `W_D` of player `A`,

    W_D = 1 / ( 1 + POW( 10, -D / 50 ) ),

is calculated from the difference of the players `BAX` scores `D`,

    D = BAX( A ) - BAX( B ).

The BAX score can be updated after each match, but it can also be updated after a series of matches.

If multiple matches are used to update the BAX score of a player, then the average of the opponents BAX scores are uses as the opponents niveau `B_Niv`,

    B_Niv = ( BAX_1 + BAX_2 + BAX_3 + ... + BAX_n ) / n,

where `n` is the number of matches played.

The estimated amount of victories for player `A`, `S_E`,

    S_E = SUM( W_D_i ),

is the sum of all individual winning probabilities. If there is only one match to be evaluated, then `W_D = S_E`.

The actual amount of victories `V_I`,

    +1 for every win
    +0 for every loss,

 is modified as follows, to give the victory score `S_I`,

    +1 for every win in 2:0 games [3:0 games for Bundesliga matches]
    +0.9 for every win in 3:1 games [for Bundesliga matches only]
    +0.8 for every win in 2:1 games [3:2 games for Bundesliga matches]
    +0.2 for every loss in 1:2 games [2:3 games for Bundesliga matches]
    +0.1 for every loss in 1:3 games [for Bundesliga matches only]
    +0.0 for every loss in 0:2 games [0:3 games for Bundesliga matches].


Two preliminary `BAX` scores are calculated from the previously introduced indices.

The `BAX_1`,

    BAX_1 = B_Niv + 7 * ( S_I - n/2 ),

and the `BAX_pre`,

    BAX_pre = BAX + 7 * ( S_I - S_E ).

From the two preliminary `BAX` scores, the updated `BAX` score is calculated. If `BAX <= B_Niv`,

    BAX_new = min( ( 5 * BAX_pre + 2 * V_I / n * BAX_1 ) / ( 5 + 2 * V_I / n), BAX_1 ),

or, if `BAX > B_Niv`,

    BAX_new = max( ( ( 4 * V_I / n + 5 ) * BAX_pre + BAX_1 ) / ( 4 * V_I / n + 6 ), BAX_1 )

For now, the preliminary `BAX` scores are used in the evaluation, because there are some issues when applying the equations for `BAX_new`, i.e. that both sides may lose points and that conservation of points is not given anymore.
