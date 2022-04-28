from main import addEdges,addNodes, tocap


edges = [('Gate 2','MPR Gate end', 54, 170),
('MPR Gate end','Reception', 27, 200),
('Reception','Reception stairs',15,210),
('Reception stairs','Student Center' ,15, 290),
('Reception','Reception Elevator ground',26,270),
('Reception', 'Office of Career Services', 30,280),
('Student Center','Reception washroom' ,16,180),
('Reception','Turnstile',14,175),
('Turnstile','MPR Library end',16,80),
('Turnstile','Library junction',40,178),
('Library junction','Office Of Student Life', 19,310),
('Office Of Student Life', 'Health and Wellness',40,310),
('Library junction', 'Cafe2go', 37,90),
('Library junction', 'Library Infp Commons', 33,62),
('Cafe2go','Cassim lab',36,185),
('Cassim lab', 'East level 1 faculty pods', 13,175),
('East level 1 faculty pods', 'Easten ramp ground', 29,206),
('Library junction', 'Central street ground faculty pods',43,207),
('Central street ground faculty pods','Central street stairs ground', 42,207),
('Central street ground faculty pods', 'ATM', 34,170),
('Central street ground faculty pods', 'Arif Habib Classroom', 43,228),
('Arif Habib Classroom', 'Earth Courtyard',13,2),
('Earth Courtyard', 'Westerm stairs ground' ,24,27),
('Western stairs ground', 'Physics lab' , 20,291),
('Physics lab', 'Western elevator ground', 8,290),
('Western elevator Ground', 'Math lab', 8,190),
('Physics lab', 'Earth Courtyard Boards', 20,200),
('Earth boards', 'Air Courtyard' ,20,200),
('Air Courtyard', 'Arif Habib Classroom', 22,80),
('Air Courtyard', 'Water Courtyard',17,170),
('Water Courtyard', 'Fire Courtyard' ,37,200),
('Fire Courtyard', 'Chemistry Lab',20,255),
('Fire Courtyard', 'Ecology Lab'  ,20,255),
('Digital Systems and Instrumentation Lab', 'Fire Courtyard',24,130),
('Communications lab', 'Fire Courtyard',24,130),
('Fire Courtyard', 'Student lounge Amphitheatre end' ,55,150),
('Student lounge amphi end', 'Soorty Hall',47,70),
('ATM', 'Soorty Hall' ,55,170),
('Soorty Hall','Student lounge garden end',38,211),
('Student lounge garden end' ,'Courts adjacent Faculty pods',20,180),
('Courts Faculty pods', 'Multipurpose Sports Courts 1' ,56,180),
('Multipurpose Sports Courts 1', 'Zen Garden' ,100,175),
('Multipurpose Sports Courts 1', 'Rahim bhai stall' ,80,30),
('Rahim Bhai stall', 'Dhaaba' ,24,108),
('Rahim Bhai stall', 'Hu Dukaan' ,17,0),
('Hu Dukaan', 'Cafeteria Dukaan end',11,90),
('Hu Dukaan', 'Amphi washroom' ,23,330),
('Amphi washroom' , 'Amphitheater lower' ,15,260),
('Amphitheater lower', 'Amphitheater upper' ,40,180),
('Amphi upper', 'C-015' ,33,107),
('C-015', 'Gym' ,27,220),
('C-015', 'Swimming Pool',44,260),
('Swimming Pool', 'Facilities office',58,15),
('Facilities office', 'Changing room',44,96),
('Facilities office', 'Engineering Workshop',21,53),
('Facilities office', 'Western Elevator lower ground',65,355),
('C-015', 'Hu Dukaan',27,45),
('Cafeteria Dukaan end', 'Cafeteria Projects Lab end',35,12),
('Cafeteria Projects Lab end', 'Ground floor Projects Lab',25,2),
('Ground floor Projects Lab', 'Power lab',25,19),
('Power lab', 'Circuits and Electronic Lab 1',27,11),
('Circuits and Electronic Lab 1', 'Music Room',23,100),
('Music Room', 'Linux And Networking Lab',7,90),
('Linux And Networking Lab','Lower ground eastern washrooms',11,155),
('Lower ground eastern washrooms', 'Visualization And Graphics Lab',28,185),
('Visualization And Graphics Lab', 'Dinshaw', 10,180),
('Dinshaw', 'rangoonwala', 6,180),
('Dinshaw', 'Easter ramp lower',15,230),
('Eastern ramp lower', 'Ground floor Projects Lab',31,290),
('Reception Elevator ground','Reception Elevator first',0,0),
('Reception Elevator first','Reception Elevator second',0,0),
('Reception Elevator second','Reception Elevator third',0,0),
('Western Elevator lower ground','Western Elevator ground',0,0),
('Western Elevator ground','Western Elevator first',0,0),
('Eastern ramp lower','Eastern ramp ground',84,0),
('Turnstile stairs ground','Turnstile',20,350),
('Turnstile stairs lower','Turnstile stairs ground',31,350),
('Turnstile stairs lower','Female lounge',52,277),
('Female lounge','Westerm stairs ground',30,175,'s'),
('Western pathway Air junction','Western pathway Wellness junction',59,4),
('Western pathway Wellness junction','Bank',81,9),
('Bank','Security office',20,18),
('Gate 2','Security office',70,280),
('ATM stairs','Tapal stairs',45,187,'s'),
('Tapal stairs','Hu Dukaan',13,177),
('Tapal stairs','Amphitheatre washroom',10,285),
('ATM','ATM stairs',13,190),

('Wellness Courtyard','Western pathway Wellness junction',47,285),
('Office Of Student Life','Wellness Courtyard',16,285),
('Central street stairs ground','Central street stairs top',24,33),
('Earth courtyard Ramp ground','Earth courtyard ramp first',90,180),
('Earth courtyard Ramp ground','Earth Courtyard',10,9),
('Western stairs ground', 'Western stairs first',49,15),
('Western stairs first', 'Western stairs second',69,15),
('Western stairs second','Western elevator second',20,268),
('Western elevator second','Second floor Ground floor Projects Lab',12,215),
('Western elevator second','Second floor faculty pods W-301-10',12,215),
('Western elevator second','W321',26,170),
('Reception stairs ground','Reception stairs first/ground junction',30,195),
('Reception stairs first/ground junction','Reception stairs first/second junction',25,15),
('Reception stairs first/second junction','Reception stairs second',30,230),

 
#######ASAD#########

('Film Studio', 'Tariq Rafi Lecture Theater', 38, 260),
('Central street stairs top', 'Tariq Rafi Lecture Theater', 24, 90),
('Central street stairs top', 'W221 Faculty Pod', 49, 302),
('W221 Faculty Pod', 'W242', 30, 160),
('W221 Faculty Pod', 'W243', 47, 174),
('W242', 'W243', 17, 200),
('W242', 'Design Studio', 19, 60),
('W221 Faculty Pod', 'Western Elevator first', 12, 40),
('Western Elevator first', 'C203 Faculty Pod', 36, 140),
('C203 Faculty Pod', 'CPE C201', 51, 32),
('CPE C201', 'Library Entrance 1st Floor', 35, 100),
('CPE C201', 'CPE Classroom', 54,0),  # Audi Route
('CPE C201', 'CPE Classroom', 42,0),  # Deans Pod Route
('Library Entrance 1st Floor', 'Discussion Rooms', 34, 140),
('Library Entrance 1st Floor',  'Yohsin Hall', 40, 64),
('CPE Classroom', 'Deans Pod', 44, 300),
('CPE Classroom', 'Auditorium Hall', 30, 80),
('CPE Classroom', 'Reception Elevator first', 12, 340),
('CPE Classroom', 'N219 faculty Pods', 19, 217),
('CPE Classroom', 'Standard Chartered Classroom', 28,317),
('CPE Classroom', 'N219 faculty Pods', 32, 350),
('Reception Staris first/ground junction', 'CPE C201', 26, 226),
('Reception Stairs first/second junction', 'Auditorium', 31, 200),
('Reception Stairs first/ground junction', 'CPE Classroom', 30, 330),
('Reception Stairs second', 'Playground',5, 55),
('Playground' , 'Second floor Admin offices', 35, 330),
('Second floor Admin offices', 'Reception Elevator second', 7,7),
('Library Entrance 1st Floor','Library Info commons',34,350),
('Library Infp Commons','Writing Centre',27,61),
('Library Infp Commons','Ehsas elevator ground',27,61),
('Ehsas elevator ground','Ehsas centre',0,0),
('Ehsas elevator ground','Yohsin Hall',0,0),


('Central street stairs ground','Central street stairs top',24,33),
('Earth courtyard Ramp ground','Earth courtyard ramp first',90,180),
('Earth courtyard Ramp ground','Earth Courtyard',10,9),
('Western stairs ground', 'Western stairs first',49,15),
('Western stairs first', 'Western stairs second',69,15),
('Western stairs second','Western elevator second',20,268),
('Western elevator second','Second floor Ground floor Projects Lab',12,215),
('Western elevator second','Second floor faculty pods W-301-10',12,215),
('Western elevator second','W-321',26,170),
('Reception stairs ground','Reception stairs first/ground junction',30,195),
('Reception stairs first/ground junction','Reception stairs first/second junction',25,15),
('Reception stairs first/second junction','Reception stairs second',30,230),




]
Edges = []
def out(edges,Edges):
    for i in edges:
        Edges.append(i)
        if len(i)==4:
            x = (i[1],i[0],i[2],(180 - i[3]))
        else:
            x = (i[1],i[0],i[2],(180 - i[3]))
        Edges.insert(Edges.index(i),x)
    return Edges

Edges = out(edges,Edges)
# print(Edges)
G=addNodes(Edges,[])
addEdges(G,Edges)
positions1=[]

mapposition=edges1[:]
p=[(5, 350), (142, 311), (215, 345), (249, 344), (237, 387), (204, 419), (154, 390), (295, 365), (248, 321),
 (216, 306), (362, 284), (368, 361), (335, 590), (332, 199), (290, 221), (443, 152), (530, 146), (618, 181), (522, 361), (623, 284), (640, 411), (596, 413), (564, 436), (475, 470), (489, 496), (513, 487), (540, 474), (587, 495), (627, 465), (662, 490), (693, 480), (693, 497), (638, 499), (635, 474), (798, 384), (737, 281), (852, 322), (902, 344), (965, 303), (1175, 228)]
a=0
while len(p)>0 and len(mapposition)>a:
    if a==0:
        positions1.append((mapposition[a][0],p[0]))
        p.pop(0)
        a+=1
        continue
    if mapposition[a][0] not in [i[0] for i in positions1]:
        positions1.append((mapposition[a][0],p[0]))
        p.pop(0)
    if mapposition[a][1] not in [i[0] for i in positions1]:
        positions1.append((mapposition[a][1],p[0]))
        p.pop(0)
        mapposition.pop(0)
    a+=1
# print ('\n'*5,positions1)
# print('\n'*5,edges1)
# positions1=tocap(positions1)
# print('Here\n'*5,positions1)

G1=addNodes(edges1,[])
addEdges(G1,edges1)


