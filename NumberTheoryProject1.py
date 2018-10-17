import math;

CALCULATE_TO = 1200;

def writeToFile( array, filename ):
    file = open(filename, "w+");
    for i in array:
        file.write( str(i) );
        file.write( "  -  " );
        for k in primeFactorization( i ):
        	file.write( str( int(k) ) );
        	file.write( " ");
        file.write( "\n" );
    file.close();

def writeMainFile( k ):
    file = open( "ProjectOneCalculations.txt", "w+");
    file.write( "i\tsum\tsum*\tpi\tpi*\n" );
    for i in list_set( k )[1:]:
        file.write( str(i) );
        file.write( '\t' );
        file.write( str( sigma(i) ) );
        file.write( '\t' );
        file.write( str( sigma_star(i) ) );
        file.write( '\t' );
        file.write( str( pi(i) ) );
        file.write( '\t' );
        file.write( str( pi_star(i)) );
        file.write( '\n' );

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
		primeFactors = primeFactors + [number];
	return primeFactors;

def sumModN( list, n ):
    acc=0;
    for element in list:
            acc = (acc + element) % n;
    if( acc <= n/2.0 ):
            return acc;
    else:
            return acc - n;

def productModN( list, n ):
    acc=1;
    for element in list:
            acc = (acc * element) % n;
    if( acc <= n/2.0 ):
            return acc;
    else:
            return acc - n;

def list_set( x ):
    if( x< 0 ):
            return [0];
    else:
            out = [];
            while( x >= 0 ):
                    out = [x] + out;
                    x = x - 1;
            return out;

def coprime_set( x ):
    list = list_set(x);
    acc = [];
    for element in list:
            if( math.gcd( element, x ) == 1 ):
                    acc = acc + [element];
    return acc;

def sigma( x ):
    return sumModN( list_set( x ), x );

def sigma_star( x ):
    return sumModN( coprime_set( x ), x );

def pi( x ):
    return productModN( list_set( x ), x );

def pi_star( x ):
    return productModN( coprime_set( x ), x );

oneValues = [];
negativeOneValues = [];
for i in list_set(CALCULATE_TO)[1:]:
	if( pi_star(i) == 1 ):
		oneValues = oneValues + [i];
	else:
		negativeOneValues = negativeOneValues + [i];

writeToFile( oneValues, "PiStarOneValues.txt");
writeToFile( negativeOneValues, "PiStarNegativeOneValues.txt");
writeMainFile(CALCULATE_TO);
print();

