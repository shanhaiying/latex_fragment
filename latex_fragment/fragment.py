from importlib import reload
from . import render_latex

class LatexFragment:
    def __init__(self, body=""):
        self._body = body

    def _repr_latex_(self):
        return render_latex.extra_packages_body(
            self._body)[1]

    def _repr_png_(self):
        return render_latex.as_png(self._body)

    # def _repr_pdf_(self):
    #     return render_latex.as_pdf(self._body)

    # def _repr_svg_(self):
    #     return render_latex.as_svg(self._body)