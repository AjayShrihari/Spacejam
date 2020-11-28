import pygame,sys
import random
from pygame.locals import *
class time:
        def time1(self):
                subclock=pygame.time.Clock()
                
                
        
ob=time()
ob.time1()
class game:
        
        def maingame(self):
                pygame.init()   #Initialising the game
                pygame.font.init()
                mainclock= pygame.time.Clock()
                window=pygame.display.set_mode((370,580),0,32)
                pygame.display.set_caption('Space Jam')
                score=0
                Texta = pygame.font.Font('SUPERPOI_R.TTF', 20)
                Textb= pygame.font.Font('SUPERPOI_R.TTF',35)
                Textc=pygame.font.Font('Capture_it.TTF',30)

                text = Texta.render('score: %d' % score, 0, (250,250,0))
                astrfrqnc=10000 # the higher the less frequent
                dbfrqc=4000
                player=pygame.Rect(170,380,20,20)
                shield=False
                shipx=pygame.image.load('Space Shooter.png')
                instr2 = pygame.image.load('arrow.png')
                instr = pygame.transform.scale(instr2,(110,110))
                instr4 = pygame.image.load('spacebar.png')
                instr3 = pygame.transform.scale(instr4,(int(180*1.3),int(30*1.3)))
                #Initialising variables

                a=0
                pb=[]
                db=[]
                astroid=[]
                drone=[]
                drone2=[]
                power=0
                p=-250
                W=(255,255,255)
                B=(0,0,0)
                R=(255,0,0)
                BL=(0,0,255)
                P=(190,190,190)
                ms=4
                bs=10
                ha=0
                ba=0
                son=0
                son2=0
                bonus=0
                highscore=0

                bugfix1=False
                bugfix2=False


                shoot=False
                test=False
                menu=True
                game=False
                option=0
                counter=0
                r=True
                r2=True
                dronetop=0
                dronetop2=0

                moveleft=False
                moveright=False
                moveup=False
                movedown=False
                #Music
                
                        
                pygame.mixer.music.load('Star Wars.mp3')
                pygame.mixer.music.play(-1)
                makesound=False
                back=[pygame.Rect(random.randint(0,350),random.randint(0,500),5,5),pygame.Rect(random.randint(0,350),random.randint(0,500),5,5),pygame.Rect(random.randint(0,350),random.randint(0,500),5,5),pygame.Rect(random.randint(0,350),random.randint(0,500),5,5),pygame.Rect(random.randint(0,350),random.randint(0,500),5,5),pygame.Rect(random.randint(0,350),random.randint(0,500),5,5),pygame.Rect(random.randint(0,350),random.randint(0,500),5,5),pygame.Rect(random.randint(0,350),random.randint(0,500),5,5),pygame.Rect(random.randint(0,350),random.randint(0,500),5,5),pygame.Rect(random.randint(0,350),random.randint(0,500),5,5),pygame.Rect(random.randint(0,350),random.randint(0,500),5,5),pygame.Rect(random.randint(0,350),random.randint(0,500),5,5),pygame.Rect(random.randint(0,350),random.randint(0,500),5,5),pygame.Rect(random.randint(0,350),random.randint(0,500),5,5),pygame.Rect(random.randint(0,350),random.randint(0,500),5,5),pygame.Rect(random.randint(0,350),random.randint(0,500),5,5),pygame.Rect(random.randint(0,350),random.randint(0,500),5,5),pygame.Rect(random.randint(0,350),random.randint(0,500),5,5),pygame.Rect(random.randint(0,350),random.randint(0,500),5,5),pygame.Rect(random.randint(0,350),random.randint(0,500),5,5),pygame.Rect(random.randint(0,350),random.randint(0,500),5,5),pygame.Rect(random.randint(0,350),random.randint(0,500),5,5),pygame.Rect(random.randint(0,350),random.randint(0,500),5,5),pygame.Rect(random.randint(0,350),random.randint(0,500),5,5),pygame.Rect(random.randint(0,350),random.randint(0,500),5,5),pygame.Rect(random.randint(0,350),random.randint(0,500),5,5),pygame.Rect(random.randint(0,350),random.randint(0,500),5,5),pygame.Rect(random.randint(0,350),random.randint(0,500),5,5),pygame.Rect(random.randint(0,350),random.randint(0,500),5,5),pygame.Rect(random.randint(0,350),random.randint(0,500),5,5),pygame.Rect(random.randint(0,350),random.randint(0,500),5,5),pygame.Rect(random.randint(0,350),random.randint(0,500),5,5),pygame.Rect(random.randint(0,350),random.randint(0,500),5,5),pygame.Rect(random.randint(0,350),random.randint(0,500),5,5),pygame.Rect(random.randint(0,350),random.randint(0,500),5,5),pygame.Rect(random.randint(0,350),random.randint(0,500),5,5),pygame.Rect(random.randint(0,350),random.randint(0,500),5,5),pygame.Rect(random.randint(0,350),random.randint(0,500),5,5)]
                backspd=1
                while True:
                    while game==False:
                        
                        moveleft=False
                        moveright=False
                        moveup=False
                        movedown=False
                        counter=0
                        bonus=0
                        astroid=[]
                        drone=[]
                        drone2=[]
                        db=[]
                        pb=[]
                        p=-250
                        player=pygame.Rect(170,380,20,20)
                        window.fill (B)
                        for event in pygame.event.get():
                            if event.type==QUIT:
                                pygame.quit()
                                sys.exit()
                            if event.type== KEYDOWN:
                                if event.key== K_DOWN and option==0:
                                    option=option+1
                                if event.key==K_UP and option==1:
                                    option=option-1
                                if event.key==K_RETURN and option==1:
                                    pygame.quit()
                                    sys.exit()
                                if event.key==K_RETURN  and option==0:    
                                    game=True
                                    score=0
                                    moveright=True
                                    
                        if option==0:
                            player.top=380
                        if option==1:
                            player.top=440
                        for bo in back:
                            pygame.draw.rect(window,W,bo)
                            bo.top+=backspd
                            if bo.top>=500:
                                bo.left=random.randint(0,300)
                                bo.top=-5
                    
                            
                        f = open('high_score.txt','r')
                        highscore = int(f.read() )
                        f.close()
                        if score>=highscore:
                            highscore=int(round(score,0))
                            f = open('high_score.txt','w')
                            f.write(str(highscore))
                            f.close()
                                   
                        #Option menu         
                        
                                
                        text1= Texta.render('score: %d' % score, 0, (250,250,0))
                        text2= Texta.render('Highscore: %d' % highscore, 0, (250,250,0))
                        text3= Texta.render('code by Ajay ', 0, (250,250,0))
                        text4= Texta.render('and Poornesh', 0, (250,250,0))
                        text5= Textb.render('Space Jam ', 0, (255,0,0))
                        text6= Texta.render('start', 0, (255,0,0))
                        text7= Texta.render('quit ', 0, (255,0,0))
                        text8= Textc.render('Instructions :-',0,(255,255,255))
                        text9= Textc.render('To Move', 0, (255,255,255))
                        text10= Textc.render('To Shoot', 0, (0,0,0))
                        
                        window.blit(text1, (5,0))
                        window.blit(text2, (5,50))
                        window.blit(text3, (5,500))
                        window.blit(text4, (5,530))
                        
                        
                        window.blit(text5, (17,120))
                        window.blit(text6, (220,375))
                        window.blit(text7, (220,435))

                        
                        window.blit(text8,  (5,220))
                        window.blit(instr,  (5,260))
                        window.blit(instr3,  (130,300))
                        window.blit(text9,  (5,350))
                        window.blit(text10,  (200,305))
                        
                        window.blit(shipx,(player.left-2,player.top))
                        mainclock.tick(30)
                        pygame.display.update()
                        
                    while game :
                        
                        if p>-250:
                            p=p-1
                        powerbar=pygame.Rect(330,560,20,p)
                        counter=counter+1
                        if p>=-1:
                            shield=False
                        window.fill (B)
                        for event in pygame.event.get():
                            if event.type==QUIT:
                                pygame.quit()
                                sys.exit()
                            if event.type== KEYDOWN:
                                if event.key== K_DOWN:
                                    movedown=True
                                    moveup=False
                                if event.key==K_UP:
                                    moveup=True
                                    movedown=False
                                if event.key==K_RIGHT:
                                    moveright=True
                                    moveleft=False
                                if event.key==K_LEFT:
                                    moveright=False
                                    moveleft=True
                                if event.key== K_SPACE and p<=-50:
                                    shoot=True
                                    
                                    
                                
                            if event.type==KEYUP:
                                if event.key== K_DOWN:
                                    movedown=False
                                if event.key==K_UP:
                                    moveup=False
                                if event.key==K_RIGHT:
                                    moveright=False
                                if event.key==K_LEFT:
                                    moveleft=False
                                            
                        i=random.randint(0,100)
                        son=random.randint(0,70)
                        son2=random.randint(0,70)
                        
                        if i>99-counter/astrfrqnc:
                            test=True
                        if shoot:
                            p=p+50
                            pb.append(pygame.Rect(player.left+5,player.top,6,16))
                            shoot=False
                        
                        for x in pb:
                            x.top-=bs
                            pygame.draw.rect(window,BL,x)
                            for z in drone:
                                if z.colliderect(x):
                                    makesound=True
                                    drone.remove(z)
                                    pb.remove(x)
                                    bugfix1=True
                                    drone.append(pygame.Rect(random.randint(0,340),-40,20,20))
                                    bonus=bonus+50
                            for z in drone2:
                                if z.colliderect(x):
                                    makesound=True
                                    drone2.remove(z)
                                    if bugfix1==False:
                                        pb.remove(x)
                                        bugfix2=True
                                    drone2.append(pygame.Rect(random.randint(0,340),-40,20,20))
                                    bonus=bonus+50
                            for z in astroid:
                                if z.colliderect(x):
                                    score=score+100
                                    astroid.remove(z)
                                    if bugfix1==False and bugfix2==False:
                                        pb.remove(x)
                                    bonus=bonus+3
                        
                            if x.top<-80:
                                pb.remove(x)
                        if makesound:
                            makesound=False
                            
                        bugfix1=False
                        bugfix2=False
                        score=counter/10 +bonus
                        if test:
                            astroid.append(pygame.Rect(random.randint(0,320),0,35,35))
                            test=False
                        for bo in back:
                            pygame.draw.rect(window,W,bo)
                            bo.top+=backspd
                            if bo.top>=500:
                                bo.left=random.randint(0,355)
                                bo.top=-5
                        for x in astroid:
                            x.top+=5
                            pygame.draw.rect(window,P,x)
                            if x.colliderect(player)and shield==False:
                                game=False
                            if x.top >600:
                                astroid.remove(x)
                        if counter==120 :
                            drone.append(pygame.Rect(0,0,20,20))
                        if counter==520 :
                            drone2.append(pygame.Rect(0,0,20,20))
                        
                        
                            
                        for x in drone :
                            pygame.draw.rect(window,BL,x)
                            x.top+=dronetop
                            if r:
                                x.left+=2
                            if x.left>=340:
                                r=False
                                dronetop=random.randint(-1,1)
                                
                            if r==False:
                                x.left-=2
                            if x.left<=0:
                                r=True
                                dronetop=random.randint(-1,1)
                            if x.top<-10:
                                dronetop=1
                            if x.top >200:
                                dronetop=-1
                            if son<=1+counter/dbfrqc:
                                db.append(pygame.Rect(x.left,x.top,5,10))
                        for w in drone2 :
                            pygame.draw.rect(window,BL,w)
                            w.top+=dronetop2
                            if r2:
                                w.left+=2
                            if w.left>=340:
                                r2=False
                                dronetop2=random.randint(-1,1)
                                
                            if r2==False:
                                w.left-=2
                            if w.left<=0:
                                r2=True
                                dronetop2=random.randint(-1,1)
                            if w.top<-10:
                                dronetop2=1
                            if w.top >220:
                                dronetop2=-1
                            
                            if son2<=1+counter/dbfrqc:
                                db.append(pygame.Rect(w.left,w.top,5,10))
                        
                            
                            
                        for x in db:

                            x.top+=random.randint(3,5)
                            if x.colliderect(player):
                                game=False
                            
                            pygame.draw.rect(window,R,x)
                            if x.top>=580:
                                db.remove(x)
                            
                            
                                          
                                 

                        if moveup and player.top>0:
                            player.top-=ms
                        if movedown and player.top<540:
                            player.top+=ms
                        if moveleft and player.left>0:
                            player.left-=ms
                        if moveright and player.left<340:
                            player.left+=ms
                        text = Texta.render('score: %d' % score, 0, (250,250,0))   
                        window.blit(text, (5,0))
                        
                        pygame.draw.rect(window,(255, 100, 0, 122),player)
                        window.blit(shipx,(player.left-2,player.top))
                        pygame.draw.rect(window,P,powerbar)
                        mainclock.tick(70)
                        pygame.display.flip()
                        pygame.display.update()
ob=game()
ob.maingame()

