# lp_palettes/scales.py
from lets_plot.plot import scale_color_manual, scale_fill_manual
from .palettes import lp_palettes_db

def scale_color_npg(palette="nrc", alpha=1.0, **kwargs):
    """
    Color scale from the Nature Publishing Group.
    """
    colors = lp_palettes_db["npg"][palette]
    return scale_color_manual(values=colors, **kwargs)

def scale_fill_npg(palette="nrc", alpha=1.0, **kwargs):
    """
    Fill scale from the Nature Publishing Group.
    """
    colors = lp_palettes_db["npg"][palette]
    return scale_fill_manual(values=colors, **kwargs)

def scale_color_aaas(palette="default", alpha=1.0, **kwargs):
    """
    Color scale from the American Association for the Advancement of Science.
    """
    colors = lp_palettes_db["aaas"][palette]
    return scale_color_manual(values=colors, **kwargs)

def scale_fill_aaas(palette="default", alpha=1.0, **kwargs):
    """
    Fill scale from the American Association for the Advancement of Science.
    """
    colors = lp_palettes_db["aaas"][palette]
    return scale_fill_manual(values=colors, **kwargs)

def scale_color_nejm(palette="default", alpha=1.0, **kwargs):
    """
    Color scale from the New England Journal of Medicine.
    """
    colors = lp_palettes_db["nejm"][palette]
    return scale_color_manual(values=colors, **kwargs)

def scale_fill_nejm(palette="default", alpha=1.0, **kwargs):
    """
    Fill scale from the New England Journal of Medicine.
    """
    colors = lp_palettes_db["nejm"][palette]
    return scale_fill_manual(values=colors, **kwargs)

def scale_color_lancet(palette="lanonc", alpha=1.0, **kwargs):
    """
    Color scale from The Lancet.
    """
    colors = lp_palettes_db["lancet"][palette]
    return scale_color_manual(values=colors, **kwargs)

def scale_fill_lancet(palette="lanonc", alpha=1.0, **kwargs):
    """
    Fill scale from The Lancet.
    """
    colors = lp_palettes_db["lancet"][palette]
    return scale_fill_manual(values=colors, **kwargs)

def scale_color_jama(palette="default", alpha=1.0, **kwargs):
    """
    Color scale from the Journal of the American Medical Association.
    """
    colors = lp_palettes_db["jama"][palette]
    return scale_color_manual(values=colors, **kwargs)

def scale_fill_jama(palette="default", alpha=1.0, **kwargs):
    """
    Fill scale from the Journal of the American Medical Association.
    """
    colors = lp_palettes_db["jama"][palette]
    return scale_fill_manual(values=colors, **kwargs)

def scale_color_jco(palette="default", alpha=1.0, **kwargs):
    """
    Color scale from the Journal of Clinical Oncology.
    """
    colors = lp_palettes_db["jco"][palette]
    return scale_color_manual(values=colors, **kwargs)

def scale_fill_jco(palette="default", alpha=1.0, **kwargs):
    """
    Fill scale from the Journal of Clinical Oncology.
    """
    colors = lp_palettes_db["jco"][palette]
    return scale_fill_manual(values=colors, **kwargs)

def scale_color_ucscgb(palette="default", alpha=1.0, **kwargs):
    """
    Color scale from the UCSC Genome Browser.
    """
    colors = lp_palettes_db["ucscgb"][palette]
    return scale_color_manual(values=colors, **kwargs)

def scale_fill_ucscgb(palette="default", alpha=1.0, **kwargs):
    """
    Fill scale from the UCSC Genome Browser.
    """
    colors = lp_palettes_db["ucscgb"][palette]
    return scale_fill_manual(values=colors, **kwargs)

def scale_color_d3(palette="category10", alpha=1.0, **kwargs):
    """
    Color scale from D3.js.
    """
    colors = lp_palettes_db["d3"][palette]
    return scale_color_manual(values=colors, **kwargs)

def scale_fill_d3(palette="category10", alpha=1.0, **kwargs):
    """
    Fill scale from D3.js.
    """
    colors = lp_palettes_db["d3"][palette]
    return scale_fill_manual(values=colors, **kwargs)

def scale_color_locuszoom(palette="default", alpha=1.0, **kwargs):
    """
    Color scale from LocusZoom.
    """
    colors = lp_palettes_db["locuszoom"][palette]
    return scale_color_manual(values=colors, **kwargs)

def scale_fill_locuszoom(palette="default", alpha=1.0, **kwargs):
    """
    Fill scale from LocusZoom.
    """
    colors = lp_palettes_db["locuszoom"][palette]
    return scale_fill_manual(values=colors, **kwargs)

def scale_color_igv(palette="default", alpha=1.0, **kwargs):
    """
    Color scale from the Integrative Genomics Viewer.
    """
    colors = lp_palettes_db["igv"][palette]
    return scale_color_manual(values=colors, **kwargs)

def scale_fill_igv(palette="default", alpha=1.0, **kwargs):
    """
    Fill scale from the Integrative Genomics Viewer.
    """
    colors = lp_palettes_db["igv"][palette]
    return scale_fill_manual(values=colors, **kwargs)

def scale_color_cosmic(palette="hallmarks_light", alpha=1.0, **kwargs):
    """
    Color scale from COSMIC.
    """
    colors = lp_palettes_db["cosmic"][palette]
    return scale_color_manual(values=colors, **kwargs)

def scale_fill_cosmic(palette="hallmarks_light", alpha=1.0, **kwargs):
    """
    Fill scale from COSMIC.
    """
    colors = lp_palettes_db["cosmic"][palette]
    return scale_fill_manual(values=colors, **kwargs)

def scale_color_uchicago(palette="light", alpha=1.0, **kwargs):
    """
    Color scale from the University of Chicago.
    """
    colors = lp_palettes_db["uchicago"][palette]
    return scale_color_manual(values=colors, **kwargs)

def scale_fill_uchicago(palette="light", alpha=1.0, **kwargs):
    """
    Fill scale from the University of Chicago.
    """
    colors = lp_palettes_db["uchicago"][palette]
    return scale_fill_manual(values=colors, **kwargs)

def scale_color_simpsons(palette="springfield", alpha=1.0, **kwargs):
    """
    Color scale from The Simpsons.
    """
    colors = lp_palettes_db["simpsons"][palette]
    return scale_color_manual(values=colors, **kwargs)

def scale_fill_simpsons(palette="springfield", alpha=1.0, **kwargs):
    """
    Fill scale from The Simpsons.
    """
    colors = lp_palettes_db["simpsons"][palette]
    return scale_fill_manual(values=colors, **kwargs)

def scale_color_gsea(palette="default", alpha=1.0, **kwargs):
    """
    Color scale from GSEA.
    """
    colors = lp_palettes_db["gsea"][palette]
    return scale_color_manual(values=colors, **kwargs)

def scale_fill_gsea(palette="default", alpha=1.0, **kwargs):
    """
    Fill scale from GSEA.
    """
    colors = lp_palettes_db["gsea"][palette]
    return scale_fill_manual(values=colors, **kwargs)

def scale_color_material(palette="red", alpha=1.0, **kwargs):
    """
    Color scale from Google Material Design.
    """
    colors = lp_palettes_db["material"][palette]
    return scale_color_manual(values=colors, **kwargs)

def scale_fill_material(palette="red", alpha=1.0, **kwargs):
    """
    Fill scale from Google Material Design.
    """
    colors = lp_palettes_db["material"][palette]
    return scale_fill_manual(values=colors, **kwargs)

def scale_color_viridis(palette="viridis", alpha=1.0, **kwargs):
    """
    Color scale from Viridis.
    """
    colors = lp_palettes_db["viridis"][palette]
    return scale_color_manual(values=colors, **kwargs)

def scale_fill_viridis(palette="viridis", alpha=1.0, **kwargs):
    """
    Fill scale from Viridis.
    """
    colors = lp_palettes_db["viridis"][palette]
    return scale_fill_manual(values=colors, **kwargs)

def scale_color_wesanderson(palette="BottleRocket1", alpha=1.0, **kwargs):
    """
    Color scale from Wes Anderson movies.
    """
    colors = lp_palettes_db["wesanderson"][palette]
    return scale_color_manual(values=colors, **kwargs)

def scale_fill_wesanderson(palette="BottleRocket1", alpha=1.0, **kwargs):
    """
    Fill scale from Wes Anderson movies.
    """
    colors = lp_palettes_db["wesanderson"][palette]
    return scale_fill_manual(values=colors, **kwargs)
