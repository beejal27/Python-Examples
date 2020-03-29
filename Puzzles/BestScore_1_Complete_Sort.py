# -*- coding: utf-8 -*-
"""
Created on Wed Mar 25 19:10:16 2020

@author: Beejal
"""
import time

#vals = [6, -5, 3, -7, 6, -1, 10, -8, -8, 8]
#vals = [ -53,-38, 32, -7,-28, -2, 80,-85, 28,-16, -1, 19, 67,-49,-51, 42, 10,-90, 21, 63,-51,-46, 29,-64,-75, 26, 78,-73,-87, 84, 14,-99,7, 98,-10,-13, -8,-92, 80,-71,-95,-34, -9,-38, 32,-86,-86, 14,-10,-26, 27,-98,-57,-67,-81,-39,-71,2,-80,-65, 13,-19, 23, 79,-72,-36,-39, 59, 78,-87, -2, 33, 31, 92,-80,-20,-92, 24,-25,-85,7, 22, 74,-25,-90, 66,-33,-86,-73,-90,-13,-69,8, 36,-56,2, 24, 88, 27,-95,-79,-55, 17, 75, 48,-17,-30,-79,-74, 37, 84,-50,-48, 81,-41,-51,-48,-67, -8,-36,-64,-48,-95,-22,-45,2, 87, 98, -6,-68,-98,-53, 98, -9, -5, -7, -6,-16,-99, 96, 45, 88,-36, 68,-85, 56,-11, 31, 90, 48, 83,-91,-58,-72,-56, 23, 22,-46,-94,3,-14,-98, 93,-46,-80,-91, 95,-95,-73,-21,-81,-70, 99, 18,-98, 49, 19, 69,-94, 49,-58, 40,-10, -1,-16, 60, 87,-13, -4,-43,-28, 48,-30, 71, 38,-35, 99,2,-47, 29, 58,-99,4, 47, 25,-30, 55, 60, 25,-42,-24, 90, 72, 25, 11, 68,-18,-50,-93, 50, 98, 84, 89,-24, 86,-49,-81,-74, -6,-97, 35,4, 55,-16, -3, 79, -5,-34,-70,6,9,-21, 50, 15, 85, 47,-61, 20, 23, 62,8,-61, 98,-13,-89,-64,-23,-76,-23,-33, 88, 58,-84,5,-85, 84, 41,-57, 81, 88, 18, 54,-55, 39,-91,7, 10, 43,-48, 58,-13,-90,-99,-41,-54, -9,-28,9, 56, 10, 54, 99,-14, 16,-29, 57,-32,-10,-12, 71, 25, 91, 86, 91, 53,-87, 87, 34, 25,-98,-30,-39, 57, 91,-95, 32, 64, 36,-53,-49, 88, 10, 18, -2, 86, 42, 12, 92,-41,-75, 79, -3, -2,-62 -100,-44,-81, 57, 19,-49,-47, 74,-13, 40,-54,-14,2, 85,-98,2, 21,-34, 52, 81, 54, 38, -2,-17, 98,-99,-40,-50,-10, 61,-59,-97,-99,-10,-79, 37, 14, 39,-65, -1, 30,-31,-82,-40,-74, 28,-89, 64,-66,-23, 22, 45,-32, 44,5, 88, 43,-12, 44, 51, 13, 41,-60,-65,-12,-77,6,-55, 22, 43, 19, -1,-13,-88,-69, 28,-71, 74,-59, 48, 86, 70, 79,-82,-63,-49,-52, 39,-29,-52, 92,-62,-63,-64, 39, 50,-34, 55,0,-76, -2,-20, 92, 95, 20,-22, -6, 88, 26,-77,-17,-63,-56, 59, 69,-23,-77,-50,-22, 12, 18, 35, 28,-44, 42,-81,6, 68,4,-62, 43, 56, 98, 96, 20, 70,-63,-66, 73, 58,-35, 59,-31,-16, 34, 42,-42, 50, 62,-26, 59,-60,-71, 49,-56,-90,-33, 73, -4,-72,-73,-66,-41, 33, 34,-91]

def best_score(vals, K):

    best_i = -1
    best_j = -1
    best_score = 0
    
    DEBUG = False
    
    start_time = time.time()
    for i in range(0, len(vals)):
        for j in range(i+1, len(vals)+1):
            seg_idx = f'{i}:{j}'
            if DEBUG:
                print(f'Segment Index :: {seg_idx}')
            segment = vals[i:j]
    
            if K > 0:
                segment = sorted(segment)
                remove_index = []
                for l in range(0, min(K, len(segment))):
                    if segment[l] < 0:
                        remove_index.append(0)
                    else:
                        break
                for index in remove_index:
                    segment.pop(index)
            segment_score = sum(segment)
            if segment_score > best_score:
                best_score = segment_score
                best_i = i
                best_j = j
    
    # Record End Time
    end_time = time.time()
    
    print(f'Time Taken = {end_time - start_time}')
    
    print(f'Best Score = {best_score}, [i:j] = {best_i}:{best_j}')
    print(f'Segment = {vals[best_i:best_j]}')
        

# Test-1
vals = [6, -5, 3, -7, 6, -1, 10, -8, -8, 8]
K = 2
best_score(vals, K)

# Test-2
vals = [6, -5, 3, -7, 6, -1, 10, -8, -8, 8]
K = 3
best_score(vals, K)

# Test-3
vals = [6, -5, 3, -7, 6, -1, 10, -8, -8, 8]
K = 4
best_score(vals, K)

# Test-4
vals = [6, -5, 3, -7, 6, -1, 10, -8, -8, 8]
K = 6
best_score(vals, K)
    
    
    