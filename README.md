# HSC-rankings
These are our internal rankings. Each player gets a BAX \[1\] and a PBR \[2\] for each discipline (Wo/Men's singles, Wo/Men's doubles, mixed doubles). There is also an additional BAX and PBR for each player for matches that are in neihter of the aforementioned disciplines, i.e. a male vs. female singles match.

\[1\]: http://www.badminton-bax.de/index.php

\[2\]: http://badminton-rating.org/

# TODOS
- [ ] Add player statistics plots (radar charts would be nice with each axis representing one discipline)
# Documentation
## Forbidden matches
Players/Pairs whose PBR ratings differ by more than 12 points, are not allowed to compete in ranked matches (of course, exceptions can be made). The PBR rating system is no longer applicable in a meaningful manner when the competing players PBR rating differences are to large.
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
