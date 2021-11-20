
def navtemplates(request):
    if('btnnazimtaboo' in request.POST or 'submenu-btnnazimtaboo' in request.POST):
        return {'txtfilename':'nazimtaboo.html'}
    elif('btndiversity' in request.POST or 'submenu-btndiversity' in request.POST):
        return {'txtfilename':'diversity.html'}
    elif('btneugenics' in request.POST or 'submenu-btneugenics' in request.POST):
        return {'txtfilename':'eugenics.html'}
    elif('btnbemoreracist' in request.POST or 'submenu-btnbemoreracist' in request.POST):
        return {'txtfilename':'bemoreracist.html'}
    elif('btnracisabiologicalfacts' in request.POST or 'submenu-btnracisabiologicalfacts' in request.POST):
        return {'txtfilename':'racisabiologicalfacts.html'}
    elif('btnsomeracesarebetter' in request.POST or 'submenu-btnsomeracesarebetter' in request.POST):
        return {'txtfilename':'someracesarebetter.html'}
    elif('btnracialdiffiniq' in request.POST or 'submenu-btnracialdiffiniq' in request.POST):
        return {'txtfilename':'racialdiffiniq.html'}
    elif('btnethnostate' in request.POST or 'submenu-btnethnostate' in request.POST):
        return {'txtfilename':'ethnostate.html'}
    elif('btnevolutionandrace' in request.POST or 'submenu-btnevolutionandrace' in request.POST):
        return {'txtfilename':'evolutionandrace.html'}
    elif('btnnegroesaredumb' in request.POST or 'submenu-btnnegroesaredumb' in request.POST):
        return {'txtfilename':'negroesaredumb.html'}
    elif('btnnegroesareapes' in request.POST or 'submenu-btnnegroesareapes' in request.POST):
        return {'txtfilename':'negroesareapes.html'}
    elif('btnwhywearediff' in request.POST or 'submenu-btnwhywearediff' in request.POST):
        return {'txtfilename':'whywearediff.html'}
    elif('btnooamyth' in request.POST or 'submenu-btnooamyth' in request.POST):
        return {'txtfilename':'ooamyth.html'}
    elif('btnfeminisgenocide' in request.POST or 'submenu-btnfeminisgenocide' in request.POST):
        return {'txtfilename':'feminisgenocide.html'}
    elif('btnfeminismandashk' in request.POST or 'submenu-btnfeminismandashk' in request.POST):
        return {'txtfilename' : 'feminismandashk.html'}
    elif('btnfeminismdestroyfamily' in request.POST or 'submenu-btnfeminismdestroyfamily' in request.POST):
        return {'txtfilename':'feminismdestroyfamily.html'}
    elif('btnfeminismidf' in request.POST or 'submenu-btnfeminismidf' in request.POST):
        return {'txtfilename':'feminismidf.html'}
    elif('btnfemalesdestorynations' in request.POST or 'submenu-btnfemalesdestorynations' in request.POST):
        return {'txtfilename':'femalesdestorynations.html'}
    elif('btnrapeisnotacrime' in request.POST or 'submenu-btnrapeisnotacrime' in request.POST):
        return {'txtfilename':'rapeisnotacrime.html'}
    elif('btnopressionmyth' in request.POST or 'submenu-btnopressionmyth' in request.POST):
        return {'txtfilename':'opressionmyth.html'}
    elif('btnmarrigemortage' in request.POST or 'submenu-btnmarrigemortage' in request.POST):
        return {'txtfilename':'marrigemortage.html'}
    elif('btnmensmarter' in request.POST or 'submenu-btnmensmarter' in request.POST):
        return {'txtfilename':'mensmarter.html'}
    elif('btnequalcontribution' in request.POST or 'submenu-btnequalcontribution' in request.POST):
        return {'txtfilename' : 'equalcontribution.html'}
    elif('btnashkenazimsjw' in request.POST or 'submenu-btnashkenazimsjw' in request.POST):
        return {'txtfilename': 'ashkenazimsjw.html'}
    elif('btnrefugee' in request.POST or 'submenu-btnrefugee' in request.POST):
        return {'txtfilename': 'refugee.html'}
    elif('btnfemvictims' in request.POST or 'submenu-btnfemvictims' in request.POST):
        return {'txtfilename':'femvictims.html'}
    elif('btnboysdiscrimnation' in request.POST or 'submenu-btnboysdiscrimnation' in request.POST):
        return {'txtfilename':'boysdiscrimnation.html'}
    elif('btnmenlivesischeap' in request.POST or 'submenu-btnmenlivesischeap' in request.POST):
        return {'txtfilename':'menlivesischeap.html'}
    elif('btnpart1' in request.POST or 'submenu-btnpart1' in request.POST):
        return {'txtfilename':'part1.html'}
    elif('btnpart2' in request.POST or 'submenu-btnpart2' in request.POST):
        return {'txtfilename':'part2.html'}
    elif('btnpart3' in request.POST or 'submenu-btnpart3' in request.POST):
        return {'txtfilename':'part3.html'}
    elif('btnwhyashkleftist' in request.POST or 'submenu-btnwhyashkleftist' in request.POST):
        return {'txtfilename':'whyashkleftist.html'}
    elif('btnashksacademic' in request.POST or 'submenu-btnashksacademic' in request.POST):
        return {'txtfilename':'ashksacademic.html'}
    elif('btnashkmedia' in request.POST or 'submenu-btnashkmedia' in request.POST):
        return {'txtfilename':'ashkmedia.html'}
    elif('btnimomenajews' in request.POST):
        return {'txtfilename':'imomizrahim.html'}
    elif('btnmeonlinetv' in request.POST):
        return {'txtfilename':'onlinetv.html'}
    elif('btn12tv' in request.POST):
        return {'txtfilename':'channel12.html', 'page_index':1, 'numofpages':3}
    elif('btncontinue' in request.POST):
        page_index = int(request.POST.get('btncontinue'));
        page_index += 1;
        return {'txtfilename':'channel12.html', 'page_index':page_index, 'numofpages':3}
    elif('btnback' in request.POST):
        page_index = int(request.POST.get('btnback'));
        page_index -= 1;
        return {'txtfilename':'channel12.html', 'page_index':page_index, 'numofpages':3}
    elif('btnwebsitedev' in request.POST):
        return {'txtfilename' : 'mywebsitedevelopment.html'}
    elif('cost_of_diversity' in request.POST):
        return {'txtfilename' : 'costofdiversity.html'}
    elif('btnnif' in request.POST or 'submenu-btnnif' in request.POST):
        return {'txtfilename' : 'nif.html', 'ashk_media_type' : 'nif'}
    elif('btnsupremecourt' in request.POST or 'submenu-btnsupremecourt' in request.POST):
        return {'txtfilename' : 'nif.html', 'ashk_media_type' : 'supreme court'}
    elif('btnethconsiparcy' in request.POST or 'submenu-btnethconsiparcy' in request.POST):
        return {'txtfilename' : 'nif.html', 'ashk_media_type' : 'diversity'}
    else:
        pass
    return {'txtfilename':'nazimbg.html'}
