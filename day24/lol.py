import re, graphlib

g = { w: ( o, a, b ) for a, o, b, w in
      re.findall( r"([a-z0-9]+) (AND|OR|XOR) ([a-z0-9]+) -> ([a-z0-9]+)", open( 0 ).read() ) }
c = max( int( w[ 1 : ] ) for w in g if re.fullmatch( r"z[0-9]+", w ) )
m = 2 ** ( c + 1 ) - 1

def test1( e, x, y, s ):
    v = ( { f"x{i:02d}": ( x >> i ) & 1 for i in range( c ) } |
          { f"y{i:02d}": ( y >> i ) & 1 for i in range( c ) } )
    for w in e:
        o, a, b = g[ s.get( w, w ) ]
        if   o == "AND": v[ w ] = v[ a ] & v[ b ]
        elif o == "OR":  v[ w ] = v[ a ] | v[ b ]
        elif o == "XOR": v[ w ] = v[ a ] ^ v[ b ]
    for i in range( c + 1 ):
        if v[ f"z{i:02d}" ] != ( ( x + y ) >> i ) & 1:
            return i
    return c + 1

def testn( s ):
    try:
        e = [ w for w in graphlib.TopologicalSorter(
                  { s.get( w, w ): { a, b } for w, ( o, a, b ) in g.items() } ).static_order()
              if w in g ]
        return min( test1( e, x, y, s )
                    for x, y in ( ( m, 0 ), ( 0, m ), ( m, 1 ), ( 1, m ), ( m, m ) ) )
    except graphlib.CycleError:
        return 0

s = {}
while len( s ) < 8:
    a, b = max( ( ( a, b ) for a in g for b in g if a < b and a not in s and b not in s ),
                key = lambda p: testn( s | { p[ 0 ]: p[ 1 ], p[ 1 ]: p[ 0 ] } ) )
    s.update( { a: b, b: a } )

print( ",".join( sorted( s ) ) )
