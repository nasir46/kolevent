from django.shortcuts import render
from kolevent.models import *






def view_list(request):
    
    sldimg = slider.objects.all()[:200]
    sldnme = slider.objects.all()[:200]
    sldmsg = slider.objects.all()[:200]
    sldcntnt = slider.objects.all()[:200]
    
    cmplogo = comp.objects.all()[0]
    cmpname = comp.objects.all()[0]
    compmsg = comp.objects.all()[0]
    comptxt = comp.objects.all()[0]
    
    abtusnme = aboutus.objects.all()[:200]
    abtustxt = aboutus.objects.all()[:200]
    abtusimg = aboutus.objects.all()[:200]

    himage = home.objects.all()[0]
    hcontent = home.objects.all()[:200]
    

    limagea = logo.objects.all()[:200]
    lurl = logo.objects.all()[:200]
    
    
    sname = services.objects.get(id=1)
    sname1 = services.objects.get(id=2)
    sname2 = services.objects.get(id=3)
    sname3 = services.objects.get(id=5)

    simgae = services.objects.get(id=1)
    simgae1 = services.objects.get(id=2)
    simgae2 = services.objects.get(id=3)
    simgae3 = services.objects.get(id=5)

    scontent = services.objects.get(id=1)
    scontent1 = services.objects.get(id=2)
    scontent2 = services.objects.get(id=3)
    scontent3 = services.objects.get(id=5)
    
    nnme = news.objects.all()[:200]
    nimage = news.objects.all()[:200]
    ncontent = news.objects.all()[:200]
    ndate = news.objects.all()[:200]
    
    
    aname = album.objects.all()[:200]
    aimage = album.objects.all()[:200]
    acontent = album.objects.all()[:200]
    
    tname = tour.objects.all()[:200]
    timage = tour.objects.all()[:1]
    tcontent = tour.objects.all()[:200]
    tdate = tour.objects.all()[:200]
    
    
    gname = gallery.objects.all()[:200]
    gimage = gallery.objects.all()[:200]
    
    twimg = twit.objects.all()[0]
    
    vdonme = video.objects.all()[:100]
    vdourl = video.objects.all()[:100]


    pronme = promotion.objects.all()[:500]
    proimg = promotion.objects.all()[:500]
    
    
    return render(request, 'index.html', {
                                          
                'sldimg':sldimg, 'sldnme':sldnme, 'sldcntnt':sldcntnt, 'sldmsg':sldmsg,

                'abtusnme':abtusnme, 'abtustxt':abtustxt, 'abtusimg':abtusimg,
                                          
                'himage':himage, 'hcontent':hcontent,  
                
                'simgae':simgae, 'simgae1':simgae1, 'simgae2':simgae2, 'simgae3':simgae3,

                'scontent':scontent, 'scontent1':scontent1, 'sconten2t':scontent2, 'scontent3':scontent3, 

                'sname':sname, 'sname1':sname1, 'sname2':sname2, 'sname3':sname3,
                                          
                'cmplogo':cmplogo, 'cmpname':cmpname, 'compmsg':compmsg, 'comptxt':comptxt,
                 
                'limagea':limagea, 'lurl':lurl,
                 
                'nnme':nnme, 'ndate':ndate, 'nimage':nimage, 'ncontent':ncontent,
                 
                'aname':aname, 'aimage':aimage, 'acontent':acontent, 
                 
                'tname':tname, 'timage':timage, 'tcontent':tcontent, 'tdate':tdate,  
                 
                'gimage':gimage, 'gname':gname,
                
                'twimg':twimg,
                
                'vdourl':vdourl, 'vdonme':vdonme,

                'pronme':pronme, 'proimg':proimg
                 
                })
