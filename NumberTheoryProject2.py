import math;

END_CONDITION = 10000;
INT_FORMAT = '{:6d}';
STR_FORMAT = '{:70s}';

#Reused function from previous project
def primeFactorization( number ):
        i = 2;
        primeFactors = [];
        while( i <= math.sqrt( number ) ):
                if( number % i == 0 ):
                        number = number / i;
                        primeFactors = primeFactors + [i];
                else:
                        i = i + 1;
        if( number > 1 ):
                primeFactors = primeFactors + [int(number)];
        return primeFactors;

#Modified function from previous project
def listOfSquaresAtMost( n ):
        if( n < 0 ):
                return [];
        else:
                out = [];
                n = math.ceil( math.sqrt( n ) );
                while( n >= 0 ):
                        out = [n*n] + out;
                        n = n - 1;
                return out;

def getPermutationCount( lst ):
        acc = 0;
        for element in lst:
                acc = acc + getSingularPermutationCount( element[0], element[1] );
        return acc;

def getSingularPermutationCount( a, b ):
        if( a==0 or b==0 ):
                if( a==b ):
                        return 1;
                else:
                        return 4;
        else:
                if( abs(a)==abs(b) ):
                        return 4;
                else:
                        return 8;

def produceSumOfSquares( n ):
        if( n < 0 ):
                raise Exception("Negative numbers are not permitted as arguments to produceSumOfSquares()");
        squareList = listOfSquaresAtMost( n );
        sumOfSquaresSet = set([]);
        decompositions = {};
        i = 0;
        while( i < len(squareList) ):
                j = i;
                while( j < len(squareList) ):
                        total = squareList[i] + squareList[j];
                        sumOfSquaresSet.add( total );
                        if( total in decompositions ):
                                decompositions[total] = decompositions[total] + [(int(math.sqrt(squareList[i])),int(math.sqrt(squareList[j])))];
                        else:
                                decompositions[total] = [(int(math.sqrt(squareList[i])),int(math.sqrt(squareList[j])))];
                        j = j + 1;
                i = i + 1;
        sums = [];
        notSums = [];
        for element in range(n + 1):
                if( element in sumOfSquaresSet ):
                        sums = sums + [element];
                else:
                        notSums = notSums + [element];
        return (sums, notSums, decompositions);

def writeMainFile( n ):
        output = produceSumOfSquares( END_CONDITION );
        file = open( "ProjectTwoCalculations.txt", "w+");
        file.write( ' ' * 5 + 'n | ' + ' ' * 70 + ' | ' + ' ' * 5 + 'f | ' + ' ' * 5 +'F | factorization\n' );
        for element in output[0]:
                file.write( INT_FORMAT.format( element ) );
                file.write( ' | ' );
                file.write( STR_FORMAT.format( str(output[2][element] ) ) );
                file.write( ' | ' );
                file.write( INT_FORMAT.format( len(output[2][element]) ) );
                file.write( ' | ' );
                file.write( INT_FORMAT.format( getPermutationCount( output[2][element] ) ) );
                file.write( ' | ' );
                file.write( str( primeFactorization( element ) ) );
                file.write( '\n' );



writeMainFile( END_CONDITION );


