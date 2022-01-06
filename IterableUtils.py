
from typing import Iterable, List, Tuple, Any, Callable, Type, TypeVar, Dict

K = TypeVar('K') 
V = TypeVar('V') 
E = TypeVar('E') 
R = TypeVar('R')

identity = lambda x:x

'''
tomado de la página 112 del libro de Miguel Toro
Reducción por grupos. Se trata de acumular los elementos de cada grupo de un iterable usando un operador binario y partiendo del primer elemento. 

'''
def grouping_reduce(iterable:Iterable[E], fkey:Callable[[E],K],op:Callable[[V,V],V], fvalue:Callable[[E],V]= identity) -> Dict[K, E]:
    a = {} 
    for e in iterable: 
        k = fkey(e)
        if k in a: 
            a[k] = op(a[k],fvalue(e)) 
        else:
            a[k] = fvalue(e) 
    return a
    
def grouping_list(iterable:Iterable[E], fkey:Callable[[E],K], fvalue:Callable[[E],V]=identity) -> Dict[K,List[V]]: 
    return grouping_reduce(iterable,fkey,lambda x,y:x+y, lambda x: [fvalue(x)])
