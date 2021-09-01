import streamlit as st
from sympy import *
from sympy.solvers import solve

x= symbols('x'); F0, F1 ,F2= symbols('F0 F1 F2', cls=Function)

st.title("""関数の極大点，極小点，変曲点""")
#st.latex('\\frac{1}{2}mx^2')
FORM_INPUT = st.text_input('極大点，極小点，変曲点を調べたい関数を入力してください．')
'調べる関数$f(x)$は'
F0 = sympify(FORM_INPUT)
st.latex(F0)
'です.'

'入力された関数の１次導関数は'

F1 = simplify(diff(F0))
st.latex(F1)
'です．また2次導関数は'
F2 = simplify(diff(F1))
st.latex(F2)
'です．'

