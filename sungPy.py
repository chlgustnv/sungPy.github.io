#---------------------------------------------------------모듈 import------------------------------------------------------------------

from vector_drawing import *
from math import *

#----------------------------------------------------------함수 정의-------------------------------------------------------------------

#□□□□□□□□□□□□□□□□□□□□□□□□□□□□□벡터 기본□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□

def add(v1, v2): #더하기 정의
    return (v1[0] + v2[0], v1[1] +  v2[1]) 

def add2(*vectors): #임의 개수 벡터 더하기 
    return (sum(v[0] for v in vectors),sum(v[1] for v in vectors))

def length(v): #길이 구하기 정의
    return sqrt(v[0]**2 + v[1]**2)

def distance(v1, v2):
    return sqrt((v2[0]-v1[0])**2 + (v2[1]-v1[1])**2)

#□□□□□□□□□□□□□□□□□□□□□□□□□□2차원 각과 삼각법□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□

def to_cartesian(polar_vector):                         #데카르 좌표로 변환  (길이, 각도) -> (x,y) 각도는 라디안 값
    length, angle = polar_vector[0], polar_vector[1]    #length = 벡터 길이, angle = 라디안 각
    return (length*cos(angle), length*sin(angle))       #cos = x/길이, sin = y/길이 

def to_polar(vector):                                   #극좌표로 변환 (x,y) -> (길이, 각도)
    x, y = vector[0], vector[1]
    angle = atan2(y,x)
    return (length(vector), angle)

def to_radian(angle):                                   #도      ->   라디안
    return angle*pi/180

def to_do_angle(angle):                                 #라디안  ->   도 
    return angle*180/pi


#----------------------------------------------------------변수 정의-------------------------------------------------------------------

dino_vectors = [(6,4), (3,1), (1,2), (-1,5), (-2,5), (-3,4), (-4,4), (-6,3),
                (-6,2),(-2,2),(-6,1), (-5,0),(-2,1),(-1,0), (0,-3), (-1,-4), 
                (1,-4), (2,-3), (1,-2), (3,-1), (5,1)]

dino_vectors2 = [add((-1.5, -2.5), v) for v in dino_vectors]

#----------------------------------------------------------코드 작성-------------------------------------------------------------------

# draw(
#     Points(*dino_vectors, color = blue),
#     Polygon(*dino_vectors, color = blue),
#     Points(*dino_vectors2, color = red),
#     Polygon(*dino_vectors2, color = red),
    
# )
# print(to_cartesian((8.5,to_radian(125))))
# print(sin(to_radian(50)))
# print(cos(to_radian(50)))
# print(tan(to_radian(116.57)))

# for n in range(-12,15):  #2.26 연습문제
#     for m in range(-14,13):
#         if distance((n,m),(1,-1)) == 13 and n > m and m > 0:
#             print(n)
#             print(m)
