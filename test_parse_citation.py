from parse_citation import parse_citation

test_md = """
# My Heading

Lorem ipsum dolor sit amet, consectetur adipiscing elit. Phasellus ac magna non augue
porttitor scelerisque ac id diam <cite data-cite="granger">Granger</cite>. Mauris elit
velit, lobortis sed interdum at, vestibulum vitae libero <strong data-cite="fperez">Perez</strong>.
Lorem ipsum dolor sit amet, consectetur adipiscing elit
<em data-cite="takluyver">Thomas</em>. Quisque iaculis ligula ut ipsum mattis viverra.

* One <cite data-cite="jdfreder">Jonathan</cite>.
* Two <cite data-cite="carreau">Matthias</cite>.
* Three <cite data-cite="ivanov">Paul</cite>.
"""

test_md_parsed = """
# My Heading

Lorem ipsum dolor sit amet, consectetur adipiscing elit. Phasellus ac magna non augue
porttitor scelerisque ac id diam \cite{granger}. Mauris elit
velit, lobortis sed interdum at, vestibulum vitae libero \cite{fperez}.
Lorem ipsum dolor sit amet, consectetur adipiscing elit
\cite{takluyver}. Quisque iaculis ligula ut ipsum mattis viverra.

* One \cite{jdfreder}.
* Two \cite{carreau}.
* Three \cite{ivanov}.
"""

def test_parse_citation():
    assert test_md_parsed == parse_citation(test_md)
