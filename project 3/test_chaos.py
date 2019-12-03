from chaos_game import chaos_game
import nose
import nose.tools as nt

"""Tests if n>=3 and 0<r<1"""
@nt.raises(ValueError)
def test_value_constructor():
     chaos = chaos_game(4,0.7)

""" Tests if n is an interger and r is a float"""     
@nt.raises(TypeError)
def test_type_constructors():
     chaos = chaos_game(4, 0.9)

"""Tests iterator """
def test_iterator():
     chaos = chaos_game(4,0.8)
     c = chaos.iterate(10000)
     assert len(c) == 10000

""" Tests the if the file given is .png """
@nt.raises(TypeError)
def test_figure_type():
     chaos = chaos_game(4,0.5)
     chaos.iterate(1000)
     chaos.savepng("figure.png")

     
     
if __name__ == '__main__':
     nose.run()
     


