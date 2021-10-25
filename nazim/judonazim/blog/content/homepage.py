
def navtemplates(request):
    if('btnnazimtaboo' in request.POST):
        return {'txtfilename':'nazimtaboo.html'}
    elif('btndiversity' in request.POST):
        return {'txtfilename':'diversity.html'}
    elif('btneugenics' in request.POST):
        return {'txtfilename':'eugenics.html'}
    elif('btnbemoreracist' in request.POST):
        return {'txtfilename':'bemoreracist.html'}
    elif('btnracisabiologicalfacts' in request.POST):
        return {'txtfilename':'racisabiologicalfacts.html'}
    elif('btnsomeracesarebetter' in request.POST):
        return {'txtfilename':'someracesarebetter.html'}
    elif('btnracialdiffiniq' in request.POST):
        return {'txtfilename':'racialdiffiniq.html'}
    elif('btnethnostate' in request.POST):
        return {'txtfilename':'ethnostate.html'}
    elif('btnevolutionandrace' in request.POST):
        return {'txtfilename':'evolutionandrace.html'}
    elif('btnnegroesaredumb' in request.POST):
        return {'txtfilename':'negroesaredumb.html'}
    elif('btnnegroesareapes' in request.POST):
        return {'txtfilename':'negroesareapes.html'}
    elif('btnwhywearediff' in request.POST):
        return {'txtfilename':'whywearediff.html'}
    elif('btnooamyth' in request.POST):
        return {'txtfilename':'ooamyth.html'}
    elif('btnfeminisgenocide' in request.POST):
        return {'txtfilename':'feminisgenocide.html'}
    elif('btnfeminismandashk' in request.POST):
        return {'txtfilename' : 'feminismandashk.html'}
    elif('btnfeminismdestroyfamily' in request.POST):
        return {'txtfilename':'feminismdestroyfamily.html'}
    elif('btnfeminismidf' in request.POST):
        return {'txtfilename':'feminismidf.html'}
    elif('btnfemalesdestorynations' in request.POST):
        return {'txtfilename':'femalesdestorynations.html'}
    elif('btnrapeisnotacrime' in request.POST):
        return {'txtfilename':'rapeisnotacrime.html'}
    elif('btnopressionmyth' in request.POST):
        return {'txtfilename':'opressionmyth.html'}
    elif('btnmarrigemortage' in request.POST):
        return {'txtfilename':'marrigemortage.html'}
    else:
        pass
    return {'txtfilename':'nazimbg.html'}
